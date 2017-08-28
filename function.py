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
class SecondWindow(QWidget):#暂时没用
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
        print(self.lineEdit1.text())   

    def handle_click(self):
        if not self.isVisible():

            self.show()    
#        if self.lineEdit23.text()=='':
#            self.lineEdit23.setText('0')
#        elif self.lineEdit23.text()!='0':
#            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 250, 420, 180))
#        elif self.lineEdit23.text()=='0':
#            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 250, 370, 180))            
#        if self.lineEdit22.text()=='0' and self.lineEdit22.text()=='0':
#            print('4')
#    @pyqtSlot()
#    def on_pushButton_2_clicked(self):
#       newWindow = SecondWindow()
#       newWindow.show()
#       newWindow.exec_()

#    def xxx(self, value):
#        print("second xxx:", value)#对比用
        #print(x+10)#这个是可以的

#    def Xm(self, value):#集中力偶位置
#        self.XmList=list(value)
#        c1=self.XmList.count(',')
#        c2=self.XmList.count('，')
#        c_xm=c1+c2+1
#        print(c_xm)


#        self.frame= MyPlot(self.tab)
#        self.frame.setGeometry(QtCore.QRect(0,230, 470, 200))
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
class  Function(  QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Function, self).__init__(parent)
        self.setupUi(self)
        self.zujian()
        self.Type2.setEnabled(True)
        # region LineEdit控件组
    def zujian(self):    
        regExp1=QRegExp(r'(?:-?\d+,?)')#正则规则1
        regExp2=QRegExp(r'^\d*$')#正则规则1       
        self.lineEdit22.setValidator(QRegExpValidator(regExp2,self)) 
        self.lineEdit23.setValidator(QRegExpValidator(regExp2,self)) 
        
        self.lineEdit1 = MyLineEdit(self.gridLayoutWidget_2)
        self.lineEdit1.setObjectName("lineEdit1")
        self.gridLayout_2.addWidget(self.lineEdit1, 2, 1, 1, 1)
#        self.lineEdit1.setValidator(QRegExpValidator(regExp1,self))         
        
        
        self.lineEdit2 = MyLineEdit(self.gridLayoutWidget_2)
        self.lineEdit2.setObjectName("lineEdit2")
        self.gridLayout_2.addWidget(self.lineEdit2, 3, 1, 1, 1)
#        self.lineEdit2.setValidator(QRegExpValidator(regExp1,self)) 


        self.lineEdit3 = MyLineEdit(self.gridLayoutWidget_2)
        self.lineEdit3.setObjectName("lineEdit3")
        self.gridLayout_2.addWidget(self.lineEdit3, 4, 1, 1, 1)
#        self.lineEdit3.setValidator(QRegExpValidator(regExp1,self)) 

        # endregion
        # region 注册过滤
        self.lineEdit3.installEventFilter(self)
        self.lineEdit2.installEventFilter(self)
        self.lineEdit1.installEventFilter(self)

        
        '''信号============================================================='''
        self.fig = plt.figure(figsize=(4, 1), dpi=80)
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)

        self.axes.set_xticks(np.linspace(-100, 550, 14, endpoint=True))
        self.axes.set(xlim=[-50,550],ylim=[-100,100])
#        self.axes.axis('off')
        self.Type1.clicked.connect(self.setEnabled)
        self.Type2.clicked.connect(self.setEnabled)
        self.Type3.clicked.connect(self.setEnabled)
        self.lineEdit21.textEdited.connect(self.setEnabled)               
        self.lineEdit22.textEdited.connect(self.setEnabled)
        self.lineEdit23.textEdited.connect(self.setEnabled)
