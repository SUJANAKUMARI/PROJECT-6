![image](https://github.com/user-attachments/assets/fe1df30b-3085-4539-a881-48579f5da816)![image](https://github.com/user-attachments/assets/8616e85c-bdf7-4151-8f9f-838d3bd03734)##PROJECT ON PHARMACEUTICAL SALES PREDICTION ACROSS MULTIPLE STORES

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

● # Trends of customer behavior during store open and closing times![image](https://github.com/user-attachments/assets/da105a13-b1b7-45df-a3bb-56703fdc1eec)






