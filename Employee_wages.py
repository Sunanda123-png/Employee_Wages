import random
import logging

import self as self

logging.basicConfig(filename="Employee_wages.log", filemode="w")


class Employeewages:

    def employee_wages(self):
        """
        :return:
        """
        PART_TIME=1
        IS_FULL_TIME = 2
        ABSENT=0
        WAGES_PER_Hour = 20
        FULL_DAY_HOUR = 8
        PART_DAY_HOUR = 4
        attendence={IS_FULL_TIME:
                        "Employee is present fulltime, " "Daily wages of the employee is:- "+str(WAGES_PER_Hour*FULL_DAY_HOUR),
                    PART_TIME:
                        "Employee is present part time, ""Daily wages of the employee is:- " + str(WAGES_PER_Hour * PART_DAY_HOUR),
                    ABSENT:
                        "Employee is not present"
                    }
        empCheck = random.randint(0, 2)
        print(attendence.get(empCheck))


class Main:
    if __name__ == "__main__":
        Employeewages.employee_wages(self)
