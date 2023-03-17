from models import Doctor, NurseLog, UpdateDoctor, UpdateNurseLog
from typing import List
import requests

doctors: List[Doctor] = []
curr_doctor_id = 1

nurses: List[NurseLog] = []
curr_nurse_id = 1

# this function send url with correct routes to request functions b


def url(route: str):
    return f"http://127.0.1:8000/{route}"


def print_recipt():
    print(
        """
        1:get all doctors
        2:get doctor by id
        3:get doctor by name
        4:get all nurse logs
        5:get nurse log by id
        6:get all logged nurse from selected doctor by  id
        7:add new doctor
        8:update new nurse
        9:update doctor info
        10:update logged nurse
        11:delete a doctor by ID
        12:deleted logged nurse by ID
        13:exit api project
        """)


def get_all_doctors():
    print("Get Doctors List: ")
    res = requests.get(url("doctors"))

    if res.status_code == 200:
        return None

    data = res.json()
    # for every variabe in data create a doctor object and print out their info

    for doctor in data:
        doctor = Doctor(id=doctor["id"], first_name=doctor["first_name"],
                        last_name=doctor["last_name"], age=doctor["age"])
        print("....")
        print(f"Doctor ID: {doctor.id}")
        print(f"Doctor Name: {doctor.first_name} {doctor.last_name}")
        print(f"Doctor Age: {doctor.age}")
        doctors.append(doctor)
    return doctors


def get_doctor_by_id():
    doctor_to_find = int(input("Enter Doctor ID: "))

    # cheak if doctors in the database
    print("Get Doctor By ID: ")
    res = requests.get(url(f"doctor_by_id/{doctor_to_find}"))
    if res.status_code == 400:
        print(".....")
        print("Doctor not found")
        return
    if not str.isdigit(doctor_to_find):
        print(".....")
        print("Doctor Id not found")
        return

    # convert data into json
    data = res.json()
    # if input value not found in the database
    if not data:
        print(".....")
        print("Doctor with ID not found")
        return
    for info in data:
        doctor = Doctor(id=info["id"], first_name=info["first_name"],
                        last_name=info["last_name"], age=info["age"])
        print("....")
        print(f"Doctor ID: {doctor.id}")
        print(f"Doctor Name: {doctor.first_name} {doctor.last_name}")
        print(f"Doctor Age: {doctor.age}")


def get_doctor_by_name():
    doctor_to_find = input("Enter Doctor First Name: ")
    doctor_to_find = doctor_to_find.strip().capitalize()

    # cheak if doctors in the database
    print("Get Doctor By Name: ")
    res = requests.get(url(f"doctor_by_name/{doctor_to_find}"))
    if res.status_code == 400:
        print(".....")
        print("Doctor not found")
        return

    # convert data into json
    data = res.json()
    # if input value not found in the database
    if not data:
        print(".....")
        print("Doctor with Name not found")
        return
    for info in data:
        doctor = Doctor(id=info["id"], first_name=info["first_name"],
                        last_name=info["last_name"], age=info["age"])
        print("....")
        print(f"Doctor ID: {doctor.id}")
        print(f"Doctor Name: {doctor.first_name} {doctor.last_name}")
        print(f"Doctor Age: {doctor.age}")


def get_all_nurse_logs():
    print("getting logged nurses:")
    res = requests.get(url("nurse_logs"))
    if res.status_code == 400:
        print(".....")
        print("No nurse logs found")
        return
    data = res.json()

    for nurse in data:
        # create nurse object
        nurse = NurseLog(id=nurse["id"], nurse_name=nurse["nurse_name"],
                         working_hour=nurse["working_hour"], room_num=nurse["room_num"], doctor_id=nurse["doctor_id"])
        print("....")
        print(f"Nurse ID: {nurse.id}")
        print(f"Nurse Name: {nurse.nurse_name}")
        print(f"Nurse Working Hour: {nurse.working_hour}")
        print(f"Nurse Room Number: {nurse.room_num}")
        print(f"Nurse Doctor ID: {nurse.doctor_id}")
        nurses.append(nurse)
    return nurses


