class Person:
    def __init__(self, name, surname, age, sex, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.email = email
list = []
licznik = 0
with open('students.txt','r') as file_r:
    for x in file_r:
        if licznik == 0:
            licznik += 1
        else:
            x_split = x.split(',')
            list.append(Person(x_split[0],x_split[1],int(x_split[2]),x_split[3],x_split[4]))
for y in list:
    if(y.age) < 30:
        print(f"{y.name}\t\t{y.surname}\t\t{y.email}")