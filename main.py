from person import *

p1 = Person()
p1.getName()
p1.SetNameAge()

s1 = Student("Taras", "Nabyt", 10)
s2 = Student("Vasya", "Pupkin", 18)
s3 = Student("Solya", "Chopyk", 21)
a = [s1, s2, s3]
for i in a:
    i.setGroupNumber()
