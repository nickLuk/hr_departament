from lib.employees import Employees

if __name__ == "__main__":
    add_banalyst()


class BAnalyst(Employees):
    def __init__(self, name: str, surname: str, age: int, salary: int, skills: str):
        Employees.__init__(self, name, surname, age, salary, skills)
        self.__skills = skills
  
   
def add_banalyst():
    try:
        name = str(input("Enter name business analyst ==> "))
        surname = str(input("Enter surname business analyst ==> "))
        age = int(input("Enter  age  business analyst==> "))
        salary = int(input("Enter salary business analyst ==> "))
        skill = str(input("Enter  skill  business analyst==> "))
        new_banalyst = BAnalyst(name, surname, age, salary, skill)
        return new_banalyst
    except:
        print("ERROR. Wrong data type")