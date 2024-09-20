# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_stream_widget.ui'
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

class Ui_CameraStream(object):
    def setupUi(self, CameraStream):
        if not CameraStream.objectName():
            CameraStream.setObjectName(u"CameraStream")
        CameraStream.resize(400, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CameraStream.sizePolicy().hasHeightForWidth())
        CameraStream.setSizePolicy(sizePolicy)
        CameraStream.setMinimumSize(QSize(400, 400))
        CameraStream.setMaximumSize(QSize(400, 400))
        CameraStream.setStyleSheet(u"background-color:black;")
        self.stream = QLabel(CameraStream)
        self.stream.setObjectName(u"stream")
        self.stream.setEnabled(False)
        self.stream.setGeometry(QRect(0, 0, 400, 400))
        sizePolicy.setHeightForWidth(self.stream.sizePolicy().hasHeightForWidth())
        self.stream.setSizePolicy(sizePolicy)
        self.stream.setMinimumSize(QSize(400, 400))
        self.stream.setMaximumSize(QSize(400, 400))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(14)
        font.setBold(True)
        self.stream.setFont(font)
        self.stream.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(CameraStream)

        QMetaObject.connectSlotsByName(CameraStream)
    # setupUi

    def retranslateUi(self, CameraStream):
        CameraStream.setWindowTitle(QCoreApplication.translate("CameraStream", u"Form", None))
        self.stream.setText(QCoreApplication.translate("CameraStream", u"<html><head/><body><p><span style=\" font-size:18pt; color:#eeeeee;\">Waiting for stream...</span></p></body></html>", None))
    # retranslateUi

