import os
import time

hosts = ["8,8,8,8","1.1.1.1","192.168.56.1"]
while True:
    print("DNS control")
    for elem in hosts:
        response = os.system(f"ping -n 1 {elem} > null")
        print(response)
        if response == 0:
            print(elem,"Your DNS ip adress is confrimed")
        else:
            print(elem,"Your DNS ip adress is denied")
        print("-"*30)
        time.sleep(5)