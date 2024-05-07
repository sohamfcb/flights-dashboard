import streamlit as st
from dbhelper import DB
import plotly.graph_objs as go
import plotly.express as px

db=DB()

st.sidebar.title('Flights Dashboard')

user_option=st.sidebar.selectbox('Menu',['Check Flights','Analytics'])

if user_option=='Check Flights':
    city=db.fetch_city_names()
    st.title('Check Flights')
    col1,col2=st.columns(2)

    with col1:
        source=st.selectbox('Source',sorted(city))

    with col2:
        destination=st.selectbox('Destination',sorted(city))

    if st.button('Search'):
        results=db.fetch_all_flights(source,destination)
        st.dataframe(results)

elif user_option=='Analytics':
    st.title('Analytics')

    airline,frequency=db.fetch_airline_frequency()

    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)



    city,frequency=db.busy_airport()

    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


    date, frequency2 = db.daily_frequency()

    # print(len(date))
    # print(len(frequency2))
    fig = px.line(
        x=date,
        y=frequency2
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    st.title('Tell me about the project')


