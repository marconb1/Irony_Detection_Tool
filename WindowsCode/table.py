# -*- coding: utf-8 -*-

import platform
import codecs

from PyQt4.QtCore import *
from PyQt4.QtGui import *

SENTENCE, IRONY = range(2)

MAGIC_NUMBER = 0x570C4
FILE_VERSION = 1

class Table(object):

    def __init__(self, TSentence, TIrony):
        self.TSentence = QString(TSentence)   
        self.TIrony = QString(TIrony)
    
    def __cmp__(self, other):
        return QString.localeAwareCompare(self.TSentence.toLower(),other.TSentence.toLower())
        
class TableModel(QAbstractTableModel):

    def __init__(self, filename=QString()):
        super(TableModel, self).__init__()
        self.filename = filename
        self.Set = []
        self.TIronies = set()
           
    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index)| Qt.ItemIsEditable) 
     
    def data(self, index, role=Qt.DisplayRole):  
        if not index.isValid() or not (0 <= index.row() < len(self.Set)):
            return QVariant()
        SetColumn = self.Set[index.row()]
        column = index.column()
        if role == Qt.DisplayRole:
            if column == SENTENCE:
                return QVariant(SetColumn.TSentence)
            elif column == IRONY:
                return QVariant(SetColumn.TIrony)                  
        return QVariant()
   
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:                                  
                return QVariant(int(Qt.AlignLeft|Qt.AlignVCenter))
            return QVariant(int(Qt.AlignRight|Qt.AlignVCenter))
        if role != Qt.DisplayRole:
            return QVariant()
        if orientation == Qt.Horizontal:
            if section == SENTENCE:                
                return QVariant("Sentence")
            elif section == IRONY:
                return QVariant("Irony")
        return QVariant(int(section + 1))
        
    def rowCount(self, index=QModelIndex()):
        return len(self.Set)

    def columnCount(self, index=QModelIndex()):
        return 2 
            
    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.Set):
            SetColumn = self.Set[index.row()]
            column = index.column()
            if column == SENTENCE:
                SetColumn.TSentence = value.toString()
            elif column == IRONY:
                SetColumn.TIrony = value.toString()
            return True
        return False

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)        
        for row in range(rows):
            self.Set.insert(position + row, Table(" "," ")) 
        self.endInsertRows()
        return True
        
    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self.Set = self.Set[:position] + self.Set[position + rows:]
        self.endRemoveRows()
        return True
        
class TableDelegate(QItemDelegate):

    def __init__(self, parent=None):
        super(TableDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        if index.column() == IRONY: 
            combobox = QComboBox(parent)
            combobox.addItems(sorted(index.model().TIronies))
            combobox.setEditable(True)
            arquivo = codecs.open("lists/ln2.txt",encoding='utf-8',mode="r")  
            conTWords = arquivo.readlines()
            lista =[]        
            for i in conTWords:
                lista.append(i.replace("\n",""))
            combobox.addItems(sorted(lista))
            return combobox            
        elif index.column() == SENTENCE:
            editor = QLineEdit(parent)
            return editor
        else:
            return QItemDelegate.createEditor(self, parent, option, index)
      
    def setModelData(self, editor, model, index):
        if index.column()== IRONY:
            text = editor.currentText()
            if text.length() >= 1:
                model.setData(index, QVariant(text))
        elif index.column() == SENTENCE:
            text = editor.text()
            if text.length() >= 1:
                model.setData(index, QVariant(text))