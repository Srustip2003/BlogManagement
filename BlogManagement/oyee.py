from importlib.resources import contents
from json import load
from logging import root
from msilib.schema import ComboBox, Error
from pickletools import uint1
import sys
from tkinter import Tk, Widget
import tkinter
from turtle import title
from unicodedata import category
from PyQt5 import QtWidgets
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import mysql.connector as conn
import colorama
from colorama import Fore, Back, Style

class r1(QMainWindow):
    def __init__(self):
        super(r1,self).__init__()
        loadUi("untitled444.ui",self)

        # self.pushButton.clicked.connect(self.back1)
        self.pushButton.clicked.connect(self.Like)
        self.pushButton_2.clicked.connect(self.Dislike)

        # self.but.clicked.connect(self.button)

    # def button(self):
        title= self.lineEdit.text()
        db=conn.connect(host="localhost",user="root",password="",database="example")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM details where title='"+title+"'")
        result=cursor.fetchone()
        self.lineEdit_2.setText(result[2])
        self.lineEdit_3.setText(result[3])


    def Like(self):
        
        global NumL
        NumL=int(self.lineEdit_2.text())
         
        NumL+=1
        self.lineEdit_2.setText(str(NumL))
        title = self.lineEdit.text()
        likee=self.lineEdit_2.text()
        db=conn.connect(host="localhost",user="root",password="",database="project")
        cursor=db.cursor()
        cursor.execute("UPDATE `example`.`details` SET `Likeee` = '"+likee+"' WHERE (`title` = '"+title+"')")
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

    # def back1(self):
    #     s4.show()
    #     s6.close()
App=QApplication(sys.argv)

s6=r1()

s6.show()
App.exec()
