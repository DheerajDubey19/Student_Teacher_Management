#Custom Exception for the age error
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age is less than 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)

#Custom Exception for the name error
class InvalidNameError(Exception):
    def __init__(self, name, message="Name is too short"):
        self.name = name
        self.message = message
        super().__init__(self.message)

