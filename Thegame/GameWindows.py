from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from GameStarter import *
from GuiClass import *
from PyQt5.QtCore import *

class selectCharacters(QWidget):
    def __init__(self, theFunction):
        super().__init__()
        self.resize(507, 647)
        self.theFunction = theFunction

        self.groupbox = QGroupBox(self)
        self.groupbox.setGeometry(10, 110, 491, 451)
        self.groupbox.setTitle("Characters")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.label1 = myLabel(self, "Select 2 Characters and write their names", font, 110, 20, 301, 31)
        font.setPointSize(10)
        self.label2 = myLabel(self, "", font, 140, 60, 211, 21)
        self.label2.setStyleSheet("color: red")
        self.label2.setVisible(False)

        font.setPointSize(12)
        self.name1 = myLabel(self.groupbox, "Name:", font, 160, 70, 51, 31)
        self.name1 = myLabel(self.groupbox, "Name:", font, 160, 340, 51, 31)

        self.names = ['']*2
        self.editNames = ['']*4
        self.editNames[0] = myTextEdit(self.groupbox, font, 210, 70, 181, 31)
        self.editNames[1] = myTextEdit(self.groupbox, font, 210, 340, 191, 31)
        self.editNames[2] = myTextEdit(self.groupbox, font, 210, 70, 181, 31)
        self.editNames[3] = myTextEdit(self.groupbox, font, 210, 340, 191, 31)
        self.editNames[2].setVisible(False)
        self.editNames[3].setVisible(False)

        self.scrollbar = QScrollBar(self.groupbox)
        self.scrollbar.setGeometry(470, 10, 16, 431)
        self.scrollbar.setMaximum(1)
        self.scrollbar.setPageStep(1)
        self.scrollbar.setSliderPosition(0)
        self.scrollbar.valueChanged.connect(self.changed)

        self.confirm = myButton(self, "Confirm", 410, 570, 91, 31)
        self.confirm.clicked.connect(self.allConfirmed)

        self.pics = ['']*2

        self.characterSelect = ['']*4
        self.characterSelect[0] = myCheckBox(self.groupbox, directory + "character 1.png", 20, 20, 141, 161)
        self.characterSelect[1] = myCheckBox(self.groupbox, directory + "character 2.png", 10, 270, 151, 161)
        self.characterSelect[2] = myCheckBox(self.groupbox, directory + "character 3.png", 20, 20, 141, 161)
        self.characterSelect[3] = myCheckBox(self.groupbox, directory + "character 4.png", 10, 270, 151, 161)
        self.characterSelect[2].setVisible(False)
        self.characterSelect[3].setVisible(False)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0 and self.scrollbar.value() != 0:
            self.scrollbar.setValue(0)
            
        elif event.angleDelta().y() < 0 and self.scrollbar.value() != 1:
            self.scrollbar.setValue(1)
            

    def allConfirmed(self):
        Determine.infoNeeded[2] = True
        i = 0
        for charac in self.characterSelect:
            if charac.isChecked():
                i += 1
        
        if i == 2:
            i = 0
            i2 = 0
            exit = True
            for charac in self.characterSelect:
                text = self.editNames[i2].toPlainText().strip()
                if charac.isChecked() and text != "":
                    self.pics[i] = charac.picture
                    self.names[i] = text
                    i+= 1

                elif i!= 2 and charac.isChecked():
                    self.label2.changeText("Cannot leave the name empty!")
                    self.label2.setVisible(True)
                    exit = False
                i2 += 1

            if exit:
                self.theFunction(self.pics, self.names)
                self.close()
        elif i > 2:
            self.label2.changeText("Cannot pick more than 2 characters")
            self.label2.setVisible(True)
        else:
            self.label2.changeText("Cannot pick less than 2 characters")
            self.label2.setVisible(True)
            
    def changed(self):
        if self.scrollbar.value() == 1:
            self.characterSelect[0].setVisible(False)
            self.characterSelect[1].setVisible(False)
            self.editNames[0].setVisible(False)
            self.editNames[1].setVisible(False)
            self.characterSelect[2].setVisible(True)
            self.characterSelect[3].setVisible(True)
            self.editNames[2].setVisible(True)
            self.editNames[3].setVisible(True)
            
        
        else:
            self.characterSelect[2].setVisible(False)
            self.characterSelect[3].setVisible(False)
            self.editNames[2].setVisible(False)
            self.editNames[3].setVisible(False)
            self.characterSelect[0].setVisible(True)
            self.characterSelect[1].setVisible(True)
            self.editNames[0].setVisible(True)
            self.editNames[1].setVisible(True)
            

