import pandas as pd
import plotly.express as px
import streamlit as st

from utils import utils

#-------------
# Settings
#-------------
st.set_page_config( page_title = 'House Rocket Insights' , layout='wide', page_icon = "🏡")

@st.cache
def get_data(path):
    data = pd.read_csv(path)
    return data

def data_preparation(data):
    data = utils.perform_cleansing(data)
    data = utils.generate_columns(data)
    return data

def hypothesis1 (data):

    df_properties_water = data[['waterfront','price']].groupby('waterfront').mean().reset_index()
    df_properties_water.columns = ['waterfront', 'price_mean']
    df_properties_water['waterfront_status'] = df_properties_water['waterfront'].apply(lambda wfront : 'yes' if wfront == 1.0 else 'no')

    fig = px.bar(df_properties_water, x='waterfront_status', y='price_mean', 
                    labels={"waterfront_status": "View to water",
                             "price_mean":"Price mean"},
                    width = 600, 
                    height = 371,
                    color = 'waterfront_status',
                    title = 'Properties with view to water')

    #st.plotly_chart(fig, use_container_width=True)    
    return fig

def hypothesis2(data):

    df_properties_1955 = data[['yr_built','price']].copy()
    df_properties_1955['before_1955'] = df_properties_1955['yr_built'].apply(lambda yr_built : 'yes' if(yr_built < 1955) else 'no')
    df_properties_1955 = df_properties_1955[['before_1955', 'price']].groupby('before_1955').mean().reset_index()

    fig = px.bar(df_properties_1955, x = 'before_1955', y = 'price', 
                    width = 600, 
                    height = 371,
                    labels={"before_1955": "Contruction before 1955",
                             "price":"Price mean"},
                    color = 'before_1955',
                    title = 'Properties constructed before 1955'
                    )
    return fig

def hypothesis3 (data):

    df_properties_basement = data[['sqft_lot','sqft_basement']].copy()
    df_properties_basement['have_basement'] = df_properties_basement['sqft_basement'].apply(lambda basement : 
                                                                                                'yes' if(basement > 0) 
                                                                                                       else 'no')
    df_properties_basement = df_properties_basement[['have_basement', 'sqft_lot']].groupby('have_basement').mean().reset_index()

    fig = px.bar(df_properties_basement, x = 'have_basement', y = 'sqft_lot', 
                    labels = {'sqft_lot' : 'Mean sqft lot', 'have_basement' : 'Property have basement?'},
                    width = 600,
                    height = 371,
                    color = 'have_basement',
                    title = 'Properties which have basement')
    
    return fig

def hypothesis4 (data):
    df_yoy_price = data[['price','date_year']].groupby('date_year').mean().reset_index()
    fig = px.bar(df_yoy_price, x = 'date_year', y = 'price',
                    labels = {'date_year' : 'Year', 'price' : 'Price mean'},
                    width = 600, 
                    height = 371,
                    title = 'Price over year')
    return fig

def hypothesis5 (data):

    df_mom_bathrooms = data[data['bathrooms'] >= 3]
    df_mom_bathrooms = df_mom_bathrooms[['date_month','price']].groupby('date_month').mean().reset_index()
    df_mom_bathrooms.sort_values(by = 'date_month')
    df_mom_bathrooms['date_month'] = df_mom_bathrooms['date_month'].astype('str')
    fig = px.bar(df_mom_bathrooms, x = 'date_month', y = 'price', 
                    width = 800, 
                    height = 494, 
                    color='price',
                    text_auto='.2s',
                    title = 'Propoerties with 3 bathrooms')
    return fig

def create_charts (*charts):
    c1, c2 = st.columns(2)

    c1.plotly_chart(charts[0])
    c2.plotly_chart(charts[1])
    c1.plotly_chart(charts[2])
    c2.plotly_chart(charts[3])
    c1.plotly_chart(charts[4])

    return None

def create_recommendation_tables (data):

    c1,c2 = st.columns(2)

    df_buying_recommendations = data.loc[data['status'] == 'buy', ['id','price']]
    c1.markdown('# Buying recommendations')
    c1.write(df_buying_recommendations)

    df_selling_recommendation = data[['id','selling_price']]
    c2.markdown('# Selling price recommendations')
    c2.write(df_selling_recommendation)

    return None

if __name__ == "__main__":

    data = get_data('datasets/kc_house_data.csv')
    df_prepared = data_preparation(data)

    st.markdown('# House Rocket Insights')
    st.markdown('# Hypothesis')

    chart1 = hypothesis1(df_prepared)
    chart2 = hypothesis2(df_prepared)
    chart3 = hypothesis3(df_prepared)
    chart4 = hypothesis4(df_prepared)
    chart5 = hypothesis5(df_prepared)

    create_charts(chart1,chart2,chart3,chart4,chart5)
    create_recommendation_tables(df_prepared)







