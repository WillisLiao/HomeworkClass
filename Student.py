from Person import Person

class Student(Person):
    def __init__(self, name, id , height, weight, gender, address, email, phone, subject, credit, score ):
        self.subject = subject
        self.credit = credit
        self.score =  score
        super().__init__( name, id , height, weight, gender, address, email, phone )

    def setSubject(self, newSubject):
        self.subject = newSubject
    def getSubject(self):
        return self.subject

    def setCredit(self, newCredit):
        self.credit = newCredit
    def getCredit(self):
        return self.credit

    def setScore(self, newScore):
        self.score = newScore
    def getScore(self):
        return self.score  
    
    def ShowInfo(self):
       print("name:{} ID:{} height:{} weight:{} gender:{} address:{} email:{} phone:{} subject:{} credit:{} score:{}".format(self.name, self.getID, self.height, self.weight, self.gender, self.address, self.email, self.getPhone, self.subject, self.credit, self.score))