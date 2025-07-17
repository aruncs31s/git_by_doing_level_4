## Task 3 of Level 4 
from task_1 import filter_name , get_branch_name , get_current_branch
from task_2 import get_led_builtin


if __name__ == "__main__":
    if get_current_branch() == "ESP8266":
        print("Level 2".center(50, "="))
        print("Task 3".center(10))
        print("""
        But after they started to using esp8266 boards, they realize a thing that , esp8266 boards are super cheep. So now they want the 'main' branch to be updated to support ESP8266 boards, and remove the old code for Arduino boards.\n
        But doing that will break support for Arduino boards, so you want to keep the old code for Arduino boards in a separate branch.
              """)
        print("----------------------------------------------------------------")
        print('Your task is to go to main and modify the code to run on ESP8266 Boards.')
        print("Please comeback after creating the specified branch  ")
        exit(1)
    elif get_current_branch() == "main" and get_led_builtin() != "D4":
        print("You have to also modify the code.")
        exit(1)
    elif get_current_branch() == "main" and get_led_builtin() == "D4":
        print("You have successfully edited the code and main branch is now only supports ESP8266.")
        print("You can now proceed to the next task.")
        exit(0)
    else:
        print("Try again")