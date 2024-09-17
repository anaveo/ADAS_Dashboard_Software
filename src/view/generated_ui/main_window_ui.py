# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)
# import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setMaximumSize(QSize(800, 480))
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.pageStack = QStackedWidget(self.centralWidget)
        self.pageStack.setObjectName(u"pageStack")
        self.pageStack.setGeometry(QRect(0, 0, 800, 400))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageStack.sizePolicy().hasHeightForWidth())
        self.pageStack.setSizePolicy(sizePolicy)
        self.pageStack.setMinimumSize(QSize(800, 400))
        self.pageStack.setMaximumSize(QSize(800, 400))
        self.pageStack.setStyleSheet(u"")
        self.navigationBar = QWidget(self.centralWidget)
        self.navigationBar.setObjectName(u"navigationBar")
        self.navigationBar.setGeometry(QRect(0, 400, 800, 80))
        sizePolicy.setHeightForWidth(self.navigationBar.sizePolicy().hasHeightForWidth())
        self.navigationBar.setSizePolicy(sizePolicy)
        self.navigationBar.setMinimumSize(QSize(800, 80))
        self.navigationBar.setMaximumSize(QSize(800, 80))
        self.navigationBar.setAutoFillBackground(False)
        self.navigationBar.setStyleSheet(u"background-color: rgb(20, 20, 20);")
        self.horizontalLayoutWidget = QWidget(self.navigationBar)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-10, 0, 809, 82))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cameraViewButton = QPushButton(self.horizontalLayoutWidget)
        self.cameraViewButton.setObjectName(u"cameraViewButton")
        sizePolicy.setHeightForWidth(self.cameraViewButton.sizePolicy().hasHeightForWidth())
        self.cameraViewButton.setSizePolicy(sizePolicy)
        self.cameraViewButton.setMinimumSize(QSize(265, 80))
        self.cameraViewButton.setMaximumSize(QSize(265, 80))
        self.cameraViewButton.setAutoFillBackground(False)
        self.cameraViewButton.setStyleSheet(u"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/icons/icon-camera-grey.png", QSize(), QIcon.Active, QIcon.Off)
        icon.addFile(u":/icons/icon-camera-white.png", QSize(), QIcon.Active, QIcon.On)
        self.cameraViewButton.setIcon(icon)
        self.cameraViewButton.setIconSize(QSize(65, 55))
        self.cameraViewButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.cameraViewButton)

        self.laneViewButton = QPushButton(self.horizontalLayoutWidget)
        self.laneViewButton.setObjectName(u"laneViewButton")
        self.laneViewButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.laneViewButton.sizePolicy().hasHeightForWidth())
        self.laneViewButton.setSizePolicy(sizePolicy)
        self.laneViewButton.setMinimumSize(QSize(265, 80))
        self.laneViewButton.setMaximumSize(QSize(265, 80))
        self.laneViewButton.setAutoFillBackground(False)
        self.laneViewButton.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon-car-grey.png", QSize(), QIcon.Active, QIcon.Off)
        icon1.addFile(u":/icons/icon-car-white.png", QSize(), QIcon.Active, QIcon.On)
        self.laneViewButton.setIcon(icon1)
        self.laneViewButton.setIconSize(QSize(65, 65))
        self.laneViewButton.setCheckable(True)
        self.laneViewButton.setChecked(True)

        self.horizontalLayout.addWidget(self.laneViewButton)

        self.diagnosticViewButton = QPushButton(self.horizontalLayoutWidget)
        self.diagnosticViewButton.setObjectName(u"diagnosticViewButton")
        self.diagnosticViewButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.diagnosticViewButton.sizePolicy().hasHeightForWidth())
        self.diagnosticViewButton.setSizePolicy(sizePolicy)
        self.diagnosticViewButton.setMinimumSize(QSize(265, 80))
        self.diagnosticViewButton.setMaximumSize(QSize(265, 80))
        self.diagnosticViewButton.setBaseSize(QSize(265, 80))
        self.diagnosticViewButton.setAutoFillBackground(False)
        self.diagnosticViewButton.setStyleSheet(u"background-color: transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon-tools-grey.png", QSize(), QIcon.Selected, QIcon.Off)
        icon2.addFile(u":/icons/icon-tools-white.png", QSize(), QIcon.Selected, QIcon.On)
        self.diagnosticViewButton.setIcon(icon2)
        self.diagnosticViewButton.setIconSize(QSize(50, 50))
        self.diagnosticViewButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.diagnosticViewButton)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        self.pageStack.setCurrentIndex(-1)
        self.diagnosticViewButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cameraViewButton.setText("")
        self.laneViewButton.setText("")
        self.diagnosticViewButton.setText("")
    # retranslateUi

