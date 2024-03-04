import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import streamlit as st 

all_df = pd.read_csv("all_data.csv")

st.header('Bike Sharing Analysis :sparkles:')

datetime_columns = ["date"]
all_df.sort_values(by="date", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["date"].min()
max_date = all_df["date"].max()

with st.sidebar:
    st.image("https://images.unsplash.com/photo-1455641374154-422f32e234cd?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

    start_date, end_date = st.date_input(
        label="Select Date Range",min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
main_df = all_df[(all_df["date"] >= str(start_date)) & (all_df["date"] <= str(end_date))]


col1,col2,col3 = st.columns(3)

with col1:
    total_orders = main_df.total_count.sum()
    st.metric("Total : ", value=total_orders)
with col2:
    total_orders = main_df.casual.sum()
    st.metric("Casual : ", value=total_orders)
with col3:
    total_orders = main_df.registered.sum()
    st.metric("Registered : ", value=total_orders)
    
st.subheader("Data Overview")

columns = ['casual', 'registered', 'total_count']

fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(main_df['date'], main_df['total_count'],label="total_count")
plt.plot(main_df['date'], main_df['casual'],label="casual")
plt.plot(main_df['date'], main_df['registered'],label="registered")
plt.xlabel('Date',size=15)
plt.ylabel('Count',size=15)
plt.legend()
st.pyplot(fig)


st.subheader('1. Musim yang mendapat permintaan bike terbanyak')

fig,ax = plt.subplots(figsize=(10,6))

sns.barplot(x='season', y='total_count', data=main_df,hue="year")

plt.xlabel("Season")
plt.ylabel("Total")

st.pyplot(fig)

st.subheader('2. Hubungan antara kecepatan angin terhadap permintaan bike')

fig,ax = plt.subplots(figsize=(10,6))

sns.scatterplot(x='windspeed', y='total_count', data=main_df,hue="season")

plt.xlabel("Windspeed")
plt.ylabel("Total")

plt.tight_layout()

st.pyplot(fig)