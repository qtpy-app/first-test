# -*- coding: utf-8 -*-
"""
Module implementing function.
"""
import time
import  math
from Ui_form1 import Ui_MainWindow

#pyqt类
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#正则式库 , 自动按键库
import re
#import pyautogui as auto

#matplotlib类
import matplotlib.pyplot as plt
import matplotlib.patches as  mpatches

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar


import numpy as np
from numpy import random
from mylineedit import MyLineEdit
import images_rc


class  Function(  QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Function, self).__init__(parent)
        self.setupUi(self)

        # region LineEdit控件组
        
        regExp1=QRegExp(r'(?:-?\d+,?)')#正则规则1
        regExp2=QRegExp(r'^\d*$')#正则规则1       
        self.lineEdit22.setValidator(QRegExpValidator(regExp2,self)) 
        self.lineEdit23.setValidator(QRegExpValidator(regExp2,self)) 
        
        self.lineEdit1 = MyLineEdit(self.gridLayoutWidget_2)
        self.lineEdit1.setObjectName("lineEdit1")
        self.gridLayout_2.addWidget(self.lineEdit1, 2, 1, 1, 1)
        self.lineEdit1.setValidator(QRegExpValidator(regExp1,self))         
        
        
        self.lineEdit2 = MyLineEdit(self.gridLayoutWidget_2)
        self.lineEdit2.setObjectName("lineEdit2")
        self.gridLayout_2.addWidget(self.lineEdit2, 3, 1, 1, 1)
        self.lineEdit2.setValidator(QRegExpValidator(regExp1,self)) 


        self.lineEdit3 = MyLineEdit(self.gridLayoutWidget_2)
        self.lineEdit3.setObjectName("lineEdit3")
        self.gridLayout_2.addWidget(self.lineEdit3, 4, 1, 1, 1)
        self.lineEdit3.setValidator(QRegExpValidator(regExp1,self)) 

        # endregion
        # region 注册过滤
        self.lineEdit3.installEventFilter(self)
        self.lineEdit2.installEventFilter(self)
        self.lineEdit1.installEventFilter(self)
        '''信号============================================================='''
        self.fig = plt.figure(figsize=(4, 1), dpi=80)
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)
        plt.xlim(0,500)
        plt.ylim(-100, 100)
#        self.toolbar = NavigationToolbar(self.canvas, self)
        self.horizontalLayout11.addWidget(self.canvas)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
#        self.lineEdit21.textEdited.connect(self.test)
#        self.lineEdit11.textEdited.connect(self.test)



#        a = SecondWindow()
#        self.lineEdit21.textEdited.connect(a.test3)

