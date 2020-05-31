from PyQt5 import *
from interface import *
from mrx import *
from math import pi
from canvas import *


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.draw.clicked.connect(self.__draw)
        self.ui.canvas = Canvas()
        self.ui.canvas.show()

    # Функции возвращающие матрицы поворотов, проекций, и точек, в зависимости от ввеённого в интерфейсе
    def rot_x(self):
        return float(self.ui.rot_x.value()) / 100 * pi

    def rot_y(self):
        return float(self.ui.rot_y.value()) / 100 * pi

    def projection(self):
        if self.ui.proect.value() == 1:
            return iso
        else:
            return dim

    def pts(self):
        return ([[self.ui.p1x_1.value(), self.ui.p1x_2.value(), self.ui.p1x_3.value(), 1],
                 [self.ui.p2x_1.value(), self.ui.p2x_2.value(), self.ui.p2x_3.value(), 1],
                 [self.ui.p3x_1.value(), self.ui.p3x_2.value(), self.ui.p3x_3.value(), 1],
                 [self.ui.p4x_1.value(), self.ui.p4x_2.value(), self.ui.p4x_3.value(), 1],
                 [self.ui.p5x_1.value(), self.ui.p5x_2.value(), self.ui.p5x_3.value(), 1], ])

    # расчёт повернутой и спроецированной матрицы точек
    def __calc_pts(self):
        return mult_mrx_mult(self.pts(), [rotate_x(self.rot_x()), rotate_y(self.rot_y()), self.projection()])

    # расчёт спроецированной матрицы осей
    def __calc_axs(self):
        return mrx_mult(axis, self.projection())

    # тут в canvas передаются новые матрицы точек и осей и он перерисовы
    def __draw(self):
        self.ui.canvas.setPoints(self.__calc_pts())
        self.ui.canvas.setAxis(self.__calc_axs())
        self.ui.canvas.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    intfc = MainWindow()
    intfc.show()
    app.exec()
