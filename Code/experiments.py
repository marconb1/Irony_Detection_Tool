# -*- coding: utf-8 -*-

####
#### The script runs on python 2.7. All the information is printed on the screen
####

#### Authors: Marco Nemetz Bochernisan e Larissa Astrogildo de Freitas
#### Version: 1.0
#### Date: 20/01/14

# Import Libraries
# Necessary PyQt4 library

import sys
import qrc_resources
import table
import os
import re
import csv
from PyQt4.QtCore import *
from PyQt4.QtGui import *

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s:s

class MainWindow(QMainWindow):

    NextId = 1
    Instances = set() 

    def __init__(self, filename = QString(), parent=None):
            
        super(MainWindow, self).__init__(parent)    
        
        self.setAttribute(Qt.WA_DeleteOnClose)
        MainWindow.Instances.add(self)      
        self.nometexto = QLabel(self)
        self.nometexto.setGeometry(QRect(55,57,50,50))
        self.nometexto.setObjectName(_fromUtf8("nometexto"))
        self.nometexto.setText(QApplication.translate("MainWindow", "Review", None, QApplication.UnicodeUTF8))  #criancao das tabs
        self.tabWidget = QTabWidget(self) 
        self.tabWidget.setGeometry(QRect(40,60, 1100, 850))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
             
        self.tabDetection = QWidget() 
        self.tabDetection.setObjectName(_fromUtf8("TabDetection")) 
        
        self.editor = QPlainTextEdit(self.tabDetection)
        self.editor.setGeometry(QRect(30,10,560,650))
        self.editor.setObjectName(_fromUtf8("editor"))

        textAba1 = open("Tweets/listOfTweetsFimDoMundo.txt").read()     
        self.editor.setPlainText(_fromUtf8(textAba1))
    
        self.radioButtonP1 = QRadioButton(self.tabDetection)
        self.radioButtonP1.setGeometry(QRect(600, 10, 60, 22))
        self.radioButtonP1.setObjectName(_fromUtf8("radioButton_1"))
        self.radioButtonP2 = QRadioButton(self.tabDetection)
        self.radioButtonP2.setGeometry(QRect(600, 30, 60, 22))
        self.radioButtonP2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButtonP3 = QRadioButton(self.tabDetection)
        self.radioButtonP3.setGeometry(QRect(600, 50, 60, 22))
        self.radioButtonP3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButtonP4 = QRadioButton(self.tabDetection)
        self.radioButtonP4.setGeometry(QRect(600, 70, 60, 22))
        self.radioButtonP4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButtonP5 = QRadioButton(self.tabDetection)
        self.radioButtonP5.setGeometry(QRect(600, 90, 60, 22))
        self.radioButtonP5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButtonP6 = QRadioButton(self.tabDetection)
        self.radioButtonP6.setGeometry(QRect(600, 110, 60, 22))
        self.radioButtonP6.setObjectName(_fromUtf8("radioButton_6"))
        self.radioButtonP7 = QRadioButton(self.tabDetection)
        self.radioButtonP7.setGeometry(QRect(600, 130, 60, 22))
        self.radioButtonP7.setObjectName(_fromUtf8("radioButton_7"))
        self.radioButtonP8 = QRadioButton(self.tabDetection)
        self.radioButtonP8.setGeometry(QRect(600, 150, 60, 22))
        self.radioButtonP8.setObjectName(_fromUtf8("radioButton_8"))
        self.radioButtonP9 = QRadioButton(self.tabDetection)
        self.radioButtonP9.setGeometry(QRect(600, 170, 60, 22))
        self.radioButtonP9.setObjectName(_fromUtf8("radioButton_9"))
        self.radioButtonP10 = QRadioButton(self.tabDetection)
        self.radioButtonP10.setGeometry(QRect(600, 190, 60, 22))
        self.radioButtonP10.setObjectName(_fromUtf8("radioButton_10"))
        self.radioButtonP11 = QRadioButton(self.tabDetection)
        self.radioButtonP11.setGeometry(QRect(600, 210, 60, 22))
        self.radioButtonP11.setObjectName(_fromUtf8("radioButton_11"))
        self.radioButtonP12 = QRadioButton(self.tabDetection)
        self.radioButtonP12.setGeometry(QRect(600, 230, 60, 22))
        self.radioButtonP12.setObjectName(_fromUtf8("radioButton_12"))
        self.radioButtonP13 = QRadioButton(self.tabDetection)
        self.radioButtonP13.setGeometry(QRect(600, 250, 60, 22))
        self.radioButtonP13.setObjectName(_fromUtf8("radioButton_13"))
        self.radioButtonP14 = QRadioButton(self.tabDetection)
        self.radioButtonP14.setGeometry(QRect(600, 270, 60, 22))
        self.radioButtonP14.setObjectName(_fromUtf8("radioButton_14"))
        self.radioButtonP15 = QRadioButton(self.tabDetection)
        self.radioButtonP15.setGeometry(QRect(600, 290, 60, 22))
        self.radioButtonP15.setObjectName(_fromUtf8("radioButton_15"))
        self.radioButtonP16 = QRadioButton(self.tabDetection)
        self.radioButtonP16.setGeometry(QRect(600, 310, 60, 22))
        self.radioButtonP16.setObjectName(_fromUtf8("radioButton_16"))
        
        self.nomep1 = QLabel(self.tabDetection)
        self.nomep1.setGeometry(QRect(650, 10, 400, 22))
        self.nomep1.setObjectName(_fromUtf8("nometexto3"))
        self.nomep1.setText(QApplication.translate("MainWindow", "List of Laughter Expression", None, QApplication.UnicodeUTF8))
  
        self.nomep2 = QLabel(self.tabDetection)
        self.nomep2.setGeometry(QRect(650,30,400,22))
        self.nomep2.setObjectName(_fromUtf8("nometexto"))
        self.nomep2.setText(QApplication.translate("MainWindow", "List of Emoticons", None, QApplication.UnicodeUTF8))

        self.nomep3 = QLabel(self.tabDetection)
        self.nomep3.setGeometry(QRect(650,50,400,22))
        self.nomep3.setObjectName(_fromUtf8("nometexto"))       
        self.nomep3.setText(QApplication.translate("MainWindow", "“só que”", None, QApplication.UnicodeUTF8))
        
        self.nomep4 = QLabel(self.tabDetection)
        self.nomep4.setGeometry(QRect(650,70,400,22))
        self.nomep4.setObjectName(_fromUtf8("nometexto"))
        self.nomep4.setText(QApplication.translate("MainWindow", "“sim,”", None, QApplication.UnicodeUTF8))

        self.nomep5 = QLabel(self.tabDetection)
        self.nomep5.setGeometry(QRect(650,90,400,22))
        self.nomep5.setObjectName(_fromUtf8("nometexto"))
        self.nomep5.setText(QApplication.translate("MainWindow", "“seria”", None, QApplication.UnicodeUTF8))
        
        self.nomep6 = QLabel(self.tabDetection)
        self.nomep6.setGeometry(QRect(650,110,400,22))
        self.nomep6.setObjectName(_fromUtf8("nometexto"))
        self.nomep6.setText(QApplication.translate("MainWindow", "“na boa”", None, QApplication.UnicodeUTF8))

        self.nomep7 = QLabel(self.tabDetection)
        self.nomep7.setGeometry(QRect(650,130,400,22))
        self.nomep7.setObjectName(_fromUtf8("nometexto"))
        self.nomep7.setText(QApplication.translate("MainWindow", "“medo”|“Medo!”|“#medo”", None, QApplication.UnicodeUTF8))        
        
        self.nomep8 = QLabel(self.tabDetection)
        self.nomep8.setGeometry(QRect(650,150,400,22))
        self.nomep8.setObjectName(_fromUtf8("nometexto"))
        self.nomep8.setText(QApplication.translate("MainWindow", "“#ironia”|“#sarcasmo”|“#joking”|“#kidding”", None, QApplication.UnicodeUTF8))

        self.nomep9 = QLabel(self.tabDetection)
        self.nomep9.setGeometry(QRect(650,170,400,22))
        self.nomep9.setObjectName(_fromUtf8("nometexto"))
        self.nomep9.setText(QApplication.translate("MainWindow", "ADV + ADV | ADJ + ADJ", None, QApplication.UnicodeUTF8))
                
        self.nomep10 = QLabel(self.tabDetection)
        self.nomep10.setGeometry(QRect(650,190,400,22))
        self.nomep10.setObjectName(_fromUtf8("nometexto"))
        self.nomep10.setText(QApplication.translate("MainWindow", "“tão” + ADJ | “tão” + ADV", None, QApplication.UnicodeUTF8))
        
        self.nomep11 = QLabel(self.tabDetection)
        self.nomep11.setGeometry(QRect(650,210,400,22))
        self.nomep11.setObjectName(_fromUtf8("nometexto"))
        self.nomep11.setText(QApplication.translate("MainWindow", "ADJ + List of Emoticons", None, QApplication.UnicodeUTF8))
        
        self.nomep12 = QLabel(self.tabDetection)
        self.nomep12.setGeometry(QRect(650,230,400,22))
        self.nomep12.setObjectName(_fromUtf8("nometexto"))
        self.nomep12.setText(QApplication.translate("MainWindow", "DET + ADJ + (PREP+DET) + NE", None, QApplication.UnicodeUTF8))
        
        self.nomep13 = QLabel(self.tabDetection)
        self.nomep13.setGeometry(QRect(660,250,400,22))
        self.nomep13.setObjectName(_fromUtf8("nometexto"))
        self.nomep13.setText(QApplication.translate("MainWindow", "Demostrative Pronouns + NE", None, QApplication.UnicodeUTF8))
        
        self.nomep14 = QLabel(self.tabDetection)
        self.nomep14.setGeometry(QRect(660,270,400,22))
        self.nomep14.setObjectName(_fromUtf8("nometexto"))
        self.nomep14.setText(QApplication.translate("MainWindow", "...<EXPR>!", None, QApplication.UnicodeUTF8))
        
        self.nomep15 = QLabel(self.tabDetection)
        self.nomep15.setGeometry(QRect(660,290,400,22))
        self.nomep15.setObjectName(_fromUtf8("nometexto"))
        self.nomep15.setText(QApplication.translate("MainWindow", "!*|?*|!*?*|?*!*", None, QApplication.UnicodeUTF8))
        
        self.nomep16 = QLabel(self.tabDetection)
        self.nomep16.setGeometry(QRect(660,310,400,22))
        self.nomep16.setObjectName(_fromUtf8("nometexto"))
        self.nomep16.setText(QApplication.translate("MainWindow", "Quotation Marks", None, QApplication.UnicodeUTF8))

        self.radioButtonP1.setText(QApplication.translate("Form", "P1", None, QApplication.UnicodeUTF8))
        self.radioButtonP2.setText(QApplication.translate("Form", "P2", None, QApplication.UnicodeUTF8))
        self.radioButtonP3.setText(QApplication.translate("Form", "P3", None, QApplication.UnicodeUTF8))
        self.radioButtonP4.setText(QApplication.translate("Form", "P4", None, QApplication.UnicodeUTF8))
        self.radioButtonP5.setText(QApplication.translate("Form", "P5", None, QApplication.UnicodeUTF8))
        self.radioButtonP6.setText(QApplication.translate("Form", "P6", None, QApplication.UnicodeUTF8))
        self.radioButtonP7.setText(QApplication.translate("Form", "P7", None, QApplication.UnicodeUTF8))        
        self.radioButtonP8.setText(QApplication.translate("Form", "P8", None, QApplication.UnicodeUTF8))
        self.radioButtonP9.setText(QApplication.translate("Form", "P9", None, QApplication.UnicodeUTF8))
        self.radioButtonP10.setText(QApplication.translate("Form", "P10", None, QApplication.UnicodeUTF8))
        self.radioButtonP11.setText(QApplication.translate("Form", "P11", None, QApplication.UnicodeUTF8))
        self.radioButtonP12.setText(QApplication.translate("Form", "P12", None, QApplication.UnicodeUTF8))
        self.radioButtonP13.setText(QApplication.translate("Form", "P13", None, QApplication.UnicodeUTF8))
        self.radioButtonP14.setText(QApplication.translate("Form", "P14", None, QApplication.UnicodeUTF8))
        self.radioButtonP15.setText(QApplication.translate("Form", "P15", None, QApplication.UnicodeUTF8))
        self.radioButtonP16.setText(QApplication.translate("Form", "P16", None, QApplication.UnicodeUTF8))
        
        self.radioButtonP1.clicked.connect(self.openP1)            
        self.radioButtonP2.clicked.connect(self.openP2)
        self.radioButtonP3.clicked.connect(self.openP3)
        self.radioButtonP4.clicked.connect(self.openP4)
        self.radioButtonP5.clicked.connect(self.openP5)
        self.radioButtonP6.clicked.connect(self.openP6)
        self.radioButtonP7.clicked.connect(self.openP7)
        self.radioButtonP8.clicked.connect(self.openP8)
        self.radioButtonP9.clicked.connect(self.openP9)
        self.radioButtonP10.clicked.connect(self.openP10)
        self.radioButtonP11.clicked.connect(self.openP11)
        self.radioButtonP12.clicked.connect(self.openP12)
        self.radioButtonP13.clicked.connect(self.openP13)
        self.radioButtonP14.clicked.connect(self.openP14)
        self.radioButtonP15.clicked.connect(self.openP15)
        self.radioButtonP16.clicked.connect(self.openP16)        

        self.setWindowTitle("Program Textos (delegate)")
        self.tabWidget.addTab(self.tabDetection, _fromUtf8(""))
        
