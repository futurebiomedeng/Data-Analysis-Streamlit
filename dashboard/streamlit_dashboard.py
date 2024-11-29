import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

st.title('Bike-Rented Dashboard')

st.sidebar.header('Choose an Option to View The Analysis:')
options = st.sidebar.radio("Select a visualization", ['Data Overview', 'Rented Bike Over Time', 'Heatmap'])

def load_data():
    df = pd.read_csv(".\data_dashboard.csv")     
    return df

df = load_data()

if options == 'Data Overview':
    st.subheader("Dataset Overview")
    st.write(df.head(20))
    st.write("The data overview.")

elif options == 'Rented Bike Over Time':
    st.subheader("Total Rentals Over Months")
    st.write('Showing how the bike rented number fluctuated throghout month.')

    plot_img = Image.open("./rentedmonth.png")
    st.image(plot_img, use_column_width=True)

    st.subheader("Total Rentals Over Days")
    st.write('Showing how the bike rented number fluctuated throghout day.')

    plot_img = Image.open("./outputday.png") 
    st.image(plot_img, use_column_width=True)


elif options == 'Heatmap':
    st.subheader('Heatmap Correlation of Every Column')
    st.write('How much does the parameters afefect the total count.')

    corrmat_img = Image.open("./correlation_matrix.png") 
    st.image(corrmat_img, use_column_width=True)

st.subheader("Key Insights")
st.write(
    """
    - Peak bike rentals occur on weekdays, mainly for commuting.
    - Higher temperatures correlate positively with bike rentals.
    - Higher humidity and wind speed negatively affect bike rentals.
    - Seasonality has minimal impact on rental patterns.
    """
)
