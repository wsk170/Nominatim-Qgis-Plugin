# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\projets\QGis plugins\nominatim\dockwidget.ui'
#
# Created: Mon Aug 26 14:19:25 2013
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_search(object):
    def setupUi(self, search):
        search.setObjectName(_fromUtf8("search"))
        search.resize(296, 345)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(search.sizePolicy().hasHeightForWidth())
        search.setSizePolicy(sizePolicy)
        search.setMinimumSize(QtCore.QSize(266, 345))
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(8, -1, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.editSearch = QtGui.QLineEdit(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editSearch.sizePolicy().hasHeightForWidth())
        self.editSearch.setSizePolicy(sizePolicy)
        self.editSearch.setMinimumSize(QtCore.QSize(20, 0))
        self.editSearch.setWhatsThis(_fromUtf8(""))
        self.editSearch.setText(_fromUtf8(""))
        self.editSearch.setObjectName(_fromUtf8("editSearch"))
        self.horizontalLayout_4.addWidget(self.editSearch)
        self.btnSearch = QtGui.QToolButton(self.dockWidgetContents)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.horizontalLayout_4.addWidget(self.btnSearch)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cbExtent = QtGui.QCheckBox(self.dockWidgetContents)
        self.cbExtent.setObjectName(_fromUtf8("cbExtent"))
        self.horizontalLayout.addWidget(self.cbExtent)
        self.btnLocalize = QtGui.QToolButton(self.dockWidgetContents)
        self.btnLocalize.setObjectName(_fromUtf8("btnLocalize"))
        self.horizontalLayout.addWidget(self.btnLocalize)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableResult = QtGui.QTableWidget(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableResult.sizePolicy().hasHeightForWidth())
        self.tableResult.setSizePolicy(sizePolicy)
        self.tableResult.setMinimumSize(QtCore.QSize(0, 30))
        self.tableResult.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableResult.setFont(font)
        self.tableResult.setMouseTracking(True)
        self.tableResult.setAlternatingRowColors(True)
        self.tableResult.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableResult.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableResult.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableResult.setShowGrid(False)
        self.tableResult.setGridStyle(QtCore.Qt.SolidLine)
        self.tableResult.setRowCount(0)
        self.tableResult.setColumnCount(3)
        self.tableResult.setObjectName(_fromUtf8("tableResult"))
        self.tableResult.setColumnCount(3)
        self.tableResult.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableResult.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableResult.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableResult.setHorizontalHeaderItem(2, item)
        self.tableResult.horizontalHeader().setVisible(True)
        self.tableResult.horizontalHeader().setSortIndicatorShown(True)
        self.tableResult.verticalHeader().setVisible(False)
        self.tableResult.verticalHeader().setDefaultSectionSize(17)
        self.tableResult.verticalHeader().setMinimumSectionSize(18)
        self.tableResult.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.tableResult)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnHelp = QtGui.QToolButton(self.dockWidgetContents)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Documents and Settings/culos/.qgis/python/plugins/atlas/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHelp.setIcon(icon)
        self.btnHelp.setObjectName(_fromUtf8("btnHelp"))
        self.horizontalLayout_2.addWidget(self.btnHelp)
        self.btnLayer = QtGui.QToolButton(self.dockWidgetContents)
        self.btnLayer.setObjectName(_fromUtf8("btnLayer"))
        self.horizontalLayout_2.addWidget(self.btnLayer)
        self.btnMask = QtGui.QToolButton(self.dockWidgetContents)
        self.btnMask.setObjectName(_fromUtf8("btnMask"))
        self.horizontalLayout_2.addWidget(self.btnMask)
        self.btnApply = QtGui.QToolButton(self.dockWidgetContents)
        self.btnApply.setMinimumSize(QtCore.QSize(0, 0))
        self.btnApply.setMouseTracking(False)
        self.btnApply.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnApply.setAcceptDrops(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("arrow_green.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnApply.setIcon(icon1)
        self.btnApply.setCheckable(False)
        self.btnApply.setAutoExclusive(False)
        self.btnApply.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnApply.setAutoRaise(False)
        self.btnApply.setObjectName(_fromUtf8("btnApply"))
        self.horizontalLayout_2.addWidget(self.btnApply)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        search.setWidget(self.dockWidgetContents)
        self.label.setBuddy(self.editSearch)

        self.retranslateUi(search)
        QtCore.QMetaObject.connectSlotsByName(search)
        search.setTabOrder(self.editSearch, self.btnSearch)
        search.setTabOrder(self.btnSearch, self.cbExtent)
        search.setTabOrder(self.cbExtent, self.btnLocalize)
        search.setTabOrder(self.btnLocalize, self.tableResult)
        search.setTabOrder(self.tableResult, self.btnHelp)
        search.setTabOrder(self.btnHelp, self.btnLayer)
        search.setTabOrder(self.btnLayer, self.btnMask)
        search.setTabOrder(self.btnMask, self.btnApply)

    def retranslateUi(self, search):
        search.setWindowTitle(QtGui.QApplication.translate("search", "OSM place search...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("search", "Name contains...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSearch.setText(QtGui.QApplication.translate("search", "->", None, QtGui.QApplication.UnicodeUTF8))
        self.cbExtent.setText(QtGui.QApplication.translate("search", "Limit to extent", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLocalize.setToolTip(QtGui.QApplication.translate("search", "Where am I ?", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLocalize.setText(QtGui.QApplication.translate("search", "<-", None, QtGui.QApplication.UnicodeUTF8))
        self.tableResult.setToolTip(QtGui.QApplication.translate("search", "Double-click to zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.tableResult.setStatusTip(QtGui.QApplication.translate("search", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.tableResult.setSortingEnabled(True)
        self.tableResult.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("search", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableResult.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("search", "Class", None, QtGui.QApplication.UnicodeUTF8))
        self.tableResult.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("search", "Infos", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHelp.setText(QtGui.QApplication.translate("search", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLayer.setToolTip(QtGui.QApplication.translate("search", "add object in new layer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLayer.setText(QtGui.QApplication.translate("search", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMask.setToolTip(QtGui.QApplication.translate("search", "create mask from selected object", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMask.setText(QtGui.QApplication.translate("search", "Mask", None, QtGui.QApplication.UnicodeUTF8))
        self.btnApply.setText(QtGui.QApplication.translate("search", "Zoom", None, QtGui.QApplication.UnicodeUTF8))

