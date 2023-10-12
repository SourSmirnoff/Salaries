import time as t


def increase(x, y):
    return x * (y / 100) + x


def experimental_txt(text):
    for char in text:
        print(char, end="", flush=True)
        t.sleep(0.01)


employeeOne = 300
employeeTwo = 400
employeeThree = 500
employeeFour = 550
employeeFive = 600
employeeSix = 700
while True:
    week = 0
    salaries = employeeThree, employeeOne, employeeSix, employeeTwo, employeeFive, employeeFour
    ascendingOrder = sorted(salaries)
    descendingOrder = sorted(salaries, reverse=True)
    experimental_txt(
        "Do you want to see current salaries in ascending order, descending order, or increase the employees "
        "salaries weekly?:\nEnter 1 for Ascending Order\nEnter 2 for Descending Order\nEnter 3 to provide a "
        "weekly salary increase\n")
    selection = int(input())
    if selection == 1:
        experimental_txt("Salaries in Ascending Order: {}\n\n".format(ascendingOrder))
        continue
    elif selection == 2:
        experimental_txt("Salaries in Descending Order: {}\n\n".format(descendingOrder))
        continue
    elif selection == 3:
        experimental_txt("Enter the Salary increase percent as a whole number:\n")
        increaseRate = int(input())
        experimental_txt("How many weeks do you want the salary increase to carryout for?:\n")
        weekAmount = int(input())
        while week <= weekAmount:
            if week == weekAmount:
                experimental_txt("After your {} week(s) of salary increases, your employees final weekly wages will "
                                 "be: \n".format(weekAmount))
                experimental_txt("\nEmployee #1: ${}\nEmployee #2: ${}\nEmployee #3: ${}"
                                 "\nEmployee #4: ${}\nEmployee #5: ${}\nEmployee #6: ${}\n\n".format(employeeOne,
                                                                                                     employeeTwo,
                                                                                                     employeeThree,
                                                                                                     employeeFour,
                                                                                                     employeeFive,
                                                                                                     employeeSix))
                break
            else:
                experimental_txt("\nEmployee Salary Week #{}: \n\nEmployee #1: ${}\nEmployee #2: ${}\nEmployee #3: ${}"
                                 "\nEmployee #4: ${}\nEmployee #5: ${}\nEmployee #6: ${}\n\n".format(week, employeeOne,
                                                                                                     employeeTwo,
                                                                                                     employeeThree,
                                                                                                     employeeFour,
                                                                                                     employeeFive,
                                                                                                     employeeSix))
            newSalaryOne = increase(int(employeeOne), int(increaseRate))
            employeeOne = newSalaryOne
            newSalaryTwo = increase(int(employeeTwo), int(increaseRate))
            employeeTwo = newSalaryTwo
            newSalaryThree = increase(int(employeeThree), int(increaseRate))
            employeeThree = newSalaryThree
            newSalaryFour = increase(int(employeeFour), int(increaseRate))
            employeeFour = newSalaryFour
            newSalaryFive = increase(int(employeeFive), int(increaseRate))
            employeeFive = newSalaryFive
            newSalarySix = increase(int(employeeSix), int(increaseRate))
            employeeSix = newSalarySix
            if week < weekAmount:
                week += 1
            else:
                break
        continue
