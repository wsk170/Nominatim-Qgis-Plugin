# Form implementation generated from reading ui file 'conf_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfDialog(object):
    def setupUi(self, ConfDialog):
        ConfDialog.setObjectName("ConfDialog")
        ConfDialog.setWindowModality(QtCore.Qt.WindowModal)
        ConfDialog.setEnabled(True)
        ConfDialog.resize(547, 192)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfDialog.sizePolicy().hasHeightForWidth())
        ConfDialog.setSizePolicy(sizePolicy)
        ConfDialog.setMinimumSize(QtCore.QSize(540, 150))
        ConfDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ConfDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(ConfDialog)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ConfDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.editOptions = QtWidgets.QLineEdit(ConfDialog)
        self.editOptions.setText("")
        self.editOptions.setObjectName("editOptions")
        self.horizontalLayout.addWidget(self.editOptions)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbEx = QtWidgets.QLabel(ConfDialog)
        self.lbEx.setToolTip("")
        self.lbEx.setObjectName("lbEx")
        self.horizontalLayout_3.addWidget(self.lbEx)
        self.btnBox = QtWidgets.QPushButton(ConfDialog)
        self.btnBox.setAutoDefault(True)
        self.btnBox.setFlat(True)
        self.btnBox.setObjectName("btnBox")
        self.horizontalLayout_3.addWidget(self.btnBox)
        self.btnCountry = QtWidgets.QPushButton(ConfDialog)
        self.btnCountry.setAutoDefault(True)
        self.btnCountry.setFlat(True)
        self.btnCountry.setObjectName("btnCountry")
        self.horizontalLayout_3.addWidget(self.btnCountry)
        self.btnMax = QtWidgets.QPushButton(ConfDialog)
        self.btnMax.setAutoDefault(True)
        self.btnMax.setFlat(True)
        self.btnMax.setObjectName("btnMax")
        self.horizontalLayout_3.addWidget(self.btnMax)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.cbStart = QtWidgets.QCheckBox(ConfDialog)
        self.cbStart.setObjectName("cbStart")
        self.verticalLayout.addWidget(self.cbStart)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.singleLayerCbx = QtWidgets.QCheckBox(ConfDialog)
        self.singleLayerCbx.setObjectName("singleLayerCbx")
        self.verticalLayout_2.addWidget(self.singleLayerCbx)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label.setBuddy(self.editOptions)

        self.retranslateUi(ConfDialog)
        self.buttonBox.accepted.connect(ConfDialog.accept)
        self.buttonBox.rejected.connect(ConfDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfDialog)
        ConfDialog.setTabOrder(self.editOptions, self.cbStart)
        ConfDialog.setTabOrder(self.cbStart, self.buttonBox)

    def retranslateUi(self, ConfDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfDialog.setWindowTitle(
            _translate("ConfDialog", "OSM place search plugin configuration")
        )
        self.label_3.setText(
            _translate(
                "ConfDialog",
                '<p>Nominatim Search from <a href="http://wiki.openstreetmap.org/wiki/Nominatim_usage_policy" target="_blank">OSM</a> <img src="http://www.openstreetmap.org/assets/osm_logo.png">, data © OpenStreetMap contributors - <a href="www.openstreetmap.org/copyright">copyright</a></p>',
            )
        )
        self.label.setText(_translate("ConfDialog", "Options : "))
        self.lbEx.setText(_translate("ConfDialog", "Ex : "))
        self.btnBox.setToolTip(_translate("ConfDialog", "Click here to pick exemple"))
        self.btnBox.setText(_translate("ConfDialog", "viewbox=-1.85,46.35,3.90,42.50"))
        self.btnCountry.setToolTip(
            _translate("ConfDialog", "Click here to pick exemple")
        )
        self.btnCountry.setText(_translate("ConfDialog", "countrycodes=FR"))
        self.btnMax.setToolTip(_translate("ConfDialog", "Click here to pick exemple"))
        self.btnMax.setText(_translate("ConfDialog", "limit=20"))
        self.cbStart.setText(
            _translate("ConfDialog", "Find the nearest location at startup")
        )
        self.singleLayerCbx.setText(
            _translate(
                "ConfDialog", "Create a layer for each object (new layer functionality)"
            )
        )