#
#        self.frame= MyPlot(self.tab)
#        self.frame.setGeometry(QtCore.QRect(0,230, 470, 200))
#        
#        self.lineEdit11.textEdited.connect(self.frame.getvvv)
#        self.lineEdit12.textEdited.connect(self.frame.getvvv)        
#        self.lineEdit21.textEdited.connect(self.frame.Get_one)
#        self.lineEdit12.textEdited.connect(self.t3)
#        self.lineEdit12.textEdited.connect(self.t4)
#        self.lineEdit11.textEdited.connect(self.t1)
#        self.lineEdit11.textEdited.connect(self.t2)
#        self.t1=''
#        self.t2=''
#        self.t3=''
#        self.t4=''
#        #1234        
#    def t1(self):
#        self.t1=self.t2
#        pass
#    def t2(self, value):
#        self.t2=self.lineEdit11.text()
#        if len(self.t1)<len(self.t2):#增加
#            auto.press('alt')
#    def t3(self):
#        self.t3=self.t4
#        pass
#    def t4(self, value):
#        self.t3=self.lineEdit12.text()
#        if len(self.t3)<len(self.t4):#增加
#            auto.press('alt')
#        try:
#            global x 
#            if self.lineEdit21.text()!='':
#                x=int(self.lineEdit21.text())
#            else:
#                pass
#        except ValueError:
#            QMessageBox.critical(self,"注意","只能输入数值!")
        # endregion
    
    def eventFilter(self, obj, event):
        self.Type1.clicked.connect(self.setEnabled)
        self.Type2.clicked.connect(self.setEnabled)
        if event.type() == QEvent.Enter:
            if self.Type2.isChecked():
                if obj ==self.lineEdit1:
                    self.frame_2.setStyleSheet("image: url(:/Resources/11.jpg);")
                elif obj == self.lineEdit2:
                    self.frame_2.setStyleSheet("image: url(:/Resources/12.jpg);")
                elif obj == self.lineEdit3:
                    self.frame_2.setStyleSheet("image: url(:/Resources/14.jpg);")
                elif obj ==self.lineEdit5:
                    self.frame_2.setStyleSheet("image: url(:/Resources/11.jpg);")
                elif obj == self.lineEdit6:
                    self.frame_2.setStyleSheet("image: url(:/Resources/12.jpg);")
                elif obj == self.lineEdit7:
                    self.frame_2.setStyleSheet("image: url(:/Resources/14.jpg);")
 
            if self.Type1.isChecked():
                if obj == self.lineEdit1:
                    self.frame_2.setStyleSheet("image: url(:/Resources/21.jpg);")
                elif obj == self.lineEdit2:
                    self.frame_2.setStyleSheet("image: url(:/Resources/22.jpg);")
                elif obj == self.lineEdit3:
                    self.frame_2.setStyleSheet("image: url(:/Resources/24.jpg);")
                elif obj == self.lineEdit5:
                    self.frame_2.setStyleSheet("image: url(:/Resources/21.jpg);")
                elif obj == self.lineEdit6:
                    self.frame_2.setStyleSheet("image: url(:/Resources/22.jpg);")
                elif obj == self.lineEdit7:
                    self.frame_2.setStyleSheet("image: url(:/Resources/24.jpg);")
        
        return False
        
    def setEnabled(self):
        if self.Type1.isChecked():
            self.lineEdit12.setEnabled(False)
            self.lineEdit11.setEnabled(False)
            self.lineEdit12.setText('')
            self.lineEdit11.setText('')
            self.pushButton3.setEnabled(True)
            self.pushButton4.setEnabled(True)
            self.pushButton1.setEnabled(False)
            self.pushButton2.setEnabled(False)
            self.checkBox1.setEnabled(True)
            self.checkBox2.setEnabled(True)
        elif self.Type2.isChecked():
            self.lineEdit12.setEnabled(True)
            self.lineEdit11.setEnabled(True)
            self.pushButton3.setEnabled(False)
            self.pushButton4.setEnabled(False)
            self.pushButton1.setEnabled(True)
            self.pushButton2.setEnabled(True)
            self.checkBox1.setEnabled(False)
            self.checkBox2.setEnabled(False)
            self.checkBox1.setChecked(False)
            self.checkBox2.setChecked(False)



#    @pyqtSlot()
#    def on_pushButton_2_clicked(self):
#       newWindow = SecondWindow()
#       newWindow.show()
#       newWindow.exec_()

class SecondWindow( QWidget):#暂时没用
#   def __init__(self, parent=None):
#        super(SecondWindow, self).__init__(parent)
#        self.resize(200, 200)
##        self.setStyleSheet("background: black")
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.hide()

        # Just some button 
        self.button1 = QtWidgets.QPushButton('Plot')
        self.button1.clicked.connect(self.plot)

        self.button2 = QtWidgets.QPushButton('Zoom')
        self.button2.clicked.connect(self.zoom)

        self.button3 = QtWidgets.QPushButton('Pan')
        self.button3.clicked.connect(self.pan)

        self.button4 = QtWidgets.QPushButton('Home')
        self.button4.clicked.connect(self.home)

        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        btnlayout = QtWidgets.QHBoxLayout()
        btnlayout.addWidget(self.button1)
        btnlayout.addWidget(self.button2)
        btnlayout.addWidget(self.button3)
        btnlayout.addWidget(self.button4)
        qw = QtWidgets.QWidget(self)
        qw.setLayout(btnlayout)
        layout.addWidget(qw)

        self.setLayout(layout)
        self.F=Function()
    def home(self):
        self.toolbar.home()
    def zoom(self):
        self.toolbar.zoom()
    def pan(self):
        self.toolbar.pan()
    def plot(self):
#        ''' plot some random stuff '''
#        data = [random.random() for i in range(25)]
#        self.axes.plot(data, '*-')
#        self.canvas.draw()
        
        pass
    def handle_click(self):
        if not self.isVisible():
            print(self.F.lineEdit11.text())
            self.show()

