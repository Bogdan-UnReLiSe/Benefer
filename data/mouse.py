import logging

from PyQt5.QtWidgets import QPushButton, QFileDialog, QInputDialog
from PyQt5.QtCore import Qt, QUrl

from PyQt5 import QtWidgets, QtCore, QtGui

from data.css import *


# Класс, позволяющий в последствии отслеживать место нажатия мышкой в пределах кнопки
class Tracker(QPushButton):
    def interaction(self, object):
        self.object = object
        self.delta_x = 0
        self.delta_y = 0

    # Метод для передачи основного класса приложения в данный
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            try:
                width = self.object.widget.width()
                height = self.object.widget.height()
                if self.object.listOfFunction.currentWidget() == self.object.page_2:
                    if self.object.x_raz.text() == '%':
                        self.object.lineOfX.setText(str(round(event.x() / width * 100)))
                    else:
                        self.object.lineOfX.setText(str(event.x()))
                    if self.object.y_raz.text() == '%':
                        self.object.lineOfY.setText(str(round(event.y() / height * 100)))
                    else:
                        self.object.lineOfY.setText(str(event.y()))
                    name, ok_pressed = QInputDialog.getText(self, "Текст", "Введите текст:")
                    if ok_pressed:
                        self.object.lineOfSoderzhanie.setText(name)
                        self.object.createText_button.click()
                elif self.object.listOfFunction.currentWidget() == self.object.page_3:
                    if self.object.x_raz_2.text() == '%':
                        self.object.lineOfX_2.setText(str(round(event.x() / width * 100)))
                    else:
                        self.object.lineOfX_2.setText(str(event.x()))
                    if self.object.y_raz_2.text() == '%':
                        self.object.lineOfY_2.setText(str(round(event.y() / height * 100)))
                    else:
                        self.object.lineOfY_2.setText(str(event.y()))
                elif self.object.listOfFunction.currentWidget() == self.object.page_4:
                    if self.object.x_raz_5.text() == '%':
                        self.object.lineOfX_5.setText(str(round(event.x() / width * 100)))
                    else:
                        self.object.lineOfX_5.setText(str(event.x()))
                    if self.object.y_raz_5.text() == '%':
                        self.object.lineOfY_5.setText(str(round(event.y() / height * 100)))
                    else:
                        self.object.lineOfY_5.setText(str(event.y()))
                elif self.object.listOfFunction.currentWidget() == self.object.page_5:
                    if self.object.x_raz_19.text() == '%':
                        self.object.lineOfX_19.setText(str(round(event.x() / width * 100)))
                    else:
                        self.object.lineOfX_19.setText(str(event.x()))
                    if self.object.y_raz_19.text() == '%':
                        self.object.lineOfY_19.setText(str(round(event.y() / height * 100)))
                    else:
                        self.object.lineOfY_19.setText(str(event.y()))
                elif self.object.listOfFunction.currentWidget() == self.object.page_5:
                    if self.object.x_raz_19.text() == '%':
                        self.object.lineOfX_19.setText(str(round(event.x() / width * 100)))
                    else:
                        self.object.lineOfX_19.setText(str(event.x()))
                    if self.object.y_raz_19.text() == '%':
                        self.object.lineOfY_19.setText(str(round(event.y() / height * 100)))
                    else:
                        self.object.lineOfY_19.setText(str(event.y()))
                elif self.object.listOfFunction.currentWidget() == self.object.page_6:
                    excep, settings = '', \
                        {'width': (int(self.object.lineOfWidth_14.text()), self.object.width_raz_14.text())}
                    try:
                        if self.object.plus_color_pero.isChecked():
                            if self.object.lineOfColor_14.text() == '':
                                self.object.lineOfColor_14.setStyleSheet(exception)
                                excep = 'All arguments are not filled in'
                            else:
                                settings['color'] = self.object.lineOfColor_14.text()
                                self.object.lineOfColor_14.setStyleSheet(norm)
                        else:
                            settings['color'] = ''
                        if excep:
                            raise Exception(excep)
                        if self.object.verticalLayout_26.count() == 0:
                            self.object.newPero.show()
                            self.object.newAction('Pero', settings)
                            self.object.pero_index = self.object.actions[-1]
                            settings['name'] = self.object.actions[-1][1].text()
                        else:
                            self.object.site.undo(self.object.actions.index(self.object.pero_index))
                            settings['name'] = \
                                self.object.actions[self.object.actions.index(self.object.pero_index)][1].text()
                        self.object.newPoint(event.x(), event.y())
                        settings['points'] = list(map(lambda x:
                                             (int(x[2].text()), x[6].text(), int(x[4].text()), x[7].text()),
                                             self.object.points))
                        self.object.site.pen(points=settings['points'],
                                             width=settings['width'],
                                             color=settings['color'],
                                             name=settings['name'],
                                             num=self.object.actions.index(self.object.pero_index))
                        self.object.actions[self.object.actions.index(self.object.pero_index)][5] = settings
                        self.object.site.save(r'templates/base.html')
                        self.object.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
                    except Exception as e:
                        logging.warning(e)
                elif self.object.listOfFunction.currentWidget() == self.object.page_edit_2:
                    if self.object.x_raz_3.text() == '%':
                        self.object.lineOfX_3.setText(str(round(event.x() / width * 100)))
                    else:
                        self.object.lineOfX_3.setText(str(event.x()))
                    if self.object.y_raz_3.text() == '%':
                        self.object.lineOfY_3.setText(str(round(event.y() / height * 100)))
                    else:
                        self.object.lineOfY_3.setText(str(event.y()))
                elif self.object.listOfFunction.currentWidget() == self.object.page_edit_3:
                    if self.object.x_raz_4.text() == '%':
                        self.object.lineOfX_4.setText(str(round(event.x() / width * 100)))
                    else:
                        self.object.lineOfX_4.setText(str(event.x()))
                    if self.object.y_raz_4.text() == '%':
                        self.object.lineOfY_4.setText(str(round(event.y() / height * 100)))
                    else:
                        self.object.lineOfY_4.setText(str(event.y()))
                elif self.object.listOfFunction.currentWidget() == self.object.page_edit_4:
                    if self.object.x_raz_7.text() == '%':
                        self.object.lineOfX_7.setText(str(round(event.x() / width * 100)))
                    else:
                        self.object.lineOfX_7.setText(str(event.x()))
                    if self.object.y_raz_7.text() == '%':
                        self.object.lineOfY_7.setText(str(round(event.y() / height * 100)))
                    else:
                        self.object.lineOfY_7.setText(str(event.y()))
                elif self.object.listOfFunction.currentWidget() == self.object.page_edit_5:
                    if self.object.x_raz_20.text() == '%':
                        self.object.lineOfX_20.setText(str(round(event.x() / width * 100)))
                    else:
                        self.object.lineOfX_20.setText(str(event.x()))
                    if self.object.y_raz_20.text() == '%':
                        self.object.lineOfY_20.setText(str(round(event.y() / height * 100)))
                    else:
                        self.object.lineOfY_20.setText(str(event.y()))
            except Exception:
                pass

    def mouseMoveEvent(self, event):
        try:
            width = self.object.widget.width()
            height = self.object.widget.height()
            if event.buttons() == Qt.LeftButton and event.x() <= width and event.y() <= height \
                    and self.object.listOfFunction.currentWidget() == self.object.page_4:
                x = int(self.object.lineOfX_5.text())
                if self.object.x_raz_5.text() == '%':
                    x = width / 100 * int(x)
                y = int(self.object.lineOfY_5.text())
                if self.object.y_raz_5.text() == '%':
                    y = height / 100 * int(y)
                w = event.x() - x
                h = event.y() - y
                if self.object.width_raz_5.text() == '%':
                    self.object.lineOfWidth_5.setText(str(round(w / width * 100)))
                else:
                    self.object.lineOfWidth_5.setText(str(int(w)))
                if self.object.height_raz_3.text() == '%':
                    self.object.lineOfHeight_3.setText(str(round(h / height * 100)))
                else:
                    self.object.lineOfHeight_3.setText(str(int(h)))
            elif event.buttons() == Qt.LeftButton and event.x() <= width and event.y() <= height \
                    and self.object.listOfFunction.currentWidget() == self.object.page_5:
                x = int(self.object.lineOfX_19.text())
                if self.object.x_raz_19.text() == '%':
                    x = width / 100 * int(x)
                y = int(self.object.lineOfY_19.text())
                if self.object.y_raz_19.text() == '%':
                    y = height / 100 * int(y)
                w = event.x() - x
                h = event.y() - y
                if self.object.width_raz_13.text() == '%':
                    self.object.lineOfWidth_13.setText(str(round(w / width * 100)))
                else:
                    self.object.lineOfWidth_13.setText(str(int(w)))
                if self.object.height_raz_9.text() == '%':
                    self.object.lineOfHeight_9.setText(str(round(h / height * 100)))
                else:
                    self.object.lineOfHeight_9.setText(str(int(h)))
            elif event.buttons() == Qt.LeftButton and event.x() <= width and event.y() <= height \
                    and self.object.listOfFunction.currentWidget() == self.object.page_3:
                x = int(self.object.lineOfX_2.text())
                if self.object.x_raz_2.text() == '%':
                    x = width / 100 * int(x)
                y = int(self.object.lineOfY_2.text())
                if self.object.y_raz_2.text() == '%':
                    y = height / 100 * int(y)
                w = event.x() - x
                h = event.y() - y
                if self.object.width_raz_2.text() == '%':
                    self.object.lineOfWidth_2.setText(str(round(w / width * 100)))
                else:
                    self.object.lineOfWidth_2.setText(str(int(w)))
                if self.object.height_raz.text() == '%':
                    self.object.lineOfHeight.setText(str(round(h / height * 100)))
                else:
                    self.object.lineOfHeight.setText(str(int(h)))
        except Exception as e:
            logging.warning(e)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.object.listOfFunction.currentWidget() == self.object.page_4:
            self.object.createRect_button.click()
            self.delta_x = 0
            self.delta_y = 0
        elif event.button() == Qt.LeftButton and self.object.listOfFunction.currentWidget() == self.object.page_5:
            self.object.createOval_button.click()
        elif event.button() == Qt.LeftButton and self.object.listOfFunction.currentWidget() == self.object.page_3:
            h = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
            if h:
                self.object.lineOfSource.setText(h)
            self.object.createImage_button.click()


"""self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.MainWidget)
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout_3.addWidget(self.webEngineView, 1, 1, 1, 1)"""

