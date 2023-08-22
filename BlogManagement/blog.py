import email
from importlib.resources import contents
from json import load
from logging import root
from msilib.schema import ComboBox, Error
from pickletools import uint1
import sys
from tkinter import Tk, Widget, messagebox
import tkinter
from turtle import title
from unicodedata import category
from PyQt5 import QtWidgets
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import mysql.connector as conn
import colorama
import re
from colorama import Fore, Back, Style
class ms(QMainWindow):
    def __init__(self):
        super(ms,self).__init__()
        loadUi("MainWindow.ui",self)
        self.pushButton.clicked.connect(self.userlogin)
        self.pushButton_admin.clicked.connect(self.adminlogin)

    def userlogin(self):
        s2.show()
        s1.close()

    def adminlogin(self):
        s5.show()
        s1.close()

class al(QMainWindow):
    def __init__(self):
        super(al,self).__init__()
        loadUi("AdminloginWindow.ui",self)
        self.pushButton.clicked.connect(self.adminlogin)

    def adminlogin(self):
        name=self.lineEdit.text()
        password=self.lineEdit_2.text()
        if self.lineEdit.text()=="riya" and self.lineEdit_2.text()=="123" or self.lineEdit.text()=="ritvik" and self.lineEdit_2.text()=="123" or self.lineEdit.text()=="tanishq" and self.lineEdit_2.text()=="123" or self.lineEdit.text()=="srusti" and self.lineEdit_2.text()=="123":
            QMessageBox.information(self,"Login Output","Login Successfull")
            s5.close()
            s12.show()
        elif name==" " or password==" ":
            QMessageBox.information(self,"Error","Enter all the details")

        else:
            QMessageBox.information(self,"Error","Invalid Username or Password")

class amp(QMainWindow):
    def __init__(self):
        super(amp,self).__init__()
        loadUi("AdminPageWindow.ui",self)
        self.pushButton_2.clicked.connect(self.addblogadmin)
        self.pushButton_3.clicked.connect(self.logoutadmin)
        self.pushButton_4.clicked.connect(self.manageuser)
        

    def addblogadmin(self):
        s12.close()
        s13.show()

    def logoutadmin(self):
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to logout ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            s12.close()
            s1.show()

    def manageuser(self):
        s12.close()
        s14.show()


class mu(QMainWindow):
    def __init__(self):
        super(mu,self).__init__()
        loadUi("ManageUser.ui",self)
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 300)
        self.pushButton_3.clicked.connect(self.back5)
        self.pushButton_2.clicked.connect(self.showuser)
        self.pushButton.clicked.connect(self.deleteuser)

    def showuser(self):

        db=conn.connect(host="localhost",user="root",password="",db="project")
        cursor=db.cursor()
        query=("SELECT * FROM blogs")
        cursor.execute(query)
        
        self.tableWidget.setRowCount(30)
        tablerow=0
        for row in cursor:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1

        db.commit()
        db.close()

    def deleteuser(self):
        author=self.plainTextEdit.toPlainText()
        db=conn.connect(host="localhost",user="root",password="",db="project")
        cursor=db.cursor()
        cursor.execute("DELETE FROM blogs WHERE author='"+author+"'")
        db.commit()
        db.close()
        QMessageBox.warning(self,"Error","User Deleted successfully")
        

    def back5(self):
        s14.close()
        s12.show()


class abp(QMainWindow):
    def __init__(self):
        super(abp,self).__init__()
        loadUi("CreateWindowAdmin.ui",self)
        self.pushButton_2.clicked.connect(self.back6)
      
    def back6(self):
        s13.close()
        s12.show()


