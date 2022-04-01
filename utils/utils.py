import pandas as pd

def perform_cleansing(data):
    data = data[data['price'] < 500000000]
    return data

def define_selling_price(table_row):
    current_price = table_row['price']
    median_price = table_row['price_median']

    if (current_price > median_price):
        return current_price*1.1
    else:
        return current_price*1.3

def generate_columns(data):
    
    #Calculate the median price by zip code.
    df_zipcode_median = data[['price','zipcode']].groupby('zipcode').median().reset_index()
    df_zipcode_median.columns = ['zipcode','price_median']

    df_recommendations_price = pd.merge(data, df_zipcode_median, on = 'zipcode', how = 'inner')

    #Generate the status column with buying recommendation.
    df_recommendations_price['status'] = df_recommendations_price.apply( lambda row : 'buy' if (row['condition'] == 5) & 
                                                                                       (row['price'] < row['price_median']) 
                                                                                    else 'not buy', axis=1)
    
    # Generate a "selling_price" with the selling price calculated.
    df_recommendations_price['selling_price'] = df_recommendations_price.apply(define_selling_price, axis=1)

    # Generate  a column with the year of the date.
    df_recommendations_price['date'] = pd.to_datetime( df_recommendations_price['date'] )
    df_recommendations_price['date_year'] = pd.to_datetime( df_recommendations_price['date'] ).dt.year
    
    # Generate  a column with the year and month period.
    df_recommendations_price['date_month'] = pd.to_datetime( df_recommendations_price['date'] ).dt.to_period('M')
    return df_recommendations_price