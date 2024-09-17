# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lane_view_page.ui'
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
import src.view.resources_rc

class Ui_LaneViewPage(object):
    def setupUi(self, LaneViewPage):
        if not LaneViewPage.objectName():
            LaneViewPage.setObjectName(u"LaneViewPage")
        LaneViewPage.resize(800, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LaneViewPage.sizePolicy().hasHeightForWidth())
        LaneViewPage.setSizePolicy(sizePolicy)
        LaneViewPage.setMinimumSize(QSize(800, 400))
        LaneViewPage.setMaximumSize(QSize(800, 400))
        self.carImage = QLabel(LaneViewPage)
        self.carImage.setObjectName(u"carImage")
        self.carImage.setGeometry(QRect(200, 0, 400, 400))
        sizePolicy.setHeightForWidth(self.carImage.sizePolicy().hasHeightForWidth())
        self.carImage.setSizePolicy(sizePolicy)
        self.carImage.setMinimumSize(QSize(400, 400))
        self.carImage.setMaximumSize(QSize(400, 400))
        self.carImage.setBaseSize(QSize(400, 400))

        self.retranslateUi(LaneViewPage)

        QMetaObject.connectSlotsByName(LaneViewPage)
    # setupUi

    def retranslateUi(self, LaneViewPage):
        LaneViewPage.setWindowTitle(QCoreApplication.translate("LaneViewPage", u"Form", None))
        self.carImage.setText(QCoreApplication.translate("LaneViewPage", u"<html><head/><body><p><img src=\":/images/image-civic-top-back.png\"/></p></body></html>", None))
    # retranslateUi

