# -*- coding: utf-8 -*-

import math
from Ui_form1 import Ui_MainWindow

# pyqt类
from PyQt5 import  QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWinExtras import *

# 正则式库 , 自动按键库
#import images_rc
import re
# import pyautogui as auto

# matplotlib类
import matplotlib.pyplot as plt
import matplotlib.patches as  mpatches
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

import numpy as np

#from mylineedit import MyLineEdit

class Function(QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Function, self).__init__(parent)
        self.setupUi(self)
        self.zujian()
        self.Type2.setEnabled(True)
        self.row=0
        self.ksb=1
#    def resizeEvent(self, event):

    def zujian(self):
        
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)#行选择模式
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#等宽
        
#        regExp1 = QRegExp(r'(?:-?\d+,?)')  # 正则规则1
#        regExp2 = QRegExp(r'^\d*$')  # 正则规则1
#        self.lineEdit22.setValidator(QRegExpValidator(regExp2, self))
#        self.lineEdit23.setValidator(QRegExpValidator(regExp2, self))
#  ''' ============================================ 弹 簧 区 域  =========================================弹 簧 区 域  ========================================='''
        self.spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(self.spacerItem1)
        self.horizontalLayout11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout11.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout11.setSpacing(0)
        self.horizontalLayout11.setObjectName("horizontalLayout11")
        self.horizontalLayout_6.addLayout(self.horizontalLayout11)
        self.horizontalLayout_6.addLayout(self.horizontalLayout11)
        self.spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(self.spacerItem2)
#  '''============================================= 弹 簧 区 域  =======================================弹 簧 区 域  ========================================='''     
#            self.spacerItem1.changeSize(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)#改变弹簧长度
#            self.horizontalLayout_6.invalidate()       # 重新布局
        self.fig = plt.figure(dpi=70)
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xticks(np.linspace(-100, 550, 14, endpoint=True))
        self.axes.set(xlim=[-50, 550], ylim=[-150, 150])
        self.axes.axis('off')
        self.horizontalLayout11.addWidget(self.canvas)
#        self.tableWidget.
#        FigureCanvas.setSizePolicy(self,
#                                   QSizePolicy.Expanding,
#                                   QSizePolicy.Expanding)
#        FigureCanvas.updateGeometry(self)
#        self.toolbar = NavigationToolbar(self.canvas, self)
        '''=============  信号  ===============  69行=============  信号  ===============  69行=============  信号  ===============  69行'''  
        self.Type1.clicked.connect(self.setEnabled)
        self.Type2.clicked.connect(self.setEnabled)
        self.Type3.clicked.connect(self.setEnabled)
        self.lineEdit21.returnPressed.connect(self.setEnabled)
        self.lineEdit21.returnPressed.connect(self.X_I)
    
        self.lineEdit22.textEdited.connect(self.setEnabled)
        self.lineEdit23.textEdited.connect(self.setEnabled)
        
        self.tableWidget.cellChanged.connect(self.get_2nd)
        self.tableWidget.currentItemChanged.connect(self.get_1st)
        
        
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.myListWidgetContext)#右键请求
        
        self.pushButton_3.clicked.connect(self.incsv)
        self.pushButton_6.clicked.connect(self.outcsv)
        self.lineEdit.returnPressed.connect(lambda:self.add_Item(1))#文本框回车信号
#        self.lineEdit.returnPressed.connect(self.draw_load)#文本框回车信号
#        self.lineEdit.returnPressed.connect(lambda:self.add_Item(1))#文本框回车信号
        self.lineEdit.installEventFilter(self)
        self.lineEdit21.installEventFilter(self)        
#        self.tableWidget.installEventFilter(self)
    def eventFilter(self,  obj, event ):
        if obj == self.lineEdit:
            if event.type()==QEvent.FocusIn:
                self.L1 = float(self.lineEdit22.text()) ;  self.L2 = float(self.lineEdit23.text())
                if  self.tableWidget.rowCount()==1:
                    if self.lineEdit24.text()=='0':
                        self.lineEdit.setText('等待中...')                        
                        self.lineEdit21.setFocus()
                        QMessageBox.critical(self,"注意","请输入梁的长度!") 
                    else:
                        if self.Type2.isChecked():
                            if self.lineEdit22.text()== self.lineEdit23.text():
                                self.groupBox_3.setEnabled(True)
        #                        self.lineEdit22.setText('请输入数值')
                                self.lineEdit.setText('等待中...')         
                                self.lineEdit22.setFocus()
                                QMessageBox.critical(self,"注意","请输入不同支点位置!") 
                            else:
                                self.groupBox_3.setEnabled(False)  
#                                self.lineEdit.setText('')   
                                if self.drawPin()==1:
                                    return 
                                if self.drawRoller()==1:
                                    return 

                if  self.tableWidget.rowCount()>1:
                    pass