class swtichsPerson(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(497, 511)
        self.number = 0 
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.hightlight = picLabel(self, directory + "highlight.png", 10, 0, 141, 191)
        self.hightlight2 = picLabel(self, directory + "highlight.png", 20, 280, 131, 191)
        self.hightlight.setVisible(False)
        self.hightlight2.setVisible(False)

        self.picture1 = picLabel(self, "", 30, 20, 0, 151)
        self.picture2 = picLabel(self, "", 30, 295, 0, 151)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.stepsLabel = myLabel(self, "Total Steps:", font, 190, 40, 101, 21)
        self.stepsLabel2 = myLabel(self, "Total Steps:", font, 170, 330, 101, 21)
        

        self.stepsLabelValue = myLabel(self, "", font, 300, 40, 47, 21)
        self.stepsLabelValue2 = myLabel(self, "", font, 280, 330, 47, 21)

        self.giveStepsLabel1 = myLabel(self, "Give Steps:", font, 190, 100, 131, 21)
        self.giveStepsLabel2 = myLabel(self, "Give Steps:", font, 180, 400, 131, 21)

        self.confirm1 = myButton(self, "Give", 250, 130, 61, 31)
        self.confirm2 = myButton(self, "Give", 240, 430, 61, 31)
        self.apply = myButton(self, "Exit", 340, 450, 61, 31)

        self.selectDefault1 = myButton(self, "Switch To", 360, 70, 81, 41)
        self.selectDefault2 = myButton(self, "Switch To", 360, 360, 81, 41)

        self.chooseSteps1 = QtWidgets.QSpinBox(self)
        self.chooseSteps1.setGeometry(180, 135, 61, 21)
        self.chooseSteps1.setMaximum(30)
        self.chooseSteps1.setMinimum(0)

        self.chooseSteps2 = QtWidgets.QSpinBox(self)
        self.chooseSteps2.setGeometry(170, 435, 61, 21)
        self.chooseSteps2.setMaximum(30)
        self.chooseSteps2.setMinimum(0)
        self.confirm1.clicked.connect(self.finalConfirmed1)
        self.confirm2.clicked.connect(self.finalConfirmed2)
        self.selectDefault1.clicked.connect(self.defaultConfirmed1)
        self.selectDefault2.clicked.connect(self.defaultConfirmed2)
        self.apply.clicked.connect(self.endAll)


    def work(self, persons, function):
        self.persons = persons
        self.function = function
        self.picture1.changePic(persons[0].picture, True)
        self.picture2.changePic(persons[1].picture, True)
        self.stepsLabelValue.changeText(persons[0].steps)
        self.stepsLabelValue2.changeText(persons[1].steps)
        
        self.chooseSteps1.setMaximum(self.persons[0].steps)
        self.chooseSteps2.setMaximum(self.persons[1].steps)

        self.adjust2()


    def finalConfirmed1(self):
        steps = int(self.chooseSteps1.value())
        self.number -= steps
        Determine.infoNeeded[1] = self.number
        self.adjust(-steps)

    def finalConfirmed2(self):
        steps = int(self.chooseSteps2.value())
        self.number += steps
        Determine.infoNeeded[1] = self.number
        self.adjust(steps)

    def defaultConfirmed1(self):
        Determine.infoNeeded[0] = 0
        self.adjust2()
    def defaultConfirmed2(self):
        Determine.infoNeeded[0] = 1
        self.adjust2()

    def adjust2(self):
        self.selectDefault1.setDisabled(False)
        self.selectDefault2.setDisabled(False)
        self.hightlight.setVisible(False)
        self.hightlight2.setVisible(False)
        if Determine.infoNeeded[0] == 0:
            self.hightlight.setVisible(True)
            self.selectDefault1.setDisabled(True)

        else:
            self.hightlight2.setVisible(True)
            self.selectDefault2.setDisabled(True)

    def adjust(self, stepsGiven):
        self.persons[0].steps += stepsGiven
        self.persons[1].steps -= stepsGiven
        self.chooseSteps1.setValue(0)
        self.chooseSteps2.setValue(0)
        self.chooseSteps1.setMaximum(self.persons[0].steps)
        self.chooseSteps2.setMaximum(self.persons[1].steps)
        self.stepsLabelValue.changeText(self.persons[0].steps)
        self.stepsLabelValue2.changeText(self.persons[1].steps)
        

    def endAll(self):
        self.function()
        self.hide()
        

class checkAllEggs(QWidget):
    def __init__(self, eggs):
        super().__init__()
        self.resize(461, 498)
        self.eggs = eggs
        self.eggLabels = ['']*5
        self.namesLabel = ['']*5
        self.fromLabel = ['']*5
        self.namesValueLabel = ['']*5
        self.fromValueLabel = ['']*5


        self.eggLabels[0] = picLabel(self, directory + "question.png", 20, 10, 0, 71)
        self.eggLabels[1] = picLabel(self, directory + "question.png", 20, 90, 0, 71)
        self.eggLabels[2] = picLabel(self, directory + "question.png", 20, 180, 0, 71)
        self.eggLabels[3] = picLabel(self, directory + "question.png", 20, 270, 0, 71)
        self.eggLabels[4] = picLabel(self, directory + "question.png", 20, 360, 0, 71)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.namesLabel[0] = myLabel(self, "Name:", font, 110, 20, 58, 16)
        self.namesLabel[1] = myLabel(self, "Name:", font, 110, 110, 58, 16)
        self.namesLabel[2] = myLabel(self, "Name:", font, 110, 190, 58, 16)
        self.namesLabel[3] = myLabel(self, "Name:", font, 110, 290, 58, 16)
        self.namesLabel[4] = myLabel(self, "Name:", font, 110, 380, 58, 16)

        self.fromLabel[0] = myLabel(self, "Gotten From:", font, 110, 50, 121, 16)
        self.fromLabel[1] = myLabel(self, "Gotten From:", font, 110, 140, 121, 16)
        self.fromLabel[2] = myLabel(self, "Gotten From:", font, 110, 220, 121, 16)
        self.fromLabel[3] = myLabel(self, "Gotten From:", font, 110, 320, 121, 16)
        self.fromLabel[4] = myLabel(self, "Gotten From:", font, 110, 410, 121, 16)

        self.namesValueLabel[0] = myLabel(self, "Unknown", font, 240, 20, 201, 16)
        self.namesValueLabel[1] = myLabel(self, "Unknown", font, 240, 110, 201, 16)
        self.namesValueLabel[2] = myLabel(self, "Unknown", font, 240, 190, 201, 16)
        self.namesValueLabel[3] = myLabel(self, "Unknown", font, 240, 290, 201, 16)
        self.namesValueLabel[4] = myLabel(self, "Unknown", font, 240, 380, 201, 16)

        self.fromValueLabel[0] = myLabel(self, "Unknown", font, 240, 50, 201, 16)
        self.fromValueLabel[1] = myLabel(self, "Unknown", font, 240, 140, 201, 16)
        self.fromValueLabel[2] = myLabel(self, "Unknown", font, 240, 220, 201, 16)
        self.fromValueLabel[3] = myLabel(self, "Unknown", font, 240, 320, 201, 16)
        self.fromValueLabel[4] = myLabel(self, "Unknown", font, 240, 410, 201, 16)

    def checkEggStatus(self):
        for i in range(0, 5):
            if self.eggs[i].getStatus():
                self.namesValueLabel[i].changeText(self.eggs[i].getName())
                self.fromValueLabel[i].changeText(room[self.eggs[i].getId()].getName())
                if i != 2:
                    self.eggLabels[i].changePic(self.eggs[i].picture, True)
                else:
                    self.eggLabels[i].setGeometry(0, 180, 120, 71)
                    self.eggLabels[i].changePic(self.eggs[i].picture)





class GivingHint(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 100, 300, 600)
        self.resize(721, 601)

        self.label = picLabel(self, directory + "home3.png", 10, 90, 711, 511)
        self.highlightPerson = picLabel(self, directory + "highlight.png", 1,1,1,1)
        self.highlightOb = ['']*30
        self.highlightOb2 = ['']*30
        self.makeRooms()
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.personWalking = picLabel(self, "", 1, 1, 0, 61)

    def updateIt(self, person, eggs):
        self.currentRoom = person.getRoom()
        self.highlightOb2[self.currentRoom.getId()].setVisible(True)
        self.eggs = eggs
        coordinates = self.currentRoom.getDirection()
        self.personWalking.changePic(person.picture, True)
        self.personWalking.move(coordinates[0], coordinates[1])

        self.eggLabel = [""]*4

        self.index = 0
        sur = self.currentRoom.getSurroundings()
        for egg in eggs:
            for ids in sur:
                if egg.getId() == ids.getId():
                    if not egg.getStatus():
                        dir = room[egg.getId()].getDirection()
                        self.eggLabel[self.index] = picLabel(self, egg.picture, dir[0]-15, dir[1]+10, 0, 41)
                        self.highlightOb[ids.getId()].setVisible(True)
                        self.index+= 1

    def buttonEnd(self):
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)

    def closeEvent(self, e: QtGui.QCloseEvent):
        self.endTask(False)
        e.accept()

    def endTask(self, shouldHide=True):
        nums = [0,1,2,4,5,6,7,9,10,11,12,14,16,17,19,21,22,23,24,25,26,27,28,29]
        for i in range(0, 24):
            self.highlightOb[nums[i]].setVisible(False)
            self.highlightOb2[nums[i]].setVisible(False)

        for i in range(0,self.index):
            self.eggLabel[i].deleteLater()
        if shouldHide:
            self.hide()

    def makeRooms(self):
        nums = [0,1,2,4,5,6,7,9,10,11,12,14,16,17,19,21,22,23,24,25,26,27,28,29]
        coorX = [19, 133, 252, 371, 490, 609, 719]
        coorY = [103, 196, 298, 400, 503, 600]
        self.coorX = coorX
        self.coorY = coorY
        forx = 0
        fory = 0

        for i in range(0, 24):
            if nums[i] == 4 or nums[i] == 9 or nums[i] == 14 or nums[i] == 19:
                x2 = (coorX[forx+1]-4) - coorX[forx]
                y2 = (coorY[fory+2]-5) - coorY[fory]
                picLabel(self, room[nums[i]].picture, coorX[forx], coorY[fory], x2, y2)
                self.highlightOb[nums[i]] = picLabel(self, directory + "highlight.png", coorX[forx], coorY[fory], x2, y2)
                self.highlightOb[nums[i]].setVisible(False)
                self.highlightOb2[nums[i]] = picLabel(self, directory + "highlight2.png", coorX[forx], coorY[fory], x2, y2)
                self.highlightOb2[nums[i]].setVisible(False)
            else:
                x2 = (coorX[forx+1]-4) - coorX[forx]
                y2 = (coorY[fory+1]-5) - coorY[fory]
                picLabel(self, room[nums[i]].picture, coorX[forx], coorY[fory], x2, y2)
                self.highlightOb[nums[i]] = picLabel(self, directory + "highlight.png", coorX[forx], coorY[fory], x2, y2)
                self.highlightOb[nums[i]].setVisible(False)
                self.highlightOb2[nums[i]] = picLabel(self, directory + "highlight2.png", coorX[forx], coorY[fory], x2, y2)
                self.highlightOb2[nums[i]].setVisible(False)
                

            fory += 1

            if nums[i] == 4 or nums[i] == 9 or nums[i] == 14 or nums[i] == 19 or nums[i] == 24:
                fory = 0
                forx += 1

            if i == 11 or i == 14:
                fory += 1


