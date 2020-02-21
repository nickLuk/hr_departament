if __name__ == "__main__":
    pass


class Employees:

    def __init__(self, name: str, surname: str, age: int, salary: int, skills: str):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__salary = salary
        self.__skills = skills

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname
        return self.__surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
        return self.__age

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary
        return self.__salary
    
    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, skills):
        self.__skills = skills
        return self.__skills

    def show_info(self):
        print("Name: ", self.__name, "\nSurname ", self.__surname,
              "\nAge ", self.__age, "\nSalary", self.__salary, "\nSkills", self.__skills)
