# Constructors
# special method in a class used 
# to create and initialize an object of a class.
# Constructor is invoked automatically when an object of a class is created.

# def __init__(self):
	# initializations

# Parameterized Constructor in Python

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")


# Default Constructor in Python
class Details1:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details1()