class ab(QMainWindow):
    def __init__(self):
        super(ab,self).__init__()
        loadUi("LoginWindow.ui",self)
        self.pushButton_4.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.login)

    def login(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        db=conn.connect(host="localhost",user="root",password="",db="project")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM details where username='"+username+"' and password='"+password+"'")
        result=cursor.fetchone()
        if result: 
            QMessageBox.information(self,"Login Output","Login Successful")
            s4.show()
            s2.close()

        elif username==" " or password==" ":
            QMessageBox.information(self,"Login Output","Enter all the details")

        else:
            QMessageBox.information(self,"Login Output","Invalid Credentials")
 
    def register(self):
        s2.close()
        s3.show()

class rs(QMainWindow):
    def __init__(self):
        super(rs,self).__init__()
        loadUi("RegisterWindow.ui",self)
        self.pushButton_5.clicked.connect(self.register1)

    def register1(self):
        username=self.lineEdit.text()
        emailid=self.lineEdit_2.text()
        password=self.lineEdit_3.text()
        confirmpassword=self.lineEdit_4.text()
        k,j,d=0,0,0
        db=conn.connect(host="localhost",user="root",password="",db="project")
        cursor=db.cursor()
        cursor.execute("SELECT username FROM details where username='"+username+"'")
        result=cursor.fetchone()

        if result:
            QMessageBox.information(self,"Login form","This data already exists")
        if username=="" or emailid=="" or password=="" or confirmpassword=="":
            QMessageBox.information(self,"Login Output","Enter all the details")
        elif password != confirmpassword:
            QMessageBox.information(self,"Login form","Confirm your Password")
 
        if len(emailid)>=12:
            if emailid[0].isalpha():
                if ("@" in emailid) and (emailid.count("@")==1):
                    if (emailid[-4]=="."):
                        db=conn.connect(host="localhost",user="root",password="",database="project")
                        cursor=db.cursor()
                        cursor.execute("Select * from details where emailid ='"+emailid+"'")
                        row=cursor.fetchone()
                        if row!=None:
                            messagebox.showerror("Error","User already exist, Please Login")
                        else:
                            cursor.execute("INSERT INTO details values('"+username+"','"+emailid+"','"+password+"','"+confirmpassword+"')")
                            db.commit()
                            db.close()
                            messagebox.showinfo("Registration Successfull","Successfully Registered")
                            s2.show()
                            s3.close()

                        
                    else:
                        messagebox.showerror("Error","Enter valid email address with .com")
                else:
                    messagebox.showerror("Error","Enter valid email address with @")
            else:
                messagebox.showerror("Error","First character should be alphabet")
            
        else:
            messagebox.showerror("Error","Invallid Email Adress")

 
class hp(QMainWindow):
    def __init__(self):
        super(hp,self).__init__()
        loadUi("HomeWindow.ui",self)
        self.pushButton_6.clicked.connect(self.recomend1)
        self.pushButton_11.clicked.connect(self.recomend2)
        self.pushButton_9.clicked.connect(self.recomend3)
        self.pushButton_12.clicked.connect(self.recomend4)
        self.pushButton_7.clicked.connect(self.createblogs)
        self.pushButton_4.clicked.connect(self.logout)
        self.pushButton_8.clicked.connect(self.readblogs)

    def recomend1(self):
       s6.show()
       s4.close()
    
    def recomend2(self):
        s7.show()
        s4.close()

    def recomend3(self):
        s8.show()
        s4.close()

    def recomend4(self):
        s9.show()
        s4.close()
    
    def createblogs(self):
        s10.show()
        s4.close()

    def logout(self):
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to logout ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            s4.close()
            s1.show()

    def readblogs(self):
        s4.close()
        s15.show()

class displaypage(QMainWindow):
    def __init__(self):
        super(displaypage,self).__init__()
        loadUi("riyasawant.ui",self)
        self.pushButton.clicked.connect(self.Like)
        self.pushButton_2.clicked.connect(self.Dislike)
        self.pushButton_3.clicked.connect(self.back7)

        # self.but.clicked.connect(self.button)

    # def button(self):
        title = self.name.toPlainText()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM blogs where title='"+title+"'")
        result=cursor.fetchone()




    def Like(self):
        
        global NumL
        NumL=int(self.like.text())
         
        NumL+=1
        self.like.setText(str(NumL))
        title = self.name.toPlainText()
        likee=self.like.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `project`.`blogs` SET `likee` = '"+likee+"' WHERE (`title` = '"+title+"')")
        db.commit()

    def Dislike(self):
        

        global NumD
        
        NumD=int(self.dlike.text())
         
        NumD+=1
        self.dlike.setText(str(NumD))
        title = self.name.toPlainText()
        dislike=self.dlike.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `project`.`blogs` SET `dislike` = '"+dislike+"' WHERE (`title` = '"+title+"')")
        db.commit()

    def ds(self):
            self.show()

    def fs(self):

            self.show()
            title=self.name.toPlainText()
            db=conn.connect(host="localhost",user="root",password="",database="project")
            cursor=db.cursor()
            cursor.execute("SELECT * FROM blogs where title='"+title+"'")
            result=cursor.fetchone()
        
            self.name.setPlainText(result[2])
            self.cont.setPlainText(result[4])
            self.like.setText(result[5])
            self.dlike.setText(result[6])
        # self.colour.setText(result[1])
        # self.discpt.setText(result[3])
            db.commit()

    def back7(self):
        s16.close()
        s15.show()

class rb(QMainWindow):
    def __init__(self):
        super(rb,self).__init__()
        loadUi("ReadBlogs.ui",self)
        self.display = displaypage()
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 600)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.pushButton_2.clicked.connect(self.searchblog)
        self.pushButton_4.clicked.connect(self.new)
        self.pushButton_3.clicked.connect(self.findblog)
        self.pushButton.clicked.connect(self.back)



    def searchblog(self):
        db=conn.connect(host="localhost",user="root",password="",db="project")
        cursor=db.cursor()
        category=self.comboBox.currentText()
        cursor.execute("SELECT author,title ,content, likee , dislike from blogs WHERE category='"+category+"'")

        self.tableWidget.setRowCount(20)
        tablerow= 0
        for row in cursor:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            # self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow+=1



    def new(self):

        row = self.tableWidget.currentRow() # Index of Row
        firstColumnInRow = self.tableWidget.item(row, 1)
        secondColumnInRow = self.tableWidget.item(row, 2) # returns QTableWidgetItem
        thirdColumnInRow = self.tableWidget.item(row, 3)
        fourthColumnInRow = self.tableWidget.item(row, 4)
        title = firstColumnInRow.text()
        content=secondColumnInRow.text()
        Like = thirdColumnInRow.text()
        Dislike = fourthColumnInRow.text() # content of this
        self.display.name.setPlainText(title)
        self.display.cont.setPlainText(content)
        self.display.like.setText(Like)
        self.display.dlike.setText(Dislike)

        self.display.ds()
        self.pushButton_3.clicked.connect(self.back)

    def back(self):
        s15.show()
        s16.close()


    def findblog(self):
        self.display.name.setPlainText(self.name.toPlainText())
        self.display.fs()


    def back(self):
        s15.close()
        s4.show()
         