class pickingUp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(611, 515)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.description = myLabel(self, "", font, 10, 10, 591, 41)
        self.description.alignCenter()

        self.background = picLabel(self, "", 10, 70, 601, 401)
        self.thePerson = picLabel(self, "", 30, 170, 0, 291)

        self.thing = picLabel(self, "", 380, 360, 0, 101)

    def showTake(self):
        
        if self.howMuch < 3 and self.howMuch >= 1:
            self.prevX += 170
            self.thePerson.move(self.prevX, 170)

        if self.howMuch == 2:
            self.description.changeText("You picked up " + self.newThing.getName())
            self.thing.setVisible(False)
        
        if self.howMuch == 3:
            self.timer.stop()
        self.howMuch += 1

    def takeIt(self, person, thing):
        self.prevX = self.thePerson.setX
        self.newThing = thing
        self.background.changePic(person.getRoom().picture)
        self.thePerson.changePic(person.picture, True)
        self.thing.changePic(self.newThing.picture, True)
        self.thing.setVisible(True)
        self.howMuch = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTake)
        self.timer.start(500)

    def closeEvent(self, e):
        self.description.changeText("")
        if self.timer.isActive():
            self.timer.stop()
        e.accept()

    def closeProper(self):
        self.description.changeText("")
        if self.timer.isActive():
            self.timer.stop()
        self.close()


