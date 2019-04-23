from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QGridLayout, QScrollArea, QPushButton, QLineEdit, QStackedWidget, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from SensorManager import Sensor, SensorManager
from functools import partial
import configparser
import json
from DataCollector import DataCollector
import random

sensorManager = SensorManager()
dataCollector = DataCollector()

class SideBar(QDialog):
    def __init__(self, parent=None):
        super(SideBar, self).__init__(parent)

        # self.setFixedHeight(200)

        self.onClick = None
        self.addNewSensor = None

        #Container Widget
        widget = QWidget()
        #Layout of Container Widget
        self.layout = QVBoxLayout(self)

        self.initLayout()

        self.layout.setContentsMargins(0,0,0,0)

        widget.setLayout(self.layout)

        #Scroll Area Properties
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        #Scroll Area Layer add
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)

        addSensorButton = QPushButton("Add Sensor")
        addSensorButton.clicked.connect(self.addSensor)

        vLayout.addWidget(addSensorButton)

        vLayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(vLayout)

    def initLayout(self):
        print("Hi")
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        for sensor in sensorManager.get():

            self.deviceButton = QPushButton("Device: " + sensor.name + "\nStatus: " + sensor.status)
            self.deviceButton.clicked.connect(partial(self.sensorSelected, sensor))
            self.layout.addWidget(self.deviceButton)

    def updateLayout(self):
        print("Hi")




    def sensorSelected(self, sensor):
        self.onClick(sensor)

    def addSensor(self):
        self.addNewSensor()

class TabBar(QDialog):
    def __init__(self, parent=None):
        super(TabBar, self).__init__(parent)

        self.tabController = None

        self.uiSetup()

    def uiSetup(self):
        self.tabItems = ["Instruments", "Overview", "Options"]
        self.tabButtons = []

        layout = QHBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        for tabItem in self.tabItems:

            tabButton = QPushButton(tabItem)
            self.tabButtons.append(tabButton)

            tabButton.clicked.connect(partial(self.tabButtonClicked, tabItem))

            layout.addWidget(tabButton)

        self.setLayout(layout)


        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(71, 129, 196))
        self.setPalette(p)

    def tabButtonClicked(self, item):
        self.tabController(item)
        self.highlightItem(item)

    def highlightItem(self, item):
        for i in range(len(self.tabButtons)):
            self.tabButtons[i].setProperty("underline", "true")
            self.tabButtons[i].update()


class ContentMenu(QDialog):
    def __init__(self, parent=None):
        super(ContentMenu, self).__init__(parent)

        self.isNew = False

        self.selectedSensor = Sensor("","","","","", 1)

        self.updateLayout = None

        self.uiSetup()

    def uiSetup(self):
        gridLayout = QVBoxLayout()
        gridLayout.setContentsMargins(0, 0, 0, 0)

        self.sensorNameLabel = QLabel("Name:")
        self.sensorNameTextBox = QLineEdit()

        self.sensorNameTextBox.editingFinished.connect(self.updateSensor)

        gridLayout.addWidget(self.sensorNameLabel)
        gridLayout.addWidget(self.sensorNameTextBox)

        self.sensorSerialLabel = QLabel("Serial Number")
        self.sensorSerialTextBox = QLineEdit()

        self.sensorSerialTextBox.editingFinished.connect(self.updateSensor)

        gridLayout.addWidget(self.sensorSerialLabel)
        gridLayout.addWidget(self.sensorSerialTextBox)

        self.sensorPortLabel = QLabel("Port")
        self.sensorPortTextBox = QLineEdit()

        self.sensorPortTextBox.editingFinished.connect(self.updateSensor)

        gridLayout.addWidget(self.sensorPortLabel)
        gridLayout.addWidget(self.sensorPortTextBox)

        self.sensorBaudRateLabel = QLabel("BaudRate")
        self.sensorBaudRateTextBox = QLineEdit()

        self.sensorBaudRateTextBox.editingFinished.connect(self.updateSensor)

        gridLayout.addWidget(self.sensorBaudRateLabel)
        gridLayout.addWidget(self.sensorBaudRateTextBox)

        self.dataCollectionButton = QPushButton()

        if(self.selectedSensor.status == "on"):
            self.dataCollectionButton.setText("Stop Data Collection")
        else:
            self.dataCollectionButton.setText("Start Data Collection")


        self.dataCollectionButton.clicked.connect(self.handleDataCollection)

        gridLayout.addWidget(self.dataCollectionButton)


        self.setLayout(gridLayout)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

    def updateSensor(self):
        self.selectedSensor.name = self.sensorNameTextBox.text()
        self.selectedSensor.port = self.sensorPortTextBox.text()
        self.selectedSensor.serial = self.sensorSerialTextBox.text()
        self.selectedSensor.baudRate = int(self.sensorBaudRateTextBox.text())

        sensorManager.update(self.selectedSensor)
        self.updateLayout()

    def setCurrentSensor(self, sensor):

        self.selectedSensor = sensor

        self.sensorNameTextBox.setText(self.selectedSensor.name)
        self.sensorSerialTextBox.setText(str(self.selectedSensor.serial))
        self.sensorPortTextBox.setText(self.selectedSensor.port)
        self.sensorBaudRateTextBox.setText(str(self.selectedSensor.baudRate))
        if(self.selectedSensor.status == "on"):
            self.dataCollectionButton.setText("Stop Data Collection")
        else:
            self.dataCollectionButton.setText("Start Data Collection")

    def handleDataCollection(self):
        if(self.selectedSensor.status == "off"):
            dataCollector.start(self.selectedSensor)
            self.selectedSensor.status = "on"
            self.dataCollectionButton.setText("Stop Data Collection")
        else:
            dataCollector.stop(self.selectedSensor)
            self.selectedSensor.status = "off"
            self.dataCollectionButton.setText("Start Data Collection")
        self.updateLayout()

    def addNewSensor(self):
        newSensor = Sensor("New Sensor", 0, 0, "/", "off", random.randint(0, 100000))
        sensorManager.add(newSensor)
        self.isNew = True

        self.selectedSensor = newSensor
        self.sensorNameTextBox.setText(self.selectedSensor.name)
        self.sensorSerialTextBox.setText(str(self.selectedSensor.serial))
        self.sensorPortTextBox.setText(self.selectedSensor.port)
        self.sensorBaudRateTextBox.setText(str(self.selectedSensor.baudRate))

        self.dataCollectionButton.setVisible(True)

