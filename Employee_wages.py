import random
import logging

import self as self

logging.basicConfig(filename="Employee_wages.log", filemode="w")


class Employeewages:

    def employee_wages(self):
        IS_FULL_TIME = 1
        WAGES_PER_Hour = 20
        FULL_DAY_HOUR = 8
        empCheck = random.randint(0, 1)
        if empCheck == IS_FULL_TIME:
            print("Employee is present")
            print("Daily wages of the employee is:- "+str(WAGES_PER_Hour*FULL_DAY_HOUR))
        else:
            print("Employee is not present")


class Main:
    if __name__ == "__main__":
        Employeewages.employee_wages(self)
