from lib.employees import Employees

if __name__ == "__main__":
    add_pmanadger()


class Pmanager(Employees):
    def __init__(self, name: str, surname: str, age: int, salary: int, skills: str):
        Employees.__init__(self, name, surname, age, salary, skills)
        self.__skills = skills


def add_pmanadger():
    try:
        name = str(input("Enter name produkt manager ===> "))
        surname = str(input("Enter surnameprodukt manager ===> "))
        age = int(input("Enter age produkt manager ===> "))
        salary = int(input("Enter salary produkt manager ===> "))
        skill = str(input("Enter skill produkt manager ===> "))
        new_pmanadger = Pmanager(name, surname, age, salary, skill)
        return new_pmanadger
    except:
        print("ERROR. Wrong data type")