#        if obj == self.lineEdit21:
#            if event.type()==QEvent.FocusIn:            
#                if  self.tableWidget.rowCount()>0:
#                    self.axes.clear()
#                    print('123')
                   
        return False        
    def setEnabled(self):
        if self.lineEdit21.text() != '':
            self.groupBox_3.setEnabled(True)
        else:
            self.groupBox_3.setEnabled(False)

        if self.Type1.isChecked():
            self.lineEdit12.setEnabled(False)
            self.lineEdit11.setEnabled(False)
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
            self.checkBox1.setEnabled(False)
            self.checkBox2.setEnabled(False)
            self.checkBox1.setChecked(False)
            self.checkBox2.setChecked(False)
            self.lineEdit22.setEnabled(True)
            self.lineEdit23.setEnabled(True)
#        elif self.Type3.isChecked():
#            self.lineEdit12.setEnabled(True)
#            self.lineEdit11.setEnabled(True)
#            self.lineEdit12.setText('')
#            self.lineEdit11.setText('')
#            self.pushButton1.setEnabled(True)
#            self.pushButton2.setEnabled(True)
#            self.checkBox1.setEnabled(True)
#            self.checkBox2.setEnabled(True)
#            self.lineEdit22.setEnabled(True)
#            self.lineEdit23.setEnabled(True)
        if self.lineEdit21.text() == '':
            self.lineEdit21.setText('0')
        elif self.lineEdit21.text() != '0':
            self.groupBox_3.setEnabled(True)
        elif self.lineEdit21.text() == '0':
            self.groupBox_3.setEnabled(False)

        if self.lineEdit22.text() == '':
            self.lineEdit22.setText('0')
                
        if self.lineEdit23.text() == '':
            self.lineEdit23.setText('0')
    def add_Item(self, type):

        brush = QtGui.QBrush(QtGui.QColor(145, 145, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        if type==1:
            row_count = self.tableWidget.rowCount()#最后一行
            if self.test(row_count) ==1:
                return
        if type==2:
            row_count=self.row
        if type==3:
            row_count=self.row+1
        self.tableWidget.insertRow(row_count)
        self.ksb=abs(float(self.tableWidget.item(0, 2).text())/20)
        self.draw_load()                                                 #画力的图在174行
        try:
            if self.tableWidget.item(row_count-1, 0).text()=='1':
                self.tableWidget.item(row_count-1, 3).setText('')
                self.tableWidget.item(row_count-1, 3).setBackground(brush)
                self.tableWidget.item(row_count-1, 3).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
    
            if self.tableWidget.item(row_count-1, 0).text()=='2':  
                self.tableWidget.item(row_count-1, 3).setText('')                
                self.tableWidget.item(row_count-1, 3).setBackground(brush)
                self.tableWidget.item(row_count-1, 3).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        except:
            pass
    def del_Item(self, type):
        index_list = []  
        for model_index in self.tableWidget.selectionModel().selectedRows():     
            index = QtCore.QPersistentModelIndex(model_index)         
            index_list.append(index)
        for self.index in index_list: 
            if type==1:
                self.tableWidget.removeRow(self.index.row())
    def myListWidgetContext(self):
        popMenu =QMenu()
        popMenu.addAction(u'在上插入行', lambda:self.add_Item(2))
        popMenu.addAction(u'在下插入行', lambda:self.add_Item(3))
        popMenu.addAction(u'删除行',lambda:self.del_Item(1))
#        popMenu.addAction(u'撤销')#有空做
        popMenu.exec_(QCursor.pos())#鼠标位置
    def test(self, row):
        txt=np.array(re.split(',|，', self.lineEdit.text()))
#        print(len(txt))
        if 3<=len(txt)<5:
            if txt[-1]=='':
                QMessageBox.critical(self,"注意","格式错误!") 
                return 1
            if float(txt[1])>self.X[-1] or float(txt[1])<0:
                QMessageBox.critical(self,"注意","力的位置超过梁的长度!") 
                return 1                
            if int(txt[0]) not in (1, 2, 3) :
                QMessageBox.critical(self,"注意","请输入正确类型!")
                return 1
            else:
                if int(txt[0]) in (1, 2) and len(txt)==4:
                    QMessageBox.critical(self,"注意","该类型请不要多输入Q!")
                    return 1
                if int(txt[0])==3 and len(txt)!=4:
                    QMessageBox.critical(self,"注意","均布力请输入Q2!")
                    return 1
                self.tableWidget.setItem(row-1, 0, QTableWidgetItem(txt[0]))
                self.tableWidget.setItem(row-1, 1, QTableWidgetItem(txt[1]))
                self.tableWidget.setItem(row-1, 2, QTableWidgetItem(txt[2]))
                if len(txt)==4:
                    self.tableWidget.setItem(row-1, 3, QTableWidgetItem(txt[3]))                
                else:
                    self.tableWidget.setItem(row-1,3, QTableWidgetItem(None))
                self.lineEdit.clear()
        else:
            QMessageBox.critical(self,"注意","格式错误!") 
            return 1
        if self.lineEdit23.text() == '':
            self.lineEdit23.setText('0')

    def X_I(self):
        self.lineEdit21.clearFocus()        
        if self.lineEdit21.text()!='':
            txt=np.array(re.split(',|，', self.lineEdit21.text()))
            if txt[-1]=='':
                    QMessageBox.critical(self,"注意","格式错误!") 
                    self.groupBox_3.setEnabled(False)
                    return 0
            else:
                txt=[float(i) for i in txt]
                self.X=[sum(txt[:i+1]) for i in range(len(txt))]
                self.X.insert(0, 0)
                self.lineEdit24.setText(str(round(self.X[-1]+0.000001, 2))) 
        else:
            QMessageBox.critical(self,"注意","请输入数值!") 
            return 0
        self.N=len(txt) ;  self.N1=self.N+1 ;   self.N11=self.N1+1
        self.Nbox.setValue(self.N)
        self.K=self.Kbox.value() ;  self.K1=self.K+1 
        self.P,  self.T, self.QL,  self.QR = [0]*self.N1,  [0]*self.N1,  [0]*self.N1,  [0]*self.N1
        "==================  参数  ======================== ==================  参数 ==================  参数 "
        self.L = float(self.lineEdit24.text())  ;  
        self.ksc = (self.L) /480       
    def get_1st(self):
        try:
            self.row = self.tableWidget.currentRow()
            self.txt0= self.tableWidget.item(self.row, 0).text()
            self.txt1= self.tableWidget.item(self.row, 1).text() 
        except:
            pass
#        print(self.row)
    def get_2nd(self):
        try:
            txt0= self.tableWidget.item(self.row, 0).text()
            txt1= self.tableWidget.item(self.row, 1).text()            
            if txt0 not in ('1', '2', '3'):
                QMessageBox.critical(self,"注意","请输入正确梁类型!") 
                self.tableWidget.item(self.row, 0).setText(self.txt0)
            if txt0!=self.txt0 and txt0=='3':
                brush = QtGui.QBrush()
                brush.setStyle(QtCore.Qt.NoBrush)
                self.tableWidget.item(self.row, 3).setBackground(brush)
                self.tableWidget.item(self.row, 3).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
            if int(txt1)>self.X[-1] or int(txt1)<0:
                QMessageBox.critical(self,"注意","力的位置超过梁的长度!") 
                self.tableWidget.item(self.row,1).setText(self.txt1)               
        except:
            pass
    def incsv(self):
        try:
            self.tableWidget.setRowCount(1)
            self.tableWidget.clearContents();
            file=QFileDialog.getOpenFileName(self, '打开文件', '/', '*.txt;;*.csv;;All Files (*)')
            r=open(file[0])
            for i, line in enumerate(r):
                txt=re.split(',|，', line.rstrip())
                print(txt)
    #            for i in range(len(txt)):
    
                self.tableWidget.setItem(i, 0, QTableWidgetItem(txt[0]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(txt[1]))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(txt[2]))
                if len(txt)>3:
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(txt[3]))
                self.tableWidget.insertRow(self.tableWidget.rowCount())
        except:
            pass

    def outcsv(self):
        try:
            file=QFileDialog.getSaveFileName(self, '保存文件', '/', '.txt;;.csv;;All Files (*)')
        #        print(file[0])
            w=open(file[0]+file[1], 'w')
            for i in range(self.tableWidget.rowCount()-1):
        
                txt=self.tableWidget.item(i, 0).text()+','+\
                      self.tableWidget.item(i, 1).text()+','
                if self.tableWidget.item(i, 0).text() in ('1', '2'):                      
                    txt=txt+self.tableWidget.item(i, 2).text()+'\n'
                else:
                    txt=txt+\
                          self.tableWidget.item(i, 2).text()+','+\
                          self.tableWidget.item(i, 3).text()+'\n'
                w.write(txt)
            w.close()
        except:
            pass
class MyPlot(Function):
    def __init__(self, parent=None):
        super(MyPlot, self).__init__(parent)
        self.checkBox1.clicked.connect(self.draw_cantilever)
        self.checkBox2.clicked.connect(self.draw_cantilever)
#        self.Type3.clicked.connect(self.update_figure)
        self.pushButton_5.clicked.connect(self.redraw)
        self.pushButton_2.clicked.connect(self.calc)
        self.drawline()
    def redraw(self):
        self.lineEdit.setEnabled(True);self.lineEdit21.setEnabled(True);
        self.axes.clear()
        self.lineEdit.clear()
        self.axes.set(xlim=[-50, 550], ylim=[-150, 150])
        self.axes.axis('off')        
        self.drawline()
        if self.radioButton_1.isChecked():
            self.tableWidget.setRowCount(1)
            self.tableWidget.clearContents();
        self.textEdit_1.clear();    self.Nbox.clear();    self.Kbox.setValue(8)    ;
        self.lineEdit21.setText('0') ;self.lineEdit22.setText('0') ;  self.lineEdit23.setText('0') ; self.lineEdit24.setText('0') ;
        self.groupBox_3.setEnabled(True)
        self.checkBox1.setChecked(False);  self.checkBox1.setChecked(False)
        self.Type2.setChecked(True) ; self.Type2.setEnabled(True);
        self.groupBox_3.setEnabled(False)
        self.canvas.draw()
        
    def drawline(self):
        self.axes.plot([0, 480], [0, 0], 'k-', linewidth=1, antialiased=False)  # 杆长
    def drawPin(self):  # 固定铰支
        e = np.array([])
        x = []
        self.pin_x = np.array(re.split('\,|\;', self.lineEdit22.text()))
        e = self.pin_x
        if e[-1] != '':
            #            for b,n in enumerate(e):
            for b in range(e.shape[0]):
                x.append(e[b])
                x[b] = float(x[b]) / self.ksc
                if int(x[b]*self.ksc)>self.X[-1] :
                    self.groupBox_3.setEnabled(True)
                    self.lineEdit.setText('等待中...')         
                    self.lineEdit22.setFocus()  
                    QMessageBox.critical(self,"注意","支点的位置超过梁的长度!") 
                    return  1  
                else: 
                    y=19           
                    if x[b] >= 0:
                        self.axes.plot([x[b]], [-8], 'k^', markersize=10, fillstyle='none')  # 三角
                        self.axes.plot([x[b] - 15, x[b] + 15], [-y, -y], 'k-', linewidth=1, antialiased=True)  # 杆长
                        p = mpatches.Rectangle((x[b] - 15, -y), 30, -7, fc='none', hatch='////')
                        self.axes.add_patch(p)  # 阴影填充
                    else:
                        x[b] = abs(x[b])
                        self.axes.plot([x[b]], [8], 'kv', markersize=10, fillstyle='none')  # 三角
                        self.axes.plot([x[b] - 15, x[b] + 15], [y,y], 'k-', linewidth=1, antialiased=True)  # 杆长
                        p = mpatches.Rectangle((x[b] - 15, y), 30, 5, fc='none', hatch='////')
                        self.axes.add_patch(p)  # 阴影填充
                    self.canvas.draw()
                    #        np.linspace(0, 1, 10, endpoint=False)
                    # 均布力
    def drawRoller(self):  # 活动铰支
        d = np.array([])
        x = []
        self.ro_x = np.array(re.split('\,|\;', self.lineEdit23.text()))
        d = self.ro_x
        if d[-1] != '':
            for b, n in enumerate(d):
                x.append(n)
                x[b] = float(x[b]) / self.ksc
                if int(x[b]*self.ksc)>self.X[-1] :
                    self.groupBox_3.setEnabled(True)
                    self.lineEdit.setText('等待中...')         
                    self.lineEdit23.setFocus()  
                    QMessageBox.critical(self,"注意","支点的位置超过梁的长度!") 
                    return  1  
                else:
                    y=18.5  
                    if x[b] >= 0:
                        self.axes.plot([x[b]], [-11], 'ko', markersize=9.5, fillstyle='none')  # 圆
                        self.axes.plot([x[b] - 15, x[b] + 15], [-y, -y], 'k-', linewidth=1, antialiased=True)  # 杆长
                        p = mpatches.Rectangle((x[b] - 15, -y), 30, -7, fc='none', hatch='////')
                        self.axes.add_patch(p)  # 阴影填充
                    else:
                        x[b] = abs(x[b])
                        self.axes.plot([x[b]], [11], 'ko', markersize=9.5, fillstyle='none')  # 圆
                        self.axes.plot([x[b] - 15, x[b] + 15], [y, y], 'k-', linewidth=1, antialiased=True)  # 杆长
                        p = mpatches.Rectangle((x[b] - 15, y), 30, 5, fc='none', hatch='////')
                        self.axes.add_patch(p)  # 阴影填充
                    self.canvas.draw()                        
    def draw_cantilever(self):  # 悬臂梁
        if len(self.axes.lines)>1:
            self.axes.lines.remove(self.axes.lines[-1])
            self.axes. patches.clear()
        if self.checkBox1.isChecked():
            self.lineEdit.clear()
            self.lineEdit22.setText('0')
            self.lineEdit23.setText('0')
            self.checkBox2.setEnabled(False)
            self.axes.plot([0, 0], [-25, 25], 'k-', linewidth=2, antialiased=True)  # 弯矩M
            self.axes.add_patch(mpatches.Rectangle((0, -25), -10, 50, fc='none', hatch='////'))  # 阴影填充
        else:
            self.checkBox2.setEnabled(True)
        if self.checkBox2.isChecked():
            self.lineEdit.clear()            
            self.lineEdit22.setText(str(self.X[-1]))
            self.lineEdit23.setText(str(self.X[-1]))
            self.checkBox1.setEnabled(False)
            self.axes.plot([482, 482], [-25, 25], 'k-', linewidth=2, antialiased=True)  # 弯矩M
            self.axes.add_patch(mpatches.Rectangle((482, -25), 10, 50, fc='none', hatch='////'))  # 阴影填充
        else:
            self.checkBox1.setEnabled(True)        
        self.canvas.draw()
        
        if (self.checkBox1.isChecked()==True and self.checkBox2.isChecked()==False)\
            or \
            (self.checkBox2.isChecked()==True and self.checkBox1.isChecked()==False):
            self.Type2.setEnabled(False) 
        else:
            self.Type2.setEnabled(True)
    def draw_load(self):
      
        row=self.tableWidget.rowCount()-2
        if self.tableWidget.item(row, 0).text()=='1':
            self.draw_concentrate_load(row)
        if self.tableWidget.item (row, 0).text()=='2':
            self.draw_Bending_moment(row)
        if self.tableWidget.item (row, 0).text()=='3':
            self.draw_distributed_load(row)            
# '''===================集中力1=======================================集中力1=======================================集中力1=======================================集中力1===================='''
    def draw_concentrate_load(self, row):  
        x=float(self.tableWidget.item(row, 1).text())/ self.ksc
        p=float(self.tableWidget.item(row, 2).text())/self.ksb

        self.axes.arrow(x, p, 0, -p, linewidth=1, head_width=8, fc='k',
                        antialiased=True, length_includes_head=True)  # 集中力P

        self.canvas.draw()
# '''===================集中力偶2=====================================集中力偶2=====================================集中力偶2=====================================集中力偶2=================='''                        
    def draw_Bending_moment(self, row): 
        MEX =float(self.tableWidget.item(row, 1).text())/ self.ksc
        ME=float(self.tableWidget.item(row, 2).text())/self.ksb
        dx=abs(ME/5)
        if ME < 0:
            self.axes.arrow(MEX , ME/2, dx, 0, linewidth=1, head_width=5, fc='k',
                            antialiased=True)  # 弯矩M
            self.axes.arrow(MEX , -ME/2, -dx, 0, linewidth=1, head_width=5, fc='k',
                            antialiased=True)  # 弯矩M
            self.axes.plot([MEX,MEX ], [ME/2, -ME/2], 'k-', linewidth=2,
                           antialiased=True)  # 弯矩M
        elif ME >= 0:
            MEX = abs(MEX)
            self.axes.arrow(MEX , ME/2, -dx, 0, linewidth=1, head_width=5, fc='k',
                            antialiased=True)  # 弯矩M
            self.axes.arrow(MEX , -ME/2, dx, 0, linewidth=1, head_width=5, fc='k',
                            antialiased=True)  # 弯矩M
            self.axes.plot([MEX , MEX], [ME/2, -ME/2], 'k-', linewidth=2,
                           antialiased=True)  # 弯矩M    
        self.canvas.draw()                           
# '''===================均布载荷3=====================================均布载荷3=====================================均布载荷3=====================================均布载荷3=================='''
    def draw_distributed_load(self, row):  
#        self.tableWidget.sortItems(1, Qt.AscendingOrder)#排序
        coord=float(self.tableWidget.item(row, 1).text())
        x1 = float(self.tableWidget.item(row, 1).text())
        q3 = float(self.tableWidget.item(row, 2).text())
        q4 = float(self.tableWidget.item(row, 3).text())
        for I in range(len(self.X)):
            try:
                if coord == self.X[I]:
                    dx=self.X[I+1]-self.X[I]
                    H = (dx / self.K)#箭头间距
                    k = (q4 - q3) / dx#斜率
                    self.axes.plot([x1/self.ksc, (x1+dx)/self.ksc], [q3/self.ksb, q4/self.ksb], 'k-', linewidth=1, antialiased=True)  
                    x=x1
                    for i in range(self.K1):
                        if k == 0:
                            y=q3
                        else:
                            y = k * (x-x1)  + q3                   
                        self.axes.arrow(x/self.ksc, y/self.ksb, 0, -y/self.ksb, linewidth=1, head_width=6, fc='k',
                                        antialiased=True, length_includes_head=True)  # 集中力P
                        x = x + H
            except:
                self.tableWidget.removeRow(self.tableWidget.rowCount()-2)
        self.canvas.draw()

    def A(self):

        for I in range(1, self.NP+1):
            COORD=float(self.tableWidget.item(I-1, 1).text())
            P=float(self.tableWidget.item(I-1, 2).text())
            print('==1', I,'N:',self.N, 'K', self.K,'NP:', self.NP, 'COORD:', COORD,'P:',  P, 'X:',self.X )
            if self.tableWidget.item(I-1, 0).text()=='1':
                for J in range(0, self.N1):
                    if COORD==self.X[J]:
                        self.P[J]=P
            elif self.tableWidget.item(I-1, 0).text()=='2':
                for J in range(0, self.N1):
                    if COORD==self.X[J]:
                        self.T[J]=P
                        
            elif self.tableWidget.item(I-1, 0).text()=='3':
                P1=float(self.tableWidget.item(I-1, 3).text())
                for J in range(1, self.N1):
                    if COORD==self.X[J-1]:
                        self.QL[J]=P
                        self.QR[J]=P1
        print( '==2','\n',self.P, '\n', self.T,'\n', self.QL,'\n', self.QR)
        
        if self.Type2.isChecked():
            if self.L1!=self.L2:
                self.C()
            else:
                QMessageBox.critical(Dialog,"注意","请选择悬臂梁!")
                return 
        elif self.Type1.isChecked():
            if self.checkBox1.isChecked():
#                print('Enter D')
                self.D()
#                print('D Done')
            elif self.checkBox2.isChecked():
#                print('Enter E')
                self.E()
#                print('E Done') 
        
    def C(self):#简支梁
        X=self.X ;        
        P=self.P ;  T=self.T ; QL=self.QL ; QR=self.QR
        L1=self.L1 ; L2=self.L2 ; SAM1=0 ; SAM2=0
#        print('==3',P,  T, QL, QR)
        for I in range(0, self.N1):
            SAM1=SAM1+P[I]*X[I]-T[I]
            SAM2=SAM2+P[I]*(X[-1]-X[I])+T[I]
            if QL[I]==0 and QR[I]==0:
                continue
            else:
                S=(X[I]-X[I-1])*(QL[I]+QR[I])/2
                C=(1-(QL[I]-QR[I])/(QL[I]+QR[I])/3)*(X[I]-X[I-1])/2
                SAM1=SAM1+S*(C+X[I-1])
                SAM2=SAM2+S*(X[-1]-X[I-1]-C)
        Y1=(SAM1*(X[-1]-L2)-SAM2*L2)/(L1-L2)/X[-1]
        Y2=(SAM2*L1-SAM1*(X[-1]-L1))/(L1-L2)/X[-1]
        for I in range(0, self.N1):
            if X[I]==L1:
                P[I]=P[I]-Y1
#                print('在X=:', X[I], 'R(%.2F):'%X[I], Y1) 
                self.textEdit_1.append('在 X = %s 处:'%str(X[I])+' '*(10-len(str(X[I]))) + 'R(%.2F)='%X[I]+ str(Y1))
            else:   
                if X[I]!=L2:
                    continue
            if X[I]==L2:
                P[I]=P[I]-Y2
#                print('在X=:%s处'% X[I], 'R(%.2F):'%X[I], Y2)
                self.textEdit_1.append('在 X = %s 处:'%str(X[I])+' '*(10-len(str(X[I]))) + 'R(%.2F)='%X[I]+ str(Y2))
            else:
                continue
        self.F( T, P, X,QL, QR, )    
    def D(self):#左端
        X=self.X;
        Y1=0;Y2=0;S=0;C=0;
        P=self.P ; T=self.T ; QL=self.QL ; QR=self.QR
        for I in range(1, self.N1):
            Y1=Y1+P[I]
            Y2=Y2+P[I]*X[I]-T[I]
            if QL[I]==0 and QR[I]==0:
                continue
            S=(X[I]-X[I-1])*(QL[I]+QR[I])/2
            C=(1-(QL[I]-QR[I])/(QL[I]+QR[I])/3)*(X[I]-X[I-1])/2
            Y1=Y1+S
            Y2=Y2+S*(X[I-1]+C)        
        P[0]=P[0]-Y1
        T[0]=T[0]+Y2
#        print('X=', 0, 'R(0):', Y1  )
#        print('X=', 0, 'M[0]:', Y2  )
        self.textEdit_1.append('在 X = 0 处:'+' '*(10-len(str(X[I]))) + 'R(0)='+ str(round(Y1, 2)))    
        self.textEdit_1.append('在 X = 0 处:'+' '*(10-len(str(X[I]))) + 'M(0)='+ str(round(Y2, 2)))
        
        self.F( T, P, X,QL, QR, )      
        
    def E(self):#右端
        X=self.X;
        Y1=0;Y2=0;S=0;C=0;
        P=self.P ; T=self.T ; QL=self.QL ; QR=self.QR
        for I in range(0, self.N1):
            Y1=Y1+P[I]
            Y2=Y2-P[I]*(X[-1]-X[I])-T[I]
            if QL[I]==0 and QR[I]==0:
                continue
            S=(X[I]-X[I-1])*(QL[I]+QR[I])/2
            C=(1-(QL[I]-QR[I])/(QL[I]+QR[I])/3)*(X[I]-X[I-1])/2
            Y1=Y1+S
            Y2=Y2-S*(X[-1]-X[I-1]-C)
        P[-1]=P[-1]-Y1
        T[-1]=T[-1]+Y2
#        print('X=', X[-1], 'R(%.2F):'%X[I], Y1  )
#        print('X=', X[-1], 'M(%.2F):'%X[I], Y2  ) 
        self.textEdit_1.append('在 X = %s 处:'%str(X[I])+' '*(10-len(str(X[I]))) + 'R(%.2F)='%X[I]+  str(round(Y1, 2)))    
        self.textEdit_1.append('在 X = %s 处:'%str(X[I])+' '*(10-len(str(X[I]))) + 'M(%.2F)='%X[I]+ str(round(Y2, 2)))       
        self.F( T, P, X,QL, QR, )    
        
    def F(self, T, P, X,QL, QR, **kwargs):
        Q=np.zeros((self.N1,self.K1))
        M=np.zeros((self.N1,self.K1))        
        XMAX=0 ; MAX=M[0, 0] ; XMIN=0;  MIN=M[0, 0]

        QMAX=0;XQ=0;QX=0;MMAX=1;
        for I in range(1, self.N1):
            for J in range(0, self.K1):
                Q[I, J]=Q[I-1,self.K]-P[I-1]
                M[I, J]=M[I-1,self.K]-T[I-1]+(Q[I-1, self.K]-P[I-1])*(X[I]-X[I-1])*J/self.K
                if QL[I]==0 and QR[I]==0:
                    if abs(Q[I, J])>QMAX:
                        QMAX=abs(Q[I,J])
                        XQ=J*(X[I]-X[I-1])/self.K+X[I-1]
                    if M[I, J]>MAX:
                        MAX=M[I, J] 
                        XMAX=J*(X[I]-X[I-1])/self.K+X[I-1]
                    if M[I, J]<MIN:
                        MIN=M[I, J] 
                        XMIN=J*(X[I]-X[I-1])/self.K+X[I-1]            
                    continue
                if J==0:
                    if abs(Q[I, J])>QMAX:
                        QMAX=abs(Q[I, J])
                        XQ=J*(X[I]-X[I-1])/self.K+X[I-1]
                    if M[I, J]>MAX:
                        MAX=M[I, J] 
                        XMAX=J*(X[I]-X[I-1])/self.K+X[I-1]
                    if M[I, J]<MIN:
                        MIN=M[I, J] 
                        XMIN=J*(X[I]-X[I-1])/self.K+X[I-1]
                    continue
                QX=QR[I]+(QL[I]-QR[I])*(self.K-J)/self.K
                S=((X[I]-X[I-1]))*(QL[I]+QX)*J/2/self.K
                C=(1-(QL[I]-QX)/(QL[I]+QX)/3)*(X[I]-X[I-1])*J/2/self.K
                Q[I, J]=Q[I, J]-S
                M[I, J]=M[I, J]-S*((X[I]-X[I-1])*J/self.K-C)
                if abs(Q[I, J])>QMAX:
                    QMAX=abs(Q[I,J])
                    XQ=J*(X[I]-X[I-1])/self.K+X[I-1]
                if M[I, J]>MAX:
                    MAX=M[I, J] 
                    XMAX=J*(X[I]-X[I-1])/self.K+X[I-1]
                if M[I, J]<MIN:
                    MIN=M[I, J] 
                    XMIN=J*(X[I]-X[I-1])/self.K+X[I-1]
#        print('最大剪力', 'X=', XQ, 'QMAX', QMAX)
        self.a.textEdit1.append('最大剪力在 X = %s 处'%XQ + 'QMAX = %s'%QMAX)         
#        print('最大弯矩', 'X=', XMAX, 'Mmax', MAX) 
        self.a.textEdit1.append('最大弯矩在 X = %s 处'%XMAX + 'Mmax = %s'%MAX)           
#        print('最小弯矩', 'X=', XMIN, 'Mmin', MIN)
        self.a.textEdit1.append('最小弯矩在 X = %s 处'%XMIN + 'Mmin = %s'%MIN)            
        if abs(MIN)>MAX:
            MMAX=abs(MIN)
        else:
            MMAX=MAX
        self.a.handle_click(X, Q, M, MMAX, QMAX, self.N1,self.K1, self.K)
    def calc(self, *args, **kwgs):
        try:
            self.K=self.Kbox.value() ; self.K1=self.K+1
            if self.K==8:
                self.K=40
                self.K1=self.K+1
            self.Kbox.setValue(self.K)
            self.lineEdit.setEnabled(False);self.lineEdit21.setEnabled(False);
            self.a=SecondWindow()
            self.textEdit_1.clear()  
            self.NP=self.tableWidget.rowCount()-1
            self.A()
        except:
            QMessageBox.critical(self,"注意","请检查输入!")         
              
class SecondWindow(QMainWindow):  # 暂时没用

    def __init__(self, parent=None):
        super().__init__(parent)

        self.fig3 = plt.figure(figsize=(4, 1), dpi=80)
        self.canvas3 = FigureCanvas(self.fig3)
        self.axes31 = self.fig3.add_subplot(211)
        self.axes32 = self.fig3.add_subplot(212)
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setWindowTitle("abcd")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox11 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox11.setObjectName("groupBox11")
        self.gridLayout11_2 = QtWidgets.QGridLayout(self.groupBox11)
        self.gridLayout11_2.setObjectName("gridLayout_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)

        self.gridLayout11_3 = QtWidgets.QGridLayout()
        self.gridLayout11_3.setObjectName("gridLayout11_3")


        self.gridLayout11_2.addLayout(self.gridLayout11_3, 1, 1, 1, 1)
        self.textEdit1 = QtWidgets.QTextEdit(self.groupBox11)
        self.textEdit1.setMinimumSize(QtCore.QSize(256, 262))
        self.textEdit1.setObjectName("textEdit1")
        self.gridLayout11_2.addWidget(self.textEdit1, 0, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox11)
        self.groupBox12 = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox12.sizePolicy().hasHeightForWidth())
        self.groupBox12.setSizePolicy(sizePolicy)
        self.groupBox12.setMinimumSize(QtCore.QSize(420, 500))#设置宽高
        self.groupBox12.setAcceptDrops(False)
        self.groupBox12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox12.setObjectName("groupBox12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout11_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout11_3.setSpacing(1)
        self.horizontalLayout11_3.setObjectName("horizontalLayout11_3")
        self.horizontalLayout_2.addLayout(self.horizontalLayout11_3)
        self.horizontalLayout.addWidget(self.groupBox12)
        
        self.horizontalLayout11_3.addWidget(self.canvas3)
        self.setCentralWidget(self.centralWidget)
        self.retranslateUi(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(self.centralWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox11.setTitle(_translate("MainWindow", "GroupBox"))

        self.groupBox12.setTitle(_translate("MainWindow", "GroupBox"))


    def home(self):
        self.toolbar.home()

    def zoom(self):
        self.toolbar.zoom()

    def pan(self):
        self.toolbar.pan()

    def handle_click(self,X, Q, M, MMAX, QMAX, N1,K1, K   ):
        self.textEdit1.clear()
        self.axes31.lines.clear()
        self.axes32.lines.clear()
        listx=[] ;
        if QMAX==0:
            QMAX
        self.N1=N1; self.K1=K1; self.K=K   
        for I in range(1, self.N1):
            for J in range(0, self.K1):
                XIJ=X[I-1]+(X[I]-X[I-1])*J/self.K
                listx.append(XIJ)
                self.axes31.plot(XIJ, Q[I, J], 'k.', markersize=2, )
                self.axes32.plot(XIJ, M[I, J], 'k.', markersize=2,)                
                
                self.textEdit1.append(str(round(XIJ, 2))+' '*4+str(round(Q[I, J], 2))+' '*4+str(round(M[I, J], 2)))
                if XIJ==(X[I]):
                    self.textEdit1.append('\n')
        
#        X1=600/X[-1];Y1=40/QMAX;Y2=40/MMAX;
        self.axes31.plot([0, 0], [np.min(Q), np.max(Q)], 'k', antialiased=True) ;  self.axes31.plot([0, max(listx)], [0, 0] , 'k', antialiased=True);
        self.axes32.plot([0, 0], [np.min(M), np.max(M)], 'k', antialiased=True);   self.axes32.plot([0, max(listx)], [0, 0] , 'k', antialiased=True);
        self.canvas3.draw()
         
        if not self.isVisible():

            self.show()

class Command(QUndoCommand):
    def __init__(self):
        pass

if __name__ == "__main__":
    import sys
    def excepthook(type, value, trace):
        try:
            #            auto.press('alt')
            pass
        except:
            pass
        sys.__excepthook__(type, value, trace)
    sys.excepthook = excepthook
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    
    Dialog = MyPlot()    

    Dialog.show()

    sys.exit(app.exec_())
    