class r1(QMainWindow):
    def __init__(self):
        super(r1,self).__init__()
        loadUi("Recomand1Window.ui",self)

        self.pushButton.clicked.connect(self.back1)
        self.pushButton_2.clicked.connect(self.Like)
        self.pushButton_3.clicked.connect(self.Dislike)

        # self.but.clicked.connect(self.button)

    # def button(self):
        title= self.lineEdit.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM blogs where title='"+title+"'")
        result=cursor.fetchone()
        # self.lineEdit_2.setText(result[5])
        # self.lineEdit_3.setText(result[6])


    def Like(self):
        
        global NumL
        NumL=int(self.lineEdit_2.text())
         
        NumL+=1
        self.lineEdit_2.setText(str(NumL))
        title = self.lineEdit.text()
        likee=self.lineEdit_2.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `project`.`blogs` SET `likee` = '"+likee+"' WHERE (`title` = '"+title+"')")
        db.commit()

    def Dislike(self):

        global NumD
        NumD=int(self.lineEdit_3.text())
         
        NumD+=1
        self.lineEdit_3.setText(str(NumD))
        title = self.lineEdit.text()
        dislike=self.lineEdit_3.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `project`.`blogs` SET `dislike` = '"+dislike+"' WHERE (`title` = '"+title+"')")
        db.commit()

    def back1(self):
        s4.show()
        s6.close()

class r2(QMainWindow):
    def __init__(self):
        super(r2,self).__init__()
        loadUi("Recomand2Window.ui",self)
        self.pushButton.clicked.connect(self.back2)
        self.pushButton_2.clicked.connect(self.Like)
        self.pushButton_3.clicked.connect(self.Dislike)

        # self.but.clicked.connect(self.button)

    # def button(self):
        title= self.lineEdit.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM blogs where title='"+title+"'")
        result=cursor.fetchone()
        # self.lineEdit_2.setText(result[5])
        # self.lineEdit_3.setText(result[6])


    def Like(self):
        
        global NumL
        NumL=int(self.lineEdit_2.text())
         
        NumL+=1
        self.lineEdit_2.setText(str(NumL))
        title = self.lineEdit.text()
        likee=self.lineEdit_2.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `project`.`blogs` SET `likee` = '"+likee+"' WHERE (`title` = '"+title+"')")
        db.commit()

    def Dislike(self):

        global NumD
        NumD=int(self.lineEdit_3.text())
         
        NumD+=1
        self.lineEdit_3.setText(str(NumD))
        title = self.lineEdit.text()
        dislike=self.lineEdit_3.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `project`.`blogs` SET `dislike` = '"+dislike+"' WHERE (`title` = '"+title+"')")
        db.commit()

    def back2(self):
        s4.show()
        s7.close()

