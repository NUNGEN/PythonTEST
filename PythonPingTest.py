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

def checkconnection

with open("taskid.cvs", "w", newline="") as file
    writer = csv.writer(file)
    writer.writerow(["Time","Process name", "Memory Usage"])
# Running the aforementioned command and saving its output
output = os.popen('tasklist').read()
test = output.splitlines()
for i in  range (7, len(test))
print(test[i])
    now = datetime.datetime.now()
    proccesName = test[i].split()
    name = proccesName[0]
    memory = proccesName[-2]
print(proccesName)

with open("taskid.cvs", "a", newline="") as file
    writer = csv.writer(file)
    writer.writerow(["Time","Process name", "Memory Usage"])
#D isplaying the output
