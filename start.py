from lib.developer import Developer, add_developer
from lib.hr_manager import HRmanager, add_hrmanager 
from lib.business_analyst import BAnalyst, add_banalyst
from lib.tester import Tester, add_tester
from lib.produkt_manager import Pmanager, add_pmanadger
from lib.employees import Employees


import pickle
import json

all_employees = []


def write_json(all_employees):
    with open("emploees.json", "w", encoding="utf-8") as file:
        json.dump(all_employees, file)

def show_info_employees():
    print("Employees")
    i = 1
    for item in all_employees:
        print(f" Id:{i}  \n Name: {item.name} \n Surname: {item.surname} \n Age: {item.age} \n Salary: {item.salary} \n Skills: {item.skills}")
        i += 1

exit = False
while not exit:
    print("=======Human Resources Department=========")
    print("""
    1. Show employees
    2. Add employee
    3. Delete employee
    4. Save in file
    0: Exit
    """)
    try:
        choice = int(input())
        if choice == 1:
            show_info_employees()
        elif choice == 2:
            print("Enter a position of the employee")
            print("""
            1. Developer
            2. Tester
            3. BAnalyst
            4. HPmanager
            5. Pmanager
            """)
            work = int (input())
            if work == 1:
                position = add_developer()
                all_employees.append(position)
                # add_employees(add_developer)
            elif work == 2:
				position = add_tester()
                all_employees.append(position)
                # add_employees(add_tester)
            elif work == 3:
				position = add_banalyst()
                all_employees.append(position)
                # add_employees(add_banalyst)
            elif work == 4:
				position = add_hrmanager()
                all_employees.append(position)
                # add_employees(add_hrmanager)
            elif work == 5:
				position = add_pmanadger()
                all_employees.append(position)
                # add_employees(add_pmanadger)
            elif work == 0:
                break
        elif choice == 3:
            show_info_employees()
            choise_del = int(input("Enter number for delete"))
            all_employees.pop(choise_del-1)
            show_info_employees()
        elif choice == 4:
            write_json(all_employees)
        elif choice == 0:
            exit = True 
        else:
            print("read manual")  
    except Exception as error:
        print("ERROR ===> ", error)  

    
    
      





