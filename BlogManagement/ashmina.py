from contextlib import redirect_stderr
from distutils.util import change_root
import email
from itertools import product
from msilib.schema import SelfReg
from operator import contains
from pydoc import plain
import sys
from tkinter import ttk
from tkinter.tix import Tree
from tkinter.ttk import Treeview
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
import colorama
from tkinter import *


class displaypage(QMainWindow):
        def __init__(self):
            super(displaypage,self).__init__()
            loadUi("riyasawant.ui",self)
            
        def ds(self):
            self.show()

class rb(QMainWindow):
    def __init__(self):
        super(rb,self).__init__()
        loadUi("ReadBlogs.ui",self)
        self.display = displaypage()
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 400)
        self.pushButton_2.clicked.connect(self.searchblog)
        self.pushButton_4.clicked.connect(self.new)


    def searchblog(self):
        db=conn.connect(host="localhost",user="root",password="",db="project")
        cursor=db.cursor()
        category=self.comboBox.currentText()
        cursor.execute("SELECT author,title ,content from createblogs WHERE category='"+category+"'")

        self.tableWidget.setRowCount(20)
        tablerow= 0
        for row in cursor:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            # self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow+=1



    def new(self):

        row = self.tableWidget.currentRow() # Index of Row
        firstColumnInRow = self.tableWidget.item(row, 1)
        secondColumnInRow = self.tableWidget.item(row, 2) # returns QTableWidgetItem
        title = firstColumnInRow.text()
        content=secondColumnInRow.text() # content of this
        self.display.name.setPlainText(title)
        self.display.cont.setPlainText(content)
        self.display.ds()

        



App=QApplication(sys.argv)

s15=rb()
s16=displaypage()
s15.show()
App.exec()   
