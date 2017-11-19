# -*- coding: utf-8 -*-
"""
Module implementing function.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
class MyLineEdit(QtWidgets.QLineEdit):
    #inp_text_signal = QtCore.pyqtSignal(str)   #定义信号
    def __init__(self,*args, **kwargse):
        super(MyLineEdit,self).__init__(*args, **kwargse)
#    def mouseDoubleClickEvent(self,e):
#        print( 'mouse double clicked'   )
#    def mousePressEvent(self,e):
#        print('mousePressEvent')
#    def focusInEvent(self,e):
#        print( 'focusInEvent')
#    def focusOutEvent(self,e):
#        self.inp_text_signal.emit("移出")   #发送信号
#    def moveEvent(self,e):
#        print( 'moveEvent')
    def leaveEvent(self,e): #鼠标离开label
        pass
#        print( 'leaveEvent')
    def enterEvent(self,e): #鼠标移入label
        pass
        
#        editFind=QLineEdit() 
#        regExp=QRegExp('\d*') 
#        editFind.setValidator(QRegExpValidator(regExp,self)) 
#        print( 'enterEvent')
#    def mouseMoveEvent(self,e):
#        print( 'mouseMoveEvent')
#1231231231
#
#123#
##
