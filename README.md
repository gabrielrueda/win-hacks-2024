# Smart Park

## About
An smart parking system that will detect parked cars using opencv and arduino for a real-life model. The information is stored in a MariaDB database and statistics/UI are shown in Streamlit framework

![logo](https://github.com/gabrielrueda/win-hacks-2024/assets/93105329/142eee82-6c98-4ad6-99e9-3a8b02e65b61)


## Setup 

### Requirements
1. Clone the repository using command:
```bash
git clone https://github.com/gabrielrueda/win-hacks-2024.git
```

2. To install the requirements, type this command:
``` bash
pip install -r requirements.txt
```

3. Set up the database (we are using mariadb):
https://mariadb.com/kb/en/getting-installing-and-upgrading-mariadb/ 

4. Activate the database using command:
```bash
mariadb -u {username} -p
```

5. Once mariadb is activated, use the following queries
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

6. Hardware tools used: 
Webcam, electric tape for outlining the parking slot sections, model cars (Hot Wheels), Arduino Nano, general electronics, and LED bulbs that will light up if spot is not taken. 

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
![IMG_3431](https://github.com/gabrielrueda/win-hacks-2024/assets/93105329/affad5a3-c802-4a17-a95e-ccb5091b0afb)
![IMG_3432](https://github.com/gabrielrueda/win-hacks-2024/assets/93105329/c9cca96a-c8fe-4633-89ba-bd3662798055)
![screenshot1](https://github.com/gabrielrueda/win-hacks-2024/assets/93105329/68b97951-af28-4ea0-a997-17336c7c3566)
![screenshot3](https://github.com/gabrielrueda/win-hacks-2024/assets/93105329/255dfb48-4232-4095-9297-6b77d5069931)
![screenshot4](https://github.com/gabrielrueda/win-hacks-2024/assets/93105329/d1002780-7bd7-4020-9bfa-aad512f5fa2b)


## Videos
https://youtu.be/vlWlhAm0BZU
