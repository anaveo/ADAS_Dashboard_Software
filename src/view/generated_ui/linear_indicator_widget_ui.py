# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linear_indicator_widget.ui'
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

class Ui_LinearIndicator(object):
    def setupUi(self, LinearIndicator):
        if not LinearIndicator.objectName():
            LinearIndicator.setObjectName(u"LinearIndicator")
        LinearIndicator.resize(265, 60)
        LinearIndicator.setMinimumSize(QSize(265, 60))
        LinearIndicator.setMaximumSize(QSize(265, 60))
        LinearIndicator.setStyleSheet(u"")
        self.lowLabel = QLabel(LinearIndicator)
        self.lowLabel.setObjectName(u"lowLabel")
        self.lowLabel.setGeometry(QRect(20, 2, 40, 20))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(14)
        font.setBold(True)
        self.lowLabel.setFont(font)
        self.lowLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.highLabel = QLabel(LinearIndicator)
        self.highLabel.setObjectName(u"highLabel")
        self.highLabel.setGeometry(QRect(205, 2, 40, 20))
        self.highLabel.setFont(font)
        self.highLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.measureLabel = QLabel(LinearIndicator)
        self.measureLabel.setObjectName(u"measureLabel")
        self.measureLabel.setEnabled(False)
        self.measureLabel.setGeometry(QRect(67, 0, 131, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measureLabel.sizePolicy().hasHeightForWidth())
        self.measureLabel.setSizePolicy(sizePolicy)
        self.measureLabel.setFont(font)
        self.measureLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(LinearIndicator)

        QMetaObject.connectSlotsByName(LinearIndicator)
    # setupUi

    def retranslateUi(self, LinearIndicator):
        LinearIndicator.setWindowTitle(QCoreApplication.translate("LinearIndicator", u"Form", None))
        self.lowLabel.setText(QCoreApplication.translate("LinearIndicator", u"<html><head/><body><p><span style=\" font-size:12pt; color:#eeeeee;\">&lt;L&gt;</span></p></body></html>", None))
        self.highLabel.setText(QCoreApplication.translate("LinearIndicator", u"<html><head/><body><p><span style=\" font-size:11pt; color:#eeeeee;\">&lt;H&gt;</span></p></body></html>", None))
        self.measureLabel.setText(QCoreApplication.translate("LinearIndicator", u"<html><head/><body><p><span style=\" font-size:12pt; color:#eeeeee;\">&lt;MEASURE&gt;</span></p></body></html>", None))
    # retranslateUi