def get_nurse_log_by_id():
    nurse_to_find = int(input("Enter Nurse ID: "))

    # cheak tif the doctor with input nurse id is in the database
    print("getting nurse log by id:")
    res = requests.get(url(f"nurse_log_by_id/{nurse_to_find}"))
    if res.status_code == 400:
        print(".....")
        print("Nurse not found")
        return
    if not str.isdigit(nurse_to_find):
        print(".....")
        print("Nurse Id not found")
        return

    # convert data into json
    data = res.json()
    # if input value not found in the database
    if not data:
        print(".....")
        print("Nurse with ID not found")
        return
    for info in data:
        nurse = NurseLog(id=info["id"], nurse_name=info["nurse_name"],
                         working_hour=info["working_hour"], room_num=info["room_num"], doctor_id=info["doctor_id"])
        print("....")
        print(f"Nurse ID: {nurse.id}")
        print(f"Nurse Name: {nurse.nurse_name}")
        print(f"Nurse Working Hour: {nurse.working_hour}")
        print(f"Nurse Room Number: {nurse.room_num}")
        print(f"Nurse Doctor ID: {nurse.doctor_id}")


def get_nurses_by_doctor():
    nurses_to_find = int(input("Enter Doctor ID: "))

    print("getting nurse log by doctor id:")
    res = requests.get(url(f"nurse_log_by_doctor_id/{nurses_to_find}"))
    if res.status_code == 400:
        print(".....")
        print("Nurse not found")
        return
    if not str.isdigit(nurses_to_find):
        print(".....")
        print("Nurse Id not found")
        return

    # convert data into json
    data = res.json()
    # if input value not found in the database
    if not data:
        print(".....")
        print("Nurse with ID not found")
        return
    for info in data:
        nurse = nurse = NurseLog(id=info["id"], nurse_name=info["nurse_name"],
                                 working_hour=info["working_hour"], room_num=info["room_num"], doctor_id=info["doctor_id"])
        print("....")
        print(f"Nurse ID: {nurse.id}")
        print(f"Nurse Name: {nurse.nurse_name}")
        print(f"Nurse Working Hour: {nurse.working_hour}")
        print(f"Nurse Room Number: {nurse.room_num}")
        print(f"Nurse Doctor ID: {nurse.doctor_id}")


def add_new_doctor():

    print("enter info for the new doctor:")
    first_name = input("Enter First Name: ")
    first_name = first_name.strip().capitalize()
    last_name = input("Enter Last Name: ")
    last_name = last_name.strip().capitalize()
    age = int(input("Enter Age: "))
    # id is auto generated
    new_doctor = Doctor(first_name=first_name, last_name=last_name, age=age)

    # send data to the server
    requests.post(url("add_doctor"), json=new_doctor.to_dict())
    print(".....")
    print(f"{first_name} {last_name} has been added into register")


def log_new_nurse():
    print("enter info for the new nurse:")
    print(".....")
    id = int(input("Enter Nurse ID: "))
    nurse_name = input("Enter Nurse Name: ")
    nurse_name = nurse_name.strip().capitalize()
    working_hour = int(input("Enter Working Hour: "))
    room_num = int(input("Enter Room Number: "))
    doctor_id = int(input("Enter Doctor ID: "))

# create new nurse object with what users write

    new_nurse_log = NurseLog(id=id, nurse_name=nurse_name, working_hour=working_hour,
                             room_num=room_num, doctor_id=doctor_id)  # id is auto generated

    # send data to the server
    requests.post(url("add_nurse_log"), json=new_nurse_log.to_dict())
    print(".....")
    print("the new nurse logged into register")


def update_doctor(doctors: List[UpdateDoctor]):
    print("....")
    print("Enter the ID of the doctor you want to update")
    doctor_to_update = int(input("Enter Doctor ID: "))
    if not str.isdigit(doctor_to_update):
        print(".....")
        print("Doctor Id not found")
        return
    # cheak tif the doctor with input doctor id is in the database
    index = None
    for i, doctor in enumerate(doctors):
        if doctor.id == int(doctor_to_update):
            index = i
            break
    if index is None:
        print(".....")
        print("Doctor with ID not found")
        return

    # change the doctor format to dictionary
    doctor = doctors[i].dict()

    # takes new info from user
    print("....")
    f_name = input("Enter First Name(leave empty): ")
    l_name = input("Enter Last Name(leave empty): ")
    age = input("Enter Age(leave empty): ")
    if f_name != "":
        doctor["first_name"] = f_name
    if l_name != "":
        doctor["last_name"] = l_name
    if age != "":
        doctor["age"] = age

    # send data to the server
    res = requests.put(url(f"update_doctor/{doctor_to_update}"), json=doctor)
    if res.status_code == 400:
        print(".....")
        print("doctor info updated successfully")
    else:
        print(".....")
        print("failed to update the doctor info.")


