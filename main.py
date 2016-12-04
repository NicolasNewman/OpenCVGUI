from PyQt4 import QtCore, QtGui
import cv2
import numpy as np
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(691, 504)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.videoFeedButtonLayout = QtGui.QVBoxLayout()
        self.videoFeedButtonLayout.setObjectName(_fromUtf8("videoFeedButtonLayout"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.defaultFeedButton = QtGui.QPushButton(self.centralwidget)
        self.defaultFeedButton.setObjectName(_fromUtf8("defaultFeedButton"))
        self.horizontalLayout_13.addWidget(self.defaultFeedButton)
        self.colorFeedButton = QtGui.QPushButton(self.centralwidget)
        self.colorFeedButton.setObjectName(_fromUtf8("colorFeedButton"))
        self.horizontalLayout_13.addWidget(self.colorFeedButton)
        self.cannyFeedButton = QtGui.QPushButton(self.centralwidget)
        self.cannyFeedButton.setObjectName(_fromUtf8("cannyFeedButton"))
        self.horizontalLayout_13.addWidget(self.cannyFeedButton)
        self.videoFeedButtonLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.blurFeedButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blurFeedButton.sizePolicy().hasHeightForWidth())
        self.blurFeedButton.setSizePolicy(sizePolicy)
        self.blurFeedButton.setObjectName(_fromUtf8("blurFeedButton"))
        self.horizontalLayout_14.addWidget(self.blurFeedButton)
        self.mogFeedButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mogFeedButton.sizePolicy().hasHeightForWidth())
        self.mogFeedButton.setSizePolicy(sizePolicy)
        self.mogFeedButton.setObjectName(_fromUtf8("mogFeedButton"))
        self.horizontalLayout_14.addWidget(self.mogFeedButton)
        self.stackedFeedButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedFeedButton.sizePolicy().hasHeightForWidth())
        self.stackedFeedButton.setSizePolicy(sizePolicy)
        self.stackedFeedButton.setObjectName(_fromUtf8("stackedFeedButton"))
        self.horizontalLayout_14.addWidget(self.stackedFeedButton)
        self.videoFeedButtonLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.videoFeedButtonLayout.addLayout(self.horizontalLayout_12)
        self.gridLayout_2.addLayout(self.videoFeedButtonLayout, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.videoFeed = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoFeed.sizePolicy().hasHeightForWidth())
        self.videoFeed.setSizePolicy(sizePolicy)
        self.videoFeed.setObjectName(_fromUtf8("videoFeed"))
        self.gridLayout.addWidget(self.videoFeed, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabLayout = QtGui.QVBoxLayout()
        self.tabLayout.setObjectName(_fromUtf8("tabLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_colorspace = QtGui.QWidget()
        self.tab_colorspace.setObjectName(_fromUtf8("tab_colorspace"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_colorspace)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.colorspaceEnableCheckbox = QtGui.QCheckBox(self.tab_colorspace)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorspaceEnableCheckbox.sizePolicy().hasHeightForWidth())
        self.colorspaceEnableCheckbox.setSizePolicy(sizePolicy)
        self.colorspaceEnableCheckbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.colorspaceEnableCheckbox.setObjectName(_fromUtf8("colorspaceEnableCheckbox"))
        self.verticalLayout.addWidget(self.colorspaceEnableCheckbox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab_colorspace)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.redLowerSlider = QtGui.QSlider(self.tab_colorspace)
        self.redLowerSlider.setMaximum(255)
        self.redLowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redLowerSlider.setObjectName(_fromUtf8("redLowerSlider"))
        self.horizontalLayout.addWidget(self.redLowerSlider)
        self.redLowerValueLabel = QtGui.QLabel(self.tab_colorspace)
        self.redLowerValueLabel.setObjectName(_fromUtf8("redLowerValueLabel"))
        self.horizontalLayout.addWidget(self.redLowerValueLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.tab_colorspace)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.redUpperSlider = QtGui.QSlider(self.tab_colorspace)
        self.redUpperSlider.setMaximum(255)
        self.redUpperSlider.setSliderPosition(255)
        self.redUpperSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redUpperSlider.setObjectName(_fromUtf8("redUpperSlider"))
        self.horizontalLayout_2.addWidget(self.redUpperSlider)
        self.redUpperValueLabel = QtGui.QLabel(self.tab_colorspace)
        self.redUpperValueLabel.setObjectName(_fromUtf8("redUpperValueLabel"))
        self.horizontalLayout_2.addWidget(self.redUpperValueLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.tab_colorspace)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.greenLowerSlider = QtGui.QSlider(self.tab_colorspace)
        self.greenLowerSlider.setMaximum(255)
        self.greenLowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenLowerSlider.setObjectName(_fromUtf8("greenLowerSlider"))
        self.horizontalLayout_4.addWidget(self.greenLowerSlider)
        self.greenLowerValueLabel = QtGui.QLabel(self.tab_colorspace)
        self.greenLowerValueLabel.setObjectName(_fromUtf8("greenLowerValueLabel"))
        self.horizontalLayout_4.addWidget(self.greenLowerValueLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_8 = QtGui.QLabel(self.tab_colorspace)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_7.addWidget(self.label_8)
        self.greenUpperSlider = QtGui.QSlider(self.tab_colorspace)
        self.greenUpperSlider.setMaximum(255)
        self.greenUpperSlider.setSliderPosition(255)
        self.greenUpperSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenUpperSlider.setObjectName(_fromUtf8("greenUpperSlider"))
        self.horizontalLayout_7.addWidget(self.greenUpperSlider)
        self.greenUpperValueLabel = QtGui.QLabel(self.tab_colorspace)
        self.greenUpperValueLabel.setObjectName(_fromUtf8("greenUpperValueLabel"))
        self.horizontalLayout_7.addWidget(self.greenUpperValueLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_9 = QtGui.QLabel(self.tab_colorspace)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        self.blueLowerSlider = QtGui.QSlider(self.tab_colorspace)
        self.blueLowerSlider.setMaximum(255)
        self.blueLowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueLowerSlider.setObjectName(_fromUtf8("blueLowerSlider"))
        self.horizontalLayout_6.addWidget(self.blueLowerSlider)
        self.blueLowerValueLabel = QtGui.QLabel(self.tab_colorspace)
        self.blueLowerValueLabel.setObjectName(_fromUtf8("blueLowerValueLabel"))
        self.horizontalLayout_6.addWidget(self.blueLowerValueLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_10 = QtGui.QLabel(self.tab_colorspace)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_5.addWidget(self.label_10)
        self.blueUpperSlider = QtGui.QSlider(self.tab_colorspace)
        self.blueUpperSlider.setMaximum(255)
        self.blueUpperSlider.setSliderPosition(255)
        self.blueUpperSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueUpperSlider.setObjectName(_fromUtf8("blueUpperSlider"))
        self.horizontalLayout_5.addWidget(self.blueUpperSlider)
        self.blueUpperValueLabel = QtGui.QLabel(self.tab_colorspace)
        self.blueUpperValueLabel.setObjectName(_fromUtf8("blueUpperValueLabel"))
        self.horizontalLayout_5.addWidget(self.blueUpperValueLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_colorspace, _fromUtf8(""))
        self.tab_canny = QtGui.QWidget()
        self.tab_canny.setObjectName(_fromUtf8("tab_canny"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_canny)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.cannyEnableCheckbox = QtGui.QCheckBox(self.tab_canny)
        self.cannyEnableCheckbox.setObjectName(_fromUtf8("cannyEnableCheckbox"))
        self.verticalLayout_2.addWidget(self.cannyEnableCheckbox)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_3 = QtGui.QLabel(self.tab_canny)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_9.addWidget(self.label_3)
        self.cannyLowerSlider = QtGui.QSlider(self.tab_canny)
        self.cannyLowerSlider.setMaximum(2000)
        self.cannyLowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.cannyLowerSlider.setObjectName(_fromUtf8("cannyLowerSlider"))
        self.horizontalLayout_9.addWidget(self.cannyLowerSlider)
        self.cannyLowerValueLabel = QtGui.QLabel(self.tab_canny)
        self.cannyLowerValueLabel.setObjectName(_fromUtf8("cannyLowerValueLabel"))
        self.horizontalLayout_9.addWidget(self.cannyLowerValueLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_4 = QtGui.QLabel(self.tab_canny)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_8.addWidget(self.label_4)
        self.cannyUpperSlider = QtGui.QSlider(self.tab_canny)
        self.cannyUpperSlider.setMaximum(2000)
        self.cannyUpperSlider.setProperty("value", 2000)
        self.cannyUpperSlider.setOrientation(QtCore.Qt.Horizontal)
        self.cannyUpperSlider.setObjectName(_fromUtf8("cannyUpperSlider"))
        self.horizontalLayout_8.addWidget(self.cannyUpperSlider)
        self.cannyUpperValueLabel = QtGui.QLabel(self.tab_canny)
        self.cannyUpperValueLabel.setObjectName(_fromUtf8("cannyUpperValueLabel"))
        self.horizontalLayout_8.addWidget(self.cannyUpperValueLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_canny, _fromUtf8(""))
        self.tab_blur = QtGui.QWidget()
        self.tab_blur.setObjectName(_fromUtf8("tab_blur"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_blur)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.blurEnableCheckbox = QtGui.QCheckBox(self.tab_blur)
        self.blurEnableCheckbox.setObjectName(_fromUtf8("blurEnableCheckbox"))
        self.horizontalLayout_18.addWidget(self.blurEnableCheckbox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_13 = QtGui.QLabel(self.tab_blur)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_21.addWidget(self.label_13)
        self.blurWidthSlider = QtGui.QSlider(self.tab_blur)
        self.blurWidthSlider.setMinimum(1)
        self.blurWidthSlider.setMaximum(50)
        self.blurWidthSlider.setProperty("value", 1)
        self.blurWidthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blurWidthSlider.setObjectName(_fromUtf8("blurWidthSlider"))
        self.horizontalLayout_21.addWidget(self.blurWidthSlider)
        self.blurWidthValueLabel = QtGui.QLabel(self.tab_blur)
        self.blurWidthValueLabel.setObjectName(_fromUtf8("blurWidthValueLabel"))
        self.horizontalLayout_21.addWidget(self.blurWidthValueLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_14 = QtGui.QLabel(self.tab_blur)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_19.addWidget(self.label_14)
        self.blurHeightSlider = QtGui.QSlider(self.tab_blur)
        self.blurHeightSlider.setMinimum(1)
        self.blurHeightSlider.setMaximum(50)
        self.blurHeightSlider.setProperty("value", 1)
        self.blurHeightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blurHeightSlider.setObjectName(_fromUtf8("blurHeightSlider"))
        self.horizontalLayout_19.addWidget(self.blurHeightSlider)
        self.blurHeightValueLabel = QtGui.QLabel(self.tab_blur)
        self.blurHeightValueLabel.setObjectName(_fromUtf8("blurHeightValueLabel"))
        self.horizontalLayout_19.addWidget(self.blurHeightValueLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_19)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_blur, _fromUtf8(""))
        self.tab_contour = QtGui.QWidget()
        self.tab_contour.setObjectName(_fromUtf8("tab_contour"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_contour)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.contourEnableCheckbox = QtGui.QCheckBox(self.tab_contour)
        self.contourEnableCheckbox.setObjectName(_fromUtf8("contourEnableCheckbox"))
        self.verticalLayout_7.addWidget(self.contourEnableCheckbox)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_5 = QtGui.QLabel(self.tab_contour)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_20.addWidget(self.label_5)
        self.contourTargetCombo = QtGui.QComboBox(self.tab_contour)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contourTargetCombo.sizePolicy().hasHeightForWidth())
        self.contourTargetCombo.setSizePolicy(sizePolicy)
        self.contourTargetCombo.setObjectName(_fromUtf8("contourTargetCombo"))
        self.contourTargetCombo.addItem(_fromUtf8(""))
        self.contourTargetCombo.addItem(_fromUtf8(""))
        self.contourTargetCombo.addItem(_fromUtf8(""))
        self.contourTargetCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_20.addWidget(self.contourTargetCombo)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.contourDrawAllCheckbox = QtGui.QCheckBox(self.tab_contour)
        self.contourDrawAllCheckbox.setObjectName(_fromUtf8("contourDrawAllCheckbox"))
        self.verticalLayout_7.addWidget(self.contourDrawAllCheckbox)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.contourLargestAreaCheckbox = QtGui.QCheckBox(self.tab_contour)
        self.contourLargestAreaCheckbox.setObjectName(_fromUtf8("contourLargestAreaCheckbox"))
        self.horizontalLayout_23.addWidget(self.contourLargestAreaCheckbox)
        self.contourAreaComboBox = QtGui.QComboBox(self.tab_contour)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contourAreaComboBox.sizePolicy().hasHeightForWidth())
        self.contourAreaComboBox.setSizePolicy(sizePolicy)
        self.contourAreaComboBox.setObjectName(_fromUtf8("contourAreaComboBox"))
        self.contourAreaComboBox.addItem(_fromUtf8(""))
        self.contourAreaComboBox.addItem(_fromUtf8(""))
        self.contourAreaComboBox.addItem(_fromUtf8(""))
        self.contourAreaComboBox.addItem(_fromUtf8(""))
        self.contourAreaComboBox.addItem(_fromUtf8(""))
        self.contourAreaComboBox.addItem(_fromUtf8(""))
        self.contourAreaComboBox.addItem(_fromUtf8(""))
        self.contourAreaComboBox.addItem(_fromUtf8(""))
        self.contourAreaComboBox.addItem(_fromUtf8(""))
        self.contourAreaComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_23.addWidget(self.contourAreaComboBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_6 = QtGui.QLabel(self.tab_contour)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_22.addWidget(self.label_6)
        self.contourDrawFramecombo = QtGui.QComboBox(self.tab_contour)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contourDrawFramecombo.sizePolicy().hasHeightForWidth())
        self.contourDrawFramecombo.setSizePolicy(sizePolicy)
        self.contourDrawFramecombo.setObjectName(_fromUtf8("contourDrawFramecombo"))
        self.contourDrawFramecombo.addItem(_fromUtf8(""))
        self.contourDrawFramecombo.addItem(_fromUtf8(""))
        self.horizontalLayout_22.addWidget(self.contourDrawFramecombo)
        self.verticalLayout_7.addLayout(self.horizontalLayout_22)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_contour, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.keypointEnableCheckbox = QtGui.QCheckBox(self.tab)
        self.keypointEnableCheckbox.setObjectName(_fromUtf8("keypointEnableCheckbox"))
        self.verticalLayout_9.addWidget(self.keypointEnableCheckbox)
        self.keypointFileLabel = QtGui.QLabel(self.tab)
        self.keypointFileLabel.setObjectName(_fromUtf8("keypointFileLabel"))
        self.verticalLayout_9.addWidget(self.keypointFileLabel)
        self.keypointFileSelect = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keypointFileSelect.sizePolicy().hasHeightForWidth())
        self.keypointFileSelect.setSizePolicy(sizePolicy)
        self.keypointFileSelect.setObjectName(_fromUtf8("keypointFileSelect"))
        self.verticalLayout_9.addWidget(self.keypointFileSelect)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.keypointAlgCombo = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keypointAlgCombo.sizePolicy().hasHeightForWidth())
        self.keypointAlgCombo.setSizePolicy(sizePolicy)
        self.keypointAlgCombo.setObjectName(_fromUtf8("keypointAlgCombo"))
        self.keypointAlgCombo.addItem(_fromUtf8(""))
        self.keypointAlgCombo.addItem(_fromUtf8(""))
        self.keypointAlgCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.keypointAlgCombo)
        self.keypointSubmitButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keypointSubmitButton.sizePolicy().hasHeightForWidth())
        self.keypointSubmitButton.setSizePolicy(sizePolicy)
        self.keypointSubmitButton.setObjectName(_fromUtf8("keypointSubmitButton"))
        self.horizontalLayout_10.addWidget(self.keypointSubmitButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_stacked = QtGui.QWidget()
        self.tab_stacked.setObjectName(_fromUtf8("tab_stacked"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.tab_stacked)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_11 = QtGui.QLabel(self.tab_stacked)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_16.addWidget(self.label_11)
        self.colorspace_combo = QtGui.QComboBox(self.tab_stacked)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorspace_combo.sizePolicy().hasHeightForWidth())
        self.colorspace_combo.setSizePolicy(sizePolicy)
        self.colorspace_combo.setObjectName(_fromUtf8("colorspace_combo"))
        self.colorspace_combo.addItem(_fromUtf8(""))
        self.colorspace_combo.addItem(_fromUtf8(""))
        self.colorspace_combo.addItem(_fromUtf8(""))
        self.colorspace_combo.addItem(_fromUtf8(""))
        self.horizontalLayout_16.addWidget(self.colorspace_combo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_12 = QtGui.QLabel(self.tab_stacked)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_17.addWidget(self.label_12)
        self.canny_combo = QtGui.QComboBox(self.tab_stacked)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canny_combo.sizePolicy().hasHeightForWidth())
        self.canny_combo.setSizePolicy(sizePolicy)
        self.canny_combo.setObjectName(_fromUtf8("canny_combo"))
        self.canny_combo.addItem(_fromUtf8(""))
        self.canny_combo.addItem(_fromUtf8(""))
        self.canny_combo.addItem(_fromUtf8(""))
        self.canny_combo.addItem(_fromUtf8(""))
        self.horizontalLayout_17.addWidget(self.canny_combo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.label_15 = QtGui.QLabel(self.tab_stacked)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_24.addWidget(self.label_15)
        self.blur_combo = QtGui.QComboBox(self.tab_stacked)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blur_combo.sizePolicy().hasHeightForWidth())
        self.blur_combo.setSizePolicy(sizePolicy)
        self.blur_combo.setObjectName(_fromUtf8("blur_combo"))
        self.blur_combo.addItem(_fromUtf8(""))
        self.blur_combo.addItem(_fromUtf8(""))
        self.blur_combo.addItem(_fromUtf8(""))
        self.blur_combo.addItem(_fromUtf8(""))
        self.horizontalLayout_24.addWidget(self.blur_combo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_24)
        self.stackedSubmitButton = QtGui.QPushButton(self.tab_stacked)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedSubmitButton.sizePolicy().hasHeightForWidth())
        self.stackedSubmitButton.setSizePolicy(sizePolicy)
        self.stackedSubmitButton.setObjectName(_fromUtf8("stackedSubmitButton"))
        self.verticalLayout_4.addWidget(self.stackedSubmitButton)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_15.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_stacked, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.mogEnableCheckbox = QtGui.QCheckBox(self.tab_2)
        self.mogEnableCheckbox.setObjectName(_fromUtf8("mogEnableCheckbox"))
        self.verticalLayout_10.addWidget(self.mogEnableCheckbox)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.label_16 = QtGui.QLabel(self.tab_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_25.addWidget(self.label_16)
        self.mogComboBox = QtGui.QComboBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mogComboBox.sizePolicy().hasHeightForWidth())
        self.mogComboBox.setSizePolicy(sizePolicy)
        self.mogComboBox.setObjectName(_fromUtf8("mogComboBox"))
        self.mogComboBox.addItem(_fromUtf8(""))
        self.mogComboBox.addItem(_fromUtf8(""))
        self.mogComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_25.addWidget(self.mogComboBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_25)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.cascadeEnableCheckbox = QtGui.QCheckBox(self.tab_3)
        self.cascadeEnableCheckbox.setObjectName(_fromUtf8("cascadeEnableCheckbox"))
        self.horizontalLayout_26.addWidget(self.cascadeEnableCheckbox)
        self.verticalLayout_12.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.cascadeFileLabel = QtGui.QLabel(self.tab_3)
        self.cascadeFileLabel.setObjectName(_fromUtf8("cascadeFileLabel"))
        self.horizontalLayout_28.addWidget(self.cascadeFileLabel)
        self.cascadeOpenFile = QtGui.QPushButton(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cascadeOpenFile.sizePolicy().hasHeightForWidth())
        self.cascadeOpenFile.setSizePolicy(sizePolicy)
        self.cascadeOpenFile.setObjectName(_fromUtf8("cascadeOpenFile"))
        self.horizontalLayout_28.addWidget(self.cascadeOpenFile)
        self.verticalLayout_12.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_30.addWidget(self.label_19)
        self.cascadeResolutionCombo = QtGui.QComboBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cascadeResolutionCombo.sizePolicy().hasHeightForWidth())
        self.cascadeResolutionCombo.setSizePolicy(sizePolicy)
        self.cascadeResolutionCombo.setObjectName(_fromUtf8("cascadeResolutionCombo"))
        self.cascadeResolutionCombo.addItem(_fromUtf8(""))
        self.cascadeResolutionCombo.addItem(_fromUtf8(""))
        self.cascadeResolutionCombo.addItem(_fromUtf8(""))
        self.cascadeResolutionCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_30.addWidget(self.cascadeResolutionCombo)
        self.cascadeResolutionSubmit = QtGui.QPushButton(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cascadeResolutionSubmit.sizePolicy().hasHeightForWidth())
        self.cascadeResolutionSubmit.setSizePolicy(sizePolicy)
        self.cascadeResolutionSubmit.setObjectName(_fromUtf8("cascadeResolutionSubmit"))
        self.horizontalLayout_30.addWidget(self.cascadeResolutionSubmit)
        self.verticalLayout_12.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_31.addWidget(self.label_18)
        self.cascadeSaveNameLabel = QtGui.QLineEdit(self.tab_3)
        self.cascadeSaveNameLabel.setText(_fromUtf8(""))
        self.cascadeSaveNameLabel.setObjectName(_fromUtf8("cascadeSaveNameLabel"))
        self.horizontalLayout_31.addWidget(self.cascadeSaveNameLabel)
        self.cascadeSaveButton = QtGui.QPushButton(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cascadeSaveButton.sizePolicy().hasHeightForWidth())
        self.cascadeSaveButton.setSizePolicy(sizePolicy)
        self.cascadeSaveButton.setObjectName(_fromUtf8("cascadeSaveButton"))
        self.horizontalLayout_31.addWidget(self.cascadeSaveButton)
        self.verticalLayout_12.addLayout(self.horizontalLayout_31)
        self.cascadeIdentifyFacesCheckbox = QtGui.QCheckBox(self.tab_3)
        self.cascadeIdentifyFacesCheckbox.setObjectName(_fromUtf8("cascadeIdentifyFacesCheckbox"))
        self.verticalLayout_12.addWidget(self.cascadeIdentifyFacesCheckbox)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem6)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_17 = QtGui.QLabel(self.tab_4)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_14.addWidget(self.label_17)
        self.facesListView = QtGui.QListView(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.facesListView.sizePolicy().hasHeightForWidth())
        self.facesListView.setSizePolicy(sizePolicy)
        self.facesListView.setObjectName(_fromUtf8("facesListView"))
        self.verticalLayout_14.addWidget(self.facesListView)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem7)
        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tabLayout.addWidget(self.tabWidget)
        self.gridLayout_2.addLayout(self.tabLayout, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.defaultFeedButton.setText(_translate("MainWindow", "Show Default", None))
        self.colorFeedButton.setText(_translate("MainWindow", "Show Colorspace", None))
        self.cannyFeedButton.setText(_translate("MainWindow", "Show Canny", None))
        self.blurFeedButton.setText(_translate("MainWindow", "Blur", None))
        self.mogFeedButton.setText(_translate("MainWindow", "MOG", None))
        self.stackedFeedButton.setText(_translate("MainWindow", "Stacked Effect", None))
        self.videoFeed.setText(_translate("MainWindow", "Video Feed", None))
        self.colorspaceEnableCheckbox.setText(_translate("MainWindow", "Enable", None))
        self.label.setText(_translate("MainWindow", "Red Lower", None))
        self.redLowerValueLabel.setText(_translate("MainWindow", "0", None))
        self.label_2.setText(_translate("MainWindow", "Red Upper", None))
        self.redUpperValueLabel.setText(_translate("MainWindow", "255", None))
        self.label_7.setText(_translate("MainWindow", "Green Lower", None))
        self.greenLowerValueLabel.setText(_translate("MainWindow", "0", None))
        self.label_8.setText(_translate("MainWindow", "Green Upper", None))
        self.greenUpperValueLabel.setText(_translate("MainWindow", "255", None))
        self.label_9.setText(_translate("MainWindow", "Blue Lower", None))
        self.blueLowerValueLabel.setText(_translate("MainWindow", "0", None))
        self.label_10.setText(_translate("MainWindow", "Blue Upper", None))
        self.blueUpperValueLabel.setText(_translate("MainWindow", "255", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_colorspace), _translate("MainWindow", "Colorspace", None))
        self.cannyEnableCheckbox.setText(_translate("MainWindow", "Enable", None))
        self.label_3.setText(_translate("MainWindow", "Lower", None))
        self.cannyLowerValueLabel.setText(_translate("MainWindow", "0", None))
        self.label_4.setText(_translate("MainWindow", "Upper", None))
        self.cannyUpperValueLabel.setText(_translate("MainWindow", "2000", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_canny), _translate("MainWindow", "Canny", None))
        self.blurEnableCheckbox.setText(_translate("MainWindow", "Enable", None))
        self.label_13.setText(_translate("MainWindow", "Kernel Width (X)", None))
        self.blurWidthValueLabel.setText(_translate("MainWindow", "1", None))
        self.label_14.setText(_translate("MainWindow", "Kernel Height (Y)", None))
        self.blurHeightValueLabel.setText(_translate("MainWindow", "1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_blur), _translate("MainWindow", "Blur", None))
        self.contourEnableCheckbox.setText(_translate("MainWindow", "Enable", None))
        self.label_5.setText(_translate("MainWindow", "Frame", None))
        self.contourTargetCombo.setItemText(0, _translate("MainWindow", "Colorspace", None))
        self.contourTargetCombo.setItemText(1, _translate("MainWindow", "Canny", None))
        self.contourTargetCombo.setItemText(2, _translate("MainWindow", "Blur", None))
        self.contourTargetCombo.setItemText(3, _translate("MainWindow", "Stacked", None))
        self.contourDrawAllCheckbox.setText(_translate("MainWindow", "Draw all contours", None))
        self.contourLargestAreaCheckbox.setText(_translate("MainWindow", "Draw contour with largest area", None))
        self.contourAreaComboBox.setItemText(0, _translate("MainWindow", "1", None))
        self.contourAreaComboBox.setItemText(1, _translate("MainWindow", "2", None))
        self.contourAreaComboBox.setItemText(2, _translate("MainWindow", "3", None))
        self.contourAreaComboBox.setItemText(3, _translate("MainWindow", "4", None))
        self.contourAreaComboBox.setItemText(4, _translate("MainWindow", "5", None))
        self.contourAreaComboBox.setItemText(5, _translate("MainWindow", "6", None))
        self.contourAreaComboBox.setItemText(6, _translate("MainWindow", "7", None))
        self.contourAreaComboBox.setItemText(7, _translate("MainWindow", "8", None))
        self.contourAreaComboBox.setItemText(8, _translate("MainWindow", "9", None))
        self.contourAreaComboBox.setItemText(9, _translate("MainWindow", "10", None))
        self.label_6.setText(_translate("MainWindow", "Draw on frame", None))
        self.contourDrawFramecombo.setItemText(0, _translate("MainWindow", "Default", None))
        self.contourDrawFramecombo.setItemText(1, _translate("MainWindow", "Selected", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_contour), _translate("MainWindow", "Contour", None))
        self.keypointEnableCheckbox.setText(_translate("MainWindow", "Enable", None))
        self.keypointFileLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.keypointFileSelect.setText(_translate("MainWindow", "Open File", None))
        self.keypointAlgCombo.setItemText(0, _translate("MainWindow", "Surf", None))
        self.keypointAlgCombo.setItemText(1, _translate("MainWindow", "Sift", None))
        self.keypointAlgCombo.setItemText(2, _translate("MainWindow", "Orb", None))
        self.keypointSubmitButton.setText(_translate("MainWindow", "Submit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Keypoint", None))
        self.label_11.setText(_translate("MainWindow", "Colorspace", None))
        self.colorspace_combo.setItemText(0, _translate("MainWindow", "0", None))
        self.colorspace_combo.setItemText(1, _translate("MainWindow", "1", None))
        self.colorspace_combo.setItemText(2, _translate("MainWindow", "2", None))
        self.colorspace_combo.setItemText(3, _translate("MainWindow", "3", None))
        self.label_12.setText(_translate("MainWindow", "Canny", None))
        self.canny_combo.setItemText(0, _translate("MainWindow", "0", None))
        self.canny_combo.setItemText(1, _translate("MainWindow", "1", None))
        self.canny_combo.setItemText(2, _translate("MainWindow", "2", None))
        self.canny_combo.setItemText(3, _translate("MainWindow", "3", None))
        self.label_15.setText(_translate("MainWindow", "Blur", None))
        self.blur_combo.setItemText(0, _translate("MainWindow", "0", None))
        self.blur_combo.setItemText(1, _translate("MainWindow", "1", None))
        self.blur_combo.setItemText(2, _translate("MainWindow", "2", None))
        self.blur_combo.setItemText(3, _translate("MainWindow", "3", None))
        self.stackedSubmitButton.setText(_translate("MainWindow", "Submit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stacked), _translate("MainWindow", "Stacked Effect", None))
        self.mogEnableCheckbox.setText(_translate("MainWindow", "Enable", None))
        self.label_16.setText(_translate("MainWindow", "Algorithm", None))
        self.mogComboBox.setItemText(0, _translate("MainWindow", "MOG", None))
        self.mogComboBox.setItemText(1, _translate("MainWindow", "MOG2", None))
        self.mogComboBox.setItemText(2, _translate("MainWindow", "GMG", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "MOG Reduction", None))
        self.cascadeEnableCheckbox.setText(_translate("MainWindow", "Enable", None))
        self.cascadeFileLabel.setText(_translate("MainWindow", "File Path", None))
        self.cascadeOpenFile.setText(_translate("MainWindow", "Open File", None))
        self.label_19.setText(_translate("MainWindow", "Use this if you have a old GPU", None))
        self.cascadeResolutionCombo.setItemText(0, _translate("MainWindow", "640x480 (Default)", None))
        self.cascadeResolutionCombo.setItemText(1, _translate("MainWindow", "320x240", None))
        self.cascadeResolutionCombo.setItemText(2, _translate("MainWindow", "240x180", None))
        self.cascadeResolutionCombo.setItemText(3, _translate("MainWindow", "160x120", None))
        self.cascadeResolutionSubmit.setText(_translate("MainWindow", "Submit", None))
        self.label_18.setText(_translate("MainWindow", "File name:", None))
        self.cascadeSaveButton.setText(_translate("MainWindow", "Save Current Frame", None))
        self.cascadeIdentifyFacesCheckbox.setText(_translate("MainWindow", "Identify Faces", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Cascade", None))
        self.label_17.setText(_translate("MainWindow", "Faces", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Resources", None))

import sys
from matplotlib import pyplot as plt
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

cap = cv2.VideoCapture(0)
lastClicked = "defult"
res = None
edges = None
blur = None
keypoint_img = None
frame = None
stacked_frame = None
MOG = None
cascade_file = None
saveCascadeROI = False
cascade_resolutionX = 0
cascade_resolutionY = 0
fgbg_mog = cv2.BackgroundSubtractorMOG()
fgbg_mog2 = cv2.BackgroundSubtractorMOG2()
colorspace_stacked_order = 0
canny_stacked_order = 1
blur_stacked_order = 2


def stacked_submit():
    global colorspace_stacked_order
    global canny_stacked_order
    global blur_stacked_order
    colorspace_stacked_order = int(ui.colorspace_combo.currentText())
    canny_stacked_order = int(ui.canny_combo.currentText())
    blur_stacked_order = int(ui.blur_combo.currentText())


def getFrameToDisplay():
    image = None
    if "defult" in lastClicked:
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QtGui.QImage.Format_RGB888)
    elif "colorspace" in lastClicked:
        image = QtGui.QImage(res, res.shape[1], res.shape[0], res.shape[1] * 3, QtGui.QImage.Format_RGB888)
    elif "canny" in lastClicked:
        global edges
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        image = QtGui.QImage(edges, edges.shape[1], edges.shape[0], edges.shape[1] * 3, QtGui.QImage.Format_RGB888)
    elif "blur" in lastClicked:
        image = QtGui.QImage(blur, blur.shape[1], blur.shape[0], blur.shape[1] * 3, QtGui.QImage.Format_RGB888)
    elif "mog" in lastClicked:
        global MOG
        MOG = cv2.cvtColor(MOG, cv2.COLOR_GRAY2BGR)
        image = QtGui.QImage(MOG, MOG.shape[1], MOG.shape[0], MOG.shape[1] * 3, QtGui.QImage.Format_RGB888)
    elif "stack" in lastClicked:
        filter_array = [colorspace_stacked_order, canny_stacked_order, blur_stacked_order]
        action_array = ["colorspace", "canny", "blur"]
        find_num = 1
        stacked_frame = frame.copy()
        filter_array_length = len(filter_array)
        for x in range(len(filter_array)):
            if filter_array[x] == 0:
                filter_array_length -= 1

        while find_num <= filter_array_length:
            for x in range(len(filter_array)):
                if filter_array[x] == find_num:
                    if action_array[x] is "colorspace":
                        stacked_frame = return_color_alg(stacked_frame)
                    elif action_array[x] is "canny":
                        stacked_frame = return_canny_alg(stacked_frame)
                    elif action_array[x] is "blur":
                        stacked_frame = return_blur_alg(stacked_frame)
                    find_num += 1
        image = QtGui.QImage(stacked_frame, stacked_frame.shape[1], stacked_frame.shape[0], stacked_frame.shape[1] * 3, QtGui.QImage.Format_RGB888)
    return image


def defult_setFeed():
    global lastClicked
    lastClicked = "defult"


def colorspace_setFeed():
    global lastClicked
    if ui.colorspaceEnableCheckbox.isChecked() is True:
        lastClicked = "colorspace"


def stacked_setFeed():
    global lastClicked
    lastClicked = "stack"


def canny_setFeed():
    global lastClicked
    if ui.cannyEnableCheckbox.isChecked() is True:
        lastClicked = "canny"

def blur_setFeed():
    global lastClicked
    if ui.blurEnableCheckbox.isChecked() is True:
        lastClicked = "blur"

def mog_setFeed():
    global lastClicked
    if ui.mogEnableCheckbox.isChecked() is True:
        lastClicked = "mog"


def color_alg(rL, rU, gL, gU, bL, bU, frame_func):
    hsv = cv2.cvtColor(frame_func, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([rL, gL, bL])
    upper_blue = np.array([rU, gU, bU])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    global res
    res = cv2.bitwise_and(frame_func, frame_func, mask=mask)


def return_color_alg(frame_local):
    rL = ui.redLowerSlider.value()
    rU = ui.redUpperSlider.value()
    gL = ui.greenLowerSlider.value()
    gU = ui.greenUpperSlider.value()
    bL = ui.blueLowerSlider.value()
    bU = ui.blueUpperSlider.value()
    hsv = cv2.cvtColor(frame_local, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([rL, gL, bL])
    upper_blue = np.array([rU, gU, bU])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res_local = cv2.bitwise_and(frame_local, frame_local, mask=mask)
    return res_local


def canny_alg(cMin, cMax, frame_func):
    global edges
    edges = cv2.Canny(frame_func.copy(), cMin, cMax)


def return_canny_alg(frame_local):
    cMin = ui.cannyLowerSlider.value()
    cMax = ui.cannyUpperSlider.value()
    edges_local = cv2.Canny(frame_local.copy(), cMin, cMax)
    edges_local = cv2.cvtColor(edges_local, cv2.COLOR_GRAY2BGR)
    return edges_local


def blur_alg(width, height, frame_func):
    global blur
    blur = cv2.blur(frame_func.copy(), (width, height))


def return_blur_alg(frame_local):
    width = ui.blurWidthSlider.value()
    height = ui.blurHeightSlider.value()
    blur_local = cv2.blur(frame_local, (width, height))
    return blur_local


def keypoint_alg(frame_local):
    alg = str(ui.keypointAlgCombo.currentText())
    print alg
    # keypoint_img is the image that the object is saved to
    if alg is "Surf":
        print ""
    elif "Sift" in alg:
        sift = cv2.SIFT()
        kp1, des1 = sift.detectAndCompute(frame_local.copy(), None)
        kp2, des2 = sift.detectAndCompute(keypoint_img, None)
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])
        img3 = cv2.drawMatchesKnn(frame_local.copy(), kp1, keypoint_img, kp2, good, flags=2)
        plt.imshow(img3), plt.show()
    elif alg is "Orb":
        print ""


def colorspace_enabled(feed):
    rL = ui.redLowerSlider.value()
    rU = ui.redUpperSlider.value()
    gL = ui.greenLowerSlider.value()
    gU = ui.greenUpperSlider.value()
    bL = ui.blueLowerSlider.value()
    bU = ui.blueUpperSlider.value()
    
    ui.redLowerValueLabel.setText(str(rL))
    ui.redUpperValueLabel.setText(str(rU))
    ui.greenLowerValueLabel.setText(str(gL))
    ui.greenUpperValueLabel.setText(str(gU))
    ui.blueLowerValueLabel.setText(str(bL))
    ui.blueUpperValueLabel.setText(str(bU))
    if ui.colorspaceEnableCheckbox.isChecked() is True:
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # lower_blue = np.array([rL, gL, bL])
        # upper_blue = np.array([rU, gU, bU])
        # mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # global res
        # res = cv2.bitwise_and(frame, frame, mask=mask)
        color_alg(rL, rU, gL, gU, bL, bU, frame)


def canny_enabled():
    cMin = ui.cannyLowerSlider.value()
    cMax = ui.cannyUpperSlider.value()

    ui.cannyLowerValueLabel.setText(str(cMin))
    ui.cannyUpperValueLabel.setText(str(cMax))
    if ui.cannyEnableCheckbox.isChecked() is True:
        # global edges
        # edges = cv2.Canny(frame.copy(), cMin, cMax)
        canny_alg(cMin, cMax, frame)


def blur_enabled():
    width = ui.blurWidthSlider.value()
    height = ui.blurHeightSlider.value()

    ui.blurWidthValueLabel.setText(str(width))
    ui.blurHeightValueLabel.setText(str(height))
    if ui.blurEnableCheckbox.isChecked() is True:
        blur_alg(width, height, frame)


def keypoint_enabled():
    if ui.keypointEnableCheckbox.isChecked() is True:
        keypoint_alg(frame)


def mog_enabled():
    if ui.mogEnableCheckbox.isChecked() is True:
        alg = ui.mogComboBox.currentText()
        global MOG
        if "MOG" in alg:
            MOG = fgbg_mog.apply(frame)
        elif "MOG2" in alg:
            MOG = fgbg_mog2.apply(frame)
        elif "GMG" in alg:
            print ""


def cascade_enabled():
    if ui.cascadeEnableCheckbox.isChecked() is True:
        global saveCascadeROI
        cascadeOne = cv2.CascadeClassifier(cascade_file)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascadeOne.detectMultiScale(gray, 1.05, 5)
        #TODO Fix lag
        for (x, y, w, h) in faces:
            roi = frame[y:y + h, x:x + w]
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
            if saveCascadeROI is True:
                file_name = 'face/' + str(ui.cascadeSaveNameLabel.text()) + ".jpg"
                cv2.imwrite(file_name, roi)
                cv2.imshow('savedImage', roi)
                saveCascadeROI = False
            file_index = []
            similarity_num = []
            if ui.cascadeIdentifyFacesCheckbox.isChecked() is True:
                hist_roi = cv2.calcHist([roi], [0], None, [256], [0, 256])
                for i in face_files:
                    saved_image = cv2.imread(i, 0)
                    hist_i = cv2.calcHist([saved_image], [0], None, [256], [0, 256])
                    d = cv2.compareHist(hist_roi, hist_i, cv2.cv.CV_COMP_BHATTACHARYYA)
                    #print str(i) + " : " + str(d)
                    #print "-"*100
                    file_index.append(i)
                    similarity_num.append(d)
                closest_match_index = similarity_num.index(min(similarity_num))
                cv2.putText(frame, file_index[closest_match_index].replace("face/", ""), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


def contour_enabled():
    global edges
    global res
    global blur
    if ui.contourEnableCheckbox.isChecked() is True:
        target_frame = str(ui.contourTargetCombo.currentText())
        # ret, thresh = cv2.threshold(edges, 127, 255, 0)
        # contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame, contours, -1, (255, 0, 0), 3)
        image = None
        if "Colorspace" in target_frame:
            res_bw = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(res_bw, 127, 255, 0)
            # image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            #TODO Thresh or Res?
            contours, hierarchy = cv2.findContours(res_bw.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            draw_contours(res, contours, hierarchy, res)
        elif "Canny" in target_frame:
            ret, thresh = cv2.threshold(edges, 127, 255, 0)
            # image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            draw_contours(edges, contours, hierarchy, edges)
        elif "Blur" in target_frame:
            blur_bw = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(blur_bw, 127, 255, 0)
            # image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            draw_contours(blur, contours, hierarchy, blur)
        elif "Stacked" in target_frame:
            print "TODO"


def draw_contours(image, contours, hierarchy, targetFrame):
    draw_frame = str(ui.contourDrawFramecombo.currentText())
    frame_draw = None
    if "Default" in draw_frame:
        frame_draw = frame
    elif "Selected" in draw_frame:
        target_frame = str(ui.contourTargetCombo.currentText())
        if "Colorspace" in target_frame:
            frame_draw = res
        elif "Canny" in target_frame:
            frame_draw = edges
        elif "Blur" in target_frame:
            frame_draw = blur
        elif "Stacked" in target_frame:
            frame_draw = stacked_frame
    if ui.contourDrawAllCheckbox.isChecked() is True:
        cv2.drawContours(frame_draw, contours, -1, (255, 0, 0), 3)
    elif ui.contourLargestAreaCheckbox.isChecked() is True:
        try:
            areas = [cv2.contourArea(c) for c in contours]
            area_draw_number = int(ui.contourAreaComboBox.currentText())
            max_index_array = []

            for x in range(0, area_draw_number):
                max_index = np.argmax(areas)
                max_index_array.append(max_index)
                cv2.drawContours(frame_draw, contours, max_index, (255, 0, 0), 3)
                del areas[max_index]
            print max_index_array
            print len(contours)

            # sort_area = np.sort(areas)
            # sort_area = sort_area.argsort()[::-1]

            #cnt = contours[max_index]
            cv2.drawContours(frame_draw, contours, max_index, (255, 0, 0), 3)
            # cnt = sort_area[area_draw_number]
            # cv2.drawContours(frame_draw, [cnt], 0, (255, 0, 0), 3)

        except ValueError:
            print "Draw all contours: ValueError"
ui.colorFeedButton.clicked.connect(colorspace_setFeed)
ui.defaultFeedButton.clicked.connect(defult_setFeed)
ui.cannyFeedButton.clicked.connect(canny_setFeed)
ui.blurFeedButton.clicked.connect(blur_setFeed)
ui.stackedFeedButton.clicked.connect(stacked_setFeed)
ui.mogFeedButton.clicked.connect(mog_setFeed)
ui.stackedSubmitButton.clicked.connect(stacked_submit)


def select_file():
    global keypoint_img
    file_path = str(QtGui.QFileDialog.getOpenFileName())
    ui.keypointFileLabel.setText(file_path)
    keypoint_img = cv2.imread(file_path)


def select_cascade():
    global cascade_file
    file_path = str(QtGui.QFileDialog.getOpenFileName())
    ui.cascadeFileLabel.setText(file_path)
    cascade_file = file_path


def cascade_getResolution():
    global cascade_resolutionX, cascade_resolutionY
    res_selection = ui.cascadeResolutionCombo.currentText()
    if "640x480" in res_selection:
        cascade_resolutionX = 640
        cascade_resolutionY = 480
    elif "320x240" in res_selection:
        cascade_resolutionX = 320
        cascade_resolutionY = 240
    elif "240x180" in res_selection:
        cascade_resolutionX = 240
        cascade_resolutionY = 180
    elif "160x120" in res_selection:
        cascade_resolutionX = 160
        cascade_resolutionY = 120
    cap.set(3, cascade_resolutionX)
    cap.set(4, cascade_resolutionY)
    cap.set(5, 30)


def cascade_saveFile():
    global saveCascadeROI
    saveCascadeROI = True

ui.keypointFileSelect.clicked.connect(select_file)
ui.cascadeOpenFile.clicked.connect(select_cascade)
ui.cascadeResolutionSubmit.clicked.connect(cascade_getResolution)
ui.cascadeSaveButton.clicked.connect(cascade_saveFile)


def errorhandler_functions():
    # errorhandler_stacked_dupe()
    x = 0


def errorhandler_stacked_dupe():
    colorspace_stacked_order_l = int(ui.colorspace_combo.currentText())
    canny_stacked_order_l = int(ui.canny_combo.currentText())
    blur_stacked_order_l = int(ui.blur_combo.currentText())
    order_array = [colorspace_stacked_order_l, canny_stacked_order_l, blur_stacked_order_l]
    ui.stackedSubmitButton.setEnabled(True)
    for x in range(len(order_array)-1):
        for y in range(x+1, len(order_array)):
            if (order_array[x] == order_array[y]) and (order_array[x] != 0 and order_array[y] != 0):
                ui.stackedSubmitButton.setEnabled(False)

ui.colorspace_combo.connect(ui.colorspace_combo, QtCore.SIGNAL("currentIndexChanged(int)"), errorhandler_stacked_dupe)
ui.canny_combo.connect(ui.canny_combo, QtCore.SIGNAL("currentIndexChanged(int)"), errorhandler_stacked_dupe)
ui.blur_combo.connect(ui.blur_combo, QtCore.SIGNAL("currentIndexChanged(int)"), errorhandler_stacked_dupe)

face_files = []
for i in os.listdir('face/'):
    face_files.append('face/' + i)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    colorspace_enabled(frame)
    canny_enabled()
    blur_enabled()
    keypoint_enabled()
    contour_enabled()
    mog_enabled()
    cascade_enabled()
    #errorhandler_functions()

    pix = QtGui.QPixmap(getFrameToDisplay())
    pix = pix.scaled(332, 218)
    ui.videoFeed.setPixmap(pix)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
sys.exit(app.exec_())
