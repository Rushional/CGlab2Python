
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


green = QPen(Qt.green, 1, Qt.SolidLine)
blue = QPen(Qt.blue, 1, Qt.SolidLine)
red = QPen(Qt.red, 1, Qt.SolidLine)
black = QPen(Qt.black, 1, Qt.SolidLine)
yellow = QPen(Qt.yellow, 1, Qt.SolidLine)
gray = QPen(Qt.gray, 1, Qt.SolidLine)
#нахождение точки по центру отрезка PQ
def midpoint(p,q):
        return [(p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0]
#получение списка средних точек по списку точек
def mid(pts_list):
        mid_list=['']*(len(pts_list)-1)
        for i in range(len(mid_list)):
            mid_list[i]=midpoint(pts_list[i],pts_list[i+1])
        return(mid_list)
#разбиение кривой безье на кривые безье поменьше
def divide(pts):
        mid_1=mid(pts)
        mid_2=mid(mid_1)
        mid_3=mid(mid_2)
        mid_4=mid(mid_3)
        return([[pts[0],mid_1[0],mid_2[0],mid_3[0],mid_4[0]],
            [mid_4[0],mid_3[1],mid_2[2],mid_1[3],pts[4]]])
#проверка является прямой ли линия заданная данными точками
def flat(pts):
        delt=1
        ax = (3.0*pts[1][0] - 2.0*pts[0][0] - pts[4][0])**2
        ay = (3.0*pts[1][1] - 2.0*pts[0][1] - pts[4][1])**2
        bx = (3.0*pts[2][0] - pts[0][0] - 2.0*pts[4][0])**2
        by = (3.0*pts[2][1] - pts[0][1] - 2.0*pts[4][1])**2

        return(max(ax,bx)+max(ay,by)<=delt)
#отрисовка маленького кусочка кривой
def drawSeg(pts,qp):
    for i in range(len(pts)-1):
        qp.drawLine(int(pts[i][0])+200,int(-pts[i][1])+200,
        int(pts[i+1][0])+200,int(-pts[i+1][1])+200)
#отрисовка кривой
def drawCrv(pts,qp):
        qp.setPen(black)
        if flat(pts):
            drawSeg(pts,qp)
        else:
            pcs=divide(pts)
            drawCrv(pcs[0],qp)
            drawCrv(pcs[1],qp)


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.points=None
        self.axis=None
    #сеттеры точек и осей
    def setPoints(self, pts):
        self.points=pts
    def setAxis(self,axs):
        self.axis=axs

    def initUI(self):
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle('TEST')
        self.show()
    #отрисовка осей
    def drawAxis(self,qp):
        qp.setPen(blue)
        qp.drawLine(self.axis[0][0]+200,self.axis[0][1]+200,self.axis[1][0]+200,self.axis[1][1]+200)
        qp.setPen(green)
        qp.drawLine(self.axis[0][0]+200,self.axis[0][1]+200,self.axis[2][0]+200,self.axis[2][1]+200)
        qp.setPen(red)
        qp.drawLine(self.axis[0][0]+200,self.axis[0][1]+200,self.axis[3][0]+200,self.axis[3][1]+200)
    #отрисовка ломанной, соединяющей контрольные точки и контрольных точек
    def drawConPoints(self,qp):
        qp.setPen(yellow)
        for i in range(len(self.points)-1):
            qp.drawLine(self.points[i][0]+200,-self.points[i][1]+200,self.points[i+1][0]+200,-self.points[i+1][1]+200)
        qp.setPen(gray)
        for i in range(len(self.points)):
            qp.drawPoint(self.points[i][0]+200,-self.points[i][1]+200)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        if self.axis!=None:
            self.drawAxis(qp)
        if self.points!=None:
            self.drawConPoints(qp)
            drawCrv(self.points,qp)
        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Canvas()
    pts=[[0,0],
            [0,100],
            [100,100],
            [100,0],
            [0,100],]
    axs=[[200,200],
            [400,200],
            [200,0],
            [200,200]]
    ex.setPoints(pts)
    ex.setAxis(axs)

    sys.exit(app.exec_())
