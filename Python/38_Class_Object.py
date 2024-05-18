class Details:
    name = "Rohan"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()

print(obj1.name)
print(obj1.age)

obj1.desc()

obj2 = Details()
obj2.name = "Hritik"
obj2.age = 25
obj2.desc()