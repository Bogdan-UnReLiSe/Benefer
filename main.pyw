import sys
from data.backend import SiteBuilder
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QColorDialog, QWidget
from PyQt5.QtCore import Qt, QUrl

from style import Ui_MainWindow
from style_fw import Ui_Key
from style_sw import Ui_StartServer

from PyQt5 import QtCore, QtMultimedia, QtGui, QtWidgets
from data.css import *
import subprocess
import os
import shutil
import glob

import logging

from data.scriptToSaveProject import saveProject


# Основной класс приложения, где реализиуется вся основная логика
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        with open('cash\key.txt', 'r') as file:
            self.key = file.read()
        self.count = 0

        # Загрузка звука клика на кнопку
        self.load_mp3('Sound/click_sound.mp3')

        self.patternBut.clicked.connect(self.openProj)

        self.lineOfWidth_14.setText('5')


        # Найстрока двух основных сцен программы(Начальной и Главной)
        self.TwoMainWindow.setCurrentWidget(self.Intro)
        self.lauchBut.clicked.connect(self.toMainWidget)
        self.lauchBut.clicked.connect(self.player.play)

        # Настройка работы listOfFunction (Группа виджетов с различными функциями для редактирования)
        self.listOfFunction.setHidden(True)
        self.listOfFunction.setCurrentWidget(self.page)
        self.title_btn.clicked.connect(self.switchLishOfFunction)
        self.text_btn.clicked.connect(self.switchLishOfFunction)
        self.image_btn.clicked.connect(self.switchLishOfFunction)
        self.figure_btn.clicked.connect(self.switchLishOfFunction)
        self.cyrcle_btn.clicked.connect(self.switchLishOfFunction)
        self.pero_btn.clicked.connect(self.switchLishOfFunction)

        self.title_btn.clicked.connect(self.player.play)
        self.text_btn.clicked.connect(self.player.play)
        self.image_btn.clicked.connect(self.player.play)
        self.figure_btn.clicked.connect(self.player.play)
        self.cyrcle_btn.clicked.connect(self.player.play)
        self.pero_btn.clicked.connect(self.player.play)

        # Настройка кнопки для сохранения файлов
        self.MainLogo.clicked.connect(self.saving)

        # Настройка вкладки для редактирования текста
        self.soderzhanie_button.clicked.connect(self.textSettings)
        self.shrift_button.clicked.connect(self.textSettings)
        self.color_button.clicked.connect(self.textSettings)
        self.size_button.clicked.connect(self.textSettings)
        self.width_button.clicked.connect(self.textSettings)
        self.x_button.clicked.connect(self.textSettings)
        self.y_button.clicked.connect(self.textSettings)
        self.createText_button.clicked.connect(self.textSettings)

        self.width_raz.clicked.connect(self.textSettings)
        self.size_raz.clicked.connect(self.textSettings)
        self.y_raz.clicked.connect(self.textSettings)
        self.x_raz.clicked.connect(self.textSettings)

        self.createText_button.clicked.connect(self.player.play)

        # Настройка кнопок для редактирования заголовка
        self.header_button.clicked.connect(self.tabSettings)
        self.icon_button.clicked.connect(self.tabSettings)

        # Настройка кнопок для редактирования картинок
        self.source_button.clicked.connect(self.imageSettings)
        self.height_button.clicked.connect(self.imageSettings)
        self.width_button_2.clicked.connect(self.imageSettings)
        self.x_button_2.clicked.connect(self.imageSettings)
        self.y_button_2.clicked.connect(self.imageSettings)
        self.createImage_button.clicked.connect(self.imageSettings)
        self.createImage_button.clicked.connect(self.player.play)

        self.width_raz_2.clicked.connect(self.imageSettings)
        self.height_raz.clicked.connect(self.imageSettings)
        self.y_raz_2.clicked.connect(self.imageSettings)
        self.x_raz_2.clicked.connect(self.imageSettings)

        # Настройка кнопок для редактирования прямоугольников
        self.width_button_5.clicked.connect(self.rectSettings)
        self.height_button_3.clicked.connect(self.rectSettings)
        self.color_button_3.clicked.connect(self.rectSettings)
        self.border_button.clicked.connect(self.rectSettings)
        self.color_button_4.clicked.connect(self.rectSettings)
        self.x_button_5.clicked.connect(self.rectSettings)
        self.y_button_5.clicked.connect(self.rectSettings)
        self.border_button_5.clicked.connect(self.rectSettings)
        self.createRect_button.clicked.connect(self.rectSettings)
        self.createRect_button.clicked.connect(self.player.play)


        self.width_raz_5.clicked.connect(self.rectSettings)
        self.height_raz_3.clicked.connect(self.rectSettings)
        self.border_raz.clicked.connect(self.rectSettings)
        self.x_raz_5.clicked.connect(self.rectSettings)
        self.y_raz_5.clicked.connect(self.rectSettings)

        # Настройка кнопок для редактирования овалов
        self.width_button_13.clicked.connect(self.ovalSettings)
        self.height_button_9.clicked.connect(self.ovalSettings)
        self.color_button_13.clicked.connect(self.ovalSettings)
        self.border_button_7.clicked.connect(self.ovalSettings)
        self.color_button_21.clicked.connect(self.ovalSettings)
        self.x_button_19.clicked.connect(self.ovalSettings)
        self.y_button_19.clicked.connect(self.ovalSettings)
        self.createOval_button.clicked.connect(self.ovalSettings)
        self.createOval_button.clicked.connect(self.player.play)

        self.width_raz_13.clicked.connect(self.ovalSettings)
        self.height_raz_9.clicked.connect(self.ovalSettings)
        self.border_raz_7.clicked.connect(self.ovalSettings)
        self.x_raz_19.clicked.connect(self.ovalSettings)
        self.y_raz_19.clicked.connect(self.ovalSettings)

        self.width_button_14.clicked.connect(self.peroSettings)
        self.color_button_14.clicked.connect(self.peroSettings)
        self.width_raz_14.clicked.connect(self.peroSettings)

        # Настройка панели действий
        self.listOfActions.setHidden(True)
        self.ActionsButton.clicked.connect(self.player.play)
        self.ActionsButton.clicked.connect(self.hideListOfAction)

        self.soderzhanie_button_2.clicked.connect(self.textChange)
        self.shrift_button_2.clicked.connect(self.textChange)
        self.color_button_2.clicked.connect(self.textChange)
        self.width_button_3.clicked.connect(self.textChange)
        self.size_button_2.clicked.connect(self.textChange)
        self.shrift_button_2.clicked.connect(self.textChange)
        self.width_raz_3.clicked.connect(self.textChange)
        self.size_raz_2.clicked.connect(self.textChange)
        self.x_button_3.clicked.connect(self.textChange)
        self.y_button_3.clicked.connect(self.textChange)
        self.x_raz_3.clicked.connect(self.textChange)
        self.y_raz_3.clicked.connect(self.textChange)
        self.editBut_2.clicked.connect(self.textChange)
        self.deleteBut_2.clicked.connect(self.textChange)
        self.deleteBut_2.clicked.connect(self.hideListOfFunction)

        self.source_button_2.clicked.connect(self.imageChange)
        self.width_button_4.clicked.connect(self.imageChange)
        self.height_button_2.clicked.connect(self.imageChange)
        self.x_button_4.clicked.connect(self.imageChange)
        self.y_button_4.clicked.connect(self.imageChange)
        self.width_raz_4.clicked.connect(self.imageChange)
        self.height_raz_2.clicked.connect(self.imageChange)
        self.x_raz_4.clicked.connect(self.imageChange)
        self.y_raz_4.clicked.connect(self.imageChange)
        self.editBut_3.clicked.connect(self.imageChange)
        self.deleteBut_3.clicked.connect(self.imageChange)
        self.deleteBut_3.clicked.connect(self.hideListOfFunction)

        self.width_button_7.clicked.connect(self.rectChange)
        self.height_button_5.clicked.connect(self.rectChange)
        self.color_button_7.clicked.connect(self.rectChange)
        self.border_button_3.clicked.connect(self.rectChange)
        self.color_button_8.clicked.connect(self.rectChange)
        self.x_button_7.clicked.connect(self.rectChange)
        self.y_button_7.clicked.connect(self.rectChange)
        self.editBut_4.clicked.connect(self.rectChange)
        self.deleteBut_4.clicked.connect(self.rectChange)
        self.deleteBut_4.clicked.connect(self.hideListOfFunction)
        self.width_raz_7.clicked.connect(self.rectChange)
        self.height_raz_5.clicked.connect(self.rectChange)
        self.border_raz_3.clicked.connect(self.rectChange)
        self.x_raz_7.clicked.connect(self.rectChange)
        self.y_raz_7.clicked.connect(self.rectChange)
        self.border_button_4.clicked.connect(self.rectChange)

        self.width_button_21.clicked.connect(self.ovalChange)
        self.height_button_15.clicked.connect(self.ovalChange)
        self.color_button_23.clicked.connect(self.ovalChange)
        self.border_button_8.clicked.connect(self.ovalChange)
        self.color_button_22.clicked.connect(self.ovalChange)
        self.x_button_20.clicked.connect(self.ovalChange)
        self.y_button_20.clicked.connect(self.ovalChange)
        self.editBut_13.clicked.connect(self.ovalChange)
        self.deleteBut_13.clicked.connect(self.ovalChange)
        self.deleteBut_13.clicked.connect(self.hideListOfFunction)
        self.width_raz_21.clicked.connect(self.ovalChange)
        self.height_raz_15.clicked.connect(self.ovalChange)
        self.border_raz_8.clicked.connect(self.ovalChange)
        self.x_raz_20.clicked.connect(self.ovalChange)
        self.y_raz_20.clicked.connect(self.ovalChange)

        self.width_button_15.clicked.connect(self.peroChange)
        self.width_raz_15.clicked.connect(self.peroChange)
        self.color_button_15.clicked.connect(self.peroChange)
        self.deleteBut_15.clicked.connect(self.peroChange)
        self.deleteBut_15.clicked.connect(self.hideListOfFunction)

        self.icon_button_3.clicked.connect(self.changeName)
        self.icon_button_4.clicked.connect(self.changeName)
        self.icon_button_5.clicked.connect(self.changeName)
        self.icon_button_6.clicked.connect(self.changeName)
        self.icon_button_19.clicked.connect(self.changeName)

        self.plus_shrift_text.clicked.connect(self.plusArguments)
        self.plus_color_text.clicked.connect(self.plusArguments)
        self.plus_width_text.clicked.connect(self.plusArguments)
        self.plus_color_rect.clicked.connect(self.plusArguments)
        self.plus_border_rect.clicked.connect(self.plusArguments)
        self.plus_colorofborder_rect.clicked.connect(self.plusArguments)
        self.plus_color_oval.clicked.connect(self.plusArguments)
        self.plus_border_oval.clicked.connect(self.plusArguments)
        self.plus_colorofborder_oval.clicked.connect(self.plusArguments)
        self.plus_vlozh.clicked.connect(self.plusArguments)

        self.plus_shrift_text_2.clicked.connect(self.plusArguments)
        self.plus_color_text_3.clicked.connect(self.plusArguments)
        self.plus_width_text_2.clicked.connect(self.plusArguments)
        self.plus_color_rect_2.clicked.connect(self.plusArguments)
        self.plus_border_rect_2.clicked.connect(self.plusArguments)
        self.plus_colorofborder_rect_2.clicked.connect(self.plusArguments)
        self.plus_color_oval_2.clicked.connect(self.plusArguments)
        self.plus_border_color_2.clicked.connect(self.plusArguments)
        self.plus_colorofborder_oval_2.clicked.connect(self.plusArguments)
        self.plus_vlozh_2.clicked.connect(self.plusArguments)

        self.plus_color_pero.clicked.connect(self.plusArguments)
        self.plus_color_pero_2.clicked.connect(self.plusArguments)

        self.play_btn.clicked.connect(self.play)

        self.frame_30.hide()
        self.frame_31.hide()
        self.frame_32.hide()
        self.frame_23.hide()
        self.frame_24.hide()
        self.frame_25.hide()
        self.frame_84.hide()
        self.frame_86.hide()
        self.frame_128.hide()
        self.frame_129.hide()
        self.frame_45.hide()

        self.newPero.hide()
        self.newPero.clicked.connect(self.peroSettings)

        self.actions = []
        self.points = []

        self.site = SiteBuilder()
        self.lineOfSize.setText('100')
        self.redactText = False

    def openProj(self):
        try:
            h = QFileDialog.getOpenFileName(self, 'Выберете html файл вашего проекта', '')[0]
            if h:
                put = '/'.join(h.split('/')[:-1])
                for i in range(len(self.actions)):
                    self.delActions(i)
                self.actions.clear()
                shutil.copy(h, f'templates/base.html')
                files = glob.glob(f'{put}/static/img/*')
                for f in files:
                    name = f.split("img")[-1][1:]
                    shutil.copy(f, f'static/img/{name}')
                self.site = SiteBuilder('base')
                for elem in self.site.prev:
                    if elem.__class__.__name__ == 'Tab':
                        mode = 'Tab'
                        settings = {'page_name': elem.page_name,
                                    'icon': elem.icon}
                    elif elem.__class__.__name__ == 'Paragraph':
                        mode = 'Text'
                        settings = {'text': elem.text,
                                    'width': elem.width,
                                    'font': elem.font,
                                    'color': elem.color,
                                    'font_size': elem.font_size,
                                    'x': elem.x,
                                    'y': elem.y,
                                    'name': elem.name}
                    elif elem.__class__.__name__ == 'Image':
                        mode = 'Image'
                        settings = {'src': elem.src,
                                    'width': elem.width,
                                    'height': elem.height,
                                    'x': elem.x,
                                    'y': elem.y,
                                    'name': elem.name}
                    elif elem.__class__.__name__ == 'Rect':
                        mode = 'Rect'
                        settings = {'width': elem.w,
                                    'height': elem.h,
                                    'border': elem.border,
                                    'border_color': elem.border_color,
                                    'color': elem.color,
                                    'x': elem.x,
                                    'y': elem.y,
                                    'name': elem.name}
                    elif elem.__class__.__name__ == 'Oval':
                        mode = 'Oval'
                        settings = {'width': elem.w,
                                    'height': elem.h,
                                    'border': elem.border,
                                    'border_color': elem.border_color,
                                    'color': elem.color,
                                    'x': elem.x,
                                    'y': elem.y,
                                    'name': elem.name}
                    self.newAction(mode, settings)
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
                self.toMainWidget()
        except Exception as e:
            logging.warning(e)

    def play(self):
        global fw, sw
        if self.key == '':
            fw = KeyWidget()
            fw.show()
            os.system(f'xTunnel -k {self.key}')
        else:
            sw = PlayWidget()
            sw.show()

    # Функция отвечает за загрузку музыкального файла и создание объекта плеера, в котором эта музыка будет содержаться.
    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    # Функция для скрытия и появления listOfFunction
    def hideOrAppearListOfFunction(self):
        if self.listOfFunction.isHidden():
            self.appearListOfFunction()
        else:
            self.hideListOfFunction()

    def appearListOfFunction(self):
        self.listOfFunction.setHidden(False)

    def hideListOfFunction(self):
        self.listOfFunction.setHidden(True)

    # Функция для смены страниц в listOfFunction
    def switchLishOfFunction(self):
        if self.sender() == self.title_btn:
            self.pushButton_2.setCursor(Qt.ArrowCursor)
            self.listOfFunction.setCurrentWidget(self.page)
            self.listOfFunction.setHidden(not(self.title_btn.isChecked()))
            for elem in [self.text_btn, self.image_btn, self.figure_btn, self.cyrcle_btn, self.pero_btn]:
                elem.setChecked(False)
        elif self.sender() == self.text_btn:
            if self.text_btn.isChecked():
                self.pushButton_2.setCursor(Qt.IBeamCursor)
            else:
                self.pushButton_2.setCursor(Qt.ArrowCursor)
            self.listOfFunction.setCurrentWidget(self.page_2)
            self.listOfFunction.setHidden(not(self.text_btn.isChecked()))
            for elem in [self.title_btn, self.image_btn, self.figure_btn, self.cyrcle_btn, self.pero_btn]:
                elem.setChecked(False)
        elif self.sender() == self.image_btn:
            if self.image_btn.isChecked():
                self.pushButton_2.setCursor(Qt.CrossCursor)
            else:
                self.pushButton_2.setCursor(Qt.ArrowCursor)
            self.listOfFunction.setCurrentWidget(self.page_3)
            self.listOfFunction.setHidden(not(self.image_btn.isChecked()))
            for elem in [self.title_btn, self.text_btn, self.figure_btn, self.cyrcle_btn, self.pero_btn]:
                elem.setChecked(False)
        elif self.sender() == self.figure_btn:
            if self.figure_btn.isChecked():
                self.pushButton_2.setCursor(Qt.CrossCursor)
            else:
                self.pushButton_2.setCursor(Qt.ArrowCursor)
            self.listOfFunction.setCurrentWidget(self.page_4)
            self.listOfFunction.setHidden(not(self.figure_btn.isChecked()))
            for elem in [self.title_btn, self.text_btn, self.image_btn, self.cyrcle_btn, self.pero_btn]:
                elem.setChecked(False)
        elif self.sender() == self.cyrcle_btn:
            if self.cyrcle_btn.isChecked():
                self.pushButton_2.setCursor(Qt.CrossCursor)
            else:
                self.pushButton_2.setCursor(Qt.ArrowCursor)
            self.listOfFunction.setCurrentWidget(self.page_5)
            self.listOfFunction.setHidden(not (self.cyrcle_btn.isChecked()))
            for elem in [self.title_btn, self.text_btn, self.image_btn, self.figure_btn, self.pero_btn]:
                elem.setChecked(False)
        elif self.sender() == self.pero_btn:
            if self.pero_btn.isChecked():
                self.pushButton_2.setCursor(Qt.CrossCursor)
            else:
                self.pushButton_2.setCursor(Qt.ArrowCursor)
            self.listOfFunction.setCurrentWidget(self.page_6)
            self.listOfFunction.setHidden(not (self.pero_btn.isChecked()))
            for elem in [self.title_btn, self.text_btn, self.image_btn, self.figure_btn, self.cyrcle_btn]:
                elem.setChecked(False)

    # Функция для переключения с Начальной к Главной сцене
    def toMainWidget(self):
        self.TwoMainWindow.setCurrentWidget(self.MainWidget)

    # Функция для сохранения файла с сайтом
    def saving(self):
        h = QFileDialog.getSaveFileName(self, 'Сохранить сайт', '', '')[0]
        if h:
            try:
                saveProject(h)
            except Exception as e:
                logging.warning(e)
            self.site.save(h + '/site.html')

    # Функция для вызова диологовых окон редактирования текста
    def textSettings(self):
        if self.sender() == self.soderzhanie_button:
            name, ok_pressed = QInputDialog.getText(self, "Текст", "Введите текст:")
            if ok_pressed:
                self.lineOfSoderzhanie.setText(name)
        elif self.sender() == self.shrift_button:
            name, ok_pressed = QInputDialog.getItem(self, "Шрифт", "Выберете шрифт:",
                                                    ("Arial", "Times New Roman"), 1, False)
            if ok_pressed:
                self.lineOfShrift.setText(name)
        elif self.sender() == self.color_button:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor.setText(color.name())
        elif self.sender() == self.size_button:
            name, ok_pressed = QInputDialog.getInt(self, "Размер", "Введите размер шрифта:", 5, 1, 1000, 1)
            if ok_pressed:
                self.lineOfSize.setText(str(name))
        elif self.sender() == self.width_button:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите максимальную ширину текста:", 5, 1, 100, 1)
            if ok_pressed:
                self.lineOfWidth.setText(str(name))
        elif self.sender() == self.x_button:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ слева:", 0, 0, 100, 1)
            if ok_pressed:
                self.lineOfX.setText(str(name))
        elif self.sender() == self.y_button:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ сверху:", 0, 0, 100, 1)
            if ok_pressed:
                self.lineOfY.setText(str(name))
        elif self.sender() == self.size_raz:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("pt", "px", "%", "vh", "vw"), 1, False)
            if ok_pressed:
                self.size_raz.setText(name)
        elif self.sender() == self.width_raz:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vw"), 1, False)
            if ok_pressed:
                self.width_raz.setText(name)
        elif self.sender() == self.x_raz:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа слева:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.x_raz.setText(name)
        elif self.sender() == self.y_raz:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа сверху:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.y_raz.setText(name)
        elif self.sender() == self.createText_button:
            try:
                excep, settings = False, {}
                if self.lineOfSoderzhanie.text() == '':
                    self.lineOfSoderzhanie.setStyleSheet(exception)
                    excep = True
                else:
                    settings['text'] = self.lineOfSoderzhanie.text()
                    self.lineOfSoderzhanie.setStyleSheet(norm)
                if self.lineOfSize.text() == '':
                    self.lineOfSize.setStyleSheet(exception)
                    excep = True
                else:
                    settings['font_size'] = (self.lineOfSize.text(), self.size_raz.text())
                    self.lineOfSize.setStyleSheet(norm)
                if self.lineOfX.text() == '':
                    self.lineOfX.setStyleSheet(exception)
                    excep = True
                else:
                    settings['x'] = (self.lineOfX.text(), self.x_raz.text())
                    self.lineOfX.setStyleSheet(norm)
                if self.lineOfY.text() == '':
                    self.lineOfY.setStyleSheet(exception)
                    excep = True
                else:
                    settings['y'] = (self.lineOfY.text(), self.y_raz.text())
                    self.lineOfY.setStyleSheet(norm)
                if self.plus_shrift_text.isChecked():
                    if self.lineOfShrift.text() == '':
                        self.lineOfShrift.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['font'] = self.lineOfShrift.text()
                        self.lineOfShrift.setStyleSheet(norm)
                else:
                    settings['font'] = ''
                if self.plus_color_text.isChecked():
                    if self.lineOfColor.text() == '':
                        self.lineOfColor.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['color'] = self.lineOfColor.text()
                        self.lineOfColor.setStyleSheet(norm)
                else:
                    settings['color'] = ''
                if self.plus_width_text.isChecked():
                    if self.lineOfWidth.text() == '':
                        self.lineOfWidth.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['width'] = (self.lineOfWidth.text(), self.width_raz.text())
                        self.lineOfWidth.setStyleSheet(norm)
                else:
                    settings['width'] = ('', '')
                if excep:
                    raise Exception
                self.newAction('Text', settings)
                self.site.paragraph(text=settings['text'],
                                    width=settings['width'],
                                    font_size=settings['font_size'],
                                    color=settings['color'],
                                    font=settings['font'],
                                    y=settings['y'],
                                    x=settings['x'],
                                    name=self.actions[-1][1].text())
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            except Exception as e:
                self.lineOfSoderzhanie.setText('')

    # Функция для вызова диологовых окон редактирования заголовка
    def tabSettings(self):
        if self.sender() == self.header_button:
            name, ok_pressed = QInputDialog.getText(self, "Заголовк", "Введите текст заголовка:")
            if ok_pressed:
                self.lineOfHeader.setText(name)
                self.site.title(name)
                self.lineOfSource_3.setText(name)
        elif self.sender() == self.icon_button:
            h = QFileDialog.getOpenFileName(self, 'Выбрать иконку', '')[0]
            if h:
                self.lineOfIcon.setText(h)
                name = h.split('/')[-1]
                shutil.copy(self.lineOfIcon.text(), f'static/img/' + name)
                self.site.icon(self)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(f'static/img/' + name), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.title_btn_25.setIcon(icon)

    # Функция для вызова диологовых окон редактирования картинок
    def imageSettings(self):
        if self.sender() == self.source_button:
            h = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
            if h:
                self.lineOfSource.setText(h)
        elif self.sender() == self.height_button:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину картинки:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfHeight.setText(str(name))
        elif self.sender() == self.width_button_2:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите длину картинки:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfWidth_2.setText(str(name))
        elif self.sender() == self.x_button_2:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ слева:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfX_2.setText(str(name))
        elif self.sender() == self.y_button_2:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ сверху:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfY_2.setText(str(name))
        elif self.sender() == self.width_raz_2:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для ширины картинки:",
                                                    ("px", "%", "vw"), 1, False)
            if ok_pressed:
                self.width_raz_2.setText(name)
        elif self.sender() == self.height_raz:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для длины картинки:",
                                                    ("px", "%", "vh"), 1, False)
            if ok_pressed:
                self.height_raz.setText(name)
        elif self.sender() == self.x_raz_2:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа слева:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.x_raz_2.setText(name)
        elif self.sender() == self.y_raz_2:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа сверху:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.y_raz_2.setText(name)
        elif self.sender() == self.createImage_button:
            try:
                excep, settings = False, {}
                if self.lineOfSource.text() == '':
                    self.lineOfSource.setStyleSheet(exception)
                    excep = True
                else:
                    self.lineOfSource.setStyleSheet(norm)
                if self.lineOfX_2.text() == '':
                    self.lineOfX_2.setStyleSheet(exception)
                    excep = True
                else:
                    self.lineOfX_2.setStyleSheet(norm)
                if self.lineOfY_2.text() == '':
                    self.lineOfY_2.setStyleSheet(exception)
                    excep = True
                else:
                    self.lineOfY_2.setStyleSheet(norm)
                if self.lineOfWidth_2.text() == '':
                    self.lineOfWidth_2.setStyleSheet(exception)
                    excep = True
                else:
                    settings['width'] = (int(self.lineOfWidth_2.text()), self.width_raz_2.text())
                    self.lineOfWidth_2.setStyleSheet(norm)
                if self.lineOfHeight.text() == '':
                    self.lineOfHeight.setStyleSheet(exception)
                    excep = True
                else:
                    settings['height'] = (int(self.lineOfHeight.text()), self.height_raz.text())
                    self.lineOfHeight.setStyleSheet(norm)
                if excep:
                    raise Exception
                name = self.lineOfSource.text().split('/')[-1]
                shutil.copy(self.lineOfSource.text(), f'static/img/' + name)
                settings['src'] = self.lineOfSource.text()
                settings['y'] = (int(self.lineOfY_2.text()), self.y_raz_2.text())
                settings['x'] = (int(self.lineOfX_2.text()), self.x_raz_2.text())
                self.newAction('Image', settings)
                self.site.image(src=f"{f'static/img/' + name}".replace('/', chr(92)),
                                width=settings['width'],
                                height=settings['height'],
                                y=settings['y'],
                                x=settings['x'],
                                name=self.actions[-1][1])
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            except Exception as e:
                pass

    def rectSettings(self):
        if self.sender() == self.width_button_5:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину прямоугольника:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfWidth_5.setText(str(name))
        elif self.sender() == self.height_button_3:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите высоту прямоугольника:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfHeight_3.setText(str(name))
        elif self.sender() == self.color_button_3:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_3.setText(color.name())
        elif self.sender() == self.border_button:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину окантовки:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfBorder.setText(str(name))
        elif self.sender() == self.color_button_4:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_4.setText(color.name())
        elif self.sender() == self.x_button_5:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ слева:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfX_5.setText(str(name))
        elif self.sender() == self.y_button_5:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ сверху:", 0, 0, 100, 1)
            if ok_pressed:
                self.lineOfY_5.setText(str(name))
        elif self.sender() == self.border_button_5:
            name, ok_pressed = QInputDialog.getItem(self, "Вложенность", "Выберете действие, относительно которого будет реализованна вложенность:",
                                                    set([elem[1].text() for elem in self.actions]), 1, False)
            if ok_pressed:
                self.lineOfBorder_5.setText(name)
        elif self.sender() == self.createRect_button:
            excep, settings = False, {}
            if self.lineOfWidth_5.text() == '':
                self.lineOfWidth_5.setStyleSheet(exception)
                excep = True
            else:
                self.lineOfWidth_5.setStyleSheet(norm)
                settings['width'] = (int(self.lineOfWidth_5.text()), self.width_raz_5.text())
            if self.lineOfHeight_3.text() == '':
                self.lineOfHeight_3.setStyleSheet(exception)
                excep = True
            else:
                self.lineOfHeight_3.setStyleSheet(norm)
                settings['height'] = (int(self.lineOfHeight_3.text()), self.height_raz_3.text())
            if self.lineOfY_5.text() == '':
                self.lineOfY_5.setStyleSheet(exception)
                excep = True
            else:
                self.lineOfY_5.setStyleSheet(norm)
                settings['y'] = (int(self.lineOfY_5.text()), self.y_raz_5.text())
            if self.lineOfX_5.text() == '':
                self.lineOfX_5.setStyleSheet(exception)
                excep = True
            else:
                self.lineOfX_5.setStyleSheet(norm)
                settings['x'] = (int(self.lineOfX_5.text()), self.x_raz_5.text())
            if self.plus_color_rect.isChecked():
                if self.lineOfColor_3.text() == '':
                    self.lineOfColor_3.setStyleSheet(exception)
                    excep = True
                else:
                    settings['color'] = self.lineOfColor_3.text()
                    self.lineOfColor_3.setStyleSheet(norm)
            else:
                settings['color'] = ''
            if self.plus_border_rect.isChecked():
                if self.lineOfBorder.text() == '':
                    self.lineOfBorder.setStyleSheet(exception)
                    excep = True
                else:
                    settings['border'] = (int(self.lineOfBorder.text()), self.border_raz.text())
                    self.lineOfBorder.setStyleSheet(norm)
            else:
                settings['border'] = ('', '')
            if self.plus_colorofborder_rect.isChecked():
                if self.lineOfColor_4.text() == '':
                    self.lineOfColor_4.setStyleSheet(exception)
                    excep = True
                else:
                    settings['border_color'] = self.lineOfColor_4.text()
                    self.lineOfColor_4.setStyleSheet(norm)
            else:
                settings['border_color'] = ''
            if self.plus_vlozh.isChecked():
                if self.lineOfBorder_5.text() == '':
                    self.lineOfBorder_5.setStyleSheet(exception)
                    excep = True
                else:
                    for i in range(len(self.actions)):
                        if self.actions[i][1].text() == self.lineOfBorder_5.text():
                            settings['relativity'] = i
                            self.lineOfBorder_5.setStyleSheet(norm)
                            break
                        elif i == len(self.actions):
                            self.lineOfBorder_5.setStyleSheet(exception)
                            excep = True
            else:
                settings['relativity'] = -1
            if excep:
                return None
            try:
                self.newAction('Rect', settings)
                self.site.square(color=settings['color'],
                                 width=settings['width'],
                                 height=settings['height'],
                                 border=settings['border'],
                                 border_color=settings['border_color'],
                                 y=settings['y'],
                                 x=settings['x'],
                                 rel_index=settings['relativity'],
                                 name=self.actions[-1][1].text())
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            except Exception as e:
                logging.warning(e)
        elif self.sender() == self.width_raz_5:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.width_raz_5.setText(name)
        elif self.sender() == self.height_raz_3:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vh", "vw"), 1, False)
            if ok_pressed:
                self.height_raz_3.setText(name)
        elif self.sender() == self.border_raz:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vh", "vw"), 1, False)
            if ok_pressed:
                self.border_raz.setText(name)
        elif self.sender() == self.x_raz_5:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа слева:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.x_raz_5.setText(name)
        elif self.sender() == self.y_raz_5:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа сверху:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.y_raz_5.setText(name)

    def ovalSettings(self):
        if self.sender() == self.width_button_13:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину овала:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfWidth_13.setText(str(name))
        elif self.sender() == self.height_button_9:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите высоту овала:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfHeight_9.setText(str(name))
        elif self.sender() == self.color_button_13:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_13.setText(color.name())
        elif self.sender() == self.border_button_7:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину окантовки:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfBorder_7.setText(str(name))
        elif self.sender() == self.color_button_21:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_21.setText(color.name())
        elif self.sender() == self.x_button_19:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ слева:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfX_19.setText(str(name))
        elif self.sender() == self.y_button_19:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ сверху:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfY_19.setText(str(name))
        elif self.sender() == self.width_raz_13:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.width_raz_13.setText(name)
        elif self.sender() == self.height_raz_9:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vh", "vw"), 1, False)
            if ok_pressed:
                self.height_raz_9.setText(name)
        elif self.sender() == self.border_raz_7:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vh", "vw"), 1, False)
            if ok_pressed:
                self.border_raz_7.setText(name)
        elif self.sender() == self.x_raz_19:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа слева:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.x_raz_19.setText(name)
        elif self.sender() == self.y_raz_19:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа сверху:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.y_raz_19.setText(name)
        elif self.sender() == self.createOval_button:
            excep, settings = False, {}
            try:
                if self.lineOfWidth_13.text() == '':
                    self.lineOfWidth_13.setStyleSheet(exception)
                    excep = True
                else:
                    self.lineOfWidth_13.setStyleSheet(norm)
                    settings['width'] = (int(self.lineOfWidth_13.text()), self.width_raz_13.text())
                if self.lineOfHeight_9.text() == '':
                    self.lineOfHeight_9.setStyleSheet(exception)
                    excep = True
                else:
                    self.lineOfHeight_9.setStyleSheet(norm)
                    settings['height'] = (int(self.lineOfHeight_9.text()), self.height_raz_9.text())
                if self.lineOfX_19.text() == '':
                    self.lineOfX_19.setStyleSheet(exception)
                    excep = True
                else:
                    self.lineOfX_19.setStyleSheet(norm)
                    settings['x'] = (int(self.lineOfX_19.text()), self.x_raz_19.text())
                if self.lineOfY_19.text() == '':
                    self.lineOfY_19.setStyleSheet(exception)
                    excep = True
                else:
                    self.lineOfY_19.setStyleSheet(norm)
                    settings['y'] = (int(self.lineOfY_19.text()), self.y_raz_19.text())
                if self.plus_color_oval.isChecked():
                    if self.lineOfColor_13.text() == '':
                        self.lineOfColor_13.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['color'] = self.lineOfColor_13.text()
                        self.lineOfColor_13.setStyleSheet(norm)
                else:
                    settings['color'] = ''
                if self.plus_border_oval.isChecked():
                    if self.lineOfBorder_7.text() == '':
                        self.lineOfBorder_7.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['border'] = (int(self.lineOfBorder_7.text()), self.border_raz_7.text())
                        self.lineOfBorder_7.setStyleSheet(norm)
                else:
                    settings['border'] = ('', '')
                if self.plus_colorofborder_oval.isChecked():
                    if self.lineOfColor_21.text() == '':
                        self.lineOfColor_21.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['border_color'] = self.lineOfColor_21.text()
                        self.lineOfColor_21.setStyleSheet(norm)
                else:
                    settings['border_color'] = ''
                if excep:
                    logging.warning(1)
                self.newAction('Oval', settings)
                self.site.oval(color=settings['color'],
                               width=settings['width'],
                               height=settings['height'],
                               border=settings['border'],
                               border_color=settings['border_color'],
                               y=settings['y'],
                               x=settings['x'],
                               name=self.actions[-1][1].text())
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            except Exception as e:
                logging.warning(e)

    def peroSettings(self):
        if self.sender() == self.width_button_14:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину линий:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfWidth_14.setText(str(name))
        elif self.sender() == self.color_button_14:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_14.setText(color.name())
        elif self.sender() == self.width_raz_14:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа слева:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.width_raz_14.setText(name)
        elif self.sender() == self.newPero:
            for i in range(len(self.points)):
                self.verticalLayout_26.removeWidget(self.points[i][0])
            self.points.clear()
            self.newPero.hide()

    # Функция для отмены последнего действия при нажатии сочетания клавиш CTRL + Z, обработки нажатия на Enter и Esc
    def keyPressEvent(self, event):
        if event.key() == (Qt.Key_Control and Qt.Key_Z):
            try:
                self.site.undo(-1)
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
                if self.actions[-1] == self.pero_index:
                    for i in range(0, len(self.points)):
                        self.verticalLayout_26.removeWidget(self.points[i][0])
                    self.points.clear()
                    self.newPero.hide()
                    self.pero_index = None
                self.delActions(-1)
            except IndexError as e:
                pass
        elif event.key() == Qt.Key_Escape:
            self.TwoMainWindow.setCurrentWidget(self.Intro)

    # Функция для скрытие/открытия листа с действиями
    def hideListOfAction(self):
        self.count = 0
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"Picture/Actions.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ActionsButton.setIcon(icon)
        self.listOfActions.setHidden(not(self.ActionsButton.isChecked()))
        try:
            if self.listOfFunction.currentWidget() in \
               [self.page_edit, self.page_edit_2, self.page_edit_3, self.page_edit_4] and \
               not (self.ActionsButton.isChecked()):
                self.listOfFunction.hide()
        except Exception as e:
            logging.warning(e)

    def newAction(self, mode, settings):
        self.actions.append([None, None, None, None, None, settings, mode])

        # Настройка Layot с содержим действия
        self.actions[-1][0] = QtWidgets.QFrame(self.listOfActions)
        self.actions[-1][0].setMinimumSize(QtCore.QSize(120, 72))
        self.actions[-1][0].setMaximumSize(QtCore.QSize(120, 72))
        self.actions[-1][0].setStyleSheet(frame)
        self.actions[-1][0].setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.actions[-1][0].setFrameShadow(QtWidgets.QFrame.Raised)

        self.actions[-1][4] = QtWidgets.QGridLayout(self.actions[-1][0])

        # Настройка кнопки с названием действия
        self.actions[-1][1] = QtWidgets.QPushButton(self.actions[-1][0])
        if 'name' in settings:
            self.actions[-1][1].setText(settings['name'])
        else:
            self.actions[-1][1].setText(f'Действие {len(self.actions)}')
        self.actions[-1][1].setEnabled(False)
        self.actions[-1][1].setMinimumSize(QtCore.QSize(64, 28))
        self.actions[-1][1].setMaximumSize(QtCore.QSize(64, 28))
        self.actions[-1][1].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.actions[-1][1].setStyleSheet("QPushButton {\n"
                                               "    color: rgb(0, 0, 0);\n"
                                               "    background-color: rgb(255, 255, 255);\n"
                                               "}")
        self.actions[-1][1].setFlat(False)
        self.actions[-1][4].addWidget(self.actions[-1][1], 2, 1, 1, 1)

        # Настройка кнопки с приоритетом действия
        self.actions[-1][2] = QtWidgets.QPushButton(self.actions[-1][0])
        self.actions[-1][2].setText(f'{len(self.actions)}')
        self.actions[-1][2].setMinimumSize(QtCore.QSize(28, 28))
        self.actions[-1][2].setMaximumSize(QtCore.QSize(28, 28))
        self.actions[-1][2].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.actions[-1][2].setStyleSheet("QPushButton {\n"
                                                "    background-color: rgb(0, 0, 0);\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    font: 63 8pt \"Yu Gothic UI Semibold\";\n"
                                                "    border-radius: 12px\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: rgb(76, 76, 76);\n"
                                                "    border-radius: 12px\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: rgb(116, 116, 116);\n"
                                                "    border-radius: 12px\n"
                                                "}")
        self.actions[-1][2].setFlat(False)
        self.actions[-1][2].clicked.connect(self.changePrior)
        self.actions[-1][4].addWidget(self.actions[-1][2], 2, 0, 1, 1)

        # Настройка кнопки редактирования действия
        self.actions[-1][3] = QtWidgets.QPushButton(self.actions[-1][0])
        self.actions[-1][3].setText("Редактировать")
        self.actions[-1][3].setMinimumSize(QtCore.QSize(100, 28))
        self.actions[-1][3].setMaximumSize(QtCore.QSize(100, 28))
        self.actions[-1][3].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.actions[-1][3].setStyleSheet("QPushButton {\n"
                                                "    background-color: rgb(0, 0, 0);\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    font: 63 8pt \"Yu Gothic UI Semibold\";\n"
                                                "    border-radius: 12px\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: rgb(76, 76, 76);\n"
                                                "    border-radius: 12px\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: rgb(116, 116, 116);\n"
                                                "    border-radius: 12px\n"
                                                "}")
        self.actions[-1][4].addWidget(self.actions[-1][3], 1, 0, 1, 2)
        self.actions[-1][3].clicked.connect(self.player.play)
        self.actions[-1][3].clicked.connect(self.appearListOfFunction)
        if mode == 'Text':
            self.actions[-1][3].clicked.connect(self.textEdit)
        elif mode == 'Image':
            self.actions[-1][3].clicked.connect(self.imageEdit)
        elif mode == 'Rect':
            self.actions[-1][3].clicked.connect(self.rectEdit)
        elif mode == 'Oval':
            self.actions[-1][3].clicked.connect(self.ovalEdit)
        elif mode == 'Pero':
            self.actions[-1][3].clicked.connect(self.peroEdit)

        # Добавление действия на панель действий
        self.verticalLayout_10.addWidget(self.actions[-1][0])

        if self.listOfActions.isHidden():
            self.count += 1
            if self.count < 9:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(f"Picture/Actions{self.count}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ActionsButton.setIcon(icon)
            else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(f"Picture/Actions9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ActionsButton.setIcon(icon)

    # Функция действия по его индексу
    def delActions(self, index):
        self.verticalLayout_10.removeWidget(self.actions[index][0])
        del self.actions[index]
        if self.listOfActions.isHidden():
            if self.count != 0:
                self.count -= 1
            if self.count == 0:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(f"Picture/Actions.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ActionsButton.setIcon(icon)
            elif self.count < 9:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(f"Picture/Actions{self.count}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ActionsButton.setIcon(icon)
            else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(f"Picture/Actions9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ActionsButton.setIcon(icon)
        for i in range(index, len(self.actions)):
            self.actions[i][2].setText(str(i + 1))

    def textEdit(self):
        self.listOfFunction.setCurrentWidget(self.page_edit_2)
        for elem in [self.title_btn, self.text_btn, self.image_btn, self.figure_btn, self.cyrcle_btn, self.pero_btn]:
            elem.setChecked(False)
        self.pushButton_2.setCursor(Qt.ArrowCursor)
        for i in range(len(self.actions)):
            if self.sender() in self.actions[i]:
                self.index = i
                break
        try:
            self.lineOfName_2.setText(self.actions[self.index][1].text())
            self.lineOfSoderzhanie_2.setText(self.actions[self.index][5]['text'])
            self.lineOfSize_2.setText(self.actions[self.index][5]['font_size'][0])
            if self.actions[self.index][5]['font'] == '':
                self.frame_16.hide()
                self.plus_shrift_text_2.setText("+Шрифт")
                self.plus_shrift_text_2.setStyleSheet(button)
                self.plus_shrift_text_2.setChecked(False)
            else:
                self.frame_16.show()
                self.lineOfShrift_2.setText(str(self.actions[self.index][5]['font']))
                self.plus_shrift_text_2.setText("-Шрифт")
                self.plus_shrift_text_2.setStyleSheet(hat)
                self.plus_shrift_text_2.setChecked(True)
            if self.actions[self.index][5]['color'] == ''\
                    or self.actions[self.index][5]['color'] == 'black':
                self.frame_17.hide()
                self.plus_color_text_3.setText("+Цвет")
                self.plus_color_text_3.setStyleSheet(button)
                self.plus_color_text_3.setChecked(False)
            else:
                self.frame_17.show()
                self.lineOfColor_2.setText(str(self.actions[self.index][5]['color']))
                self.plus_color_text_3.setText("-Цвет")
                self.plus_color_text_3.setStyleSheet(hat)
                self.plus_color_text_3.setChecked(True)
            if self.actions[self.index][5]['width'][0] == ''\
                    or self.actions[self.index][5]['width'][0] == '0':
                self.frame_18.hide()
                self.plus_width_text_2.setText("+Ширина")
                self.plus_width_text_2.setStyleSheet(button)
                self.plus_width_text_2.setChecked(False)
            else:
                self.frame_18.show()
                self.lineOfWidth_3.setText(self.actions[self.index][5]['width'][0])
                self.plus_width_text_2.setText("-Ширина")
                self.plus_width_text_2.setStyleSheet(hat)
                self.plus_width_text_2.setChecked(True)
            self.lineOfX_3.setText(self.actions[self.index][5]['x'][0])
            self.lineOfY_3.setText(self.actions[self.index][5]['y'][0])

            self.width_raz_3.setText(self.actions[self.index][5]['width'][1])
            self.size_raz_2.setText(self.actions[self.index][5]['font_size'][1])
            self.x_raz_3.setText(self.actions[self.index][5]['x'][1])
            self.y_raz_3.setText(self.actions[self.index][5]['y'][1])
        except Exception as e:
            logging.warning(e)

    def imageEdit(self):
        try:
            self.listOfFunction.setCurrentWidget(self.page_edit_3)
            for elem in \
                    [self.title_btn, self.text_btn, self.image_btn, self.figure_btn, self.cyrcle_btn, self.pero_btn]:
                elem.setChecked(False)
            self.pushButton_2.setCursor(Qt.ArrowCursor)
            for i in range(len(self.actions)):
                if self.sender() in self.actions[i]:
                    self.index = i
                    break
            self.lineOfName_3.setText(self.actions[self.index][1].text())
            self.lineOfSource_2.setText(self.actions[self.index][5]['src'])
            self.lineOfWidth_4.setText(str(self.actions[self.index][5]['width'][0]))
            self.lineOfHeight_2.setText(str(self.actions[self.index][5]['height'][0]))
            self.lineOfX_4.setText(str(self.actions[self.index][5]['x'][0]))
            self.lineOfY_4.setText(str(self.actions[self.index][5]['y'][0]))

            self.width_raz_4.setText(self.actions[self.index][5]['width'][1])
            self.height_raz_2.setText(self.actions[self.index][5]['height'][1])
            self.x_raz_4.setText(self.actions[self.index][5]['x'][1])
            self.y_raz_4.setText(self.actions[self.index][5]['y'][1])
        except Exception as e:
            logging.warning(e)

    def rectEdit(self):
        try:
            self.listOfFunction.setCurrentWidget(self.page_edit_4)
            for elem in \
                    [self.title_btn, self.text_btn, self.image_btn, self.figure_btn, self.cyrcle_btn, self.pero_btn]:
                elem.setChecked(False)
            self.pushButton_2.setCursor(Qt.ArrowCursor)
            for i in range(len(self.actions)):
                if self.sender() in self.actions[i]:
                    self.index = i
                    break
            self.lineOfName_4.setText(self.actions[self.index][1].text())
            self.lineOfWidth_7.setText(str(self.actions[self.index][5]['width'][0]))
            self.lineOfHeight_5.setText(str(self.actions[self.index][5]['height'][0]))
            if self.actions[self.index][5]['color'] == ''\
                    or self.actions[self.index][5]['color'] == 'black':
                self.frame_39.hide()
                self.plus_color_rect_2.setText("+Цвет")
                self.plus_color_rect_2.setStyleSheet(button)
                self.plus_color_rect_2.setChecked(False)
            else:
                self.frame_39.show()
                self.lineOfColor_8.setText(self.actions[self.index][5]['color'])
                self.plus_color_rect_2.setText("-Цвет")
                self.plus_color_rect_2.setStyleSheet(hat)
                self.plus_color_rect_2.setChecked(True)
            if self.actions[self.index][5]['border'][0] == ''\
                    or self.actions[self.index][5]['border'][0] == '0':
                self.frame_38.hide()
                self.plus_border_rect_2.setText("+Окантовка")
                self.plus_border_rect_2.setStyleSheet(button)
                self.plus_border_rect_2.setChecked(False)
            else:
                self.frame_38.show()
                self.lineOfBorder_3.setText(str(self.actions[self.index][5]['border'][0]))
                self.plus_border_rect_2.setText("-Окантовка")
                self.plus_border_rect_2.setStyleSheet(hat)
                self.plus_border_rect_2.setChecked(True)
                self.border_raz_3.setText(self.actions[self.index][5]['border'][1])
            if self.actions[self.index][5]['border_color'] == ''\
                    or self.actions[self.index][5]['border_color'] == 'black':
                self.frame_37.hide()
                self.plus_colorofborder_rect_2.setText("+Цвет окантовки")
                self.plus_colorofborder_rect_2.setStyleSheet(button)
                self.plus_colorofborder_rect_2.setChecked(False)
            else:
                self.frame_37.show()
                self.lineOfColor_7.setText(self.actions[self.index][5]['border_color'])
                self.plus_colorofborder_rect_2.setText("-Цвет окантовки")
                self.plus_colorofborder_rect_2.setStyleSheet(hat)
                self.plus_colorofborder_rect_2.setChecked(True)
            if self.actions[self.index][5]['relativity'] == -1:
                self.frame_42.hide()
                self.plus_vlozh_2.setText("+Вложенность")
                self.plus_vlozh_2.setChecked(False)
            else:
                self.frame_42.show()
                self.lineOfBorder_4.setText(self.actions[self.actions[self.index][5]['relativity']][1].text())
                self.plus_vlozh_2.setText("-Вложенность")
                self.plus_vlozh_2.setChecked(True)
            self.lineOfX_7.setText(str(self.actions[self.index][5]['x'][0]))
            self.lineOfY_7.setText(str(self.actions[self.index][5]['y'][0]))

            self.width_raz_7.setText(self.actions[self.index][5]['width'][1])
            self.height_raz_5.setText(self.actions[self.index][5]['height'][1])
            self.x_raz_7.setText(self.actions[self.index][5]['x'][1])
            self.y_raz_7.setText(self.actions[self.index][5]['y'][1])
        except Exception as e:
            logging.warning(e)

    def ovalEdit(self):
        self.listOfFunction.setCurrentWidget(self.page_edit_5)
        for elem in [self.title_btn, self.text_btn, self.image_btn, self.figure_btn, self.cyrcle_btn, self.pero_btn]:
            elem.setChecked(False)
        self.pushButton_2.setCursor(Qt.ArrowCursor)
        for i in range(len(self.actions)):
            if self.sender() in self.actions[i]:
                self.index = i
                break
        self.lineOfName_13.setText(self.actions[self.index][1].text())
        self.lineOfWidth_21.setText(str(self.actions[self.index][5]['width'][0]))
        self.lineOfHeight_15.setText(str(self.actions[self.index][5]['height'][0]))
        if self.actions[self.index][5]['color'] == ''\
                or self.actions[self.index][5]['color'] == 'black':
            self.frame_135.hide()
            self.plus_color_oval_2.setText("+Цвет")
            self.plus_color_oval_2.setStyleSheet(button)
            self.plus_color_oval_2.setChecked(False)
        else:
            self.frame_135.show()
            self.lineOfColor_23.setText(self.actions[self.index][5]['color'])
            self.plus_color_oval_2.setText("-Цвет")
            self.plus_color_oval_2.setStyleSheet(hat)
            self.plus_color_oval_2.setChecked(True)
        if self.actions[self.index][5]['border'][0] == ''\
                or self.actions[self.index][5]['border'][0] == '0':
            self.frame_136.hide()
            self.plus_border_color_2.setText("+Окантовка")
            self.plus_border_color_2.setStyleSheet(button)
            self.plus_border_color_2.setChecked(False)
        else:
            self.frame_136.show()
            self.lineOfBorder_8.setText(str(self.actions[self.index][5]['border'][0]))
            self.plus_border_color_2.setText("-Окантовка")
            self.plus_border_color_2.setStyleSheet(hat)
            self.plus_border_color_2.setChecked(True)
            self.border_raz_8.setText(self.actions[self.index][5]['border'][1])
        if self.actions[self.index][5]['border_color'] == ''\
                or self.actions[self.index][5]['border_color'] == 'black':
            self.frame_134.hide()
            self.plus_colorofborder_oval_2.setText("+Цвет окантовки")
            self.plus_colorofborder_oval_2.setStyleSheet(button)
            self.plus_colorofborder_oval_2.setChecked(False)
        else:
            self.frame_134.show()
            self.lineOfColor_22.setText(self.actions[self.index][5]['border_color'])
            self.plus_colorofborder_oval_2.setText("-Цвет окантовки")
            self.plus_colorofborder_oval_2.setStyleSheet(hat)
            self.plus_colorofborder_oval_2.setChecked(True)
        self.lineOfX_20.setText(str(self.actions[self.index][5]['x'][0]))
        self.lineOfY_20.setText(str(self.actions[self.index][5]['y'][0]))

        self.width_raz_21.setText(self.actions[self.index][5]['width'][1])
        self.height_raz_15.setText(self.actions[self.index][5]['height'][1])
        self.x_raz_20.setText(self.actions[self.index][5]['x'][1])
        self.y_raz_20.setText(self.actions[self.index][5]['y'][1])

    def peroEdit(self):
        try:
            self.listOfFunction.setCurrentWidget(self.page_edit_6)
            for elem in [self.title_btn, self.text_btn, self.image_btn, self.figure_btn, self.cyrcle_btn, self.pero_btn]:
                elem.setChecked(False)
            for i in range(len(self.actions)):
                if self.sender() in self.actions[i]:
                    self.index = i
                    break
            self.lineOfName_15.setText(self.actions[self.index][1].text())
            self.lineOfWidth_15.setText(str(self.actions[self.index][5]['width'][0]))
            self.width_raz_15.setText(self.actions[self.index][5]['width'][1])
            if self.actions[self.index][5]['color'] == '':
                self.frame_88.hide()
                self.plus_color_pero_2.setText("+Цвет")
                self.plus_color_pero_2.setStyleSheet(button)
                self.plus_color_pero_2.setChecked(False)
            else:
                self.frame_88.show()
                self.lineOfColor_15.setText(self.actions[self.index][5]['color'])
                self.plus_color_pero_2.setText("-Цвет")
                self.plus_color_pero_2.setStyleSheet(hat)
                self.plus_color_pero_2.setChecked(True)
            for i in reversed(range(self.verticalLayout_32.count())):
                self.verticalLayout_32.itemAt(i).widget().setParent(None)
            for point in self.actions[self.index][5]['points']:
                self.newPoint(point[0], point[2], mode='edit')
        except Exception:
            pass

    def textChange(self):
        if self.sender() == self.soderzhanie_button_2:
            name, ok_pressed = QInputDialog.getText(self, "Текст", "Введите текст:")
            if ok_pressed:
                self.lineOfSoderzhanie_2.setText(name)
        elif self.sender() == self.shrift_button_2:
            name, ok_pressed = QInputDialog.getItem(self, "Шрифт", "Выберете шрифт:",
                                                    ("Arial", "Times New Roman"), 1, False)
            if ok_pressed:
                self.lineOfShrift_2.setText(name)
        elif self.sender() == self.color_button_2:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_2.setText(color.name())
        elif self.sender() == self.width_button_3:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите максимальную ширину текста:", 5, 1, 100, 1)
            if ok_pressed:
                self.lineOfWidth_3.setText(str(name))
        elif self.sender() == self.size_button_2:
            name, ok_pressed = QInputDialog.getInt(self, "Размер", "Введите размер шрифта:", 5, 1, 1000, 1)
            if ok_pressed:
                self.lineOfSize_2.setText(str(name))
        elif self.sender() == self.shrift_button_2:
            name, ok_pressed = QInputDialog.getItem(self, "Шрифт", "Выберете шрифт:",
                                                    ("Arial", "Times New Roman"), 1, False)
            if ok_pressed:
                self.lineOfShrift_2.setText(name)
        elif self.sender() == self.width_raz_3:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vw"), 1, False)
            if ok_pressed:
                self.width_raz_3.setText(name)
        elif self.sender() == self.size_raz_2:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("pt", "px", "%", "vh", "vw"), 1, False)
            if ok_pressed:
                self.size_raz_2.setText(name)
        elif self.sender() == self.x_button_3:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ слева:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfX_3.setText(str(name))
        elif self.sender() == self.y_button_3:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ сверху:", 0, 0, 100, 1)
            if ok_pressed:
                self.lineOfY_3.setText(str(name))
        elif self.sender() == self.x_raz_3:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа слева:",
                                                    ("px", "%"), 1, False)
            if ok_pressed:
                self.x_raz_3.setText(name)
        elif self.sender() == self.y_raz_3:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа сверху:",
                                                    ("px", "%"), 1, False)
            if ok_pressed:
                self.y_raz_3.setText(name)
        elif self.sender() == self.editBut_2:
            try:
                settings = {'text': self.lineOfSoderzhanie_2.text(),
                            'font_size': (self.lineOfSize_2.text(), self.size_raz_2.text()),
                            'y': (self.lineOfY_3.text(), self.y_raz_3.text()),
                            'x': (self.lineOfX_3.text(), self.x_raz_3.text()),
                            'name': self.lineOfName_2.text()
                            }
                excep = False
                if self.plus_shrift_text_2.isChecked():
                    if self.lineOfShrift_2.text() == '':
                        self.lineOfShrift_2.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['font'] = self.lineOfShrift_2.text()
                        self.lineOfShrift_2.setStyleSheet(norm)
                else:
                    settings['font'] = ''
                if self.plus_color_text_3.isChecked():
                    if self.lineOfColor_2.text() == '':
                        self.lineOfColor_2.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['color'] = self.lineOfColor_2.text()
                        self.lineOfColor_2.setStyleSheet(norm)
                else:
                    settings['color'] = ''
                if self.plus_width_text_2.isChecked():
                    if self.lineOfWidth_3.text() == '':
                        self.lineOfWidth_3.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['width'] = (self.lineOfWidth_3.text(), self.width_raz_3.text())
                        self.lineOfWidth_3.setStyleSheet(norm)
                else:
                    settings['width'] = ('', '')
                if excep:
                    raise Exception
                self.site.undo(self.index)
                self.actions[self.index][4] = settings
                self.actions[self.index][1].setText(self.lineOfName_2.text())
                self.site.paragraph(text=settings['text'],
                                    width=settings['width'],
                                    font_size=settings['font_size'],
                                    color=settings['color'],
                                    font=settings['font'],
                                    y=settings['y'],
                                    x=settings['x'], num=self.index, name=self.actions[self.index][1].text())
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            except Exception as e:
                logging.warning(e)
        elif self.sender() == self.deleteBut_2:
            self.site.undo(self.index)
            self.site.save(r'templates/base.html')
            self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            self.delActions(self.index)

    def imageChange(self):
        try:
            if self.sender() == self.source_button_2:
                h = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
                if h:
                    self.lineOfSource_2.setText(h)
            elif self.sender() == self.width_button_4:
                name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину картинки:", 0, 0, 1200, 1)
                if ok_pressed:
                    self.lineOfWidth_4.setText(str(name))
            elif self.sender() == self.height_button_2:
                name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите высоту картинки:", 0, 0, 1200, 1)
                if ok_pressed:
                    self.lineOfHeight_2.setText(str(name))
            elif self.sender() == self.width_raz_4:
                name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для ширины картинки:",
                                                        ("px", "%", "vw"), 1, False)
                if ok_pressed:
                    self.width_raz_4.setText(name)
            elif self.sender() == self.height_raz_2:
                name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для длины картинки:",
                                                        ("px", "%", "vh"), 1, False)
                if ok_pressed:
                    self.height_raz_2.setText(name)
            elif self.sender() == self.x_button_4:
                name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ слева:", 0, 0, 1200, 1)
                if ok_pressed:
                    self.lineOfX_4.setText(str(name))
            elif self.sender() == self.y_button_4:
                name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ сверху:", 0, 0, 100, 1)
                if ok_pressed:
                    self.lineOfY_4.setText(str(name))
            elif self.sender() == self.x_raz_4:
                name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа слева:",
                                                        ("px", "%"), 1, False)
                if ok_pressed:
                    self.x_raz_4.setText(name)
            elif self.sender() == self.y_raz_4:
                name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа сверху:",
                                                        ("px", "%"), 1, False)
                if ok_pressed:
                    self.y_raz_4.setText(name)
            elif self.sender() == self.editBut_3:
                settings = {'src': self.lineOfSource_2.text(),
                            'y': (int(self.lineOfY_4.text()), self.y_raz_4.text()),
                            'x': (int(self.lineOfX_4.text()), self.x_raz_4.text()),
                            'name': self.lineOfName_3.text()
                            }
                excep = False
                if self.lineOfWidth_4.text() == '':
                    self.lineOfWidth_4.setStyleSheet(exception)
                    excep = True
                else:
                    settings['width'] = (int(self.lineOfWidth_4.text()), self.width_raz_4.text())
                    self.lineOfWidth_4.setStyleSheet(norm)
                if self.lineOfHeight_2.text() == '':
                    self.lineOfHeight_2.setStyleSheet(exception)
                    excep = True
                else:
                    settings['height'] = (int(self.lineOfHeight_2.text()), self.height_raz_2.text())
                    self.lineOfHeight_2.setStyleSheet(norm)
                if excep:
                    raise Exception
                name = self.lineOfSource.text().split('/')[-1]
                shutil.copy(self.lineOfSource_2.text(), f'static/img/' + name)
                self.site.undo(self.index)
                self.actions[self.index][5] = settings
                self.actions[self.index][1].setText(self.lineOfName_3.text())
                self.site.image(src=f"{f'static/img/' + name}".replace('/', chr(92)),
                                width=settings['width'],
                                height=settings['height'],
                                y=settings['y'],
                                x=settings['x'], num=self.index, name=self.actions[self.index][1].text())
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            elif self.sender() == self.deleteBut_3:
                self.site.undo(self.index)
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
                self.delActions(self.index)
        except Exception as e:
            pass

    def rectChange(self):
        if self.sender() == self.width_button_7:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину прямоугольника:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfWidth_7.setText(str(name))
        elif self.sender() == self.height_button_5:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите высоту прямоугольника:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfHeight_5.setText(str(name))
        elif self.sender() == self.color_button_8:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_8.setText(color.name())
        elif self.sender() == self.border_button_3:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину окантовки:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfBorder_3.setText(str(name))
        elif self.sender() == self.color_button_7:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_7.setText(color.name())
        elif self.sender() == self.x_button_7:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ слева:", 0, 0, 1200, 1)
            if ok_pressed:
                self.lineOfX_7.setText(str(name))
        elif self.sender() == self.y_button_7:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ сверху:", 0, 0, 100, 1)
            if ok_pressed:
                self.lineOfY_7.setText(str(name))
        elif self.sender() == self.border_button_4:
            name, ok_pressed = QInputDialog.getItem(self, "Вложенность", "Выберете действие, относительно которого будет реализованна вложенность:",
                                                    set([elem[1].text() for elem in self.actions]), 1, False)
            if ok_pressed:
                self.lineOfBorder_4.setText(name)
        elif self.sender() == self.editBut_4:
            try:
                settings = {'width': (int(self.lineOfWidth_7.text()), self.width_raz_7.text()),
                            'height': (int(self.lineOfHeight_5.text()), self.height_raz_5.text()),
                            'y': (int(self.lineOfY_7.text()), self.y_raz_7.text()),
                            'x': (int(self.lineOfX_7.text()), self.x_raz_7.text()),
                            'name': self.lineOfName_4.text()
                            }
                excep = False
                if self.plus_color_rect_2.isChecked():
                    if self.lineOfColor_8.text() == '':
                        self.lineOfColor_8.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['color'] = self.lineOfColor_8.text()
                        self.lineOfColor_8.setStyleSheet(norm)
                else:
                    settings['color'] = ''
                if self.plus_border_rect_2.isChecked():
                    if self.lineOfBorder_3.text() == '':
                        self.lineOfBorder_3.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['border'] = (int(self.lineOfBorder_3.text()), self.border_raz_3.text())
                        self.lineOfBorder_3.setStyleSheet(norm)
                else:
                    settings['border'] = ('', '')
                if self.plus_colorofborder_rect_2.isChecked():
                    if self.lineOfColor_7.text() == '':
                        self.lineOfColor_7.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['border_color'] = self.lineOfColor_7.text()
                        self.lineOfColor_7.setStyleSheet(norm)
                else:
                    settings['border_color'] = ''
                if self.plus_vlozh_2.isChecked():
                    if self.lineOfBorder_4.text() == '':
                        self.lineOfBorder_4.setStyleSheet(exception)
                        excep = True
                    else:
                        for i in range(len(self.actions)):
                            if self.actions[i][1].text() == self.lineOfBorder_4.text():
                                settings['relativity'] = i
                                self.lineOfBorder_4.setStyleSheet(norm)
                                break
                            elif i == len(self.actions):
                                self.lineOfBorder_4.setStyleSheet(exception)
                                excep = True
                else:
                    settings['relativity'] = -1
                if excep:
                    raise Exception
                self.site.undo(self.index)
                self.actions[self.index][4] = settings
                self.actions[self.index][1].setText(self.lineOfName_4.text())
                self.site.square(color=settings['color'],
                                 width=settings['width'],
                                 height=settings['height'],
                                 border=settings['border'],
                                 border_color=settings['border_color'],
                                 y=settings['y'],
                                 x=settings['x'], num=self.index, name=self.actions[self.index][1].text(),
                                 rel_index=settings['relativity'])
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            except Exception as e:
                logging.warning(e)
        elif self.sender() == self.deleteBut_4:
            self.site.undo(self.index)
            self.site.save(r'templates/base.html')
            self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            self.delActions(self.index)
        elif self.sender() == self.width_raz_7:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vw"), 1, False)
            if ok_pressed:
                self.width_raz_7.setText(name)
        elif self.sender() == self.height_raz_5:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vh"), 1, False)
            if ok_pressed:
                self.height_raz_5.setText(name)
        elif self.sender() == self.border_raz_3:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "vh", "vw"), 1, False)
            if ok_pressed:
                self.border_raz_3.setText(name)
        elif self.sender() == self.x_raz_7:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа слева:",
                                                    ("px", "%"), 1, False)
            if ok_pressed:
                self.x_raz_7.setText(name)
        elif self.sender() == self.y_raz_7:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа сверху:",
                                                    ("px", "%"), 1, False)
            if ok_pressed:
                self.y_raz_7.setText(name)

    def ovalChange(self):
        if self.sender() == self.width_button_21:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину овала:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfWidth_21.setText(str(name))
        elif self.sender() == self.height_button_15:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите высоту овала:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfHeight_15.setText(str(name))
        elif self.sender() == self.color_button_23:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_23.setText(color.name())
        elif self.sender() == self.border_button_8:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину окантовки:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfBorder_8.setText(str(name))
        elif self.sender() == self.color_button_22:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_22.setText(color.name())
        elif self.sender() == self.x_button_20:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ слева:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfX_20.setText(str(name))
        elif self.sender() == self.y_button_20:
            name, ok_pressed = QInputDialog.getInt(self, "Отступ", "Введите отступ сверху:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfY_20.setText(str(name))
        elif self.sender() == self.width_raz_21:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.width_raz_21.setText(name)
        elif self.sender() == self.height_raz_15:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.height_raz_15.setText(name)
        elif self.sender() == self.border_raz_8:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность:",
                                                    ("px", "%", "vh", "vw"), 1, False)
            if ok_pressed:
                self.border_raz_8.setText(name)
        elif self.sender() == self.x_raz_20:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа слева:",
                                                    ("px", "%"), 1, False)
            if ok_pressed:
                self.x_raz_20.setText(name)
        elif self.sender() == self.y_raz_20:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа сверху:",
                                                    ("px", "%"), 1, False)
            if ok_pressed:
                self.y_raz_20.setText(name)
        elif self.sender() == self.editBut_13:
            try:
                settings = {'width': (int(self.lineOfWidth_21.text()), self.width_raz_21.text()),
                            'height': (int(self.lineOfHeight_15.text()), self.height_raz_15.text()),
                            'y': (int(self.lineOfY_20.text()), self.y_raz_20.text()),
                            'x': (int(self.lineOfX_20.text()), self.x_raz_20.text()),
                            'name': self.lineOfName_13.text()
                            }
                excep = False
                if self.plus_color_oval_2.isChecked():
                    if self.lineOfColor_23.text() == '':
                        self.lineOfColor_23.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['color'] = self.lineOfColor_23.text()
                        self.lineOfColor_23.setStyleSheet(norm)
                else:
                    settings['color'] = ''
                if self.plus_border_color_2.isChecked():
                    if self.lineOfBorder_8.text() == '':
                        self.lineOfBorder_8.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['border'] = (int(self.lineOfBorder_8.text()), self.border_raz_8.text())
                        self.lineOfBorder_8.setStyleSheet(norm)
                else:
                    settings['border'] = ('', '')
                if self.plus_colorofborder_oval_2.isChecked():
                    if self.lineOfColor_22.text() == '':
                        self.lineOfColor_22.setStyleSheet(exception)
                        excep = True
                    else:
                        settings['border_color'] = self.lineOfColor_22.text()
                        self.lineOfColor_22.setStyleSheet(norm)
                else:
                    settings['border_color'] = ''
                if excep:
                    raise Exception
                self.site.undo(self.index)
                self.actions[self.index][4] = settings
                self.actions[self.index][1].setText(self.lineOfName_13.text())
                self.site.oval(color=settings['color'],
                               width=settings['width'],
                               height=settings['height'],
                               border=settings['border'],
                               border_color=settings['border_color'],
                               y=settings['y'],
                               x=settings['x'], num=self.index, name=self.actions[self.index][1].text())
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            except Exception as e:
                logging.warning(e)
        elif self.sender() == self.deleteBut_13:
            self.site.undo(self.index)
            self.site.save(r'templates/base.html')
            self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
            self.delActions(self.index)

    def peroChange(self):
        if self.sender() == self.width_button_15:
            name, ok_pressed = QInputDialog.getInt(self, "Ширина", "Введите ширину линий:", 0, 0, 9999, 1)
            if ok_pressed:
                self.lineOfWidth_15.setText(str(name))
        elif self.sender() == self.color_button_15:
            color = QColorDialog.getColor()
            if color.isValid():
                self.lineOfColor_15.setText(color.name())
        elif self.sender() == self.width_raz_15:
            name, ok_pressed = QInputDialog.getItem(self, "Размерность", "Выберете размерность для отступа слева:",
                                                    ("px", "%", "vw", "vh"), 1, False)
            if ok_pressed:
                self.width_raz_15.setText(name)
        elif self.sender() == self.deleteBut_15:
            try:
                self.site.undo(self.index)
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
                if self.actions[self.index] == self.pero_index:
                    for i in range(len(self.points)):
                        self.verticalLayout_26.removeWidget(self.points[i][0])
                    self.points.clear()
                    self.newPero.hide()
                    self.pero_index = None
                self.delActions(self.index)
            except Exception as e:
                pass

    def changeName(self):
        name, ok_pressed = QInputDialog.getText(self, "Название", "Введите новое название:")
        if ok_pressed:
            if self.sender() == self.icon_button_3:
                self.lineOfName.setText(name)
            elif self.sender() == self.icon_button_4:
                self.lineOfName_2.setText(name)
            elif self.sender() == self.icon_button_5:
                self.lineOfName_3.setText(name)
            elif self.sender() == self.icon_button_6:
                self.lineOfName_4.setText(name)
            elif self.sender() == self.icon_button_19:
                self.lineOfName_13.setText(name)

    def plusArguments(self):
        if self.sender() == self.plus_shrift_text:
            check = self.plus_shrift_text.isChecked()
            self.frame_30.setVisible(check)
            if check:
                self.plus_shrift_text.setText('-Шрифт')
                self.plus_shrift_text.setStyleSheet(hat)
            else:
                self.plus_shrift_text.setText('+Шрифт')
                self.plus_shrift_text.setStyleSheet(button)
                self.lineOfShrift.setStyleSheet(norm)
        elif self.sender() == self.plus_color_text:
            check = self.plus_color_text.isChecked()
            self.frame_31.setVisible(check)
            if check:
                self.plus_color_text.setText('-Цвет')
                self.plus_color_text.setStyleSheet(hat)
            else:
                self.plus_color_text.setText('+Цвет')
                self.plus_color_text.setStyleSheet(button)
                self.lineOfColor.setStyleSheet(norm)
        elif self.sender() == self.plus_width_text:
            check = self.plus_width_text.isChecked()
            self.frame_32.setVisible(check)
            if check:
                self.plus_width_text.setText('-Ширина')
                self.plus_width_text.setStyleSheet(hat)
            else:
                self.plus_width_text.setText('+Ширина')
                self.plus_width_text.setStyleSheet(button)
                self.lineOfWidth.setStyleSheet(norm)
        elif self.sender() == self.plus_color_rect:
            check = self.plus_color_rect.isChecked()
            self.frame_23.setVisible(check)
            if check:
                self.plus_color_rect.setText('-Цвет')
                self.plus_color_rect.setStyleSheet(hat)
            else:
                self.plus_color_rect.setText('+Цвет')
                self.plus_color_rect.setStyleSheet(button)
                self.lineOfColor_3.setStyleSheet(norm)
        elif self.sender() == self.plus_border_rect:
            check = self.plus_border_rect.isChecked()
            self.frame_24.setVisible(check)
            if check:
                self.plus_border_rect.setText('-Окантовка')
                self.plus_border_rect.setStyleSheet(hat)
            else:
                self.plus_border_rect.setText('+Окантовка')
                self.plus_border_rect.setStyleSheet(button)
                self.lineOfBorder.setStyleSheet(norm)
        elif self.sender() == self.plus_colorofborder_rect:
            check = self.plus_colorofborder_rect.isChecked()
            self.frame_25.setVisible(check)
            if check:
                self.plus_colorofborder_rect.setText('-Цвет окантовки')
                self.plus_colorofborder_rect.setStyleSheet(hat)
            else:
                self.plus_colorofborder_rect.setText('+Цвет окантовки')
                self.plus_colorofborder_rect.setStyleSheet(button)
                self.lineOfColor_4.setStyleSheet(norm)
        elif self.sender() == self.plus_vlozh:
            check = self.plus_vlozh.isChecked()
            self.frame_45.setVisible(check)
            if check:
                self.plus_vlozh.setText('-Вложенность')
            else:
                self.plus_vlozh.setText('+Вложенность')
                self.lineOfBorder_5.setStyleSheet(norm)
        elif self.sender() == self.plus_vlozh_2:
            check = self.plus_vlozh_2.isChecked()
            self.frame_42.setVisible(check)
            if check:
                self.plus_vlozh_2.setText('-Вложенность')
            else:
                self.plus_vlozh_2.setText('+Вложенность')
                self.lineOfBorder_4.setStyleSheet(norm)
        elif self.sender() == self.plus_shrift_text_2:
            check = self.plus_shrift_text_2.isChecked()
            self.frame_16.setVisible(check)
            if check:
                self.plus_shrift_text_2.setText('-Шрифт')
                self.plus_shrift_text_2.setStyleSheet(hat)
            else:
                self.plus_shrift_text_2.setText('+Шрифт')
                self.plus_shrift_text_2.setStyleSheet(button)
                self.lineOfShrift_2.setStyleSheet(norm)
        elif self.sender() == self.plus_color_text_3:
            check = self.plus_color_text_3.isChecked()
            self.frame_17.setVisible(check)
            if check:
                self.plus_color_text_3.setText('-Цвет')
                self.plus_color_text_3.setStyleSheet(hat)
            else:
                self.plus_color_text_3.setText('+Цвет')
                self.plus_color_text_3.setStyleSheet(button)
                self.lineOfColor_2.setStyleSheet(norm)
        elif self.sender() == self.plus_width_text_2:
            check = self.plus_width_text_2.isChecked()
            self.frame_18.setVisible(check)
            if check:
                self.plus_width_text_2.setText('-Ширина')
                self.plus_width_text_2.setStyleSheet(hat)
            else:
                self.plus_width_text_2.setText('+Ширина')
                self.plus_width_text_2.setStyleSheet(button)
                self.lineOfWidth_3.setStyleSheet(norm)
        elif self.sender() == self.plus_color_rect_2:
            check = self.plus_color_rect_2.isChecked()
            self.frame_39.setVisible(check)
            if check:
                self.plus_color_rect_2.setText('-Цвет')
                self.plus_color_rect_2.setStyleSheet(hat)
            else:
                self.plus_color_rect_2.setText('+Цвет')
                self.plus_color_rect_2.setStyleSheet(button)
                self.lineOfColor_8.setStyleSheet(norm)
        elif self.sender() == self.plus_border_rect_2:
            check = self.plus_border_rect_2.isChecked()
            self.frame_38.setVisible(check)
            if check:
                self.plus_border_rect_2.setText('-Окантовка')
                self.plus_border_rect_2.setStyleSheet(hat)
            else:
                self.plus_border_rect_2.setText('+Окантовка')
                self.plus_border_rect_2.setStyleSheet(button)
                self.lineOfBorder_3.setStyleSheet(norm)
        elif self.sender() == self.plus_colorofborder_rect_2:
            check = self.plus_colorofborder_rect_2.isChecked()
            self.frame_37.setVisible(check)
            if check:
                self.plus_colorofborder_rect_2.setText('-Цвет окантовки')
                self.plus_colorofborder_rect_2.setStyleSheet(hat)
            else:
                self.plus_colorofborder_rect_2.setText('+Цвет окантовки')
                self.plus_colorofborder_rect_2.setStyleSheet(button)
                self.lineOfColor_7.setStyleSheet(norm)
        elif self.sender() == self.plus_color_oval:
            check = self.plus_color_oval.isChecked()
            self.frame_84.setVisible(check)
            if check:
                self.plus_color_oval.setText('-Цвет')
                self.plus_color_oval.setStyleSheet(hat)
            else:
                self.plus_color_oval.setText('+Цвет')
                self.plus_color_oval.setStyleSheet(button)
                self.lineOfColor_13.setStyleSheet(norm)
        elif self.sender() == self.plus_border_oval:
            check = self.plus_border_oval.isChecked()
            self.frame_128.setVisible(check)
            if check:
                self.plus_border_oval.setText('-Окантовка')
                self.plus_border_oval.setStyleSheet(hat)
            else:
                self.plus_border_oval.setText('+Окантовка')
                self.plus_border_oval.setStyleSheet(button)
                self.lineOfBorder_7.setStyleSheet(norm)
        elif self.sender() == self.plus_colorofborder_oval:
            check = self.plus_colorofborder_oval.isChecked()
            self.frame_129.setVisible(check)
            if check:
                self.plus_colorofborder_oval.setText('-Цвет окантовки')
                self.plus_colorofborder_oval.setStyleSheet(hat)
            else:
                self.plus_colorofborder_oval.setText('+Цвет окантовки')
                self.plus_colorofborder_oval.setStyleSheet(button)
                self.lineOfColor_21.setStyleSheet(norm)
        elif self.sender() == self.plus_color_oval_2:
            check = self.plus_color_oval_2.isChecked()
            self.frame_135.setVisible(check)
            if check:
                self.plus_color_oval_2.setText('-Цвет')
                self.plus_color_oval_2.setStyleSheet(hat)
            else:
                self.plus_color_oval_2.setText('+Цвет')
                self.plus_color_oval_2.setStyleSheet(button)
                self.lineOfColor_23.setStyleSheet(norm)
        elif self.sender() == self.plus_border_color_2:
            check = self.plus_color_oval_2.isChecked()
            self.frame_136.setVisible(check)
            if check:
                self.plus_border_color_2.setText('-Окантовка')
                self.plus_border_color_2.setStyleSheet(hat)
            else:
                self.plus_border_color_2.setText('+Окантовка')
                self.plus_border_color_2.setStyleSheet(button)
                self.lineOfBorder_8.setStyleSheet(norm)
        elif self.sender() == self.plus_colorofborder_oval_2:
            check = self.plus_colorofborder_oval_2.isChecked()
            self.frame_134.setVisible(check)
            if check:
                self.plus_colorofborder_oval_2.setText('-Цвет окантовки')
                self.plus_colorofborder_oval_2.setStyleSheet(hat)
            else:
                self.plus_colorofborder_oval_2.setText('+Цвет окантовки')
                self.plus_colorofborder_oval_2.setStyleSheet(button)
                self.lineOfColor_22.setStyleSheet(norm)
        elif self.sender() == self.plus_color_pero:
            check = self.plus_color_pero.isChecked()
            self.frame_86.setVisible(check)
            if check:
                self.plus_color_pero.setText('-Цвет')
                self.plus_color_pero.setStyleSheet(hat)
            else:
                self.plus_color_pero.setText('+Цвет')
                self.plus_color_pero.setStyleSheet(button)
                self.lineOfColor_14.setStyleSheet(norm)
        elif self.sender() == self.plus_color_pero_2:
            check = self.plus_color_pero_2.isChecked()
            self.frame_88.setVisible(check)
            if check:
                self.plus_color_pero_2.setText('-Цвет')
                self.plus_color_pero_2.setStyleSheet(hat)
            else:
                self.plus_color_pero_2.setText('+Цвет')
                self.plus_color_pero_2.setStyleSheet(button)
                self.lineOfColor_15.setStyleSheet(norm)

    def closeEvent(self, event):
        files = glob.glob('static/img/*')
        for f in files:
            os.remove(f)
        os.remove('templates/base.html')
        sys.exit(0)

    def changePrior(self):
        try:
            for i in range(len(self.actions)):
                if self.sender() in self.actions[i]:
                    self.index = i
                    break
            name, ok_pressed = QInputDialog.getInt(self, "Приоритет", "Введите приоритет действия:", 0, 1, len(self.actions), 1)
            if ok_pressed:
                self.actions[name - 1], self.actions[self.index] = \
                    self.actions[self.index], self.actions[name - 1]
                for i in range(len(self.verticalLayout_10)):
                    self.verticalLayout_10.takeAt(i)
                for i in range(len(self.actions)):
                    self.actions[i][2].setText(str(i + 1))
                    self.verticalLayout_10.addWidget(self.actions[i][0])
                self.site.replace(self.index, name - 1)
                self.site.save(r'templates/base.html')
                self.webEngineView.setUrl(QUrl.fromLocalFile(r'\templates\base.html'))
        except Exception as e:
            logging.warning(e)

    def newPoint(self, x, y, mode='settings'):
        self.points.append([None, None, None, None, None, None, None, None])

        self.points[-1][0] = QtWidgets.QFrame(self.listOfFunction)
        self.points[-1][0].setMinimumSize(QtCore.QSize(120, 72))
        self.points[-1][0].setMaximumSize(QtCore.QSize(120, 72))
        self.points[-1][0].setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 16px\n"
                                     "")
        self.points[-1][0].setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.points[-1][0].setFrameShadow(QtWidgets.QFrame.Raised)

        self.points[-1][1] = QtWidgets.QGridLayout(self.points[-1][0])
        self.points[-1][1].setContentsMargins(4, 5, 5, 5)
        self.points[-1][1].setSpacing(4)

        self.points[-1][2] = QtWidgets.QPushButton(self.points[-1][0])
        self.points[-1][2].setEnabled(False)
        self.points[-1][2].setMinimumSize(QtCore.QSize(28, 28))
        self.points[-1][2].setMaximumSize(QtCore.QSize(28, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.points[-1][2].setFont(font)
        self.points[-1][2].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.points[-1][2].setStyleSheet("QPushButton {\n"
                                      "    color: rgb(0, 0, 0);\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 12px\n"
                                      "}")
        self.points[-1][2].setText(str(x))
        self.points[-1][2].setFlat(False)
        self.points[-1][1].addWidget(self.points[-1][2], 1, 1, 1, 1)

        self.points[-1][3] = QtWidgets.QPushButton(self.points[-1][0])
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points[-1][3].sizePolicy().hasHeightForWidth())
        self.points[-1][3].setSizePolicy(sizePolicy)
        self.points[-1][3].setMinimumSize(QtCore.QSize(56, 28))
        self.points[-1][3].setMaximumSize(QtCore.QSize(56, 28))
        self.points[-1][3].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.points[-1][3].setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(0, 0, 0);\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    font: 63 8pt \"Yu Gothic UI Semibold\";\n"
                                       "    border-radius: 12px\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(76, 76, 76);\n"
                                       "    border-radius: 12px\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(116, 116, 116);\n"
                                       "    border-radius: 12px\n"
                                       "}")
        self.points[-1][3].setText('X')
        self.points[-1][1].addWidget(self.points[-1][3], 0, 0, 1, 1)

        self.points[-1][4] = QtWidgets.QPushButton(self.points[-1][0])
        self.points[-1][4].setEnabled(False)
        self.points[-1][4].setMinimumSize(QtCore.QSize(28, 28))
        self.points[-1][4].setMaximumSize(QtCore.QSize(28, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.points[-1][4].setFont(font)
        self.points[-1][4].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.points[-1][4].setStyleSheet("QPushButton {\n"
                                      "    color: rgb(0, 0, 0);\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 12px\n"
                                      "}")
        self.points[-1][4].setText(str(y))
        self.points[-1][1].addWidget(self.points[-1][4], 1, 3, 1, 1)

        self.points[-1][5] = QtWidgets.QPushButton(self.points[-1][0])
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points[-1][5].sizePolicy().hasHeightForWidth())
        self.points[-1][5].setSizePolicy(sizePolicy)
        self.points[-1][5].setMinimumSize(QtCore.QSize(56, 28))
        self.points[-1][5].setMaximumSize(QtCore.QSize(56, 28))
        self.points[-1][5].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.points[-1][5].setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(0, 0, 0);\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    font: 63 8pt \"Yu Gothic UI Semibold\";\n"
                                       "    border-radius: 12px\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(76, 76, 76);\n"
                                       "    border-radius: 12px\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(116, 116, 116);\n"
                                       "    border-radius: 12px\n"
                                       "}")
        self.points[-1][5].setText('Y')
        self.points[-1][1].addWidget(self.points[-1][5], 0, 2, 1, 1)

        self.points[-1][6] = QtWidgets.QPushButton(self.points[-1][0])
        self.points[-1][6].setMinimumSize(QtCore.QSize(28, 28))
        self.points[-1][6].setMaximumSize(QtCore.QSize(28, 28))
        self.points[-1][6].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.points[-1][6].setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(0, 0, 0);\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    font: 63 8pt \"Yu Gothic UI Semibold\";\n"
                                    "    border-radius: 12px\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(76, 76, 76);\n"
                                    "    border-radius: 12px\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: rgb(116, 116, 116);\n"
                                    "    border-radius: 12px\n"
                                    "}")
        self.points[-1][6].setText('px')
        self.points[-1][1].addWidget(self.points[-1][6], 1, 0, 1, 1)

        self.points[-1][7] = QtWidgets.QPushButton(self.points[-1][0])
        self.points[-1][7].setMinimumSize(QtCore.QSize(28, 28))
        self.points[-1][7].setMaximumSize(QtCore.QSize(28, 28))
        self.points[-1][7].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.points[-1][7].setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(0, 0, 0);\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    font: 63 8pt \"Yu Gothic UI Semibold\";\n"
                                    "    border-radius: 12px\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(76, 76, 76);\n"
                                    "    border-radius: 12px\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: rgb(116, 116, 116);\n"
                                    "    border-radius: 12px\n"
                                    "}")
        self.points[-1][7].setText('px')
        self.points[-1][1].addWidget(self.points[-1][7], 1, 2, 1, 1)

        if mode == 'settings':
            self.verticalLayout_26.addWidget(self.points[-1][0])
        else:
            self.verticalLayout_32.addWidget(self.points[-1][0])
            del self.points[-1]


class KeyWidget(QWidget, Ui_Key):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.get_key)

    def get_key(self):
        if self.lineEdit.text() == '':
            pass
        else:
            benefer.key = self.lineEdit.text()
            with open('cash\key.txt', 'w') as file:
                file.write(benefer.key)
            self.close()


class PlayWidget(QWidget, Ui_StartServer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.cmd)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_AttributeCount)
        self.closeBut.clicked.connect(self.close)
        self.closeBut_2.clicked.connect(self.minimize)

    def close(self):
        self.hide()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.dragPos)
        self.dragPos = event.globalPos()
        event.accept()

    def cmd(self):
        benefer.site.save(r"templates/base.html")
        os.system(f'start /min python server.py')
        self.hide()
        subprocess.run(['cmd'])

    def minimize(self):
        self.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    benefer = MyWidget()
    benefer.show()
    sys.exit(app.exec_())
