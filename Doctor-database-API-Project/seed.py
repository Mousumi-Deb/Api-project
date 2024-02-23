import json
import sqlite3

try:
    # connect to the database
    conn = sqlite3.connect('doctor.db')
    cursor = conn.cursor()

    # open json file
    with open("seed.json") as f:
        data = json.load(f)

    # seed data for table doctors
    for doctor in data['doctors']:
        query = """INSERT INTO doctors (
                first_name, last_name, age
            )
            VALUES (
                ?, ?, ?)"""
        values = (doctor["first_name"], doctor["last_name"], doctor["age"])
        cursor.execute(query, values)

    # seed data for table nurses
    for nurse in data['nurses']:
        query = """INSERT INTO nurses (
                nurse_name, working_hour, room_num, doctor_id
            )
            VALUES (
                ?, ?, ?, ?)"""
        values = (nurse["nurse_name"], nurse["working_hour"],
                  nurse["room_num"], nurse["doctor_id"])
        cursor.execute(query, values)

    # commit changes and close the database connection
    conn.commit()
except Exception as e:
    print("An error occurred:", e)
finally:
    conn.close()
