
import subprocess

def get_led_builtin():
    with open("code.cpp", "r") as file:
        lines = file.readlines()
    for line in lines:
        if "LED_BUILTIN" in line:
            led_define_line = line.strip()
            break
    pin = led_define_line.split(" ")[-1].strip(";")
    return pin

def filter_name(branch_name):
    if branch_name.startswith("*"):
        return branch_name[1:].strip()
    return branch_name.strip()
def get_branch_names():
    branches = subprocess.run(
        ["git", "branch"],
        stdout=subprocess.PIPE,
        text=True,
    )
    branch_names = branches.stdout.strip().split("\n")
    return [filter_name(name) for name in branch_names]
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

status = "detached" if "detached" in get_current_branch().split(" ") else "not detached"
if __name__ == "__main__":
    if status == "detached":
        if  "Arduino" not in get_branch_names() and "ESP8266" in get_branch_names():
            print("Level 2".center(50, "="))
            print("Task 4".center(10))
            print("""
            Now that you found the old code for Arduino boards, i want you to create a new branch called 'Arduino' and move the old code to that branch.\n
            And then you will have 3 branches, 'main', 'ESP8266' and 'Arduino'.\n
            But now there is a problem that , 'main' branch is for ESP8266 and the 'ESP8266' branch is for ESP8266 boards\n
            So you have to remove the redundant branch 'ESP8266' and keep only the branches 'Arduino' and 'main'""")
            print("----------------------------------------------------------------")
            print('Your task is to create a new branch called "Arduino" from this commit.')
            print("Please comeback after checking out the older commit ")
            exit(1)
        elif "Arduino" in get_branch_names(): 
            if "ESP8266" in get_branch_names():
                print("You have successfully created new branch for 'Arduino' boards.")
                print("Now you should delete the 'ESP8266' branch.")
                exit(1)
            else:
                print("You have successfully deleted the 'ESP8266' branch.")
                print("checkout to 'main' branch and proceed to the next task.")
                exit(0)
        else:
            if get_current_branch() == "main":
                print("You have completed all the tasks now answer the quiz")
                print("to answer the quiz, run python quiz.py")
                exit(0)