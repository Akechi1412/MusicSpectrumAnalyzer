# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QToolBar, QToolButton, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(630, 650))
        MainWindow.setMaximumSize(QSize(630, 650))
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/images/equalizer.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QProgressBar {\n"
"	background-color: transparent;\n"
"	border: 0px solid grey;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(30,129,176);\n"
"	height: 40px;\n"
"	margin: 0px;\n"
"	margin-top: 5px;		\n"
"	border-radius: 4px\n"
"}\n"
"QToolButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QStatusBar {\n"
"	margin-top: 10px;\n"
"}")
        self.actionOpen_Music = QAction(MainWindow)
        self.actionOpen_Music.setObjectName(u"actionOpen_Music")
        icon1 = QIcon()
        icon1.addFile(u":/images/open-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_Music.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon()
        icon2.addFile(u":/images/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon3 = QIcon()
        icon3.addFile(u":/images/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelp.setIcon(icon3)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon4 = QIcon()
        iconThemeName = u"accessories-calculator"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u":/images/quit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.actionQuit.setIcon(icon4)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionConnect.setCheckable(False)
        icon5 = QIcon()
        icon5.addFile(u":/images/connect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConnect.setIcon(icon5)
        self.actionAvailablePort = QAction(MainWindow)
        self.actionAvailablePort.setObjectName(u"actionAvailablePort")
        self.actionAvailablePort.setCheckable(True)
        self.actionAvailablePort.setChecked(True)
        self.actionCOM2 = QAction(MainWindow)
        self.actionCOM2.setObjectName(u"actionCOM2")
        self.actionCOM2.setCheckable(True)
        self.actionCOM3 = QAction(MainWindow)
        self.actionCOM3.setObjectName(u"actionCOM3")
        self.actionCOM3.setCheckable(True)
        self.actionCOM4 = QAction(MainWindow)
        self.actionCOM4.setObjectName(u"actionCOM4")
        self.actionCOM4.setCheckable(True)
        self.actionCOM5 = QAction(MainWindow)
        self.actionCOM5.setObjectName(u"actionCOM5")
        self.actionCOM5.setCheckable(True)
        self.actionCOM6 = QAction(MainWindow)
        self.actionCOM6.setObjectName(u"actionCOM6")
        self.actionCOM6.setCheckable(True)
        self.actionCOM7 = QAction(MainWindow)
        self.actionCOM7.setObjectName(u"actionCOM7")
        self.actionCOM7.setCheckable(True)
        self.actionCOM8 = QAction(MainWindow)
        self.actionCOM8.setObjectName(u"actionCOM8")
        self.actionCOM8.setCheckable(True)
        self.actionCOM9 = QAction(MainWindow)
        self.actionCOM9.setObjectName(u"actionCOM9")
        self.actionCOM9.setCheckable(True)
        self.actionCOM10 = QAction(MainWindow)
        self.actionCOM10.setObjectName(u"actionCOM10")
        self.actionMode_1 = QAction(MainWindow)
        self.actionMode_1.setObjectName(u"actionMode_1")
        self.actionMode_1.setCheckable(True)
        self.actionMode_2 = QAction(MainWindow)
        self.actionMode_2.setObjectName(u"actionMode_2")
        self.actionMode_2.setCheckable(True)
        self.actionMode_3 = QAction(MainWindow)
        self.actionMode_3.setObjectName(u"actionMode_3")
        self.actionMode_3.setCheckable(True)
        self.actionMode_4 = QAction(MainWindow)
        self.actionMode_4.setObjectName(u"actionMode_4")
        self.actionMode_4.setCheckable(True)
        self.actionMode_5 = QAction(MainWindow)
        self.actionMode_5.setObjectName(u"actionMode_5")
        self.actionMode_5.setCheckable(True)
        self.actionAvailable_Port = QAction(MainWindow)
        self.actionAvailable_Port.setObjectName(u"actionAvailable_Port")
        self.action_COM1 = QAction(MainWindow)
        self.action_COM1.setObjectName(u"action_COM1")
        self.action_COM1.setCheckable(True)
        self.action_COM2 = QAction(MainWindow)
        self.action_COM2.setObjectName(u"action_COM2")
        self.action_COM2.setCheckable(True)
        self.action_COM3 = QAction(MainWindow)
        self.action_COM3.setObjectName(u"action_COM3")
        self.action_COM3.setCheckable(True)
        self.action_COM4 = QAction(MainWindow)
        self.action_COM4.setObjectName(u"action_COM4")
        self.action_COM4.setCheckable(True)
        self.action_COM5 = QAction(MainWindow)
        self.action_COM5.setObjectName(u"action_COM5")
        self.action_COM5.setCheckable(True)
        self.action_COM6 = QAction(MainWindow)
        self.action_COM6.setObjectName(u"action_COM6")
        self.action_COM6.setCheckable(True)
        self.action_COM7 = QAction(MainWindow)
        self.action_COM7.setObjectName(u"action_COM7")
        self.action_COM7.setCheckable(True)
        self.action_COM8 = QAction(MainWindow)
        self.action_COM8.setObjectName(u"action_COM8")
        self.action_COM8.setCheckable(True)
        self.action_COM9 = QAction(MainWindow)
        self.action_COM9.setObjectName(u"action_COM9")
        self.action_COM9.setCheckable(True)
        self.action_COM10 = QAction(MainWindow)
        self.action_COM10.setObjectName(u"action_COM10")
        self.action_COM10.setCheckable(True)
        self.action_COM11 = QAction(MainWindow)
        self.action_COM11.setObjectName(u"action_COM11")
        self.action_COM11.setCheckable(True)
        self.action_COM12 = QAction(MainWindow)
        self.action_COM12.setObjectName(u"action_COM12")
        self.action_COM12.setCheckable(True)
        self.action_COM13 = QAction(MainWindow)
        self.action_COM13.setObjectName(u"action_COM13")
        self.action_COM13.setCheckable(True)
        self.action_COM14 = QAction(MainWindow)
        self.action_COM14.setObjectName(u"action_COM14")
        self.action_COM14.setCheckable(True)
        self.action_COM15 = QAction(MainWindow)
        self.action_COM15.setObjectName(u"action_COM15")
        self.action_COM15.setCheckable(True)
        self.action_COM16 = QAction(MainWindow)
        self.action_COM16.setObjectName(u"action_COM16")
        self.action_COM16.setCheckable(True)
        self.action_COM17 = QAction(MainWindow)
        self.action_COM17.setObjectName(u"action_COM17")
        self.action_COM17.setCheckable(True)
        self.action_COM18 = QAction(MainWindow)
        self.action_COM18.setObjectName(u"action_COM18")
        self.action_COM18.setCheckable(True)
        self.action_COM19 = QAction(MainWindow)
        self.action_COM19.setObjectName(u"action_COM19")
        self.action_COM19.setCheckable(True)
        self.action_COM20 = QAction(MainWindow)
        self.action_COM20.setObjectName(u"action_COM20")
        self.action_COM20.setCheckable(True)
        self.action_COM21 = QAction(MainWindow)
        self.action_COM21.setObjectName(u"action_COM21")
        self.action_COM21.setCheckable(True)
        self.action_COM22 = QAction(MainWindow)
        self.action_COM22.setObjectName(u"action_COM22")
        self.action_COM22.setCheckable(True)
        self.action_COM23 = QAction(MainWindow)
        self.action_COM23.setObjectName(u"action_COM23")
        self.action_COM23.setCheckable(True)
        self.action_COM24 = QAction(MainWindow)
        self.action_COM24.setObjectName(u"action_COM24")
        self.action_COM24.setCheckable(True)
        self.action_COM25 = QAction(MainWindow)
        self.action_COM25.setObjectName(u"action_COM25")
        self.action_COM25.setCheckable(True)
        self.action_COM26 = QAction(MainWindow)
        self.action_COM26.setObjectName(u"action_COM26")
        self.action_COM26.setCheckable(True)
        self.action_COM27 = QAction(MainWindow)
        self.action_COM27.setObjectName(u"action_COM27")
        self.action_COM27.setCheckable(True)
        self.action_COM28 = QAction(MainWindow)
        self.action_COM28.setObjectName(u"action_COM28")
        self.action_COM28.setCheckable(True)
        self.actionPrimaryColor = QAction(MainWindow)
        self.actionPrimaryColor.setObjectName(u"actionPrimaryColor")
        self.actionSecondaryColor = QAction(MainWindow)
        self.actionSecondaryColor.setObjectName(u"actionSecondaryColor")
        self.actionTertiaryColor = QAction(MainWindow)
        self.actionTertiaryColor.setObjectName(u"actionTertiaryColor")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 587, 529))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar_Spectrum1 = QProgressBar(self.layoutWidget)
        self.progressBar_Spectrum1.setObjectName(u"progressBar_Spectrum1")
        self.progressBar_Spectrum1.setMinimumSize(QSize(40, 360))
        self.progressBar_Spectrum1.setMaximum(8)
        self.progressBar_Spectrum1.setValue(1)
        self.progressBar_Spectrum1.setTextVisible(False)
        self.progressBar_Spectrum1.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_Spectrum1)

        self.progressBar_Spectrum2 = QProgressBar(self.layoutWidget)
        self.progressBar_Spectrum2.setObjectName(u"progressBar_Spectrum2")
        self.progressBar_Spectrum2.setMinimumSize(QSize(40, 360))
        self.progressBar_Spectrum2.setMaximum(8)
        self.progressBar_Spectrum2.setValue(2)
        self.progressBar_Spectrum2.setTextVisible(False)
        self.progressBar_Spectrum2.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_Spectrum2)

        self.progressBar_Spectrum3 = QProgressBar(self.layoutWidget)
        self.progressBar_Spectrum3.setObjectName(u"progressBar_Spectrum3")
        self.progressBar_Spectrum3.setMinimumSize(QSize(40, 360))
        self.progressBar_Spectrum3.setMaximum(8)
        self.progressBar_Spectrum3.setValue(3)
        self.progressBar_Spectrum3.setTextVisible(False)
        self.progressBar_Spectrum3.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_Spectrum3)

        self.progressBar_Spectrum4 = QProgressBar(self.layoutWidget)
        self.progressBar_Spectrum4.setObjectName(u"progressBar_Spectrum4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.progressBar_Spectrum4.sizePolicy().hasHeightForWidth())
        self.progressBar_Spectrum4.setSizePolicy(sizePolicy1)
        self.progressBar_Spectrum4.setMinimumSize(QSize(40, 360))
        self.progressBar_Spectrum4.setMaximum(8)
        self.progressBar_Spectrum4.setValue(4)
        self.progressBar_Spectrum4.setTextVisible(False)
        self.progressBar_Spectrum4.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_Spectrum4)

        self.progressBar_Spectrum5 = QProgressBar(self.layoutWidget)
        self.progressBar_Spectrum5.setObjectName(u"progressBar_Spectrum5")
        self.progressBar_Spectrum5.setMinimumSize(QSize(40, 360))
        self.progressBar_Spectrum5.setMaximum(8)
        self.progressBar_Spectrum5.setValue(5)
        self.progressBar_Spectrum5.setTextVisible(False)
        self.progressBar_Spectrum5.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_Spectrum5)

        self.progressBar_Spectrum6 = QProgressBar(self.layoutWidget)
        self.progressBar_Spectrum6.setObjectName(u"progressBar_Spectrum6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar_Spectrum6.sizePolicy().hasHeightForWidth())
        self.progressBar_Spectrum6.setSizePolicy(sizePolicy2)
        self.progressBar_Spectrum6.setMinimumSize(QSize(40, 360))
        self.progressBar_Spectrum6.setMaximum(8)
        self.progressBar_Spectrum6.setValue(6)
        self.progressBar_Spectrum6.setTextVisible(False)
        self.progressBar_Spectrum6.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_Spectrum6)

        self.progressBar_Spectrum7 = QProgressBar(self.layoutWidget)
        self.progressBar_Spectrum7.setObjectName(u"progressBar_Spectrum7")
        self.progressBar_Spectrum7.setMinimumSize(QSize(40, 360))
        self.progressBar_Spectrum7.setMaximum(8)
        self.progressBar_Spectrum7.setValue(7)
        self.progressBar_Spectrum7.setTextVisible(False)
        self.progressBar_Spectrum7.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_Spectrum7)

        self.progressBar_Spectrum8 = QProgressBar(self.layoutWidget)
        self.progressBar_Spectrum8.setObjectName(u"progressBar_Spectrum8")
        self.progressBar_Spectrum8.setMinimumSize(QSize(40, 360))
        self.progressBar_Spectrum8.setMaximum(8)
        self.progressBar_Spectrum8.setValue(8)
        self.progressBar_Spectrum8.setTextVisible(False)
        self.progressBar_Spectrum8.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_Spectrum8)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame_Hz_labels = QFrame(self.layoutWidget)
        self.frame_Hz_labels.setObjectName(u"frame_Hz_labels")
        self.frame_Hz_labels.setFrameShape(QFrame.StyledPanel)
        self.frame_Hz_labels.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_Hz_labels)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_Spectrum1 = QLabel(self.frame_Hz_labels)
        self.label_Spectrum1.setObjectName(u"label_Spectrum1")

        self.horizontalLayout_2.addWidget(self.label_Spectrum1)

        self.label_Spectrum2 = QLabel(self.frame_Hz_labels)
        self.label_Spectrum2.setObjectName(u"label_Spectrum2")

        self.horizontalLayout_2.addWidget(self.label_Spectrum2)

        self.label_Spectrum3 = QLabel(self.frame_Hz_labels)
        self.label_Spectrum3.setObjectName(u"label_Spectrum3")

        self.horizontalLayout_2.addWidget(self.label_Spectrum3)

        self.label_Spectrum4 = QLabel(self.frame_Hz_labels)
        self.label_Spectrum4.setObjectName(u"label_Spectrum4")

        self.horizontalLayout_2.addWidget(self.label_Spectrum4)

        self.label_Spectrum5 = QLabel(self.frame_Hz_labels)
        self.label_Spectrum5.setObjectName(u"label_Spectrum5")

        self.horizontalLayout_2.addWidget(self.label_Spectrum5)

        self.label_Spectrum6 = QLabel(self.frame_Hz_labels)
        self.label_Spectrum6.setObjectName(u"label_Spectrum6")

        self.horizontalLayout_2.addWidget(self.label_Spectrum6)

        self.label_Spectrum7 = QLabel(self.frame_Hz_labels)
        self.label_Spectrum7.setObjectName(u"label_Spectrum7")

        self.horizontalLayout_2.addWidget(self.label_Spectrum7)

        self.label_Spectrum8 = QLabel(self.frame_Hz_labels)
        self.label_Spectrum8.setObjectName(u"label_Spectrum8")

        self.horizontalLayout_2.addWidget(self.label_Spectrum8)


        self.verticalLayout.addWidget(self.frame_Hz_labels)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelPosition = QLabel(self.layoutWidget)
        self.labelPosition.setObjectName(u"labelPosition")
        font = QFont()
        font.setPointSize(12)
        self.labelPosition.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelPosition)

        self.horizontalSliderPlayer = QSlider(self.layoutWidget)
        self.horizontalSliderPlayer.setObjectName(u"horizontalSliderPlayer")
        self.horizontalSliderPlayer.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSliderPlayer.setStyleSheet(u"QSlider {\n"
"	margin: 8px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	border-radius: 5px;\n"
"	height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(190,190,190);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	border: 5px solid transparent;\n"
"	width: 6px;\n"
"	height: 6px;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(2,2,2);\n"
"	margin: -3px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"	border: none;\n"
"	width: 16px;\n"
"	height: 16px;\n"
"	border-radius: 8px;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"	border: 5px solid white;\n"
"	width: 6px;\n"
"	height: 6px;\n"
"	border-radius: 8px;\n"
"}")
        self.horizontalSliderPlayer.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSliderPlayer)

        self.labelDuration = QLabel(self.layoutWidget)
        self.labelDuration.setObjectName(u"labelDuration")
        self.labelDuration.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelDuration)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButtonPlay = QToolButton(self.layoutWidget)
        self.toolButtonPlay.setObjectName(u"toolButtonPlay")
        self.toolButtonPlay.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButtonPlay.setStyleSheet(u"QToolButton {\n"
"	background-color: rgb(204,204,204);\n"
"	padding: 10px;\n"
"	border-radius: 6px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/images/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonPlay.setIcon(icon6)
        self.toolButtonPlay.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.toolButtonPlay)

        self.toolButtonPause = QToolButton(self.layoutWidget)
        self.toolButtonPause.setObjectName(u"toolButtonPause")
        self.toolButtonPause.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButtonPause.setStyleSheet(u"QToolButton {\n"
"	background-color: rgb(204,204,204);\n"
"	padding: 10px;\n"
"	border-radius: 6px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/images/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonPause.setIcon(icon7)
        self.toolButtonPause.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.toolButtonPause)

        self.toolButtonStop = QToolButton(self.layoutWidget)
        self.toolButtonStop.setObjectName(u"toolButtonStop")
        self.toolButtonStop.setBaseSize(QSize(24, 24))
        self.toolButtonStop.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButtonStop.setStyleSheet(u"QToolButton {\n"
"	background-color: rgb(204,204,204);\n"
"	padding: 10px;\n"
"	border-radius: 6px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/images/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonStop.setIcon(icon8)
        self.toolButtonStop.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.toolButtonStop)

        self.horizontalSpacer = QSpacerItem(298, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.toolButtonVolume = QToolButton(self.layoutWidget)
        self.toolButtonVolume.setObjectName(u"toolButtonVolume")
        self.toolButtonVolume.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButtonVolume.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/images/medium-volume.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonVolume.setIcon(icon9)
        self.toolButtonVolume.setIconSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.toolButtonVolume)

        self.horizontalSliderVolume = QSlider(self.layoutWidget)
        self.horizontalSliderVolume.setObjectName(u"horizontalSliderVolume")
        self.horizontalSliderVolume.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSliderVolume.setStyleSheet(u"QSlider {\n"
"	margin: 5px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	border-radius: 3px;\n"
"	height: 6px;\n"
"	margin: 0px;\n"
"	background-color: rgb(190,190,190);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background-color: rgb(2,2,2);\n"
"	margin: -3px;\n"
"	border: none;\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	border-radius: 6px;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"	border: 4px solid white;\n"
"	width: 4px;\n"
"	height: 4px;\n"
"	border-radius: 6px;\n"
"}")
        self.horizontalSliderVolume.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.horizontalSliderVolume)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 630, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuMode = QMenu(self.menuEdit)
        self.menuMode.setObjectName(u"menuMode")
        icon10 = QIcon()
        icon10.addFile(u":/images/mode.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuMode.setIcon(icon10)
        self.menuColor = QMenu(self.menuEdit)
        self.menuColor.setObjectName(u"menuColor")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuPort = QMenu(self.menuTools)
        self.menuPort.setObjectName(u"menuPort")
        icon11 = QIcon()
        icon11.addFile(u":/images/usb-port.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuPort.setIcon(icon11)
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_Music)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.menuMode.menuAction())
        self.menuEdit.addAction(self.menuColor.menuAction())
        self.menuMode.addAction(self.actionMode_1)
        self.menuMode.addAction(self.actionMode_2)
        self.menuMode.addAction(self.actionMode_3)
        self.menuMode.addAction(self.actionMode_4)
        self.menuMode.addAction(self.actionMode_5)
        self.menuColor.addAction(self.actionPrimaryColor)
        self.menuColor.addAction(self.actionSecondaryColor)
        self.menuColor.addAction(self.actionTertiaryColor)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuTools.addAction(self.actionConnect)
        self.menuTools.addAction(self.menuPort.menuAction())
        self.menuPort.addAction(self.actionAvailablePort)
        self.menuPort.addAction(self.action_COM1)
        self.menuPort.addAction(self.action_COM2)
        self.menuPort.addAction(self.action_COM3)
        self.menuPort.addAction(self.action_COM4)
        self.menuPort.addAction(self.action_COM5)
        self.menuPort.addAction(self.action_COM6)
        self.menuPort.addAction(self.action_COM7)
        self.menuPort.addAction(self.action_COM8)
        self.menuPort.addAction(self.action_COM9)
        self.menuPort.addAction(self.action_COM10)
        self.menuPort.addAction(self.action_COM11)
        self.menuPort.addAction(self.action_COM12)
        self.menuPort.addAction(self.action_COM13)
        self.menuPort.addAction(self.action_COM14)
        self.menuPort.addAction(self.action_COM15)
        self.menuPort.addAction(self.action_COM16)
        self.menuPort.addAction(self.action_COM17)
        self.menuPort.addAction(self.action_COM18)
        self.menuPort.addAction(self.action_COM19)
        self.menuPort.addAction(self.action_COM20)
        self.menuPort.addAction(self.action_COM21)
        self.menuPort.addAction(self.action_COM22)
        self.menuPort.addAction(self.action_COM23)
        self.menuPort.addAction(self.action_COM24)
        self.menuPort.addAction(self.action_COM25)
        self.menuPort.addAction(self.action_COM26)
        self.menuPort.addAction(self.action_COM27)
        self.menuPort.addAction(self.action_COM28)
        self.toolBar.addAction(self.actionOpen_Music)
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MSpezer", None))
        self.actionOpen_Music.setText(QCoreApplication.translate("MainWindow", u"Open Music", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.actionAvailablePort.setText(QCoreApplication.translate("MainWindow", u"Avaiable Port", None))
        self.actionCOM2.setText(QCoreApplication.translate("MainWindow", u"COM1", None))
        self.actionCOM3.setText(QCoreApplication.translate("MainWindow", u"COM2", None))
        self.actionCOM4.setText(QCoreApplication.translate("MainWindow", u"COM3", None))
        self.actionCOM5.setText(QCoreApplication.translate("MainWindow", u"COM4", None))
        self.actionCOM6.setText(QCoreApplication.translate("MainWindow", u"COM4", None))
        self.actionCOM7.setText(QCoreApplication.translate("MainWindow", u"COM5", None))
        self.actionCOM8.setText(QCoreApplication.translate("MainWindow", u"COM8", None))
        self.actionCOM9.setText(QCoreApplication.translate("MainWindow", u"COM9", None))
        self.actionCOM10.setText(QCoreApplication.translate("MainWindow", u"COM10", None))
        self.actionMode_1.setText(QCoreApplication.translate("MainWindow", u"Mode 1", None))
        self.actionMode_2.setText(QCoreApplication.translate("MainWindow", u"Mode 2", None))
        self.actionMode_3.setText(QCoreApplication.translate("MainWindow", u"Mode 3", None))
        self.actionMode_4.setText(QCoreApplication.translate("MainWindow", u"Mode 4", None))
        self.actionMode_5.setText(QCoreApplication.translate("MainWindow", u"Mode 5", None))
        self.actionAvailable_Port.setText(QCoreApplication.translate("MainWindow", u"Available Port", None))
        self.action_COM1.setText(QCoreApplication.translate("MainWindow", u"COM1", None))
        self.action_COM2.setText(QCoreApplication.translate("MainWindow", u"COM2", None))
        self.action_COM3.setText(QCoreApplication.translate("MainWindow", u"COM3", None))
        self.action_COM4.setText(QCoreApplication.translate("MainWindow", u"COM4", None))
        self.action_COM5.setText(QCoreApplication.translate("MainWindow", u"COM5", None))
        self.action_COM6.setText(QCoreApplication.translate("MainWindow", u"COM6", None))
        self.action_COM7.setText(QCoreApplication.translate("MainWindow", u"COM7", None))
        self.action_COM8.setText(QCoreApplication.translate("MainWindow", u"COM8", None))
        self.action_COM9.setText(QCoreApplication.translate("MainWindow", u"COM9", None))
        self.action_COM10.setText(QCoreApplication.translate("MainWindow", u"COM10", None))
        self.action_COM11.setText(QCoreApplication.translate("MainWindow", u"COM11", None))
        self.action_COM12.setText(QCoreApplication.translate("MainWindow", u"COM12", None))
        self.action_COM13.setText(QCoreApplication.translate("MainWindow", u"COM13", None))
        self.action_COM14.setText(QCoreApplication.translate("MainWindow", u"COM14", None))
        self.action_COM15.setText(QCoreApplication.translate("MainWindow", u"COM15", None))
        self.action_COM16.setText(QCoreApplication.translate("MainWindow", u"COM16", None))
        self.action_COM17.setText(QCoreApplication.translate("MainWindow", u"COM17", None))
        self.action_COM18.setText(QCoreApplication.translate("MainWindow", u"COM18", None))
        self.action_COM19.setText(QCoreApplication.translate("MainWindow", u"COM19", None))
        self.action_COM20.setText(QCoreApplication.translate("MainWindow", u"COM20", None))
        self.action_COM21.setText(QCoreApplication.translate("MainWindow", u"COM21", None))
        self.action_COM22.setText(QCoreApplication.translate("MainWindow", u"COM22", None))
        self.action_COM23.setText(QCoreApplication.translate("MainWindow", u"COM23", None))
        self.action_COM24.setText(QCoreApplication.translate("MainWindow", u"COM24", None))
        self.action_COM25.setText(QCoreApplication.translate("MainWindow", u"COM25", None))
        self.action_COM26.setText(QCoreApplication.translate("MainWindow", u"COM26", None))
        self.action_COM27.setText(QCoreApplication.translate("MainWindow", u"COM27", None))
        self.action_COM28.setText(QCoreApplication.translate("MainWindow", u"COM28", None))
        self.actionPrimaryColor.setText(QCoreApplication.translate("MainWindow", u"Primary Color", None))
        self.actionSecondaryColor.setText(QCoreApplication.translate("MainWindow", u"Secondary Color", None))
        self.actionTertiaryColor.setText(QCoreApplication.translate("MainWindow", u"Tertiary Color", None))
        self.progressBar_Spectrum1.setFormat("")
        self.progressBar_Spectrum2.setFormat("")
        self.progressBar_Spectrum3.setFormat("")
        self.progressBar_Spectrum4.setFormat("")
        self.progressBar_Spectrum5.setFormat("")
        self.progressBar_Spectrum6.setFormat("")
        self.progressBar_Spectrum7.setFormat("")
        self.progressBar_Spectrum8.setFormat("")
        self.label_Spectrum1.setText(QCoreApplication.translate("MainWindow", u"      31Hz", None))
        self.label_Spectrum2.setText(QCoreApplication.translate("MainWindow", u"      73Hz", None))
        self.label_Spectrum3.setText(QCoreApplication.translate("MainWindow", u"    173Hz", None))
        self.label_Spectrum4.setText(QCoreApplication.translate("MainWindow", u"     411Hz", None))
        self.label_Spectrum5.setText(QCoreApplication.translate("MainWindow", u"    974Hz", None))
        self.label_Spectrum6.setText(QCoreApplication.translate("MainWindow", u"   2.3kHz", None))
        self.label_Spectrum7.setText(QCoreApplication.translate("MainWindow", u"    5.5kHz", None))
        self.label_Spectrum8.setText(QCoreApplication.translate("MainWindow", u"   13kHz", None))
        self.labelPosition.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.labelDuration.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
#if QT_CONFIG(tooltip)
        self.toolButtonPlay.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Play</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonPlay.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolButtonPause.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pause</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonPause.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolButtonStop.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Stop</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonStop.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolButtonVolume.setToolTip(QCoreApplication.translate("MainWindow", u"Volume", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonVolume.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuMode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.menuColor.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuPort.setTitle(QCoreApplication.translate("MainWindow", u"Port", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