#        self.toolbar = NavigationToolbar(self.canvas, self)
        self.horizontalLayout11.addWidget(self.canvas)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    
    def eventFilter(self, obj, event):

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
            self.lineEdit22.setText('0')
            self.lineEdit23.setText('0')
            self.lineEdit22.setEnabled(False)
            self.lineEdit23.setEnabled(False)
        elif self.Type2.isChecked():

            self.pushButton1.setEnabled(True)
            self.pushButton2.setEnabled(True)
            self.lineEdit12.setEnabled(True)
            self.lineEdit11.setEnabled(True)
            
            self.pushButton3.setEnabled(False)
            self.pushButton4.setEnabled(False)
            self.checkBox1.setEnabled(False)
            self.checkBox2.setEnabled(False)
            self.checkBox1.setChecked(False)
            self.checkBox2.setChecked(False)
            self.lineEdit22.setEnabled(True)
            self.lineEdit23.setEnabled(True)   
        elif self.Type3.isChecked():
            self.lineEdit12.setEnabled(True)
            self.lineEdit11.setEnabled(True)            
            self.lineEdit12.setText('')
            self.lineEdit11.setText('')
            self.pushButton1.setEnabled(True)
            self.pushButton2.setEnabled(True)            
            self.checkBox1.setEnabled(True)
            self.checkBox2.setEnabled(True)
            self.lineEdit22.setEnabled(True)
            self.lineEdit23.setEnabled(True)     
        if self.lineEdit21.text()=='':
            self.lineEdit21.setText('0')   
        elif self.lineEdit21.text()!='0':
            self.groupBox_3.setEnabled(True) 
        elif self.lineEdit21.text()=='0':    
            self.groupBox_3.setEnabled(False)   
            
        if self.lineEdit22.text()=='':
            self.lineEdit22.setText('0')    
        elif self.lineEdit22.text()!='0' and self.lineEdit23.text()=='0':
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 250, 420, 180))
        elif self.lineEdit22.text()=='0' and self.lineEdit23.text()!='0':
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 250, 420, 180))
        elif  self.lineEdit22.text()!='0' and self.lineEdit23.text()!='0':
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 250,420, 180))
        elif self.lineEdit22.text()=='0' and self.lineEdit23.text()=='0':
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 250,370, 180))
        
        if self.lineEdit23.text()=='':
            self.lineEdit23.setText('0')   

class MyPlot(Function):
    """动态画布：每秒自动更新，更换一条折线。"""
    def __init__(self, parent=None):
        super(MyPlot, self).__init__(parent)
        timer = QtCore.QTimer(self)
#        self.lineEdit11.textEdited.connect(self.click_do_something)#第三步
#        timer.timeout.connect(self.update_figure)
        timer.start(1000)
        self.Type1.clicked.connect(self.update_figure)  
        self.Type2.clicked.connect(self.update_figure)  
        self.Type3.clicked.connect(self.update_figure)
        
        self.lineEdit1.textEdited.connect(self.update_figure)
        self.lineEdit2.textEdited.connect(self.update_figure)
        self.lineEdit3.textEdited.connect(self.update_figure)
        self.lineEdit11.textEdited.connect(self.update_figure)
        self.lineEdit12.textEdited.connect(self.update_figure)
        
        self.lineEdit21.textEdited.connect(self.update_figure)
        self.lineEdit22.textEdited.connect(self.update_figure)
        self.lineEdit23.textEdited.connect(self.update_figure)     
        self.checkBox1.stateChanged.connect(self.update_figure)
        self.checkBox2.stateChanged.connect(self.update_figure)   
        self.drawline()
        self.K=1.0  #绘图因子
        self.P, self.Q, self.ME=np.array([]), np.array([]), np.array([])
        self.PX, self.QX, self.MEX=[], [], []
        self.NME, self.NP, self.NQ=0, 0, 0
        
    def drawline(self):
        self.axes.plot([0, 480],[0, 0], 'k-', linewidth=1, antialiased=False)#杆长
#        if self.lineEdit22.text()!='0':
#            self.axes.plot([20, 50],[0, 0], 'k-', linewidth=1, antialiased=False)#杆长
        if self.lineEdit23.text()!='0':
            self.axes.plot([480, 530],[0, 0], 'k-', linewidth=1, antialiased=False)#杆长
    def drawPin(self):#固定铰支
        e=np.array([])
        x=[]
        self.pin_x=np.array(re.split('\,|\;',self.lineEdit11.text()))
        e=self.pin_x
        if e[-1]!='':
