class Person:
    def __init__(self, name, id , height, weight, gender, address, email, phone ):
        self.name = name
        self.__id = id 
        self.height = height
        self.weight = weight
        self.gender = gender
        self.address = address
        self.email = email
        self.__phone = phone
    
    def setName(self, newName):
        self.name = newName
    def getName(self):
        return self.name
    
    @property
    def id(self):
        return ("No Data")
    @id.setter
    def setID(self, newID):
        self.__id = newID
    @id.getter
    def getID(self):
        return self.__id

    def setHeight(self,newHeight):
        self.height = newHeight
    def getHeight(self):
        return self.height

    def setWeight(self,newWeight):
        self.weight = newWeight
    def getWeight(self):
        return self.weight

    def setGender(self, newGender):
        self.gender = newGender       
    def getGender(self):
        return self.gender

    def setAddress(self, newAddress):
        self.address = newAddress
    def getAddress(self):
        return self.address

    def setEmail(self, newEmail):
        self.email = newEmail
    def getEmail(self):
        return self.email    
    
    @property
    def phone(self):
        return("No Data")

    @phone.setter
    def setPhone(self, newPhone):
        self.__phone = newPhone
    @phone.getter
    def getPhone(self):
        return self.__phone  
    #def StudentInfo(self):
       #print(" name:{}\n ID:{}\n height:{}\n weight:{}\n gender:{}\n address:{}\n email:{}\n phone:{}".format(self.name, self.ID, self.height, self.weight, self.gender, self.address, self.email, self.phone))