#!/usr/bin/env python3
import hashlib

"""
If you found self here , this a just a python script using only the print and input functions.
"""


def main():

    print("Level 4".center(50, "="))
    print()

    should_continue = input("Did you finish reading README (y/N): ").lower().strip()

    if should_continue not in ["y", "yes"]:
        print("Please read the README".center(50))
        exit(1)
    print("")
    print("Question 1:")
    print("Imaigine you are asked to create a new branch called new-branch.")
    print("Which command would you use to create the specified branch? ")
    print()

    ans_1 = input("Please enter the command: ").lower().strip()

    if hashlib.md5(ans_1.encode()).hexdigest() not in [
        "57bbe662f351b2cb134e6116368b7f89",
        "1adfba80874d51bf721f36a04e2a2058",
    ]:
        print("Incorrect! Please read level_0 again.")
        return

    print("Correct!")

    print()

    print("Question 2:")
    print("Which command is used to checkout that specified branch? ")
    ans_2 = input("Please enter the command: ").lower().strip()

    if hashlib.md5(ans_2.encode()).hexdigest() not in [
        "f5f30735bee7060fd7d1fe2737159182"
    ]:
        print("Incorrect! Please read level_0 again.")
        return

    print("Correct!")

    print()

    print("Question 3:")
    print("You want to immediately create a new branch and switch to it.")

    ans_3 = (
        input("Which command can be used to create and switch to a new branch? ")
        .lower()
        .strip()
    )

    if ans_3 not in ["git switch -c new-branch"]:
        print("Incorrect! Read the README again.")
        return

    print("Correct!")

    print()
    print("Question 4:")
    print("You want to delete a branch called new-branch.")
    ans_4 = input("Which command would you use to delete the branch? ").lower().strip()
    if hashlib.md5(ans_4.encode()).hexdigest() not in [
        "5f0c5ab3073c41947a069eddfcc41e53"
    ]:
        print("Incorrect! Please read level_0 again.")
        return
    print("Correct!")

    print()
    print("Question 5:")
    print("You want to force delete a branch called new-branch.")
    ans_5 = input("Which command would you use to force delete the branch? ").strip()
    if hashlib.md5(ans_5.encode()).hexdigest() not in [
        "cf6b55e617e2c3484bbb5c34c1a920b0"
    ]:
        print("Incorrect! Please read level_0 again.")
        return
    print("Correct!")

    print()
    print("Question 6: ")
    print("Which commit does HEAD point to ")
    print("1. Very first commit")
    print("2. Current commit")
    print("3. Last commit")
    ans_6 = input("Please enter the answer: ").lower().strip()
    if ans_6 != "2":
        print("Incorrect! Please read level_0 again.")
        exit(0)
    print("Correct!")

    print("Question 7:")
    print("what does detached HEAD mean? ")
    print("1. When HEAD points to a branch")
    print("2. When HEAD points directly to a commit instead of a branch")
    ans_7 = input("Please enter the answer: ").lower().strip()
    if ans_7 != "2":
        print("Incorrect! Please read level_0 again.")
        exit(0)
    print("Correct!")
    print()
    print(" Level 4 Completed ".center(50, "="))


if __name__ == "__main__":
    main()
