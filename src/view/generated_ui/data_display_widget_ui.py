# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_display_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

from src.view.widgets.linear_indicator_widget import LinearIndicator

class Ui_DataDisplay(object):
    def setupUi(self, DataDisplay):
        if not DataDisplay.objectName():
            DataDisplay.setObjectName(u"DataDisplay")
        DataDisplay.resize(265, 165)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DataDisplay.sizePolicy().hasHeightForWidth())
        DataDisplay.setSizePolicy(sizePolicy)
        DataDisplay.setMinimumSize(QSize(265, 165))
        DataDisplay.setMaximumSize(QSize(265, 165))
        DataDisplay.setStyleSheet(u"background-color:rgb(34,40,49)")
        self.errorLabel = QLabel(DataDisplay)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(0, 120, 265, 25))
        self.errorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nameLabel = QLabel(DataDisplay)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(0, 0, 265, 50))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(14)
        font.setBold(True)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.indicator_1 = LinearIndicator(DataDisplay)
        self.indicator_1.setObjectName(u"indicator_1")
        self.indicator_1.setGeometry(QRect(0, 60, 265, 60))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.indicator_1.sizePolicy().hasHeightForWidth())
        self.indicator_1.setSizePolicy(sizePolicy1)
        self.indicator_1.setMinimumSize(QSize(265, 60))
        self.indicator_1.setMaximumSize(QSize(265, 60))

        self.retranslateUi(DataDisplay)

        QMetaObject.connectSlotsByName(DataDisplay)
    # setupUi

    def retranslateUi(self, DataDisplay):
        DataDisplay.setWindowTitle(QCoreApplication.translate("DataDisplay", u"Form", None))
        self.errorLabel.setText(QCoreApplication.translate("DataDisplay", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#ff0000;\">ERROR</span></p></body></html>", None))
        self.nameLabel.setText(QCoreApplication.translate("DataDisplay", u"<html><head/><body><p><span style=\" color:#eeeeee;\">&lt;NAME&gt;</span></p></body></html>", None))
    # retranslateUi

