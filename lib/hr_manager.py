from lib.employees import Employees

if __name__ == "__main__":
    add_hrmanager()


class HRmanager(Employees):
    def __init__(self, name: str, surname: str, age: int, salary: int, skills: str):
        Employees.__init__(self, name, surname, age, salary, skills)
        self.__skills = skills
    
   
def add_hrmanager():
    try:
        name = str(input("Enter name hr manager ==> "))
        surname = str(input("Enter surname hr manager ==> "))
        age = int(input("Enter age hr manager ==> "))
        salary = int(input("Enter age hr manager ==> "))
        skill = str(input("Enter skill hr manager ==> "))
        new_hrmanager = HRmanager(name, surname, age, salary, skill)
        return new_hrmanager
    except:
        print("ERROR. Wrong data type")