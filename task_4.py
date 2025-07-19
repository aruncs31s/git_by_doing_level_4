
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
    if status != "detached":
        print("Level 4".center(50, "="))
        print("Task 4".center(10))
        print("""
        After editing you've realized that you forgot to backup the old code for Arduino boards.\n
        You have to continue support for Arduino boards, 
       """)
        print("----------------------------------------------------------------")
        print('Your task is to checkout older commit where the code was for Arduino boards.')
        print("Please comeback after checking out the older commit ")
        exit(1)
    if status == "detached":
        if get_led_builtin() == "D4":
            print("This is not the commit we are looking for")
            exit(1)
        elif get_led_builtin() == "13":
            print("You have found the old code for Arduino boards.")
            print("You can now proceed to the next task.")
            exit(1)
