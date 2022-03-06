from Person import Person
class Teacher(Person):

    def __init__(self, name, id , height, weight, gender, address, email, phone ):
        self.course = ''
        super().__init__( name, id , height, weight, gender, address, email, phone )

    def setCourse(self, newCourse):
        self.course = newCourse
    def getCourse(self):
        return self.course