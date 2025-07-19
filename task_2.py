## Task 2 of Level 4 
import json
import os
import subprocess
from unittest import result
from task_1 import filter_name , get_branch_name , get_current_branch

def get_led_builtin():
    with open("code.cpp", "r") as file:
        lines = file.readlines()
    for line in lines:
        if "LED_BUILTIN" in line:
            led_define_line = line.strip()
            break
    pin = led_define_line.split(" ")[-1].strip(";")
    return pin


if __name__ == "__main__":
    if get_current_branch() == "main" and str(get_led_builtin()) == "13" :
        print("Level 4".center(50, "="))
        print("Task 2".center(10))
        print("""
        Now that you have created the branch 'ESP8266',\n
        You should checkout ESP8266 branch and modify the code.cpp to run on ESP8266 Boards
              """)
        print("----------------------------------------------------------------")
        print("So, please checkout the checkout the branch ESP8266 and modify the code.\n")
        print("LED_BUILTIN for ESP8266 is D4 so change the LED_BUILTIN defenition to D4.\n")
        exit(1)
    elif get_current_branch() == "main" and str(get_led_builtin()) != "13":
        print("Do not change the code in main branch")
        exit(1)

    elif get_current_branch() == "ESP8266" and get_led_builtin() != "D4":
        print("Please change the code.cpp to run on ESP8266 Boards.")
        exit(1)

    elif get_current_branch() == "ESP8266" and  get_led_builtin() == "D4":
        print("You have successfully completed this level.")
        print("You can now proceed to the next task.")
        exit(0)
    else: 
        print("Please change the code.cpp")