#    def xxx(self, value):
#        print("second xxx:", value)#对比用
        #print(x+10)#这个是可以的
        
class Input(QWidget):#暂时没用
    x2=100
#    self._
    def __init__(self, *args, **kwargs):
        super(Input,  self).__init__(*args, **kwargs)

    def L1_and_L2(self):#, value):#梁类型判定
        print('1234567')
    def Xp(self, value):#集中力位置
        self.XpList=value.split(','or'，')
        c_xp=len(self.XpList)
        print(self.XpList)
#        print(c_xp)

#    def P(self):#集中力大小
#    
    def Xm(self, value):#集中力偶位置
        self.XmList=list(value)
        c1=self.XmList.count(',')
        c2=self.XmList.count('，')
        c_xm=c1+c2+1
        print(c_xm)
#    def Me(self):#集中力偶大小
#    
    def X1_and_X2(self):#均布力位置
        pass
    def Q1_and_Q2(self):#均布力大小
        pass
        
class MyPlot(Function):
    """动态画布：每秒自动更新，更换一条折线。"""
    def __init__(self, parent=None):
        super(MyPlot, self).__init__(parent)
        timer = QtCore.QTimer(self)
#        self.lineEdit11.textEdited.connect(self.click_do_something)#第三步
#        timer.timeout.connect(self.update_figure)
        timer.start(1000)
        self.lineEdit11.textEdited.connect(self.update_figure)
        self.lineEdit11.textEdited.connect(self.drawPin)     
        self.drawline()
        self.drawPin()
        self.drawRoller()

    def drawline(self):
        self.axes.plot([50, 450],[0, 0], 'k-', linewidth=1, antialiased=False)#杆长
    def drawRoller(self):
        self.axes.plot([100, 400], [0, 0], 'ko',  markersize=10, fillstyle= 'none')#圆        
        for p in[mpatches.Rectangle((60,-5), 30, 10, fc='none', hatch='////'), 
            mpatches.Rectangle((120,0), 30, 10, fc='none', hatch='////')]:
            self.axes.add_patch(p)#阴影填充

        self.axes.arrow(30, 10, 0, -50, linewidth=1,head_width=20, fc='k',  antialiased=True)#集中力P
        self.axes.arrow(30, 10, 10,0, linewidth=1,head_width=5, fc='k', antialiased=True)#弯矩M
        self.axes.arrow(30, 40, -10,0, linewidth=1,head_width=5, fc='k', antialiased=True)#弯矩M
        self.axes.plot([30, 30], [10, 40],  'k-', linewidth=2, antialiased=True)#弯矩M
    def drawPin(self):#这里有问题
        #        self.ro_x=re.split('\,|\;',Dialog.lineEdit12.text())
        self.axes.cla()
        self.drawline()
        self.drawRoller()
        self.axes.set(xlim=[0,500],ylim=[-100,100])
        d=np.array([])
        x=[]
        self.pin_x=np.array(re.split('\,|\;',self.lineEdit11.text()))
        if len(self.pin_x)%2==0:
            d=self.pin_x.reshape((-1, 2))
        else:
            pass
        for b in range(d.shape[0]):
            x.append(d[b][0])
            sanjiao=self.axes.plot([x[b]],[0], 'k^',  markersize=10, fillstyle= 'none')#三角
#                sanjiao.clf()
#            print(sanjiao)
#            self.canvas.draw()
#            i=sanjiao.pop(0)
#            i.remove()
#            print('x', x[b])
#        np.linspace(0, 1, 10, endpoint=False) 
        #均布力
    def update_figure(self):
        self.canvas.draw()
        self.drawline()
        self.drawPin()
        self.drawRoller()     
        
  
    
if __name__ == "__main__":
    import sys
    def excepthook(type, value, trace): 
        try:
#            QMessageBox.critical(Dialog,"注意","只能输入数值!")
#            time.sleep(0.05)
#            auto.press('alt')
            pass
        except:
            pass
        sys.__excepthook__(type, value, trace)  
    sys.excepthook = excepthook
    app = QtWidgets.QApplication(sys.argv)
    Dialog= MyPlot()
    Dialog.show()
    a = SecondWindow()
    Dialog.pushButton_2.clicked.connect(a.handle_click)
    sys.exit(app.exec_())