#            for b,n in enumerate(e):
            for b in range(e.shape[0]):
                x.append(e[b])
                x[b]=float(x[b])/self.K
                if x[b]>=0:
                    self.axes.plot([x[b]],[-8], 'k^',  markersize=10, fillstyle= 'none')#三角
                    self.axes.plot([x[b]-15, x[b]+15],[-16, -16], 'k-', linewidth=1, antialiased=True)#杆长
                    p=mpatches.Rectangle((x[b]-15,-16), 30, -7, fc='none', hatch='////')
                    self.axes.add_patch(p)#阴影填充
                else:
                    x[b]=abs(x[b])
                    self.axes.plot([x[b]],[8], 'kv',  markersize=10, fillstyle= 'none')#三角
                    self.axes.plot([x[b]-15, x[b]+15],[16, 16], 'k-', linewidth=1, antialiased=True)#杆长
                    p=mpatches.Rectangle((x[b]-15,16), 30, 5, fc='none', hatch='////')
                    self.axes.add_patch(p)#阴影填充  

#        np.linspace(0, 1, 10, endpoint=False) 
        #均布力
    def drawRoller(self):#活动铰支
        d=np.array([])
        x=[]
        self.ro_x=np.array(re.split('\,|\;', self.lineEdit12.text())) 
        d=self.ro_x
        if d[-1]!='':
            for b,n in enumerate(d):
                x.append(n)
                x[b]=float(x[b])/self.K
                if x[b]>=0:
                    self.axes.plot([x[b]], [-9] ,'ko',  markersize=9.5, fillstyle= 'none')#圆        
                    self.axes.plot([x[b]-15, x[b]+15],[-16, -16], 'k-', linewidth=1, antialiased=True)#杆长
                    p=mpatches.Rectangle((x[b]-15,-16), 30, -7, fc='none', hatch='////')
                    self.axes.add_patch(p)#阴影填充
                else:
                    x[b]=abs(x[b])
                    self.axes.plot([x[b]], [9] ,'ko',  markersize=9.5, fillstyle= 'none')#圆        
                    self.axes.plot([x[b]-15, x[b]+15],[16, 16], 'k-', linewidth=1, antialiased=True)#杆长
                    p=mpatches.Rectangle((x[b]-15,16), 30, 5, fc='none', hatch='////')
                    self.axes.add_patch(p)#阴影填充
      
    def draw_cantilever(self):#悬臂梁
        if self.checkBox1.isChecked():
            self.axes.plot([50, 50], [-25, 25],  'k-', linewidth=2, antialiased=True)#弯矩M
            self.axes.add_patch(mpatches.Rectangle((50,-25), -10, 50, fc='none', hatch='////'))#阴影填充    
        if self.checkBox2.isChecked():
            self.axes.plot([452, 452], [-25, 25],  'k-', linewidth=2, antialiased=True)#弯矩M
            self.axes.add_patch(mpatches.Rectangle((450,-25), 10, 50, fc='none', hatch='////'))#阴影填充    

#'''===================集中力==================''' 

    def draw_concentrate_load(self):#集中力
        self.P=np.array([])
        self.PX=[]
        self.p_x=np.array(re.split('\,|\;',self.lineEdit1.text()))
        if len(self.p_x)%2==0:
            self.P=self.p_x.reshape((-1, 2))
            self.NP=self.P.shape[0]#集中力个数
            for b in range(self.NP):
                if self.P[b][-1]!='':
                    self.PX.append(self.P[b][0])
                    self.PX[b]=float(self.PX[b])
                    if self.PX[b]>=0:
                        self.axes.arrow(self.PX[b]/self.K, 25, 0, -25, linewidth=1,head_width=8, fc='k',  antialiased=True, length_includes_head=True)#集中力P

#'''===================均布载荷=================='''
    def draw_distributed_load(self):#均布载荷
        self.Q=np.array([])
        x1, x2, q3, q4, k=[], [], [], [], []
        self.p_x=np.array(re.split('\,|\;',self.lineEdit2.text()))
        if len(self.p_x)%4==0:
            self.Q=self.p_x.reshape((-1, 4))
            self.NQ=self.Q.shape[0]#集中力个数
            for a in range(self.Q.shape[0]):
                if self.Q[a][-1]!='':
                    x1.append(self.Q[a][0])
                    x1[a]=float(x1[a])
                    x2.append(self.Q[a][1])
                    x2[a]=float(x2[a])
                    q3.append(self.Q[a][2])
                    q3[a]=float(q3[a])
                    q4.append(self.Q[a][3])
                    q4[a]=float(q4[a])
                    H=(x2[a]-x1[a])/10
                    k=locals()#动态变量
                    k[a]=(q4[a]-q3[a])/(x2[a]-x1[a])
