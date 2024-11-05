from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


app = Flask(__name__)

# Load your models
model_sales = joblib.load('model_sales_rfr.joblib')
model_customers = joblib.load('model_customers_rfr.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    store_id = request.form['store_id']
    file = request.files['file']
    
    # Read the CSV file
    df = pd.read_csv(file)
    
    # Ensure required columns are present
    required_columns = ['Date', 'IsHoliday', 'IsWeekend', 'IsPromo', 'Open', 'Assortment', 'StoreType', 'DayOfWeek', 'Weekday', 'Store']
    for col in required_columns:
        if col not in df.columns:
            return f"Error: Missing column {col} in uploaded file."
    
    # Filter the DataFrame for the entered Store ID
    store_data = df[df['Store'] == int(store_id)]
    
    if store_data.empty:
        return f"Error: No data found for Store ID {store_id}."
    
    # Prepare the input data for prediction
    X_sales = store_data[['Open', 'IsPromo', 'IsHoliday', 'Assortment', 'StoreType', 'IsWeekend', 'DayOfWeek', 'Weekday']]
    X_customers = store_data[['Open', 'IsPromo', 'IsHoliday', 'Assortment', 'StoreType', 'IsWeekend', 'DayOfWeek', 'Weekday']]
    
    # Make predictions
    predicted_sales = model_sales.predict(X_sales)
    predicted_customers = model_customers.predict(X_customers)
    
    # Prepare results
    store_data['Predicted_Sales'] = predicted_sales
    store_data['Predicted_Customers'] = predicted_customers
    
    # Save predictions to CSV (only the filtered data)
    output_file = 'predictions.csv'
    store_data.to_csv(output_file, index=False)
    
    # Check if 'static' directory exists, if not create it
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Plotting
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=store_data, x='Date', y='Predicted_Sales', label='Predicted Sales', color='blue')
    sns.lineplot(data=store_data, x='Date', y='Predicted_Customers', label='Predicted Customers', color='orange')
    plt.title(f'Predicted Sales and Customers for Store ID: {store_id}')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('static/prediction_plot.png')
    
    return render_template('index.html', plot='prediction_plot.png', predictions=output_file, store_id=store_id)

@app.route('/download')
def download():
    return send_file('predictions.csv', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
