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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)

from src.view.widgets.data_display_widget import DataDisplay
# import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setMaximumSize(QSize(800, 480))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 400))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(800, 400))
        self.stackedWidget.setMaximumSize(QSize(800, 400))
        self.stackedWidget.setStyleSheet(u"")
        self.cameraViewTab = QWidget()
        self.cameraViewTab.setObjectName(u"cameraViewTab")
        self.label_2 = QLabel(self.cameraViewTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 130, 100, 100))
        self.label_2.setMinimumSize(QSize(100, 100))
        self.label_2.setMaximumSize(QSize(100, 100))
        self.stackedWidget.addWidget(self.cameraViewTab)
        self.diagnosticViewTab = QWidget()
        self.diagnosticViewTab.setObjectName(u"diagnosticViewTab")
        self.diagnosticViewTab.setStyleSheet(u"background-color:rgb(34,40,49)")
        self.gridLayoutWidget = QWidget(self.diagnosticViewTab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 797, 472))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.dataDisplay_3 = DataDisplay(self.gridLayoutWidget)
        self.dataDisplay_3.setObjectName(u"dataDisplay_3")
        sizePolicy.setHeightForWidth(self.dataDisplay_3.sizePolicy().hasHeightForWidth())
        self.dataDisplay_3.setSizePolicy(sizePolicy)
        self.dataDisplay_3.setMinimumSize(QSize(265, 235))
        self.dataDisplay_3.setMaximumSize(QSize(265, 235))

        self.gridLayout.addWidget(self.dataDisplay_3, 0, 2, 1, 1)

        self.dataDisplay_1 = DataDisplay(self.gridLayoutWidget)
        self.dataDisplay_1.setObjectName(u"dataDisplay_1")
        sizePolicy.setHeightForWidth(self.dataDisplay_1.sizePolicy().hasHeightForWidth())
        self.dataDisplay_1.setSizePolicy(sizePolicy)
        self.dataDisplay_1.setMinimumSize(QSize(265, 235))
        self.dataDisplay_1.setMaximumSize(QSize(265, 235))

        self.gridLayout.addWidget(self.dataDisplay_1, 0, 0, 1, 1)

        self.dataDisplay_2 = DataDisplay(self.gridLayoutWidget)
        self.dataDisplay_2.setObjectName(u"dataDisplay_2")
        sizePolicy.setHeightForWidth(self.dataDisplay_2.sizePolicy().hasHeightForWidth())
        self.dataDisplay_2.setSizePolicy(sizePolicy)
        self.dataDisplay_2.setMinimumSize(QSize(265, 235))
        self.dataDisplay_2.setMaximumSize(QSize(265, 235))

        self.gridLayout.addWidget(self.dataDisplay_2, 0, 1, 1, 1)

        self.dataDisplay_4 = DataDisplay(self.gridLayoutWidget)
        self.dataDisplay_4.setObjectName(u"dataDisplay_4")
        sizePolicy.setHeightForWidth(self.dataDisplay_4.sizePolicy().hasHeightForWidth())
        self.dataDisplay_4.setSizePolicy(sizePolicy)
        self.dataDisplay_4.setMinimumSize(QSize(265, 160))
        self.dataDisplay_4.setMaximumSize(QSize(265, 160))

        self.gridLayout.addWidget(self.dataDisplay_4, 1, 0, 1, 1)

        self.dataDisplay_5 = DataDisplay(self.gridLayoutWidget)
        self.dataDisplay_5.setObjectName(u"dataDisplay_5")
        sizePolicy.setHeightForWidth(self.dataDisplay_5.sizePolicy().hasHeightForWidth())
        self.dataDisplay_5.setSizePolicy(sizePolicy)
        self.dataDisplay_5.setMinimumSize(QSize(265, 160))
        self.dataDisplay_5.setMaximumSize(QSize(265, 160))

        self.gridLayout.addWidget(self.dataDisplay_5, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.diagnosticViewTab)
        self.laneViewTab = QWidget()
        self.laneViewTab.setObjectName(u"laneViewTab")
        self.label = QLabel(self.laneViewTab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 140, 271, 141))
        self.stackedWidget.addWidget(self.laneViewTab)
        self.Navigation_Bar = QWidget(self.centralwidget)
        self.Navigation_Bar.setObjectName(u"Navigation_Bar")
        self.Navigation_Bar.setGeometry(QRect(0, 400, 800, 80))
        sizePolicy.setHeightForWidth(self.Navigation_Bar.sizePolicy().hasHeightForWidth())
        self.Navigation_Bar.setSizePolicy(sizePolicy)
        self.Navigation_Bar.setMinimumSize(QSize(800, 80))
        self.Navigation_Bar.setMaximumSize(QSize(800, 80))
        self.Navigation_Bar.setAutoFillBackground(False)
        self.Navigation_Bar.setStyleSheet(u"background-color: rgb(20, 20, 20);")
        self.horizontalLayoutWidget = QWidget(self.Navigation_Bar)
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.diagnosticViewButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Camera View Window", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lane View Window", None))
        self.cameraViewButton.setText("")
        self.laneViewButton.setText("")
        self.diagnosticViewButton.setText("")
    # retranslateUi

