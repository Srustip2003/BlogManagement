from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PySide2 import*
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from mysql.connector import Error
from fileinput import filename
import sys
from tkinter import messagebox
import tkinter  as tk 
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tokenize import Name
from PIL import Image, ImageTk
import io
from turtle import title, window_width
import PyQt5
import mysql.connector as conn
from PyQt5 import QtWidgets

class displaypage(QMainWindow):    
        
    def __init__(self):
        super(displaypage,self).__init__()
        loadUi("riyasawant.ui",self)
           
    def ds(self):
        self.show()
        title=self.name.toPlainText()
        db=conn.connect(host="localhost",user="root",password="",database="example")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM details where title='"+title+"'")
        result=cursor.fetchone()
        
        self.name.setPlainText(result[0])
        self.cont.setPlainText(result[1])
        # self.colour.setText(result[1])
        # self.discpt.setText(result[3])
        db.commit()

class Shirtss(QMainWindow):
    def __init__(self):
        super(Shirtss,self).__init__()
        loadUi("ReadBlogs.ui",self)
        self.display = displaypage()
    
        self.pushButton_3.clicked.connect(self.passinfof1)

           
    def passinfof1(self):
        self.display.name.setPlainText(self.name.toPlainText())
        self.display.ds()


App=QApplication(sys.argv)
# dp=displaypage()
ss=Shirtss()

ss.show()
App.exec()