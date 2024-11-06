![image](https://github.com/user-attachments/assets/95e55bde-2ed3-431f-b848-5325a908d591)![image](https://github.com/user-attachments/assets/fe1df30b-3085-4539-a881-48579f5da816)![image](https://github.com/user-attachments/assets/8616e85c-bdf7-4151-8f9f-838d3bd03734)##PROJECT ON PHARMACEUTICAL SALES PREDICTION ACROSS MULTIPLE STORES

![image](https://github.com/user-attachments/assets/4a419f37-37c2-4193-b5e8-8cf8c4fda6af)

Project Scenario:
Rossmann Pharmaceuticals needs a robust sales forecasting tool to accurately predict sales across all its stores six weeks in advance. The finance team relies on these forecasts for budgeting and planning, while store managers traditionally depend on experience and intuition. With numerous factors impacting sales, such as promotions, holidays, competition, and seasonal trends, Rossmann requires a data-driven solution to support more accurate and standardized predictions across stores. 

Project Description:
As a Machine Learning Engineer at Nexthikes, my role is to design and deploy an end-to-end sales forecasting solution for Rossmann Pharmaceuticals. The solution will analyze historical sales data and key influencing factors, producing six-week-ahead sales forecasts for each store. This tool will empower the finance team with timely, precise sales projections and allow analysts to easily visualize and download data for further insights. The project will ultimately improve sales predictability across Rossmann’s network and support better planning at both store and corporate levels.

# DATA DESCRIPTION

SOURCE OF MOBILE DATA:  The data used for the analysis is provided by Next Hikes.

FEATURES/VARIABLES INCLUDED:  There are around  55 features and variables included in the data.   The most common and important variables include Experience Score, Engagement Score and Satisfaction Score etc.

DATA SIZE AND FORMAT: The dataset includes store-specific details, promotions, holidays, customer count, and competitor information, all crucial for forecasting sales.

NECESSARY LIBRARIES TO BE IMPORTED:   
Jupyter notebook anTask 1 – EXPLORATION OF CUSTOMER PURCHASE BEHAVIOUR
d VS Code.
Technical Skills: Pandas, Matplotlib, Numpy, HTML and CSS ,
Flask.
Creation of new features
Predictive pipeline: Exploratory data analysis, data wrangling, building and
fine-tuning models
Building model using MLOps Techniques

# Task 1 – EXPLORATION OF CUSTOMER PURCHASE BEHAVIOUR

# Check for distribution in both training and test sets- are the promotions distributed similarly between these two groups?

![image](https://github.com/user-attachments/assets/0219a7be-6a40-4ed1-9295-2ce4c34abb7a)

INTERPRETATIONS:**
Based on the bar graphs above, it appears that the distribution of promotions is quite similar between the training and test sets. Here’s a more detailed interpretation:
   
This similarity in distribution suggests that the promotion data is balanced between the training and test sets, which is crucial for ensuring that the machine learning model can generalize well and is not biased due to an uneven distribution of promotions.
    
IN SIMPLE: The similar distribution of promotions in both the training and test sets means that the data is balanced. This helps your machine learning model work well and avoid bias.

# Check & compare sales behavior before, during and after holidays

![image](https://github.com/user-attachments/assets/5d93fc9e-ed98-4405-b962-d87762cf35d7)

INTERPRETATIONS:  Overall, the data suggests that pharmaceutical sales are highest before the holidays, likely due to consumers preparing in advance, and then decrease during the holidays as some stores might be closed and some stores might have stores opened for only few hours, and further increase after holidays that means the sales is picking up and coming back to normal.

# Find out any seasonal (Christmas, Easter etc) purchase behaviours

![image](https://github.com/user-attachments/assets/52dea03c-2079-4581-bdde-51791f62d03f)

![image](https://github.com/user-attachments/assets/62ab9917-b9c5-4284-bb54-d426ce104dc3)

![image](https://github.com/user-attachments/assets/29a1d72f-9dab-4f9f-8b8a-cfaa46cc9686)

INTERPRETATIONS:
    
Christmas Season (Orange): The orange-shaded area represents the Christmas season, which typically falls in December. The sales data exhibits a significant increase during this period, with a peak in December. This suggests that pharmaceutical sales tend to surge during the Christmas season, possibly due to:
    
1. Increased demand for cold and flu medications during the winter months.
    
2. Higher sales of health and wellness products as people prepare for the holiday season.
    
3. Gift purchases or stocking up on medications before the year-end.
Easter Season (Blue):The blue-shaded area represents the Easter season, which typically falls in March or April. The sales data shows a smaller, yet still noticeable, increase during this period. This might be attributed to:
    
1. Increased demand for allergy medications during the spring season.
    
2. Sales of health and wellness products related to spring-related activities (e.g., outdoor activities).

# What can you say about the correlation between sales and number of customers?

![image](https://github.com/user-attachments/assets/c417eb30-b884-47a2-babf-b0f2ae5f0a05)

![image](https://github.com/user-attachments/assets/e253b48f-a48d-404d-a428-3aabf61f08d7)

INTERPRETATION:
The correlation coefficient of 0.91 between Sales and Customers indicates a strong positive relationship. This means that as the number of customers increases, sales are also likely to increase significantly, and vice versa.
    
This information can be very useful for businesses to predict sales trends based on customer data.

# How does promo affect sales? Are the promos attracting more customers? How does it affect already existing customers? 

![image](https://github.com/user-attachments/assets/531618a3-328b-48d3-a5f3-4e0d3229455b)

How does promo affect sales?

**Promotions significantly increase sales.** The "Average Sales During Promotions vs Non-Promotions" plot clearly shows a much higher average sales figure when promotions are running. This strongly suggests that promotions are effective at driving revenue.
    
**Are the promos attracting more customers?**

**Yes,** promotions appear to be attracting more customers. The "Average Customers During Promotions vs Non-Promotions" plot indicates a higher average number of customers during promotional periods. This suggests that promotions are successful in bringing in a larger customer base.
    
**How does it affect already existing customers?**

**Promotions likely encourage higher spending per existing customer.** The "Sales Per Customer During Promotions vs Non-Promotions" plot reveals a higher average spend per customer when promotions are active. This indicates that promotions not only attract new customers but also incentivize existing customers to purchase more.

# # Could the promos be deployed in more effective ways? Which stores should promos be deployed in? # Analyze Sales Performance During Promotions.

![image](https://github.com/user-attachments/assets/50c83e79-9035-43c0-8a89-8d736532abbb)

![image](https://github.com/user-attachments/assets/425c3778-de8f-4381-888f-34bfb780b71f)

# Effectiveness of Promotions by Store Type

![image](https://github.com/user-attachments/assets/3150ab51-aab8-4d77-97e7-96bf64c62dbe)

![image](https://github.com/user-attachments/assets/24f9633c-6285-4377-8863-db630f5c39bd)

# Effectiveness of Promotions by Store Type

Sales Increase During Promotions:**Store Type 'a' has the highest sales increase at around 40%. Store Type 'c' and 'd' have similar sales increases of approximately 30%. Store Type 'b' has the lowest sales increase during promotions, around 10%. 

 Customers Increase During Promotions: Store Type 'a' also shows the largest increase in customers during promotions, around 30%. Store Type 'c' and 'd' follow, with customer increases of approximately 25% and 30%, respectively.
3. Store Type 'b' again has the lowest customer increase, with less than 10%.

Can promotions be deployed in more effective ways?**

**SUMMARY:**

In summary, promotions are most effective in store types 'a', 'c', and 'd', and these should be the primary focus for future promotional activities. Store type 'b' should either be given a tailored approach or deprioritized based on the current data."

● # Trends of customer behavior during store open and closing times

![image](https://github.com/user-attachments/assets/d2aab13c-9786-4646-bd95-ce116282bf3b)

**Key Insights:**

Clear Correlation: There is a direct correlation between store opening times and both sales and customer activity. When the store is open, both sales and customer counts are significantly higher.


2. No Activity During Closure: As expected, there are no sales or customer activity when the store is closed.

## Find Stores Open on All Weekdays:

![image](https://github.com/user-attachments/assets/fbf4699e-f2db-4ca6-95a8-431da343947d)

![image](https://github.com/user-attachments/assets/8a02905a-d947-4541-bd37-3bd24ffb03c7)

![image](https://github.com/user-attachments/assets/ba05b4ab-f797-4955-8bd1-6ba51fd77678)

**Interpretation:**

 The analysis reveals a significant difference in average weekend sales between two groups of stores:
**1. Stores Open All Weekdays:**   
These stores have an average weekend sales figure of approximately $7359. This suggests that consistent weekday operations contribute to higher customer familiarity and loyalty, which may translate into better sales on weekends.
2.  Stores Not Open All Weekdays:**
In contrast, stores that do not operate all weekdays have an average weekend sales figure of about $2,811. This lower sales average could indicate that limited operational days lead to reduced customer engagement or lower brand visibility, resulting in fewer sales during weekends.
Overall, the data suggests that stores with regular hours throughout the week likely cultivate a stronger customer base, which positively affects their weekend performance.

# Check how the assortment type affects sales
![image](https://github.com/user-attachments/assets/031bae23-b0f2-4b1d-909c-907df9e5311f)

![image](https://github.com/user-attachments/assets/1d6dd2b2-7707-44b0-8810-57a5c8c36562)

**Interpretation:**
    
**Assortment Type ‘a’ Basic:** This type has average sales of approximately.

**Assortment Type ‘b’ Extra:** This type shows the lowest average sales.
    
**Assortment Type ‘c’ Extended:** This type has the highest sales.

From this we can see that assortment type ‘c’  that is the Extended type is the most successful in terms of average sales, while type ‘b’ that is extra type  has the least average sales.

# How does the distance to the next competitor affect sales? What if the store and its competitors all happen to be in city centres, does the distance matter in that case?

![image](https://github.com/user-attachments/assets/36a01312-c2ff-4b03-9cdc-c2f0deaaa85a)

**Overall Correlation:**
    
The overall correlation between sales and competition distance is very weak (0.01), indicating that distance to the next competitor has little to no effect on sales in general.
    
**City Centre Scenario:**

If all stores and their competitors are located in city centers, where distances are generally shorter due to higher density, the weak correlation suggests that distance may not be an important factor. In such cases, other factors like foot traffic, store visibility, and local demand might have a more significant influence on sales.

# LOGGING

CREATED A LOGGER FILE CALLED sales_logger.py and the logs are saved in the file named sales_prediction_log

![image](https://github.com/user-attachments/assets/ad4b28d4-008b-43c7-92ce-65f774cd40e3)

![image](https://github.com/user-attachments/assets/ce3fe26c-425b-4b41-8759-6179298fc968)

# TASK 2 -- PREDICTION OF STORE SALES

Prediction of sales is the central task in this challenge. you want to predict daily sales in various stores up to 6 weeks ahead of time. This will help the company plan ahead of time.

THE FUTURE PREDICTION OF SALES IS DONE AND THIS IS SAVED AS THE FILE NAMED “future_predictions_all_stores.csv”

The steps involved in the prediction of store sales include 
1. PREPROCESSING
It is important to process the data into a format where it can be fed to a machine learning model. This typically means converting all non-numeric columns to numeric, handling NaN values and generating new features from already existing features.
In our case, you have a few datetime columns to preprocess. you can extract the
following from them: - weekdays, - weekends, - number of days to holidays
- Number of days after holiday
- Beginning of month, mid month and ending of month
- (think of more features to extract), extra marks for it
As a final thing, you have to scale the data. This helps with predictions especially when
using machine learning algorithms that use Euclidean distances. you can use the
standard scaler in sklearn for this.
ALL THESE PREPROCESSING WAS DONE AND CREATED A DATAFRAME CALLED “df_train”

2. OUTLIERS REMOVAL:  Outliers were removed and the dataframe named “df_filtered” was created.

3. BUILDING MODELS WITH SKLEARN PIPELINES – This was done successfully. Below is the output

   ![image](https://github.com/user-attachments/assets/8f623095-54d9-48c9-b2af-839737d05efa)

4. CREATE A PIPELINE FOR IMPUTING, SCALING AND MODEL FITTING AND ALSO ACCURACY

   ![image](https://github.com/user-attachments/assets/1e0bb3ff-3383-48b4-a684-3d37d312109b)

5.  SERIALIZING THE MODELS

![image](https://github.com/user-attachments/assets/415337e6-c1f3-44a1-97ba-5b14fd8ef906)

6. IDENTIFYING THE FEATURE IMPORTANCES

![image](https://github.com/user-attachments/assets/2cfea06f-ef18-4667-a48d-c4f8c5069cb6)

![image](https://github.com/user-attachments/assets/b973e8b6-a211-4781-a581-a3f633777d28)