class r3(QMainWindow):
    def __init__(self):
        super(r3,self).__init__()
        loadUi("Recomand3Window.ui",self)
        self.pushButton.clicked.connect(self.back3)
        self.pushButton_2.clicked.connect(self.Like)
        self.pushButton_3.clicked.connect(self.Dislike)

        # self.but.clicked.connect(self.button)

    # def button(self):
        title= self.lineEdit.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM blogs where title='"+title+"'")
        result=cursor.fetchone()



    def Like(self):
        
        global NumL
        NumL=int(self.lineEdit_2.text())
         
        NumL+=1
        self.lineEdit_2.setText(str(NumL))
        title = self.lineEdit.text()
        likee=self.lineEdit_2.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `project`.`blogs` SET `likee` = '"+likee+"' WHERE (`title` = '"+title+"')")
        db.commit()

    def Dislike(self):

        global NumD
        NumD=int(self.lineEdit_3.text())
         
        NumD+=1
        self.lineEdit_3.setText(str(NumD))
        title = self.lineEdit.text()
        dislike=self.lineEdit_3.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `project`.`blogs` SET `dislike` = '"+dislike+"' WHERE (`title` = '"+title+"')")
        db.commit()

    def back3(self):
        s4.show()
        s8.close()

class r4(QMainWindow):
    def __init__(self):
        super(r4,self).__init__()
        loadUi("Recomand4Window.ui",self)
        self.pushButton.clicked.connect(self.back4)
        self.pushButton_2.clicked.connect(self.Like)
        self.pushButton_3.clicked.connect(self.Dislike)

        # self.but.clicked.connect(self.button)

    # def button(self):
        # title= self.lineEdit.text()
        # db=conn.connect(host="localhost",user="root",password="",database="project")
        # cursor=db.cursor()
        # cursor.execute("SELECT * FROM blogs where title='"+title+"'")
        # result=cursor.fetchone()
        # self.lineEdit_2.setText(result[5])
        # self.lineEdit_3.setText(result[6])


    def Like(self):
        
        global NumL
        NumL=int(self.lineEdit_2.text())
         
        NumL+=1
        self.lineEdit_2.setText(str(NumL))
        title = self.lineEdit.text()
        likee=self.lineEdit_2.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `project`.`blogs` SET `likee` = '"+likee+"' WHERE (`title` = '"+title+"')")
        db.commit()

    def Dislike(self):

        global NumD
        NumD=int(self.lineEdit_3.text())
         
        NumD+=1
        self.lineEdit_3.setText(str(NumD))
        title = self.lineEdit.text()
        dislike=self.lineEdit_3.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `project`.`blogs` SET `dislike` = '"+dislike+"' WHERE (`title` = '"+title+"')")
        db.commit()

    def back4(self):
        s4.show()
        s9.close()

class tc(QDialog):
    def __init__(self):
        super(tc,self).__init__()
        loadUi("ConditionsWindow.ui",self)
        self.pushButton.clicked.connect(self.createblog)

    def createblog(self):
        if self.checkBox.isChecked()==True:
            s10.close()
            s11.show()
            
        else:
            QMessageBox.information(self,"Invalid","Aceept all the terms and conditions")

class cb(QDialog):
    def __init__(self):
        super(cb,self).__init__()
        loadUi("CreateWindow.ui",self)
        self.pushButton_2.clicked.connect(self.publishblog)
        self.pushButton.clicked.connect(self.back5)
        

    def publishblog(self):
        mydb=conn.connect(
            host="localhost",
            user="root",
            password="",
            database="project"
        )
        mycursor=mydb.cursor()
        emailid=self.lineEdit.text()
        title=self.lineEdit_2.text()
        author=self.lineEdit_3.text()
        category=self.comboBox.currentText()
        content=self.plainTextEdit.toPlainText()


        # outcome=mycursor.fetchone()
        colorama.init()
        db=conn.connect(host="localhost",user="root",password="",db="project")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM blogs where title='"+title+"'")
        result=cursor.fetchone()

        if result:
            QMessageBox.information(self,"Login form","This blog already exists")


    
        elif("mortal"in content):
            spam=True
        elif("religion" in content):
            spam=True
        elif ("corruption" in content):
            spam=True
        elif("politics" in content):
            spam=True
        elif("illegal" in content):
            spam=True
        elif (len(content)>=2000):
            spam=True
        else:
            spam=False

        if (spam):
            QMessageBox.information(self,"Error","Invalid words have been used")

        else:
                    query="INSERT INTO blogs (emailid,author,title,category,content) VALUES (%s,%s,%s,%s,%s)"
                    value=(emailid,author,title,category,content)

                    mycursor.execute(query,value)
                    mydb.commit()
                    QMessageBox.information(self,"Login Output","Succesfully Published!")
                    s4.show()
                    s11.close()
    def back5(self):
        s4.show()
        s11.close()



App=QApplication(sys.argv)
s1=ms()
s2=ab()
s3=rs()
s4=hp()
s5=al()
s6=r1()
s7=r2()
s8=r3()
s9=r4()
s10=tc()
s11=cb()
s12=amp()
s13=abp()
s14=mu()
s15=rb()
s16=displaypage()
s1.show()
App.exec()