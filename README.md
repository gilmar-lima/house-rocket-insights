# House Rocket Insights

# 1. Business Problem
House Rocket is a real estate company trying to figure out a way to improve the process by which properties are 
negotiated, our main goal is to provide insights that are relevant for the business and figure out which are the best 
buying opportunities.   
# 2. Business Assumptions
We take into account the following assumptions:

**Properties recommendation conditions**:
- Properties in which the price is less than the region's median and it is in good conditions, will be considered good 
buying opportunities.
- Good condition is considered equal 5.


**Selling price calculation conditions**:
- If the price is greater than the region's median. The selling price will be the buying price + 10%.

- If the price is less than the region's median. The selling price will be the buying price + 30%.

**Outliers**:
- We are considering houses with prive above 500 000 000 as an outlier.
# 3. Solution Plan
**Step 1. Data Extraction:** download the dataset from Kaggle site.

**Step 2. Data Cleansing:** perform data cleansing by removing wrong dates and outliers.

**Step 3. Data Transformation:** 
- Group properties by zip code and calculate the median of the prices within the group.
- Generate a "status" column informing if it is recommended to buy the property or not.
- Generate a "selling_price" with the selling price calculated.

**Step 4. Exploratory Data Analysis:** perform the exploratory data analysis in order to find insights that are 
relevant for the business.

**Step 5. Create Visualizations:** 
- Create visualizations on streamlit for each of the hypothesis.
- Create table with buying recommendations.
- Create table with selling prices recommendations.

# 4. Main Insights
**Hypothesis 1:** Properties with view to water are 30% more expensive.

 **False**: As observed, properties with water front are more than 30% more expensive.

**Hypothesis 2:** Properties with construction date less than 1955 are 50% cheaper on average.

 **False**: As observed, properties with construction date before 1955 have the same value as newer properties.

**Hypothesis 3:** Properties without basement are 50% bigger in lot size than ones without basement.

**False:** Properties without basement are 20% bigger on average.

**Hypothesis 4:** The rising rate on price of properties year over year is 10%.

**False:** As observed, the rising rate year over year is less than 10%.

**Hypothesis 5:** Properties with 3 bathrooms have a rising price month over month of 15%

**False:** As observed, the rate of prices is not constant.

# 5. Business Results
# 6. Conclusion

