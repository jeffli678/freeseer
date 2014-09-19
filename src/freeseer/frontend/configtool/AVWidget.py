#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
freeseer - vga/presentation capture software

Copyright (C) 2011  Free and Open Source Software Learning Centre
http://fosslc.org

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

For support, questions, suggestions or any other inquiries, visit:
http://wiki.github.com/Freeseer/freeseer/

@author: Thanh Ha
'''

from PyQt4 import QtCore
from PyQt4 import QtGui


class AVWidget(QtGui.QWidget):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtGui.QWidget.__init__(self, parent)

        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addStretch(0)
        self.setLayout(self.mainLayout)

        config_icon = QtGui.QIcon.fromTheme("preferences-system")

        self.fontSize = self.font().pixelSize()
        self.fontUnit = "px"
        if self.fontSize == -1:  # Font is set as points, not pixels.
            self.fontUnit = "pt"
            self.fontSize = self.font().pointSize()

        self.boxStyle = "QGroupBox {{ font-weight: bold; font-size: {}{} }}".format(self.fontSize + 1, self.fontUnit)
        self.BOX_WIDTH = 400
        self.BOX_HEIGHT = 60

        #
        # Audio Input
        #

        self.audioLayout = QtGui.QGridLayout()
        self.audioGroupBox = QtGui.QGroupBox("Audio Input")
        self.audioGroupBox.setLayout(self.audioLayout)
        self.mainLayout.insertWidget(0, self.audioGroupBox)

        self.audioGroupBox.setCheckable(True)
        self.audioGroupBox.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.audioGroupBox.setFixedSize(self.BOX_WIDTH, self.BOX_HEIGHT)
        self.audioGroupBox.setStyleSheet(self.boxStyle)

        self.audioMixerLabel = QtGui.QLabel("Audio Mixer")
        self.audioMixerLabel.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.audioMixerComboBox = QtGui.QComboBox()
        self.audioMixerLabel.setBuddy(self.audioMixerComboBox)
        self.audioMixerSetupPushButton = QtGui.QToolButton()
        self.audioMixerSetupPushButton.setText("Setup")
        self.audioMixerSetupPushButton.setIcon(config_icon)
        self.audioMixerSetupPushButton.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.audioMixerSetupPushButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.audioLayout.addWidget(self.audioMixerLabel, 0, 0)
        self.audioLayout.addWidget(self.audioMixerComboBox, 0, 1)
        self.audioLayout.addWidget(self.audioMixerSetupPushButton, 0, 2)

        #
        # Video Input
        #

        self.videoLayout = QtGui.QGridLayout()
        self.videoGroupBox = QtGui.QGroupBox("Video Input")
        self.videoGroupBox.setLayout(self.videoLayout)
        self.mainLayout.insertWidget(0, self.videoGroupBox)

        self.videoGroupBox.setCheckable(True)
        self.videoGroupBox.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.videoGroupBox.setFixedSize(self.BOX_WIDTH, self.BOX_HEIGHT)
        self.videoGroupBox.setStyleSheet(self.boxStyle)

        self.videoMixerLabel = QtGui.QLabel("Video Mixer")
        self.videoMixerLabel.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.videoMixerComboBox = QtGui.QComboBox()
        self.videoMixerLabel.setBuddy(self.videoMixerComboBox)
        self.videoMixerSetupPushButton = QtGui.QToolButton()
        self.videoMixerSetupPushButton.setText("Setup")
        self.videoMixerSetupPushButton.setIcon(config_icon)
        self.videoMixerSetupPushButton.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.videoMixerSetupPushButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.videoLayout.addWidget(self.videoMixerLabel, 0, 0)
        self.videoLayout.addWidget(self.videoMixerComboBox, 0, 1)
        self.videoLayout.addWidget(self.videoMixerSetupPushButton, 0, 2)

        #
        # Record to Stream
        #

        self.streamLayout = QtGui.QGridLayout()
        self.streamGroupBox = QtGui.QGroupBox("Record to Stream")
        self.streamGroupBox.setLayout(self.streamLayout)
        self.mainLayout.insertWidget(0, self.streamGroupBox)

        self.streamGroupBox.setCheckable(True)
        self.streamGroupBox.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.streamGroupBox.setFixedSize(self.BOX_WIDTH, self.BOX_HEIGHT)
        self.streamGroupBox.setStyleSheet(self.boxStyle)

        self.streamLabel = QtGui.QLabel("Stream Format")
        self.streamLabel.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.streamComboBox = QtGui.QComboBox()
        self.streamLabel.setBuddy(self.streamComboBox)
        self.streamSetupPushButton = QtGui.QToolButton()
        self.streamSetupPushButton.setText("Setup")
        self.streamSetupPushButton.setIcon(config_icon)
        self.streamSetupPushButton.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.streamSetupPushButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.streamLayout.addWidget(self.streamLabel, 0, 0)
        self.streamLayout.addWidget(self.streamComboBox, 0, 1)
        self.streamLayout.addWidget(self.streamSetupPushButton, 0, 2)

        #
        # Record to File
        #

        self.fileLayout = QtGui.QGridLayout()
        self.fileGroupBox = QtGui.QGroupBox("Record to File")
        self.fileGroupBox.setLayout(self.fileLayout)
        self.mainLayout.insertWidget(0, self.fileGroupBox)

        self.fileGroupBox.setCheckable(True)
        self.fileGroupBox.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.fileGroupBox.setFixedSize(self.BOX_WIDTH, self.BOX_HEIGHT + 40)
        self.fileGroupBox.setStyleSheet(self.boxStyle)

        self.fileDirLabel = QtGui.QLabel("Record Directory")
        self.fileDirLineEdit = QtGui.QLineEdit()
        self.fileDirLabel.setBuddy(self.fileDirLineEdit)
        self.fileDirPushButton = QtGui.QPushButton("Browse...")
        self.fileLayout.addWidget(self.fileDirLabel, 0, 0)
        self.fileLayout.addWidget(self.fileDirLineEdit, 0, 1)
        self.fileLayout.addWidget(self.fileDirPushButton, 0, 2)

        self.fileLabel = QtGui.QLabel("File Format")
        self.fileLabel.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.fileComboBox = QtGui.QComboBox()
        self.fileLabel.setBuddy(self.fileComboBox)
        self.fileSetupPushButton = QtGui.QToolButton()
        self.fileSetupPushButton.setText("Setup")
        self.fileSetupPushButton.setIcon(config_icon)
        self.fileSetupPushButton.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.fileSetupPushButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.fileLayout.addWidget(self.fileLabel, 1, 0)
        self.fileLayout.addWidget(self.fileComboBox, 1, 1)
        self.fileLayout.addWidget(self.fileSetupPushButton, 1, 2)

        # Blank line
        self.mainLayout.insertSpacerItem(0, QtGui.QSpacerItem(0, self.fontSize * 2))
        # Heading
        self.title = QtGui.QLabel(u"{0} Recording {1}".format(u'<h1>', u'</h1>'))
        self.mainLayout.insertWidget(0, self.title)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    main = AVWidget()
    main.show()
    sys.exit(app.exec_())
