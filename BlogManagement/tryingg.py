from contextlib import redirect_stderr
from distutils.util import change_root
from itertools import product
from mailbox import mboxMessage
from msilib.schema import SelfReg
from operator import contains
from pydoc import plain
import sys
from tkinter import messagebox, ttk
from tkinter.tix import Tree
# from PyQt4.QtGui import *
from turtle import bgcolor, title
from unicodedata import category
from unittest import result
from xml.sax.handler import ContentHandler
from PyQt5 import QtWidgets
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import mysql.connector as conn
from PyQt5.QtGui import QPixmap
from pymysql import NULL
from tkinter import *
from colorama import Fore, Back, Style

class addn(QMainWindow):
    def __init__(self):
        super(addn,self).__init__()
        loadUi("untitled.ui",self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.pushButton.clicked.connect(self.adddata)
        self.pushButton_2.clicked.connect(self.delete_data)
        # self.pushButton_3.clicked.connect(self.refresh)
    
    def adddata(self):
        db=conn.connect(host="localhost",user="root",password="",db="project")
        cursor=db.cursor()
        category=self.comboBox.currentText()
        cursor.execute("SELECT emailid ,author,title from createblogs WHERE category='"+category+"'")

        self.tableWidget.setRowCount(50)
        tablerow= 0
        for row in cursor:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1
        db.commit()


    def delete_data(self):
        author=self.lineEdit.text()

        db=conn.connect(host="localhost",user="root",password="",db="project")
        cursor=db.cursor()
        cursor.execute("DELETE FROM createblogs WHERE author='"+author+"'")
        db.commit()
        db.close()
        QMessageBox.warning(self,"Error","Deleted successfully")

    # def refresh(self):
    #     db=conn.connect(host="localhost",user="root",password="",db="project")
    #     cursor=db.cursor()
        
    #     query = "SELECT * FROM createblogs"
    #     result = cursor.execute(query)
    #     self.tableWidget.setRowCount(0)
    #     for row_number, row_data in enumerate(result):
    #         self.tableWidget.insertRow(row_number)
    #         for column_number, data in enumerate(row_data):
    #             self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
    #     db.close()



App=QApplication(sys.argv)
# a1=demo()
a1=addn()
a1.show()
App.exec()