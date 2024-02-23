CREATE TABLE doctors(
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL
    );

CREATE TABLE nurses (
    id INTEGER PRIMARY KEY,
    nurse_name TEXT NOT NULL,
    working_hours INTEGER NOT NULL,
    room_number INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES doctors (id)
);