#----------------------------------------------------------------------------------------------------------------

        self.TabManualTagging = QWidget()                            
     
        self.plainTextEditAba2 = QPlainTextEdit(self.TabManualTagging)
        self.plainTextEditAba2.setGeometry(QRect(30,50,560,650))
        self.plainTextEditAba2.setObjectName(_fromUtf8("plainTextEditAba2"))        

        self.model = table.TableModel(QString("table.dat"))
        
        self.tab = QTableView(self.TabManualTagging)     
        self.tab.setGeometry(QRect(750,140, 215, 550))
        self.tab.setModel(self.model)
        self.tab.setItemDelegate(table.TableDelegate(self))
     
        self.addLineButton = QPushButton(self.TabManualTagging)
        self.addLineButton.setGeometry(QRect(700,50, 100, 37))
        self.addLineButton.setText(QApplication.translate("None","Add", None, QApplication.UnicodeUTF8))
        
        self.removeLineButton = QPushButton(self.TabManualTagging)
        self.removeLineButton.setGeometry(QRect(800, 50, 100, 37))
        self.removeLineButton.setText(QApplication.translate("None","Remove", None, QApplication.UnicodeUTF8))

        self.exportButton = QPushButton(self.TabManualTagging)
        self.exportButton.setGeometry(QRect(900, 50, 100, 37))        
        self.exportButton.setText(QApplication.translate("None","Export", None, QApplication.UnicodeUTF8))
        
        self.connect(self.addLineButton, SIGNAL("clicked()"), self.addLine)
        self.connect(self.removeLineButton, SIGNAL("clicked()"), self.removeLine)
        self.connect(self.exportButton, SIGNAL("clicked()"), self.export)
  
        self.setWindowTitle("Program Textos (delegate)")
        self.tabWidget.addTab(self.TabManualTagging, _fromUtf8(""))
        