class OptionsMenu(QDialog):
    def __init__(self, parent=None):
        super(OptionsMenu, self).__init__(parent)

        self.uiSetup()

    def uiSetup(self):

        layout = QFormLayout()

        config = configparser.ConfigParser()
        config.read('config.ini')

        filedirectory = config['DEFAULT']['filedirectory']
        address = config['DEFAULT']['Secondaryaddress']

        self.addressTextField = QLineEdit(address)
        self.directoryTextField = QLineEdit(filedirectory)

        self.addressTextField.textChanged.connect(self.setPrefs)
        self.directoryTextField.textChanged.connect(self.setPrefs)

        layout.addRow(QLabel("Secondary Computer Address"), self.addressTextField)
        layout.addRow(QLabel("File Storage Directory"), self.directoryTextField)

        self.setLayout(layout)

    def setPrefs(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set('DEFAULT', 'filedirectory', self.directoryTextField.text())
        config.set('DEFAULT', 'Secondaryaddress', self.addressTextField.text())
        config.write(open("config.ini", "w"))



class OverviewMenu(QDialog):
    def __init__(self, parent=None):
        super(OverviewMenu, self).__init__(parent)

        self.uiSetup()

    def uiSetup(self):

        self.setFixedHeight(200)

        self.onClick = None
        self.addNewSensor = None

        #Container Widget
        widget = QWidget()
        #Layout of Container Widget
        layout = QVBoxLayout(self)

        for sensor in sensorManager.get():

            self.deviceButton = QLabel("Device: " + sensor.name + "\nStatus: " + sensor.status + "\nMost Recent Data:")

            layout.addWidget(self.deviceButton)

        widget.setLayout(layout)

        #Scroll Area Properties
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(widget)

        #Scroll Area Layer add
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)

        vLayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(vLayout)



class ContainerWindow(QDialog):
    def __init__(self, parent=None):
        super(ContainerWindow, self).__init__(parent)

        self.tabItems =  ["Instruments", "Overview", "Options"]

        self.currentTab = self.tabItems[0]

        self.uiSetup()


    def uiSetup(self):

        # Creating tab bar
        tabBar = TabBar()
        tabBar.tabController = self.selectedTab
        tabBar.tabItems = self.tabItems

        # Creating Instuments Layout

        subLayout = QHBoxLayout()

        self.cm = ContentMenu()
        self.cm.setCurrentSensor(sensorManager.get()[0])

        self.sb = SideBar()
        self.sb.onClick = self.cm.setCurrentSensor
        self.sb.addNewSensor = self.cm.addNewSensor

        self.cm.updateLayout = self.sb.updateLayout

        subLayout.addWidget(self.sb)
        subLayout.addWidget(self.cm)

        subLayout.setContentsMargins(0,0,0,0)


        instumentWidget = QWidget()

        instumentWidget.setLayout(subLayout)


        # Creating Overview Layout

        overviewWidget = OverviewMenu()

        # Creating Options layout

        optionsWidget = OptionsMenu()

        # adding to stack layout
        self.stacked = QStackedWidget()

        self.stacked.addWidget(instumentWidget)
        self.stacked.addWidget(overviewWidget)
        self.stacked.addWidget(optionsWidget)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(tabBar)
        mainLayout.addWidget(self.stacked)

        mainLayout.setContentsMargins(0,0,0,0)


        self.setLayout(mainLayout)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(247, 247, 247))
        self.setPalette(p)

    def selectedTab(self, name):
        self.currentTab = name

        if(self.currentTab == self.tabItems[0]):
            self.stacked.setCurrentIndex(0)
        elif(self.currentTab == self.tabItems[1]):
            self.stacked.setCurrentIndex(1)
        else:
            self.stacked.setCurrentIndex(2)


def main():

    app = QApplication([])
    with open("main.css","r") as stylesheet:
        app.setStyleSheet(stylesheet.read())
    cw = ContainerWindow()
    cw.show()
    app.exec_()

main()


# contentMenu = ContentMenu()
# contentMenu.show()
# sideBar = SideBar()
# sidebar.show()
