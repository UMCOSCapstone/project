from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QGridLayout, QScrollArea, QPushButton, QLineEdit, QStackedWidget, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from SensorManager import Sensor, SensorManager
from functools import partial
from DataCollector2 import DataCollector

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
        layout = QVBoxLayout(self)

        layout.setContentsMargins(0,0,0,0)

        for sensor in sensorManager.get():

            self.deviceButton = QPushButton("Device: " + sensor.name + "\nStatus: " + sensor.status)

            self.deviceButton.clicked.connect(partial(self.sensorSelected, sensor))

            layout.addWidget(self.deviceButton)

        widget.setLayout(layout)

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

        layout = QHBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        for tabItem in self.tabItems:

            tabButton = QPushButton(tabItem)

            tabButton.clicked.connect(partial(self.tabButtonClicked, tabItem))

            layout.addWidget(tabButton)

        self.setLayout(layout)


        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(71, 129, 196))
        self.setPalette(p)

    def tabButtonClicked(self, item):
        self.tabController(item)


class ContentMenu(QDialog):
    def __init__(self, parent=None):
        super(ContentMenu, self).__init__(parent)

        self.isNew = False

        self.selectedSensor = Sensor("","","","","")

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

        if(self.isNew):
            self.selectedSensor.serial = self.sensorSerialTextBox.text()

        self.selectedSensor.baudRate = int(self.sensorBaudRateTextBox.text())

        sensorManager.update(self.selectedSensor)

    def setCurrentSensor(self, sensor):
        self.isNew = False

        self.selectedSensor = sensor

        self.sensorNameTextBox.setText(self.selectedSensor.name)
        self.sensorSerialTextBox.setText(str(self.selectedSensor.serial))
        self.sensorPortTextBox.setText(self.selectedSensor.port)
        self.sensorBaudRateTextBox.setText(str(self.selectedSensor.baudRate))

        self.dataCollectionButton.setVisible(True)

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

    def addNewSensor(self):
        newSensor = Sensor("New Sensor", 0, 0, "/", "off")
        sensorManager.add(newSensor)
        self.isNew = True

        self.selectedSensor = newSensor
        self.sensorNameTextBox.setText(self.selectedSensor.name)
        self.sensorSerialTextBox.setText(str(self.selectedSensor.serial))
        self.sensorPortTextBox.setText(self.selectedSensor.port)
        self.sensorBaudRateTextBox.setText(str(self.selectedSensor.baudRate))

        self.dataCollectionButton.setVisible(False)

class OptionsMenu(QDialog):
    def __init__(self, parent=None):
        super(OptionsMenu, self).__init__(parent)

        self.uiSetup()

    def uiSetup(self):

        layout = QFormLayout()

        layout.addRow(QLabel("Secondary Computer Address"), QLineEdit("localhost:8080"))
        layout.addRow(QLabel("File Storage Directory"), QLineEdit("/var/backup/external"))

        self.setLayout(layout)




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
