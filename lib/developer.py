from lib.employees import Employees

if __name__ == "__main__":
    add_developer()


class Developer(Employees):
    def __init__(self, name: str, surname: str, age: int, salary: int, skills: str):
        Employees.__init__(self, name, surname, age, salary, skills)
        self.__skills: str = skills
 
def add_developer():
    try:
        name = str(input("Enter  name developer ==> "))
        surname = str(input("Enter surname developer ==> "))
        age = int(input("Enter age developer ==> "))
        salary = int(input("Enter salary developer ==> "))
        skills = str(input("Enter skills developer ==> "))
        new_developer = Developer(name, surname, salary, age, skills)
        return new_developer
    except:
        print("ERROR. Wrong data type")
