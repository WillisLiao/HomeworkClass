
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x300')



def openNewWindow():
    root = Tk()
    root.geometry('400x300')

    root.withdraw()
    newWindow1 = Toplevel(root)
    newWindow1.title("New Window ")
    newWindow1.geometry("400x300")
    Label(newWindow1, text="add new object").pack()
    btn = Button(newWindow1,
                 text = "Close",
                 command = lambda: newWindowClose(newWindow1))
    btn.pack(pady = 5)

    L1 = Label(newWindow1, text="name, ID, height, weight, gender, address, email, phone")
    L1.pack()
    entry1 = Entry(newWindow1, width = 20)
    entry1.pack()

    entry2 = Entry(newWindow1, width = 20)
    entry2.pack()

    entry3 = Entry(newWindow1, width = 20)
    entry3.pack()

    entry4 = Entry(newWindow1, width = 20)
    entry4.pack()

    entry5 = Entry(newWindow1, width = 20)
    entry5.pack()

    entry6 = Entry(newWindow1, width = 20)
    entry6.pack()

    entry7 = Entry(newWindow1, width = 20)
    entry7.pack()

    entry8 = Entry(newWindow1, width = 20)
    entry8.pack()
    def button_command():
        text = entry1.get()
        text2 = entry2.get()
        text3 = entry3.get()
        text4 = entry4.get()
        text5 = entry5.get()
        text6 = entry6.get()
        text7 = entry7.get()
        text8 = entry8.get()
        list.append( Person(text, text2, text3, text4, text5, text6, text7, text8) )

        print("Added successfully!\nClose this window and click Show person list")
        return None
    Button(newWindow1, text="Add", command=button_command).pack()


def openNewWindow2():
    root.withdraw()
    newWindow2 = Toplevel(root)
    newWindow2.title("New Window 2")
    newWindow2.geometry("400x300") 
    Label(newWindow2, text="choose which property to change\n first bar for Subject\nsecond for Credit\n third for Score").pack()
    #
    entryA = Entry(newWindow2, width = 20)
    entryA.pack()

    entryB = Entry(newWindow2, width = 20)
    entryB.pack()

    entryC = Entry(newWindow2, width = 20)
    entryC.pack()

    def button_command2():
        A = entryA.get()
        if A == '':
            pass
        else:
            ChangeSubjectClass1(A)
        B = entryB.get()
        if B =='':
            pass
        else:
            ChangeCreditClass1(B)
        C = entryC.get()
        if C =='':
            pass
        else:
            ChangeScoreClass1(C)
        print("Changed successfully! click Show class list")
    def button_command3():
        A = entryA.get()
        if A =='':
            pass
        else:
            ChangeSubjectClass2(A)
        B = entryB.get()
        if B =='':
            pass
        else:
            ChangeCreditClass2(B)
        C = entryC.get()
        if C =='':
            pass
        else:
            ChangeScoreClass2(C)
        print("Changed successfully! click Show class list")

    def button_command4():
        A = entryA.get()
        if A =='':
            pass
        else:
            ChangeSubjectClass3(A)
        B = entryB.get()
        if B =='':
            pass
        else:        
            ChangeCreditClass3(B)
        C = entryC.get()
        if C =='':
            pass
        else:
            ChangeScoreClass3(C)    
        print("Changed successfully! click Show class list")
    
    Button(newWindow2, text="class1", command=button_command2).pack()
    Button(newWindow2, text="class2", command=button_command3).pack()
    Button(newWindow2, text="class3", command=button_command4).pack()
    Button(newWindow2, text="Show class info", command=ShowClassInfo).pack()

    btn = Button(newWindow2,
                 text = "Close",
                 command = lambda: newWindowClose(newWindow2))
    btn.pack(pady = 5)
