from lib.employees import Employees

if __name__ == "__main__":
    add_tester()


class Tester(Employees):
    def __init__(self, name: str, surname: str, age: int, salary: int, skills: str):
        Employees.__init__(self, name, surname, age, salary, skills)
        self.__skills = skills
    
   

def add_tester():
    try:
        name = str(input("Enter name tester ==> "))
        surname = str(input("Enter surnametester ==> "))
        age = int(input("Enter age tester ==> "))
        salary = int(input("Enter salary tester ==> "))
        skill = str(input("Enter skill tester ==> "))
        new_tester = Tester(name, surname, age, salary, skill)
        return new_tester
    except:
        print("ERROR. Wrong data type")