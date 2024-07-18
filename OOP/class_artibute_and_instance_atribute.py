class Humans:
    legs = 2# This is a class attribute which is common to all the instances of this class
    def __init__(self, gender : str ="Male", name : str = "Rocky") -> None:
        """Everything defined below is a instance attribute"""
        self.gender = gender
        self.name = name
h = Humans()
print(h.legs)# accesing the class attribute through the instance
print(Humans.legs)# accesing the class attribute through the class itself

#Now accesing the instance attribute
print(h.name)
print(h.gender)

#print(Humans.gender)
"""This throws and error because we are trying to
   access the instance attribute using class itself
"""
# Now lets change the class attribute
h.legs = 3
print(h.legs)# This will show the value 3
print(Humans.legs)# This will show the value 2 
"""This happens because changes made to 
   class attribute is only limited to object
   itself and not in class
"""
h.gender = "Female"
print(h.gender)