def openNewWindow3():
    root.withdraw()
    newWindow3 = Toplevel(root)
    newWindow3.title("New Window 3")
    newWindow3.geometry("400x300") 
    Label(newWindow3, text="degree\n major\nweb address").pack()
    #
    entryA = Entry(newWindow3, width = 20)
    entryA.pack()

    entryB = Entry(newWindow3, width = 20)
    entryB.pack()

    entryC = Entry(newWindow3, width = 20)
    entryC.pack()

    def button_command2():
        A = entryA.get()
        if A == '':
            pass
        else:
            ChangeSubjectClass1(A)
        B = entryB.get()
        if B =='':
            pass
        else:
            ChangeCreditClass1(B)
        C = entryC.get()
        if C =='':
            pass
        else:
            ChangeScoreClass1(C)
        print("Changed successfully! click Show class list")
    def button_command3():
        A = entryA.get()
        if A =='':
            pass
        else:
            ChangeSubjectClass2(A)
        B = entryB.get()
        if B =='':
            pass
        else:
            ChangeCreditClass2(B)
        C = entryC.get()
        if C =='':
            pass
        else:
            ChangeScoreClass2(C)
        print("Changed successfully! click Show class list")

    def button_command4():
        A = entryA.get()
        if A =='':
            pass
        else:
            ChangeSubjectClass3(A)
        B = entryB.get()
        if B =='':
            pass
        else:        
            ChangeCreditClass3(B)
        C = entryC.get()
        if C =='':
            pass
        else:
            ChangeScoreClass3(C)    
        print("Changed successfully! click Show class list")

    Button(newWindow3, text="class1", command=button_command2).pack()
    Button(newWindow3, text="class2", command=button_command3).pack()
    Button(newWindow3, text="class3", command=button_command4).pack()
    Button(newWindow3, text="Show class info", command=ShowClassInfo).pack()
    btn = Button(newWindow3,
                 text = "Close",
                 command = lambda: newWindowClose(newWindow3))
    btn.pack(pady = 5)



    #
    btn = Button(newWindow2,
                 text = "Close",
                 command = lambda: newWindowClose(newWindow2))
    btn.pack(pady = 5)
    person3=Person("Joemama", "sadasd", "186", "69", "male", "FengChia", "willisrain04@gmail.com", "0966931862")
    list.append(person3)

def newWindowClose(self):
    root.deiconify()
    self.destroy()

class Person:
    def __init__(self, name, ID , height, weight, gender, address, email, phone ):
        self.name = name
        self.ID = ID 
        self.height = height
        self.weight = weight
        self.gender = gender
        self.address = address
        self.email = email
        self.phone = phone
    
    def setName(self, newName):
        self.name = newName
    def getName(self):
        return self.name

    def setID(self, newID):
        self.__ID = newID
    def getID(self):
        return self.__ID

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

    def setPhone(self, newPhone):
        self.__phone = newPhone
    def getPhone(self):
        return self.__phone  
    def StudentInfo(self):
       print(" name:{}\n ID:{}\n height:{}\n weight:{}\n gender:{}\n address:{}\n email:{}\n phone:{}".format(self.name, self.ID, self.height, self.weight, self.gender, self.address, self.email, self.phone))

# creating list       
list = [] 
  
# appending instances to list 
list.append( Person("Willis", "D1047316", "186", "69", "male", "FengChia", "willisrain04@gmail.com", "0966931862" ) )
print(list)
list.append( Person("Aaron", "D1047316", "186", "69", "male", "FengChia", "willisrain04@gmail.com", "0966931862") )
list.append( Person("XMY", "D1047316", "186", "69", "male", "FengChia", "willisrain04@gmail.com", "0966931862") )


person1=Person("Ice", "D1047316", "186", "69", "male", "FengChia", "willisrain04@gmail.com", "0966931862" )
person2=Person("Cold", "D1047316", "186", "69", "male", "FengChia", "willisrain04@gmail.com", "0966931862")
list.append(person1)

def ShowInfoList():
    for obj in list:
        print( obj.name, obj.ID, obj.height, obj.weight, obj.gender, obj.address, obj.email, obj.phone, sep =' ' )

