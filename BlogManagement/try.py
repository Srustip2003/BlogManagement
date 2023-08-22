from contextlib import redirect_stderr
from distutils.util import change_root
from itertools import product
from mailbox import mboxMessage
from msilib.schema import SelfReg
from operator import contains
from pprint import pp
from pydoc import plain
import sys
from tkinter import messagebox, ttk
from tkinter.tix import Tree
# from PyQt4.QtGui import *
from turtle import bgcolor
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
from tkinter.ttk import Treeview

class addn(QMainWindow):
    def __init__(self):
        super(addn,self).__init__()
        loadUi("untitled.ui",self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.pushButton.clicked.connect(self.adddata)
        self.pushButton_2.clicked.connect(self.delete_data)
        self.pushButton_4.clicked.connect(self.view_data)
    
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
        author=self.plainTextEdit.toPlainText()
        db=conn.connect(host="localhost",user="root",password="",db="project")
        cursor=db.cursor()
        cursor.execute("DELETE FROM createblogs WHERE author='"+author+"'")
        db.commit()
        db.close()
        QMessageBox.warning(self,"Error","User Deleted successfully")

    def view_data(self):
        a2.show()
        a1.close()
        cc=self.tableWidget.focus()
        contentt=self.tableWidget.item(cc)
        pp=contentt['values']
        if(len(pp) !=0):
            title=self.lineEdit.text.set(pp[0])
            blog=self.plainTextEdit.toPlainText.set(pp[1])


class viewn(QMainWindow):
    def __init__(self):
        super(viewn,self).__init__()
        loadUi("newpage.ui",self)



App=QApplication(sys.argv)
# a1=demo()
a1=addn()
a2=viewn()
a1.show()

App.exec()