class Won(QWidget):
    def __init__(self, persons, theFunction):
        
        super().__init__()
        self.resize(611, 515)
        self.theFunction = theFunction

        font = QtGui.QFont()
        font.setPointSize(14)
        self.description = myLabel(self, "You Won!!", font, 10, 10, 591, 41)
        self.description.alignCenter()

        self.background = picLabel(self, directory + "fireworks.jpg", 10, 70, 601, 401)
        self.thePerson1 = picLabel(self, persons[0].picture, 30, 170, 0, 291)
        self.thePerson2 = picLabel(self, persons[1].picture, 370, 170, 0, 291)
        self.amount = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.happy)

    def startIt(self):
        self.show()
        self.timer.start(500)


    def happy(self):
        if self.amount == 1 or self.amount == 3:
            self.thePerson1.move(30, 70)
            self.thePerson2.move(370, 70)
        if self.amount == 2 or self.amount == 4:
            self.thePerson1.move(30, 170)
            self.thePerson2.move(370, 170)
        if self.amount == 5:
            self.timer.stop()
        self.amount += 1

    def closeEvent(self, e):
        self.theFunction()
        if self.timer.isActive():
            self.timer.stop()
        e.accept()



class showStatus(QWidget):
    def __init__(self, persons):
        super().__init__()
        self.resize(1030, 704)
        self.persons = persons
        self.pic1 = picLabel(self, persons[0].picture, 260, 10, 0, 201)
        self.pic2 = picLabel(self, persons[1].picture, 570, 10, 0, 201)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.stepsUsedLabel = myLabel(self, "Steps Used:", font, 20, 260, 91, 41)
        self.stepsUsedValue1 = myLabel(self, "", font, 300, 260, 91, 41)
        self.stepsUsedValue2 = myLabel(self, "", font, 610, 260, 91, 41)
        self.stepsUsedValue3 = myLabel(self, "", font, 860, 260, 91, 41)
        self.stepsUsedValue1.alignCenter()
        self.stepsUsedValue2.alignCenter()
        self.stepsUsedValue3.alignCenter()

        self.wallHit = myLabel(self, "Times you hit a wall:", font, 20, 340, 151, 41)
        self.wallHit1 = myLabel(self, "", font, 300, 340, 91, 41)
        self.wallHit2 = myLabel(self, "", font, 610, 340, 91, 41)
        self.wallHit3 = myLabel(self, "", font, 860, 340, 91, 41)
        self.wallHit1.alignCenter()
        self.wallHit2.alignCenter()
        self.wallHit3.alignCenter()

        self.objects = myLabel(self, "Amount of Objects Gotten:", font, 20, 430, 201, 41)
        self.objects1 = myLabel(self, "", font, 300, 430, 91, 41)
        self.objects2 = myLabel(self, "", font, 610, 430, 91, 41)
        self.objects3 = myLabel(self, "", font, 860, 430, 91, 41)
        self.objects1.alignCenter()
        self.objects2.alignCenter()
        self.objects3.alignCenter()

        self.visitedRooms = myLabel(self, "Rooms Visited in Total:", font, 20, 520, 181, 41)
        self.visitedRoomsValue = myLabel(self, "", font, 860, 520, 91, 41)
        self.visitedRoomsValue.alignCenter()

        font.setPointSize(16)
        self.totalLabel = myLabel(self, "Total", font, 860, 40, 91, 41)

    def updateStatus(self):
        self.stepsUsedValue1.changeText(self.persons[0].stepsUsed)
        self.stepsUsedValue2.changeText(self.persons[1].stepsUsed)
        self.stepsUsedValue3.changeText(self.persons[0].stepsUsed + self.persons[1].stepsUsed)

        self.wallHit1.changeText(self.persons[0].hitWall)
        self.wallHit2.changeText(self.persons[1].hitWall)
        self.wallHit3.changeText(self.persons[0].hitWall + self.persons[1].hitWall)

        self.objects1.changeText(self.persons[0].objectsGot)
        self.objects2.changeText(self.persons[1].objectsGot)
        self.objects3.changeText(str(self.persons[0].objectsGot + self.persons[1].objectsGot) + "/5")

        self.visitedRoomsValue.changeText(str(self.checkRoomsVisited()) + "/24")

    def checkRoomsVisited(self):
        getVisited = 0
        for r in room:
            if r.isVisited:
                getVisited += 1

        return int(getVisited)