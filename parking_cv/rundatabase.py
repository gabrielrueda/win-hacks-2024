import mysql.connector
import pandas as pd
import altair as alt
import streamlit as st
from datetime import datetime, date, timedelta

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

# # Define your insert query with placeholders
# insert_query = "INSERT INTO PARKING_SLOTS VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


# # Execute the query with the Python variables as parameters
# cursor.execute(insert_query, ('2024-02-17 11:20:11', 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0))

#1 = slot taken
#0 slot is empty

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
st.write(df)

#TO DO: pass this information to streamlit.py
# - pass "insert to database" code to app.py
# - pass value to parameter for {value}/11 number of car slots available in streamlit.py

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

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()