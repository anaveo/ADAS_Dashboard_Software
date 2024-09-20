# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_view_page.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

from src.view.widgets.camera_stream_widget import CameraStream

class Ui_CameraViewPage(object):
    def setupUi(self, CameraViewPage):
        if not CameraViewPage.objectName():
            CameraViewPage.setObjectName(u"CameraViewPage")
        CameraViewPage.resize(800, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CameraViewPage.sizePolicy().hasHeightForWidth())
        CameraViewPage.setSizePolicy(sizePolicy)
        CameraViewPage.setMinimumSize(QSize(800, 400))
        CameraViewPage.setMaximumSize(QSize(800, 400))
        self.rightCamStream = CameraStream(CameraViewPage)
        self.rightCamStream.setObjectName(u"rightCamStream")
        self.rightCamStream.setGeometry(QRect(400, 0, 400, 400))
        sizePolicy.setHeightForWidth(self.rightCamStream.sizePolicy().hasHeightForWidth())
        self.rightCamStream.setSizePolicy(sizePolicy)
        self.rightCamStream.setMinimumSize(QSize(400, 400))
        self.rightCamStream.setMaximumSize(QSize(400, 400))
        self.leftCamStream = CameraStream(CameraViewPage)
        self.leftCamStream.setObjectName(u"leftCamStream")
        self.leftCamStream.setGeometry(QRect(0, 0, 400, 400))
        sizePolicy.setHeightForWidth(self.leftCamStream.sizePolicy().hasHeightForWidth())
        self.leftCamStream.setSizePolicy(sizePolicy)
        self.leftCamStream.setMinimumSize(QSize(400, 400))
        self.leftCamStream.setMaximumSize(QSize(400, 400))

        self.retranslateUi(CameraViewPage)

        QMetaObject.connectSlotsByName(CameraViewPage)
    # setupUi

    def retranslateUi(self, CameraViewPage):
        CameraViewPage.setWindowTitle(QCoreApplication.translate("CameraViewPage", u"Form", None))
    # retranslateUi

