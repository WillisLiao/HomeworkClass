from Student import Student
from Teacher import Teacher
from Person import Person

def main():
    while True:
        action = input("add student[S]\tchange student[G]\tshow student[C]\nadd teacher[T]\tchange teacher[U]\tshow teacher[B]\nadd staff[K]\tchange staff[F]\t        show staff[A]\nexit[E]\nwhat do you want?:")

        if action =="S":
            studentlist = []
            m = 0
            while True:
                m += 1
                name = input('name:') 
                id = input('id: ') 
                height = input('height:')
                weight = input('weight:')
                gender = input('gender:')
                address = input('address: ')
                email = input('email: ')
                phone = input('phone:')
                subject = input('subject: ')
                credit = input('credit: ')
                score = input('score: ')
                studentlist.append(Student(name, id , height, weight, gender, address, email, phone, subject, credit, score ))
                more = input("type A if you're done\ntype B to add more: ")
                if more == "A":
                    break
        elif action =="G":
                for  i in range(0,len(studentlist)):
                    print(f"{studentlist[i-1][0]}. 學生名: {studentlist[i-1][1]}\t學號: {studentlist[i-1][2]}\tHeight: {studentlist[i-1][3]}\tWeight: {studentlist[i-1][4]}\t性別: {studentlist[i-1][5]}\t地址: {studentlist[i-1][6]}\tEmail: {studentlist[i-1][7]}\t聯絡電話: {studentlist[i-1][8]}\t科目: {studentlist[i-1][9]}\t學分: {studentlist[i-1][10]}\t分數: {studentlist[i-1][11]}\n")
                number = int(input("欲修改之學生編號: "))
                for i in range(1,len(studentlist)+1):
                    if i == number : 
                        newName = input("欲修改之姓名: ")
                        newID = input("欲修改之學號: ")
                        newHeight = input("欲修改之身高: ")
                        newWeight = input("欲修改之體重: ")
                        newGender = input("欲修改之性別: ")
                        newAddress = input("欲修改之地址: ")
                        newEmail = input("欲修改之電子郵件: ")
                        newPhone = input("欲修改之聯絡電話: ")
                        newSubject = input("欲修改之科目: ")
                        newCredit = input("欲修改之學分: ")
                        newScore = input("欲修改之成績: ")
                        global student1
                        if newName!= '':
                            student1.setName(newName)
                            studentlist[i-1][1] = student1.getName()
                        if newID !='':
                            student1.setID(newID)
                            studentlist[i-1][2] = student1.getID()
                        if newHeight !='':
                            student1.setHeight(newHeight)
                            studentlist[i-1][3] = student1.getHeight()
                        if newWeight !='':
                            student1.setWeight(newWeight)
                            studentlist[i-1][4] = student1.getWeight()
                        if newGender!= '':
                            student1.setGender(newGender)
                            studentlist[i-1][5] = student1.getGender()
                        if newAddress!= '':
                            student1.setAddress(newAddress)
                            studentlist[i-1][6] = student1.getAddress()
                        if newEmail!= '':
                            student1.setEmail(newEmail)
                            studentlist[i-1][7] = student1.getEmail()
                        if newPhone!= '':
                            student1.setPhone(newPhone)
                            studentlist[i-1][8] = student1.getPhone()
                        if newSubject!= '':
                            student1.setSubject(newSubject)
                            studentlist[i-1][9] = student1.getSubject()
                        if newCredit!= '':
                            student1.setCredit(newCredit)
                            studentlist[i-1][10] = student1.getCredit()
                        if newScore!= '':
                            student1.setScore(newScore)
                            studentlist[i-1][11] = student1.getScore()
            
        
        elif action =="C":
            for i in range(m):
                studentlist[i].ShowStudentInfo()

        elif action =="T":
            pass

        elif action =="U":
            pass

        elif action =="B":
            pass

        elif action =="K":
            pass

        elif action =="F":
            pass

        elif action =="V":
            pass

        elif action =="E":
            break


































    

        
        
        
        
    for i in range(m):

            studentlist[i].ShowInfo()
    






if __name__=='__main__':
    main()