#                    t=locals()
                    t=k[a]
                    self.axes.plot([x1[a], x2[a]],[q3[a], q4[a]], 'k-', linewidth=1, antialiased=True)#杆长
                    for i in range(11):
                        y=locals()
                        y[a]=t*(x1[a]-x2[a])+q4[a] 
                        self.axes.arrow(x1[a],y[a], 0, -(y[a]-0) , linewidth=1,head_width=6, fc='k',  antialiased=True, length_includes_head=True)#集中力P
                        x1[a]=x1[a]+H
            
#'''================集中力偶=================='''            
    def draw_Bending_moment(self):#集中力偶
        self.ME=np.array([])
        self.MEX=[]
        self.p_x=np.array(re.split('\,|\;',self.lineEdit3.text()))
        if len(self.p_x)%2==0:
            self.ME=self.p_x.reshape((-1, 2))
            self.NME=self.ME.shape[0]#集中力个数
        for b in range(self.ME.shape[0]):
            if self.ME[b][-1]!='':
                self.MEX.append(self.ME[b][0])
                self.MEX[b]=float(self.MEX[b])
                if self.MEX[b]>=0:
                    self.axes.arrow(self.MEX[b]/self.K, 16, 10,0, linewidth=1,head_width=5, fc='k', antialiased=True)#弯矩M
                    self.axes.arrow(self.MEX[b]/self.K, -15, -10,0, linewidth=1,head_width=5, fc='k', antialiased=True)#弯矩M
                    self.axes.plot([self.MEX[b]/self.K,self.MEX[b]/self.K], [15, -15],  'k-', linewidth=2, antialiased=True)#弯矩M
                else :
                    self.MEX[b]=abs(self.MEX[b])
                    self.axes.arrow(self.MEX[b]/self.K, 16, -10,0, linewidth=1,head_width=5, fc='k', antialiased=True)#弯矩M
                    self.axes.arrow(self.MEX[b]/self.K, -15, 10,0, linewidth=1,head_width=5, fc='k', antialiased=True)#弯矩M
                    self.axes.plot([self.MEX[b]/self.K,self.MEX[b]/self.K], [15, -15],  'k-', linewidth=2, antialiased=True)#弯矩M                    
    
    def update_figure(self):
        self.calc()
        self.axes.cla()
        self.axes.set_xticks(np.linspace(-100, 550, 14, endpoint=True))
        self.axes.set(xlim=[-50,550],ylim=[-100,100])
#        self.axes.axis('off')
        self.drawline()
        
        self.draw_cantilever()

        self.draw_concentrate_load()  
        self.draw_distributed_load()
        self.draw_Bending_moment()
        
        self.drawRoller()  
        self.drawPin()

        self.canvas.draw()
#        print(self.NP,self.NQ,self.NM )
    def calc(self):
        L=float(self.lineEdit21.text())
        L1=float(self.lineEdit22.text())
        L2=float(self.lineEdit23.text())
        self.K=(L1+L2+L)/480
        if self.lineEdit23.text()!='0':
            self.K=(L1+L2+L)/530
        print(self.K)
        QX, MX=0 , 0
        N=100
        H=(L1+L2+L)/N
        for I in range(N):
            X=I*H
#            QB(I), M(I)=0, 0
            if self.NME==0:
                if self.NP==0:
                    if self.NQ==0:
                        pass
                    else:
                        pass
                else :
                    pass
            else : 
                pass
        for a in range(self.NME):
            
            if self.Type1.isChecked():
                if self.lineEdit22.text()=='' and self.lineEdit23.text()=='':
                    pass
            if self.Type2.isChecked():
                if self.lineEdit22.text()=='0' and self.lineEdit23.text()=='0':#简支梁
                    pass
                if self.lineEdit22.text()=='0' and self.lineEdit23.text()!='0':#右外伸梁
                    pass
                if self.lineEdit22.text()!='0' and self.lineEdit23.text()=='0':#左外伸梁
                    pass
                if self.lineEdit22.text()!='0' and self.lineEdit23.text()!='0':#左右外伸梁
                    pass
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
