# Smart Park

## About
An smart parking system that will detect parked cars using opencv and arduino for a real-life model. The information is stored in a MariaDB database and statistics/UI are shown in Streamlit framework

## Setup 

### Requirements
1. To install the requirements, type this command:
``` bash
pip install -r requirements.txt
```

2. Set up the database (we are using mariadb):
https://mariadb.com/kb/en/getting-installing-and-upgrading-mariadb/ 

3. Activate the database using command:
```bash
mariadb -u {username} -p
```

4. Once mariadb is activated, use the following queries
``` sql
CREATE TABLE PARKING_SLOTS (
    DetectedTime Timestamp NOT NULL,
    Slot1 BOOLEAN NOT NULL,
    Slot2 BOOLEAN NOT NULL,
    Slot3 BOOLEAN NOT NULL,
    Slot4 BOOLEAN NOT NULL,
    Slot5 BOOLEAN NOT NULL,
    Slot6 BOOLEAN NOT NULL,
    Slot7 BOOLEAN NOT NULL,
    Slot8 BOOLEAN NOT NULL,
    Slot9 BOOLEAN NOT NULL,
    Slot10 BOOLEAN NOT NULL,
    Slot11 BOOLEAN NOT NULL
);
```

5. Hardware tools used: 
Webcam,/.... (TO DO**)

### Run
1. To run the UI application, write command:
``` bash
streamlit run streamlit.py
```
 **NOTE: to get up to date information for slots changing, you must refresh page**
 
 2. Connect micro USB-B to USB port to computer
 
 3. To run the parking slot demonstration, write command:
 ``` bash
 python3 install app.py
```
 
 
## Snapshots
TO-do -- after video made


## Videos
To-do -- after video made
