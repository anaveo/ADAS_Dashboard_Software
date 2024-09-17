# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diagnostic_view_page.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QSizePolicy,
    QWidget)

from src.view.widgets.data_display_widget import DataDisplay

class Ui_DiagnosticViewPage(object):
    def setupUi(self, DiagnosticViewPage):
        if not DiagnosticViewPage.objectName():
            DiagnosticViewPage.setObjectName(u"DiagnosticViewPage")
        DiagnosticViewPage.resize(800, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DiagnosticViewPage.sizePolicy().hasHeightForWidth())
        DiagnosticViewPage.setSizePolicy(sizePolicy)
        DiagnosticViewPage.setMinimumSize(QSize(800, 400))
        DiagnosticViewPage.setMaximumSize(QSize(800, 400))
        self.gridLayoutWidget = QWidget(DiagnosticViewPage)
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


        self.retranslateUi(DiagnosticViewPage)

        QMetaObject.connectSlotsByName(DiagnosticViewPage)
    # setupUi

    def retranslateUi(self, DiagnosticViewPage):
        DiagnosticViewPage.setWindowTitle(QCoreApplication.translate("DiagnosticViewPage", u"Form", None))
    # retranslateUi

