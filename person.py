class Person:
    def __init__(self, name="Ivan", age="18"):

        self.name = name
        self.age = age

    def getName(self):

        print("Студент:", self.name, self.age)

    def SetNameAge(self):

        self.name = input("Введи імя")
        self.age = input("Введи вік")
        print("Ваші дані оновлено:", self.name, self.age)


class Student(Person):
    def __init__(self, name, age, number):
        super().__init__(name, age)

        self.number = number

        print(self.name, self.age, self.number)

    def setGroupNumber(self):
        self.number = int(input("Введи номер групи"))
        print("Номер групи студента", self.name, "було змінено на:", self.number)
