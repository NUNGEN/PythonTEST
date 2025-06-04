# import os
# import time
# 
# import csv
# import datetime
# #time status
# #05.04.20.25, OK
# #05.04.20.25, file
# hosts = ["8,8,8,8","1.1.1.1","192.168.56.1"]
# 
# with open("ping_log.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Time", "Status"])
# 
# while True:
#     print("DNS control")
#     for elem in hosts:
#         response = os.system(f"ping -n 1 {elem} > null")
#         print(response)
#         if response == 0:
#             result = "OK"
#             print(elem,"Your DNS ip adress is confrimed")
#         else:
#             result = "File"
#             print(elem,"Your DNS ip adress is denied")
#             
#         with open("ping_log.csv","a",newline = "") as file:
#             writer = csv.writer(file)
#             writer.writerow([now,result])
#             
#         print("-"*30)
#         time.sleep(5)


# with open("ping log.csv", "u", newline="") as file:
#     writer = csv.writer (file)
#     writer.writerow(["Proccess name", "ProcessId"])
# while True:
#     now = datetime.datetime.now()
#     tasks = os.popen("tasklist")
import os
import csv
from datetime import datetime

def collect_process_info(filename="tasklist.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Process Name", "Memory Usage"])
        output = os.popen('tasklist').read().splitlines()
        for line in output[7:]:
            parts = line.split()
            if len(parts) >= 5:
                name = parts[0]
                memory = parts[-2]
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([now, name, memory])

class Event:
    def __init__(self, note, officer_name):
        self.timestamp = datetime.now()
        self.note = note
        self.officer_name = officer_name

    def __str__(self):
        return f"[{self.timestamp:%Y-%m-%d %H:%M:%S}] {self.officer_name}: {self.note}"

class Case:
    def __init__(self, case_id, description):
        self.case_id = case_id
        self.description = description
        self.status = "open"
        self.events = []

    def add_event(self, event):
        if self.status != "closed":
            self.events.append(event)

    def close_case(self):
        self.status = "closed"

    def get_timeline(self):
        return sorted(self.events, key=lambda e: e.timestamp)

    def get_status(self):
        return self.status

    def get_description(self):
        return self.description

    def get_case_id(self):
        return self.case_id

class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number
        self.cases = []

    def assign_case(self, case):
        self.cases.append(case)

    def get_case_by_id(self, case_id):
        return next((case for case in self.cases if case.case_id == case_id), None)

    def get_summary(self):
        open_cases = sum(case.status == "open" for case in self.cases)
        closed_cases = sum(case.status == "closed" for case in self.cases)
        return f"{self.name} ({self.badge_number}) — {open_cases} открытых, {closed_cases} закрытых дел"

    def get_info(self):
        return f"{self.name}, значок № {self.badge_number}"

if __name__ == "__main__":
    collect_process_info()

    officer = PoliceOfficer("John Doe", "12345")

    case1 = Case(1, "Кража со взломом на улице Main, 123")
    case2 = Case(2, "Вандализм в Центральном парке")

    officer.assign_case(case1)
    officer.assign_case(case2)

    event1 = Event("Осмотрел место преступления", officer.name)
    case1.add_event(event1)

    event2 = Event("Допросил свидетеля", officer.name)
    case1.add_event(event2)

    case1.close_case()

    print(officer.get_summary())

    case = officer.get_case_by_id(1)
    if case:
        for e in case.get_timeline():
            print(e)