class Student(Person):
    def __init__(self,subject, credit, score ):
       # super().__init__(name, ID, height, weight, gender, address, email, phone, subject, credit, score)
        self.subject = subject
        self.credit = credit
        self.score = score
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
    def ClassInfo(self):
        print("subject:{}\n credit:{}\n score:{}".format(self.subject, self.credit, self.score))



class1=Student("程式設計(1042393)", "3", "99")
class2=Student("基礎數學(1042393)", "3", "99")
class3=Student("創意思考(1042393)", "3", "99")
def ShowClassInfo():
    class1.ClassInfo()
    class2.ClassInfo()
    class3.ClassInfo()
#################################   
def ChangeSubjectClass1(A):

    class1.setSubject(A)
    class1.getSubject()
def ChangeSubjectClass2(A):

    class2.setSubject(A)
    class2.getSubject()
def ChangeSubjectClass3(A):
    class3.setSubject(A)
    class3.getSubject()
def ChangeCreditClass1(B):

    class1.setCredit(B)
    class1.getCredit()
def ChangeCreditClass2(B):

    class2.setCredit(B)
    class2.getCredit()
def ChangeCreditClass3(B):
    class3.setCredit(B)
    class3.getCredit()
def ChangeScoreClass1(C):

    class1.setScore(C)
    class1.getScore()
def ChangeScoreClass2(C):

    class2.setScore(C)
    class2.getScore()
def ChangeScoreClass3(C):
    class3.setScore(C)
    class3.getScore()
class Teacher(Person):
    def __init__(self,degree, major, web_address ):
        super().__init__(degree, major, web_address)
        self.degree = degree
        self.major = major
        self.web_address = web_address 
    def setSDegree(self, newDegree):
        self.degree = newDegree
    def getDegree(self):
        return self.degree

    def setmMajor(self, newMajor):
        self.credit = newCredit
    def getCredit(self):
        return self.credit

    def setScore(self, newScore):
        self.score = newScore
    def getScore(self):
        return self.score
    def ClassInfo(self):
        print("subject:{}\n credit:{}\n score:{}".format(self.subject, self.credit, self.score))



class1=Student("程式設計(1042393)", "3", "99")
class2=Student("基礎數學(1042393)", "3", "99")
class3=Student("創意思考(1042393)", "3", "99")
def ShowClassInfo():
    class1.ClassInfo()
    class2.ClassInfo()
    class3.ClassInfo()
#################################   
def ChangeSubjectClass1(A):

    class1.setSubject(A)
    class1.getSubject()
def ChangeSubjectClass2(A):

    class2.setSubject(A)
    class2.getSubject()
def ChangeSubjectClass3(A):
    class3.setSubject(A)
    class3.getSubject()
def ChangeCreditClass1(B):

    class1.setCredit(B)
    class1.getCredit()
def ChangeCreditClass2(B):

    class2.setCredit(B)
    class2.getCredit()
def ChangeCreditClass3(B):
    class3.setCredit(B)
    class3.getCredit()
def ChangeScoreClass1(C):

    class1.setScore(C)
    class1.getScore()
def ChangeScoreClass2(C):

    class2.setScore(C)
    class2.getScore()
def ChangeScoreClass3(C):
    class3.setScore(C)
    class3.getScore()
lab1 = Label(root, text="What do you want?")
lab1.pack(pady = 10)
btn1 = Button(root,
              text="Add person",
              command = openNewWindow)
btn1.pack(pady = 10)

btn4 = Button(root,
              text="Add teacher",
              command = openNewWindow3)
btn4.pack(pady = 10)

btn2 = Button(root,
              text="Change student class",
              command = openNewWindow2)
btn2.pack(pady = 10)

btn3 = Button(root,
              text="Show person list",
              command = ShowInfoList)

           
btn3.pack(pady = 10)


root.mainloop()