#-----------------------------------------------------------------------------------------------------------------           

        fileNewAction = self.createAction("&New", self.fileNew, QKeySequence.New, "filenew", "Create a text file") 
        fileSaveAction = self.createAction("&Save", self.fileSave, QKeySequence.Save, "filesave", "Save the text")                          
        fileCloseAction = self.createAction("&Close", self.close, QKeySequence.Close, "fileclose", "Close this text editor")                     
        fileQuitAction = self.createAction("&Quit", self.fileQuit, "Ctrl+m", "filequit", "Close the application")                     
        editCopyAction = self.createAction("&Copy", self.editor.copy, QKeySequence.Copy, "editcopy", "Copy text to the clipboard") 
        editCutAction = self.createAction("&Cut", self.editor.cut, QKeySequence.Cut, "editcut", "Cut text to the clipboard")                    
        editPasteAction = self.createAction("&Paste", self.editor.paste, QKeySequence.Paste, "editpaste", "Paste in the clipboard's text")
        editInsertAction = self.createAction("&Insert", self.addLineTable, QKeySequence.Print,"Insert", "Insert in the clipboard's text")

        fileMenu = self.menuBar().addMenu("&File")       
        self.addActions(fileMenu, (fileNewAction, fileSaveAction, None, fileCloseAction, fileQuitAction))
                
        editMenu = self.menuBar().addMenu("&Edit")       
        self.addActions(editMenu, (editCopyAction, editCutAction, editPasteAction, editInsertAction))

        self.windowMenu = self.menuBar().addMenu("&Window")
        
        self.connect(self.windowMenu, SIGNAL("aboutToShow()"), self.updateWindowMenu)

        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolbar")
        self.addActions(fileToolbar, (fileNewAction, fileSaveAction))

        editToolbar = self.addToolBar("Edit")
        editToolbar.setObjectName("EditToolbar")
        self.addActions(editToolbar, (editCopyAction, editCutAction, editPasteAction))

        self.connect(self, SIGNAL("destroyed(QObject*)"), MainWindow.updateInstances)

        self.resize(1500, 1200)
        self.scroll(400,400)

        self.setWindowTitle(QApplication.translate("Form", filename, None, QApplication.UnicodeUTF8))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDetection), QApplication.translate("Form", "Pattern Detection", None, QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabManualTagging), QApplication.translate("Form", "Manual Tagging", None, QApplication.UnicodeUTF8))
      
        self.filename = filename
        if self.filename.isEmpty():
            self.filename = QString("Unnamed-%d.txt" % MainWindow.NextId)
            MainWindow.NextId += 1000
            self.editor.document().setModified(False)
            self.setWindowTitle("Irony Tool  - %s" % self.filename)
        else:
            self.readListOfTweets()
           
    @staticmethod
    def updateInstances(qobj):
        MainWindow.Instances = set([window for window in MainWindow.Instances if isAlive(window)])     

    def loadFile(self):
        fh = None       
        try:
            fh = QFile(self.filename)
            if not fh.open(QIODevice.ReadOnly):
                raise IOError, unicode(fh.errorString())
            stream = QTextStream(fh)
            stream.setCodec("UTF-8")
            text = stream.readAll()
            self.editor.setPlainText(text)
            listOfTweets = []
            arquivo = open(self.filename)
            for linhaDeTweets in arquivo:
                listOfTweets = listOfTweets + [linhaDeTweets] 
            arquivo.close()            
            return listOfTweets          
            listOfTweetsPOS = readListOfTweetsPOS()
            listOfSentencesPOS = sentenceSplit(listOfTweetsPOS)
            listOfEmoticons = readListOfEmoticons()
            listOfLaughter = readListOfLaughter()
            listOfEmoticonsPolaridade = readListOfEmoticonsPolarity()
            listOfAdjectivesPolarity = readListOfAdjectivesPolarity()
            self.editor.document().setModified(False)
        except (IOError, OSError), e:
            QMessageBox.warning(self, "Main Window -- Load Error", "Failed to load %s: %s" % (self.filename, e))
        finally:
            if fh is not None:
                fh.close()
        self.editor.document().setModified(False)
        self.setWindowTitle("Main Window - %s" % QFileInfo(self.filename).fileName())  
        
    def addLine(self):                        
        row = self.model.rowCount()   
        self.model.insertRows(row)
        index = self.model.index(row, 0)
        tableView = self.tab        
        tableView.setFocus()
        tableView.setCurrentIndex(index)
        tableView.edit(index)

    def removeLine(self):             
        tableView = self.tab
        index = tableView.currentIndex()
        if not index.isValid():            
            return
        row = index.row()
        TSentence = self.model.data(self.model.index(row, TABELA.SENTENCE)).toString()                    
        TIrony = self.model.data(self.model.index(row, TABELA.IRONY)).toString()
        if QMessageBox.question(self, "Line - Remove", 
                QString("Remove %1 %2?").arg(TSentence).arg(TIrony),
                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            return
        self.model.removeRows(row)

    def addLineTable(self):        
        row = self.model.rowCount()   
        self.model.insertRows(row)
        column = 0
        index = self.model.index(row, column)        
        tableView = self.tab            
        tableView.setFocus()
        tableView.setCurrentIndex(index)
        cursor = self.plainTextEditAba2.textCursor()
        format = cursor.charFormat() 
        format.setBackground(Qt.red)
        format.setForeground(Qt.blue)
        cursor.setCharFormat(format)
        textSelected = cursor.selectedText()  
        self.model.setData(index, QVariant(textSelected))          
        
    def export(self):        
        Filename = "Filename"
        filename = unicode(QFileDialog.getSaveFileName(self, "Document - Choose Export File", Filename+".csv"))
        if not filename:
                return
        fh = None
        try:            
                fh = QFile(filename)
                if not fh.open(QIODevice.WriteOnly):                     
                    raise IOError, unicode(fh.errorString())
                stream = QTextStream(fh)
                stream.setCodec("UTF-8")              
                for row in range(self.model.rowCount()):
                    TSentence = self.model.data(
                    self.model.index(row, TABELA.SENTENCE)).toString()
                    TIrony = self.model.data(   
                    self.model.index(row, TABELA.IRONY)).toString()                    
                    stream  << "\""<< TSentence << "\"" << ";" << "\""<< TIrony <<"\"" <<"\n"                     
        except (IOError, OSError), e:
            QMessageBox.warning(self, "Text - Error", "Failed to export: %s" % e)           
        finally:
            if fh:
                fh.close()
        QMessageBox.warning(self, "Text - Export", "Successfully exported text to %s" % filename)
                      
    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal="triggered()"):        
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action
    
    def addActions(self, target, actions):         
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)
    
    def fileQuit(self):        
        QApplication.closeAllWindows()

    def fileNew(self):        
        MainWindow().show()

    def fileSave(self):        
        if self.filename.startsWith("Text"):
            return self.fileSaveAs()
        fh = None
        try:
            fh = QFile(self.filename)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError, unicode(fh.errorString())
            stream = QTextStream(fh)
            stream.setCodec("UTF-8")
            stream << self.editor.toPlainText()
            self.editor.document().setModified(False) 
        except (IOError, OSError), e:         
            QMessageBox.warning(self, "Text - Save Error", "Failed to save %s: %s" % (self.filename, e))
        finally:
            if fh is not None:
                fh.close()
        return True 

    def updateWindowMenu(self):        
        self.windowMenu.clear()
        for window in MainWindow.Instances:
            if isAlive(window):
                self.windowMenu.addAction(window.windowTitle(),self.raiseWindow)

    def raiseWindow(self):        
        action = self.sender()
        if not isinstance(action, QAction):
            return
        for window in MainWindow.Instances:
            if isAlive(window) and window.windowTitle() == action.text():  
                window.activateWindow()
                window.raise_()
                break        
                
    def saveResultP1(self, List): 
        output = open("Results/resultP1.txt","w")    
        for item in List:
            output.write(item)          
        output.close()
        
    def saveResultP2(self, List): 
        output = open("Results/resultP2.txt","w")    
        for item in List:
            output.write(item)  
        output.close()
        
    def saveResultP3(self, List): 
        output = open("Results/resultP3.txt","w")    
        for item in List:
            output.write(item)                  
        output.close()
        
    def saveResultP4(self, List): 
        output = open("Results/resultP4.txt","w")    
        for item in List:
            output.write(item)         
        output.close()
        
    def saveResultP5(self, List): 
        output = open("Results/resultP5.txt","w")    
        for item in List:
            output.write(item)  
        output.close()
        
    def saveResultP6(self, List): 
        output = open("Results/resultP6.txt","w")    
        for item in List:
            output.write(item)                
        output.close()
        
    def saveResultP7(self, List): 
        output = open("Results/resultP7.txt","w")    
        for item in List:
            output.write(item)         
        output.close()
        
    def saveResultP8(self, List): 
        output = open("Results/resultP8.txt","w")    
        for item in List:
            output.write(item)         
        output.close()
        
    def saveResultP9(self, List): 
        output = open("Results/resultP9.txt","w")    
        for item in List:
            output.write(item)          
        output.close()
        
    def saveResultP10(self, List): 
        output = open("Results/resultP10.txt","w")    
        for item in List:
            output.write(item)         
        output.close()
        
    def saveResultP11(self, List): 
        output = open("Results/resultP11.txt","w")    
        for item in List:
            output.write(item)                
        output.close()
        
    def saveResultP12(self, List): 
        output = open("Results/resultP12.txt","w")    
        for item in List:
            output.write(item)             
        output.close()
        
    def saveResultP13(self, List): 
        output = open("Results/resultP13.txt","w")    
        for item in List:
            output.write(item)         
        output.close()                   

    def saveResultP14(self, List): 
        output = open("Results/resultP14.txt","w")    
        for item in List:
            output.write(item)                
        output.close()
        
    def saveResultP15(self, List): 
        output = open("Results/resultP15.txt","w")    
        for item in List:
            output.write(item)             
        output.close()
        
    def saveResultP16(self, List): 
        output = open("Results/resultP16.txt","w")    
        for item in List:
            output.write(item)             
        output.close()
        
    def readListOfTweets(self):
        listOfTweets = []
        fileTweets = open("Tweets/listOfTweetsFimDoMundo.txt")    
        for line in fileTweets:
            listOfTweets = listOfTweets + [line]      
        fileTweets.close()
        return listOfTweets
        
    def readListOfLaughter(self):
	listOfLaughter = []
	fileLaughter = open("Lists/listOfLaughter.txt")
	for line in fileLaughter:
	    listOfLaughter = listOfLaughter + [line] 
	fileLaughter.close()
	return listOfLaughter   

    def readListOfTweetsPOS(self):
	listOfTweetsPOS = []
	fileTweetsPOS = open("Tweets/listOfTweetsPOSFimDoMundo.txt")	
	for line in fileTweetsPOS:
	    word = line.partition('\t')
	    marcacao = word[2].partition('\t')
	    listOfTweetsPOS = listOfTweetsPOS + [(word[0], marcacao[0])]       
	return listOfTweetsPOS	

    def readListOfEmoticonsPolarity(self):    
	listOfEmoticonsPolarity = []
	with open("Lists/listOfEmoticonsPolarity.csv") as e:
	    emoticons = csv.reader(e, delimiter=';')
	    for emoticon in emoticons:
		listOfEmoticonsPolarity = listOfEmoticonsPolarity + [emoticon]       
	return listOfEmoticonsPolarity

    def readListOfAdjectivesPolarity(self):
	listOfAdjectivesPolarity = []
	with open("Lists/listOfAdjectivesPolarity.csv") as a:
	    adjectives = csv.reader(a, delimiter=';')
	    for adjective in adjectives:
		listOfAdjectivesPolarity = listOfAdjectivesPolarity + [adjective]
	return listOfAdjectivesPolarity	

    def readListOfEmoticons(self):
	listOfEmoticons = []
	fileEmoticons = open("Lists/listOfEmoticons.txt")
	for line in fileEmoticons:
	    listOfEmoticons = listOfEmoticons + [line] 
	fileEmoticons.close()
	return listOfEmoticons	

    def sentenceSplit(self, listOfTweetsPOS):
	listOfSentencesPOS = dict()
	indicesIds = []
	indice = 0
	for tupla in listOfTweetsPOS:
	    er = re.findall("\d{18}", tupla[0])
	    if er:
		indicesIds = indicesIds+[indice]
	    indice = indice + 1	    
	for i in range(0, len(indicesIds)):
	    if (i == len(indicesIds)-1):
		intervalo = range(indicesIds[i]+2, len(listOfTweetsPOS))
	    else:
		intervalo = range(indicesIds[i]+2, indicesIds[i+1])
	    tweet = []        
	    for j in intervalo:            
		tweet = tweet + [listOfTweetsPOS[j]]
		listOfSentencesPOS[indicesIds[i]] = tweet
	return listOfSentencesPOS    	

    def verifyEntity(self, word):
	if word.istitle():        
	    return True
	else:       
	    return False
                                 
    def identifyPattern1(self, listOfTweets, listOfLaughter): #List of Laugther
	listOfLaughterIdentified = []
	for tweet in listOfTweets:
	    for laughter in listOfLaughter:
		if laughter in tweet:
		    listOfLaughterIdentified = listOfLaughterIdentified + [tweet] 
	return listOfLaughterIdentified

    def identifyPattern2(self, listOfTweets, listOfEmoticons): #List of Emoticons
	listOfEmoticonsIdentified = []
	for tweet in listOfTweets:
	    for emoticon in listOfEmoticons:
		if emoticon in tweet:
		    listOfEmoticonsIdentified = listOfEmoticonsIdentified + [tweet] 
	return listOfEmoticonsIdentified     
	
    def identifyPattern3(self, listOfTweets):  #só que
        expression = " só que "
        listOfTweetsIdentified = []
        for tweet in listOfTweets:
            if expression in tweet:
                listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
        return listOfTweetsIdentified

    def identifyPattern4(self, listOfTweets): #sim,
        expression = " sim, "
        listOfTweetsIdentified = []
        for tweet in listOfTweets:
            if expression in tweet:
                listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
        return listOfTweetsIdentified

    def identifyPattern5(self, listOfTweets): #seria
         expression = " seria "
         listOfTweetsIdentified = []
         for tweet in listOfTweets:
            if expression in tweet:
                listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
         return listOfTweetsIdentified    

    def identifyPattern6(self, listOfTweets): #na boa
	expression = " na boa "
	listOfTweetsIdentified = []
	for tweet in listOfTweets:
	    if expression in tweet:
		listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
	return listOfTweetsIdentified         
         
    def identifyPattern7(self, listOfTweets): #medo, Medo!, #medo
         listaOfTerms = ["medo", "Medo!", "#medo"]
         listOfTweetsIdentified = []
         for tweet in listOfTweets:
            for term in listaOfTerms:
                if term in tweet:
		  listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
         return listOfTweetsIdentified

    def identifyPattern8(self, listOfTweets): # #sarcasmo, #ironia, #joking, #kidding 
	listOfTerms = ["#sarcasmo", "#ironia", "#joking", "#kidding"]
	listOfTweetsIdentified = []
	for tweet in listOfTweets:
	    for term in listOfTerms:
		if term in tweet:
		    listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
	return listOfTweetsIdentified       

    def identifyPattern9(self, listOfSentencesPOS): #ADV+ADV|ADJ+ADJ
      listOfTweetsIdentified = []           
      for sentence in listOfSentencesPOS.values():
	  for indice, word in enumerate(sentence):
	      if (sentence[indice-1][1] == "ADJ" and word[1] == "ADJ" and sentence[indice-1][0] == word[0]) or (sentence[indice-1][1] == "ADV" and word[1] == "ADV" and sentence[indice-1][0] == word[0]):  
		  tweet = ""
		  for i in range(0,len(sentence)):
		      tweet = tweet + " " + sentence[i][0]
		  tweet = tweet + "\n"
		  listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
      return listOfTweetsIdentified  	
	
    def identifyPattern10(self, listOfSentencesPOS): #Tão+ADJ ou Tão+ADV
	expression = "Tão"
	listOfTweetsIdentified = []           
	for sentence in listOfSentencesPOS.values():
	    for indice, word in enumerate(sentence):
		if sentence[indice-1][0] == expression and (word[1] == "ADJ" or word[1] == "ADV"):  
		    tweet = ""
		    for i in range(0,len(sentence)):
			tweet = tweet + " " + sentence[i][0]
		    tweet = tweet + "\n"
		    listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
	return listOfTweetsIdentified                
        
    def identifyPattern11(self, listOfTweets, listOfEmoticonsPolarity, listOfAdjectivesPolarity): #ADJ+List of Emoticons
	listOfTweetsIdentified = []
	for tweet in listOfTweets:
	    for adjective in listOfAdjectivesPolarity:
		for emoticon in listOfEmoticonsPolarity:
		    if (adjective[0] in tweet) and (emoticon[0] in tweet) and (adjective[1]!=emoticon[1]):
			listOfTweetsIdentified = listOfTweetsIdentified + [tweet] 
	return listOfTweetsIdentified

    def identifyPattern12(self, listOfSentencesPOS): #DET+ADJ+(PREP+DET)+EN    
	listOfTweetsIdentified = []           
	for sentence in listOfSentencesPOS.values():
	    for indice, word in enumerate(sentence):	  
		if word[1] == "DET" and indice+3 < len(sentence) and sentence[indice+1][1] == "ADJ" and sentence[indice+2][1] == "PRP+DET":
		    entity = self.verifyEntity(sentence[indice+3][0])   
		    if entity:
			tweet = ""
			for i in range(0,len(sentence)):
			    tweet = tweet + " " + sentence[i][0]
			tweet = tweet + "\n"
			listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
	return listOfTweetsIdentified           
	
    def identifyPattern13(self, listOfSentencesPOS): #Demostrative Pronouns+NE
	listOfDemostrativePronouns = ["Esse", "Essa", "Isso", "Esses", "Essas", "Aquele", "Aquela", "Aquilo", "Aqueles", "Aquelas", "Este", "Esta", "Isto", "Estes", "Estas", "esse", "essa", "isso", "esses", "essas", "aquele", "aquela", "aquilo", "aqueles", "aquelas", "este", "esta", "isto", "estes", "estas"]
	listOfTweetsIdentified = []           
	for sentence in listOfSentencesPOS.values():
	    for indice, word in enumerate(sentence):
		for pronouns in listOfDemostrativePronouns:                  
		    if word[0] == pronouns and indice+1 < len(sentence):                  
			entity = self.verifyEntity(sentence[indice+1][0])   
			if entity:
			    tweet = ""
			    for i in range(0,len(sentence)):
				tweet = tweet + " " + sentence[i][0]
			    tweet = tweet + "\n"
			    listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
	return listOfTweetsIdentified         
	
    def identifyPattern14(self, listOfTweets): #...<EXPR>!    
        listOfTweetsIdentified = []
        for tweet in listOfTweets:
            er = re.findall("\.{3}[\s\w]*[\s]!", tweet)
            if er:
                listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
        return listOfTweetsIdentified        

    def identifyPattern15(self, listOfTweets): #!*|?*|!*?*|?*!*
	listOfTweetsIdentified = []
	for tweet in listOfTweets:
	    er = re.findall(".*\?\?|.*!!|.*\?!|.*!\?", tweet)
	    if er:
		listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
	return listOfTweetsIdentified    
		
    def identifyPattern16(self, listOfTweets): #Quotation Marks
         listOfTweetsIdentified = []
         for tweet in listOfTweets:
            er = re.findall("[\w\s].*[\"].+[\w].+[\s].*[\"].+[\w\s].* | [\w\s].*[\~].+[\w].+[\s].*[\~].+[\w\s].*", tweet)
            if er:
                listOfTweetsIdentified = listOfTweetsIdentified + [tweet]
         return listOfTweetsIdentified
          
    def openP1(self, e):
        listOfTweets = self.readListOfTweets()                   
        listOfLaughter = self.readListOfLaughter()
        pattern1 = self.identifyPattern1(listOfTweets, listOfLaughter)
        self.saveResultP1(pattern1)
        textAba2 = open("Results/resultP1.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2)         
        
    def openP2(self, e):
        listOfTweets = self.readListOfTweets()
        listOfEmoticons = self.readListOfEmoticons()
        pattern2 = self.identifyPattern2(listOfTweets, listOfEmoticons)      
        self.saveResultP2(pattern2)
        textAba2 = open("Results/resultP2.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2)         
        
    def openP3(self, e):      
        listOfTweets = self.readListOfTweets()          
        pattern3 = self.identifyPattern3(listOfTweets)
        self.saveResultP3(pattern3)
        textAba2 = open("Results/resultP3.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2) 
        
    def openP4(self, e):
        listOfTweets = self.readListOfTweets()          
        pattern4 = self.identifyPattern4(listOfTweets)
        self.saveResultP4(pattern4)
        textAba2 = open("Results/resultP4.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2) 
        
    def openP5(self, e): 
        listOfTweets = self.readListOfTweets()
        pattern5 = self.identifyPattern5(listOfTweets)
        self.saveResultP5(pattern5)                             
        textAba2 = open("Results/resultP5.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2) 
        
    def openP6(self, e):        
        listOfTweets = self.readListOfTweets()                                        
        pattern6 = self.identifyPattern6(listOfTweets)
        self.saveResultP6(pattern6)
        textAba2 = open("Results/resultP6.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2) 
        
    def openP7(self, e):
        listOfTweets = self.readListOfTweets() 
        pattern7 = self.identifyPattern7(listOfTweets)                        
        self.saveResultP7(pattern7)
        textAba2 = open("Results/resultP7.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2) 
        
    def openP8(self, e):
        listOfTweets = self.readListOfTweets()
        pattern8 = self.identifyPattern8(listOfTweets)                  
        self.saveResultP8(pattern8)
        textAba2 = open("Results/resultP8.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2) 
        
    def openP9(self, e):
        listOfTweetsPOS = self.readListOfTweetsPOS()
        listOfSentencesPOS = self.sentenceSplit(listOfTweetsPOS)        
        pattern9 = self.identifyPattern9(listOfSentencesPOS)
        self.saveResultP9(pattern9)
        textAba2 = open("Results/resultP9.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2)         
        
    def openP10(self, e):   
        listOfTweetsPOS = self.readListOfTweetsPOS()
        listOfSentencesPOS = self.sentenceSplit(listOfTweetsPOS)
        pattern10 = self.identifyPattern10(listOfSentencesPOS)
        self.saveResultP10(pattern10)
        textAba2 = open("Results/resultP10.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2) 
        
    def openP11(self, e):  
        listOfTweets = self.readListOfTweets()     
        listOfEmoticonsPolaridade = self.readListOfEmoticonsPolarity()
        listOfAdjectivesPolarity = self.readListOfAdjectivesPolarity()               
        pattern11 = self.identifyPattern11(listOfTweets,listOfEmoticonsPolaridade,listOfAdjectivesPolarity)
        self.saveResultP11(pattern11)
        textAba2 = open("Results/resultP11.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2) 
        
    def openP12(self, e):
        listOfTweetsPOS = self.readListOfTweetsPOS()
        listOfSentencesPOS = self.sentenceSplit(listOfTweetsPOS)
        pattern12 = self.identifyPattern12(listOfSentencesPOS)                 
        self.saveResultP12(pattern12) #
        textAba2 = open("Results/resultP12.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2)
        
    def openP13(self, e): 
        listOfTweetsPOS = self.readListOfTweetsPOS()
        listOfSentencesPOS = self.sentenceSplit(listOfTweetsPOS)
        pattern13 = self.identifyPattern13(listOfSentencesPOS)
        self.saveResultP13(pattern13)                     
        textAba2 = open("Results/resultP13.txt").read()
        self.plainTextEditAba2.setPlainText(textAba2)  

    def openP14(self, e):   
        listOfTweets = self.readListOfTweets()  
        pattern14 = self.identifyPattern14(listOfTweets)
        self.saveResultP14(pattern14)
        textAba2 = open("Results/resultP14.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2) 
        
    def openP15(self, e):                      
        listOfTweets = self.readListOfTweets()            
        pattern15 = self.identifyPattern15(listOfTweets)
        self.saveResultP15(pattern15)
        textAba2 = open("Results/resultP15.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2) 
        
    def openP16(self, e):
        listOfTweets = self.readListOfTweets()
        pattern16 = self.identifyPattern16(listOfTweets)                 
        self.saveResultP16(pattern16) 
        textAba2 = open("Results/resultP16.txt").read()     
        self.plainTextEditAba2.setPlainText(textAba2)
        
def isAlive(qobj):    
    import sip
    try:        
        sip.unwrapinstance(qobj)
    except RuntimeError:
        return False
    return True

app = QApplication(sys.argv)
MainWindow().show()
app.setWindowIcon(QIcon(":/icon.png")) 
app.exec_()