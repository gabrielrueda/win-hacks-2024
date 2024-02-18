import streamlit as st
import pandas as pd
import altair as alt
from datetime import time, timedelta,datetime, date
import mysql.connector

#parking credentials
st.image('images/parking.jpg', width=100) 
st.title('Smart Lot')
st.write("123 Park St.")


#gets the current date
today = date.today()
#format the date accordingly
date = today.strftime("%B %d, %Y")
#gets the current time
current_time = datetime.now()
# Format the time in 12-hour format
time_in_12_hour_format = current_time.strftime("%I:%M:%S %p")


#where i am storing database authorization credentials
credentials = []

#import credentials from a text file
with open('credentials.txt', 'r') as f:
    for content in f:
        #add to array of content
        credentials.append(content.strip())

#db credentials for database\
conn = mysql.connector.connect(
    host=credentials[0],
    user=credentials[1],
    password=credentials[2],
    database=credentials[3]
)

# Create a cursor object
cursor = conn.cursor()

#1 = slot taken
#0 slot is empty

#go this once it is activated
cursor.execute("SELECT * FROM PARKING_SLOTS;")
#gets values
slot_values = cursor.fetchall()


data_df = {
    'date': [],
    'value': []
}

#gets get the time in the last 48 hours -- generate a graph of data made in the last 48 hours
current_time = datetime.now()
two_days_ago = current_time - timedelta(days=2)

for slot in slot_values:
    #append new value in dataframe where 
    if slot[0] >= two_days_ago:
        data_df['date'].append(slot[0].strftime('%Y-%m-%d %H:%M:%S'))
        data_df['value'].append(sum(slot[1:]))


df = pd.DataFrame.from_dict(data_df)

#gets the largest value in row
cursor.execute("SELECT * FROM PARKING_SLOTS ORDER BY DetectedTime DESC LIMIT 1;")
slots_taken = cursor.fetchall()

spots_taken = 0

for slots in slots_taken:
    spots_taken = 10 - sum(slots[1:])


#our sample parking spot space 
total_spots = 10

#this is for the options for the display manager
option = st.selectbox(
    'Profile Options:',
    ('User View', 'Admin View'))

# if 'find_button' not in st.session_state:
#     st.session_state.find_button = False

# if 'authenticate_button' not in st.session_state:
#     st.session_state.authenticate_button = False

# Handling authentication and displaying data based on option selected
if option == "Admin View":
    # Check if authentication button is clicked 
    if st.button("Authenticate"):
        #check if password is correct
        #this is for user authentication
        # password = st.text_input("Enter password", value="", max_chars=None, type="password")
        # if password == "hello":  # Change to your actual password
        # Display data for admin

        st.write(f"Spots Taken: {spots_taken}")
        st.write(f"Spots Spots: {total_spots}")
        st.write(date)
        st.write(time_in_12_hour_format)

        #sample dataframe -- change once actual data is found          
        chart = alt.Chart(df).mark_line(color='blue').encode(
                x=alt.X('date', title='Time'), 
                y=alt.Y('value', title='Number of available cars'),
                tooltip=['date', 'value']
            ).properties(
                title='Line Graph of Available Cars Slots in the Last 48 Hours',
                width=700,
                height=400
            )
        st.altair_chart(chart, use_container_width=True)

        # else:
        #     st.write("Authentication error")

else:  # User View
    container = st.container(border=True)
    container.write(date)
    container.write(time_in_12_hour_format)
    container.write(f"{spots_taken} / {total_spots} spots available")


    