# import all the necessary libraries

from fastapi import FastAPI
from typing import List, Dict

from db import DB
from models import Doctor, NurseLog, UpdateDoctor, UpdateNurseLog

from fastapi.responses import HTMLResponse

app = FastAPI()
db = DB("doctor.db")

app.doctors: List["Doctor"] = []
app.curr_doctor_id = 1

app.nurses: List["NurseLog"] = []
app.curr_nurse_id = 1

# at least 2 routes to get data (get)


@app.get("/", response_class=HTMLResponse)
def root():
    with open("index.html") as html_file:
        return html_file.read()

# return all doctors


@app.get("/doctors")
def get_doctors():
    data = db.get(table="doctors")
    return data


@app.get("/doctor_by_id/{id}")
def get_doctor_by_id(id: int):
    data = db.get(table="doctors", where={"id": str(id)})
    return data

# Return a diver based on the doctor's name


@app.get("/doctor_by_name/{name}")
def get_doctor_by_name(name: str):
    data = db.get(table="doctors", where=("first_name", name))
    return data

# return a list with all the logs based doctor


@app.get("/api_projects")
def get_nurse():
    data = db.get(table="nurse")
    return data

# return a specific log based on the id


@app.get("/api_projects/{id}")
def get_nurse_by_id(id: int):
    data = db.get(table="nurse", where=("id", str(id)))
    return data

# return all logs based from a specific doctor


@app.get("/api_projects_by_doctor/{id}")
def get_nurse_by_doctor(id: int):
    data = db.get(table="nurse", where=("doctor_id", str(id)))
    return data

# create at least 2 routes to create data (post)


@app.post("/add_doctor")  # add new doctor
def add_doctor(doctor: Doctor):
    doctor.id = app.curr_doctor_id
    app.doctor.append(doctor)
    app.curr_doctor_id += 1
    db.insert(
        table="doctors",
        fields={
            "first_name": doctor.first_name,
            "last_name": doctor.last_name,
            "age": str(doctor.age)
        })

# add new nurse


@app.post("/add_api_project")
def log_doctor(nurse: NurseLog):
    nurse.id = app.curr_nurse_id
    app.curr_nurse_id += 1
    db.insert(
        table="nurse",
        fields={
            "id": str(nurse.id),
            "name": nurse.name,
            "working_hour": nurse.working_hour,
            "room_num": nurse.room_num,
            "doctor_id": str(nurse.doctor_id)
        })

# at least 2 routes to update data (put)
# remember to add id in body (json) when cheaking the thunder client


@app.put("/update_doctor/{id}")
def update_doctor(id: int, doctor: UpdateDoctor):
    data = db.update(
        table="doctors",
        fields={
            "first_name": doctor.first_name,
            "last_name": doctor.last_name,
            "age": str(doctor.age)
        },
        where=("id", str(id)),
    )
    return data


@app.put("/update_api_project/{id}")
def update_api_project(id: int, nurse: UpdateNurseLog):
    data = db.update(
        table="nurse",
        fields={
            "name": nurse.name,
            "working_hour": nurse.working_hour,
            "room_num": nurse.room_num,
            "doctor_id": str(nurse.doctor_id)
        },
        where=("id", str(id)),
    )
    return data

# at least 2 routes to delete data (delete)


@app.delete("/delete_doctor/{id}")  # delete doctor based on id
def delete_doctor(id: int):
    db.delete(table="doctors", where={"id": str(id)})


@app.delete("/delete_api_project/{id}")  # delete nurse based on doc_id
def delete_nurse(id: int):
    db.delete(table="nurses", where={"id": str(id)})
