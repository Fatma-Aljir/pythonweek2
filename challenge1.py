class person:

    def __int__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender



p1 = person("James", 26, "male")
print("Name:", p1.name, "Age:", p1.age, "Gender:", p1.gender)