def update_nurse(nurses: List[UpdateNurseLog]):
    print("....")
    print("you are requesting to update logged nurse")
    nurse_to_update = int(input("Enter Nurse ID for update: "))
    if not str.isdigit(nurse_to_update):
        print(".....")
        print("Nurse Id not found")
        return
    # cheak tif the nurse with input nurse id is in the database
    index = None
    for i, nurse in enumerate(nurses):
        if nurse.id == int(nurse_to_update):
            index = i
            break
    if index is None:
        print(".....")
        print("Nurse with ID not found")
        return
    # change the nurse format to dictionary
    nurse = nurses[i].dict()

    # takes new info from user
    print("....")
    nurse_name = input("Enter Nurse Name(leave empty): ")
    working_hour = input("Enter Working Hour(leave empty): ")
    room_num = input("Enter Room Number(leave empty): ")
    doctor_id = input("Enter Doctor ID(leave empty): ")
    if nurse_name != "":
        nurse["nurse_name"] = nurse_name
    if working_hour != "":
        nurse["working_hour"] = working_hour
    if room_num != "":
        nurse["room_num"] = room_num
    if doctor_id != "":
        nurse["doctor_id"] = doctor_id

    # send data to the server
    res = requests.put(url(f"update_nurse_log/{nurse_to_update}"), json=nurse)
    if res.status_code == 400:
        print(".....")
        print("nurse info updated successfully")
    else:
        print(".....")
        print("failed to update the nurse info.")


def delete_doctor(doctors: List[UpdateDoctor]):
    print("deteting doctor from register")
    doctor_to_delate = int(input("Enter Doctor ID for delete: "))
    if not str.isdigit(doctor_to_delate):
        print(".....")
        print("Doctor Id unvalid")
        return
    # cheak tif the doctor with input doctor id is in the database
    index = None
    for i, doctor in enumerate(doctors):
        if doctor.id == int(doctor_to_delate):
            index = i
            break
    if index is None:
        print(".....")
        print("Doctor with ID not found")
        return
    # send data to the server
    res = requests.delete(url(f"delete_doctor/{doctor_to_delate}"))
    print(".....")
    print("successfully deleted doctor from register {doctor_to_delete}.")


def delete_nurse():
    print("deteting nurse from register")
    log_to_delete = int(input("Enter Nurse ID for delete: "))
    if not str.isdigit(log_to_delete):
        print(".....")
        print("Nurse Id unvalid")
        return
    # cheak tif the nurse with input nurse id is in the database
    index = None
    for i, nurse in enumerate(nurses):
        if nurse.id == int(log_to_delete):
            index = i
            break
    if index is None:
        print(".....")
        print("Nurse with ID not found")
        return
    # send data to the server
    res = requests.delete(url(f"delete_nurse_log/{log_to_delete}"))
    print(".....")
    print("successfully deleted nurse from register {log_to_delete}.")


def main():
    print("Welcome to the hospital register")
    print("....")
    print_recipt()
    choice = input("Enter your choice: ")
    choice = choice.strip().lower()
    if not str.isdigit(choice):
        print("Enter a valid  alternatives.")
        return
    match int(choice):
        case 1:
            doctor = get_all_doctors()
        case 2:
            get_doctor_by_id()
        case 3:
            get_doctor_by_name()
        case 4:
            get_all_nurse_logs()
        case 5:
            get_nurse_log_by_id()
        case 6:
            get_nurses_by_doctor()
        case 7:
            add_new_doctor()
        case 8:
            log_new_nurse()
        case 9:
            update_doctor(doctor)
        case 10:
            update_nurse(nurses)
        case 11:
            delete_doctor(doctor)
        case 12:
            delete_nurse(nurses)
        case 13:
            exit()
        case _:
            print("Enter a valid  alternatives.")


while __name__ == "__main__":
    main()
