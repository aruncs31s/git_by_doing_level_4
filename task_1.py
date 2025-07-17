## Task 1 of Level 4 
import json
import os
import subprocess
from unittest import result

def check_branch_branches():
      branches = subprocess.run(
        ["git", "branch"],
        stdout=subprocess.PIPE,
        text=True,
        )
      branch_count = len(str(branches.stdout).strip().split("\n"))
      return branch_count

def filter_name(branch_name):
    if branch_name.startswith("*"):
        return branch_name[1:].strip()
    return branch_name.strip()

def get_branch_name():
    branches = subprocess.run(
        ["git", "branch"],
        stdout=subprocess.PIPE,
        text=True,
    )
    branch_names =  branches.stdout.strip().split("\n")
    filtered_names = [filter_name(name) for name in branch_names]
    return filtered_names
def get_current_branch():
    branches = subprocess.run(
        ["git", "branch"],
        stdout=subprocess.PIPE,
        text=True,
    )
    branch_names = branches.stdout.strip().split("\n")
    for name in branch_names:
        if name.startswith("*"):
            branch_name = filter_name(name)
            break
    return branch_name


if __name__ == "__main__":
    if check_branch_branches() < 2 and get_current_branch() == "main":
        print("Level 2".center(50, "="))
        print("Task 1".center(10))
        print("""
        This directory contains the the code for the famous LED Blink\n
        But this code is for Arduino Boards \n
        But we also want to run this code on ESP8266 Boards\n
        So we are converting this code to run on ESP8266 Boards\n
        and We want to keep the old code for Arduino as the main code.\n
        Inorder to do that we have to create a new branch and do the ESP8266 code there.""")
        print("----------------------------------------------------------------")
        print('Your task is to create a new branch named "ESP8266"')
        print("Please comeback after creating the specified branch  ")
        exit(1)
    elif "ESP8266" not in get_branch_name():
        print('Your task is to create a new branch named "ESP8266"')
        print("Please comeback after creating the specified branch  ")
        exit(1)
    else:
        print("You have successfully created the branch 'ESP8266'.")
        print("You can now proceed to the next task.")
        exit(0)
