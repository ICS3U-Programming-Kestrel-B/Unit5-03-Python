#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Dec. 5, 2022
# This program asks for a
# grade and then prints the
# average percent of that
# grade


def main():
    # introductory paragraph
    print("This program asks for a")
    print("grade and then prints the")
    print("average percent of that")
    print("grade")
    print("")

    # initializing user_mark
    user_mark = input("Enter a mark: ")

    def calculate(user_mark):
        # initializing user_mark_percent
        user_mark_percent = 0;
        match user_mark:
            case "R":
                user_mark_percent = 24.5;
                return user_mark_percent;
            case "1-":
                user_mark_percent = 51;
                return user_mark_percent;
            case "1":
                user_mark_percent = 54.5;
                return user_mark_percent;
            case "1+":
                user_mark_percent = 58;
                return user_mark_percent;
            case "2-":
                user_mark_percent = 61;
                return user_mark_percent;
            case "2":
                user_mark_percent = 64.5;
                return user_mark_percent;
            case "2+":
                user_mark_percent = 68;
                return user_mark_percent;
            case "3-":
                user_mark_percent = 71;
                return user_mark_percent;
            case "3":
                user_mark_percent = 74.5;
                return user_mark_percent;
            case "3+":
                user_mark_percent = 78;
                return user_mark_percent;
            case "4-":
                user_mark_percent = 83;
                return user_mark_percent;
            case "4":
                user_mark_percent = 90.5;
                return user_mark_percent;
            case "4+":
                user_mark_percent = 97.5;
                return user_mark_percent;
            # invalid input
            case "":
                user_mark_percent = -10;
                return user_mark_percent;
        return user_mark_percent

    # displaying to user
    print(("The mark converted to a percent is {}%.").format(user_mark_percent))


if __name__ == "__main__":
    main()
