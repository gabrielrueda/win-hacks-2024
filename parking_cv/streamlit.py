import streamlit as st
import pandas as pd
import altair as alt
from datetime import time, timedelta,datetime, date

#parking credentials
st.image('images/parking.jpg', width=100) 
st.title('This is a title')
st.write("123 Park St.")

#gets the current date
today = date.today()
#format the date accordingly
date = today.strftime("%B %d, %Y")
#gets the current time
current_time = datetime.now()
# Format the time in 12-hour format
time_in_12_hour_format = current_time.strftime("%I:%M:%S %p")

#default values -- change later
spot_taken = 0
total_spots = 11

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

        st.write(f"Spots Taken: {spot_taken}")
        st.write(f"Spots Spots: {total_spots}")
        st.write(date)
        st.write(time_in_12_hour_format)

        #sample dataframe -- change once actual data is found
        data = pd.DataFrame({
                                'Variable': ['Something 1', 'Something 2', 'Something 3', 'Something 4'],
                                'Value': [1,
                                        2,
                                        3,
                                        4]  
                        })

        # Used to specify a color for each category
        color_scale = alt.Scale(domain=['Something 1', 'Something 2', 'Something 3', 'Something 4'],
                                                            range=['yellow', 'red', 'blue', 'purple'])

        # Create an altair bar chart with the information
        chart = alt.Chart(data).mark_bar().encode(
                                        x=alt.X('Variable', title='Car Monitoring'), 
                                        y=alt.Y('Value', title='Values'),
                                        tooltip=['Variable', 'Value'],
                                        color=alt.Color('Variable:N', scale=color_scale)  # Specify the color scale
                                    ).properties(
                                        title='48 Hour Statistics for Parking Lot',
                                        width=700,
                                        height=400
                                    ).interactive()  # Corrected typo from interative() to interactive()

        #write the chart to the screen
        st.write(chart)

        # else:
        #     st.write("Authentication error")

else:  # User View
    st.write(date)
    st.write(time_in_12_hour_format)
    st.write(f"{spot_taken} / {total_spots} spots available")


    