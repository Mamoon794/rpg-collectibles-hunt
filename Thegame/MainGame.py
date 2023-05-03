from GuiClass import *
from GameWindows import *
import sys
from house import *

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.hide()
        self.wonGame = False
        
        self.setGeometry(50, 100, 300, 600)
        self.resize(1135, 653)
        self.keyReleaseEvent = self.moves
        self.rechargeSteps = 0
        self.stepsRequired = 5
        self.currentPerson = 0
        self.whereMoved = ""
        self.slowMoveX = [70, 370, 220]
        self.slowMoveY = [90, 165, 130]
        self.persons = [Person(directory + "character 1.png", "Acree", room[0]), Person(directory + "character 2.png", "Terrimous", room[17])]
        self.eggs = [Egg("Crystal Gem", directory + "Crystal gem.png", 10), Egg("Flower", directory + "Flowers.png", 4), Egg("Crown", directory + "crown.png", 19),
        Egg("Wand", directory + "Wand.png", 27), Egg("Sword", directory + "sword.png", 28)]
        self.currentRoom = self.persons[self.currentPerson].getRoom()
        self.selection = selectCharacters(self.finalizeCharacters)
        self.timer = QTimer(self)
        self.win1 = GivingHint()
        self.wi = swtichsPerson()
        self.moves = pickingUp()
        self.showValue = checkAllEggs(self.eggs)
        self.selection.show()

    def inTheRoom(self):
        self.currentRoom.isVisited = True
            

    def finalizeCharacters(self, pics, names):
        self.persons[0].picture = pics[0]
        self.persons[1].picture = pics[1]
        self.persons[0]._name = names[0]
        self.persons[1]._name = names[1]
        self.finalStatus = showStatus(self.persons)
        self.initUI()
        self.show()

    def shows(self):
        self.currentPerson = Determine.infoNeeded[0]
        self.personWalking.changePic(self.persons[self.currentPerson].picture, True)
        self.personWalking.changeGeo(220, 130, 0, 431)
        self.endResult.setText(self.persons[self.currentPerson].say)
        self.currentPersonLabel.setText(self.persons[self.currentPerson].getName())
        self.currentRoomLabel.setText(self.persons[self.currentPerson].getRoom().getName())
        self.currentRoom = self.persons[self.currentPerson].getRoom()
        self.inTheRoom()
        self.label.changePic(self.currentRoom.getPic())
        if self.wonGame:
            self.hintUsed()

        self.updateStepsLeft() 
        self.noSteps()    
    
    def initUI(self):
        self.inTheRoom()
        self.label = picLabel(self, self.currentRoom.getPic(), 10, 90, 711, 511)

        self.rechargeProgress = progressBar(self, self.stepsRequired, 0, 930, 370, 118, 23)

        self.stepsLeft = progressBar(self, self.persons[self.currentPerson].steps, self.persons[self.currentPerson].steps, 930, 290, 118, 23)
        self.stepsLeft.setFormat("Steps")

        font = QtGui.QFont()
        font.setPointSize(22)
        self.description = myLabel(self, "Description", font, 850, 30, 151, 51)

        font.setPointSize(14)
        self.roomLabel = myLabel(self, "World:", font, 810, 140, 61, 21)
        

        font.setPointSize(12)
        self.currentRoomLabel = myLabel(self, self.currentRoom.getName(), font, 930, 142, 191, 20)
        
        self.personLabel = myLabel(self, "Current Person:", font, 810, 210, 111, 21)

        self.currentPersonLabel = myLabel(self, self.persons[self.currentPerson].getName(), font, 930, 212, 151, 16)

        self.stepsLeftLabel = myLabel(self, "Steps Left:", font, 810, 290, 81, 21)

        self.hintRechargeLabel = myLabel(self, "Hint Recharge:", font, 810, 370, 111, 21)

        self.thingsTakenLabel = myLabel(self, "All Valuables:", font, 810, 440, 101, 21)
        
        font.setPointSize(22)
        self.endResult = myLabel(self, "", font, 10, 20, 691, 51)
        self.endResult.alignCenter()

        font.setPointSize(10)
        self.stepsLeftNum = myLabel(self, self.persons[self.currentPerson].steps, font, 970, 293, 21, 16)

        self.hint = myButton(self, "Hint", 930, 367, 91, 31)
        self.hint.setVisible(False)
        self.hint.clicked.connect(self.hintUsed)

        self.noStepsLeft = myButton(self, "Switch Person", 930, 285, 91, 31)
        self.noStepsLeft.setVisible(False)
        self.noStepsLeft.clicked.connect(self.switchOnly)

        self.personWalking = picLabel(self, self.persons[self.currentPerson].picture, 220, 130, 0, 431)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(0, 0, 1135, 21)

        self.menuStatus = QtWidgets.QMenu(self.menubar)
        self.menuStatus.setTitle("Status")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setTitle("Game")

        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.objectTaken = QtWidgets.QAction(self, text="Objects Taken")
        self.objectTaken.setStatusTip("Check all the objects taken")
        self.objectTaken.triggered.connect(self.showEgg)

        self.actionSteps_Left = QtWidgets.QAction(self, text="Move Status")
        self.actionSteps_Left.setStatusTip("Check the steps left for all characters")
        self.actionSteps_Left.triggered.connect(self.switchPerson)

        self.actionInstructions = QtWidgets.QAction(self, text="Status of game")
        self.actionInstructions.setStatusTip("The Status of the whole game")
        self.actionInstructions.triggered.connect(self.theStatus)

        self.valuable = ['']*5
        self.valuable[0] = picLabel(self, self.eggs[0].picture, 810, 480, 0, 31)
        self.valuable[1] = picLabel(self, self.eggs[1].picture, 860, 480, 0, 31)
        self.valuable[2] = picLabel(self, self.eggs[2].picture, 910, 480, 0, 31)
        self.valuable[3] = picLabel(self, self.eggs[3].picture, 980, 480, 0, 31)
        self.valuable[4] = picLabel(self, self.eggs[4].picture, 1020, 480, 0, 31)

        self.valuable[0].setVisible(False)
        self.valuable[1].setVisible(False)
        self.valuable[2].setVisible(False)
        self.valuable[3].setVisible(False)
        self.valuable[4].setVisible(False)

        self.menuStatus.addAction(self.objectTaken)
        self.menuStatus.addAction(self.actionSteps_Left)
        self.menuHelp.addAction(self.actionInstructions)
        self.menubar.addAction(self.menuStatus.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

    def theStatus(self):
        self.finalStatus.updateStatus()
        self.finalStatus.show()

    def switchPerson(self):
        self.wi.show()
        self.wi.work(self.persons, self.shows)

    def switchOnly(self):
        Determine.infoNeeded[0] += 1
        if (Determine.infoNeeded[0] > 1):
            Determine.infoNeeded[0] = 0
        self.shows()


    def hintUsed(self):
        if not self.wonGame:
            self.rechargeSteps = 0
            self.rechargeProgress.setValue(self.rechargeSteps)
            self.hint.setVisible(False)
            self.rechargeProgress.setVisible(True)

        if self.wonGame:
            if self.win1.isVisible():
                self.win1.endTask(False)
            self.win1.buttonEnd()

        self.win1.updateIt(self.persons[self.currentPerson], self.eggs)
        self.win1.show()
        if not self.wonGame:
            QtCore.QTimer.singleShot(2000, self.win1.endTask)

    
    def wonTask(self):
        for pers in self.persons:
            pers.say = ""
            pers.steps = 1

        self.stepsLeft.setVisible(True)
        self.endResult.changeText("")
        self.noStepsLeft.setVisible(False)
        self.stepsLeft.setValue(1)
        self.stepsLeftNum.changeText(1)
        
        self.hintUsed()
            


    def moves(self, event):
        if event.key() == Qt.Key_Left or event.key() == Qt.Key_A:
            self.moveLeft()
        if event.key() == Qt.Key_Right or event.key() == Qt.Key_D:
            self.moveRight()
        if event.key() == Qt.Key_Up or event.key() == Qt.Key_W:
            self.moveUp()
        if event.key() == Qt.Key_Down or event.key() == Qt.Key_S:
            self.moveDown()
        if event.key() == Qt.Key_H:
            self.hintUsed()
        if event.key() == Qt.Key_K:
            self.switchOnly()

    def moveLeft(self):
        self.startCheck()
        if not self.wonGame:
            self.persons[self.currentPerson].move("a")
            self.whereMoved = "a"
        else:
            self.persons[self.currentPerson].move("a", False)
            self.whereMoved = "a"
        self.endCheck()

    def moveUp(self):
        self.startCheck()
        if not self.wonGame:
            self.persons[self.currentPerson].move("w")
            self.whereMoved = "w"
        else:
            self.persons[self.currentPerson].move("w", False)
            self.whereMoved = "w"
        self.endCheck()

    def moveRight(self):
        self.startCheck()
        if not self.wonGame:
            self.persons[self.currentPerson].move("d")
            self.whereMoved = "d"
        else:
            self.persons[self.currentPerson].move("d", False)
            self.whereMoved = "d"
        self.endCheck()

    def moveDown(self):
        self.startCheck()
        if not self.wonGame:
            self.persons[self.currentPerson].move("s")
            self.whereMoved = "s"
        else:
            self.persons[self.currentPerson].move("s", False)
            self.whereMoved = "s"
        self.endCheck()

        
    def startCheck(self):
        if self.timer.isActive():
            self.timer.stop()
        if self.persons[self.currentPerson].steps != 0 and not self.wonGame:
            self.recharging()

    def slowMove(self):
        if self.howMuch == 1:
            self.label.changePic(self.currentRoom.getPic())
        if self.howMuch > 2:
            self.timer.stop()
        elif self.whereMoved == "a":
            self.personWalking.move(self.slowMoveX[self.howMuch], 130)

        elif self.whereMoved == "w":
            self.personWalking.move(self.slowMoveX[self.howMuch], self.slowMoveY[self.howMuch])

        elif self.whereMoved == "s":
            self.personWalking.move(self.slowMoveX[1-self.howMuch], self.slowMoveY[1-self.howMuch])

        elif self.whereMoved == "d":
            self.personWalking.move(self.slowMoveX[1-self.howMuch], 130)


        self.howMuch += 1

    def showMove(self):
        self.howMuch = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.slowMove)
        self.timer.start(200)

    def showEgg(self):
        self.showValue.checkEggStatus()
        self.showValue.show()

    def getEgg(self, theEgg):
        for thing in self.valuable:
            if thing.pic == theEgg.picture:
                thing.setVisible(True)
                self.moves.takeIt(self.persons[self.currentPerson], theEgg)
                self.moves.show()
                QtCore.QTimer.singleShot(2000, self.moves.closeProper)
                self.persons[self.currentPerson].say = "You picked up " + theEgg._name
                self.endResult.setText(self.persons[self.currentPerson].say)

    def endCheck(self):
        shouldShow = True
        self.currentRoom = self.persons[self.currentPerson].getRoom()
        self.currentRoomLabel.setText(self.currentRoom.getName())
        self.inTheRoom()

        if self.wonGame:
            self.hintUsed()

        for egg in self.eggs:
            if self.currentRoom.getId() == egg.getId() and not egg.getStatus():
                self.persons[self.currentPerson].steps += 5
                self.persons[self.currentPerson].objectsGot += 1
                egg.pickup()
                self.getEgg(egg)
                shouldShow = False
            
        if self.persons[self.currentPerson].canGo and shouldShow:
            self.showMove()
        else:
            self.personWalking.move(self.slowMoveX[2], 130)
            self.label.changePic(self.currentRoom.getPic())

        if self.gotEggs() and not self.wonGame:
            self.wonGame = True
            self.persons[self.currentPerson].say = "You won!!"
            self.won = Won(self.persons, self.wonTask)
            QtCore.QTimer.singleShot(2010, self.won.startIt)
            
        if not self.wonGame:
            self.updateStepsLeft() 
            self.noSteps()
        else:
            self.hint.setVisible(True)
            self.rechargeProgress.setVisible(False)

        if not self.wonGame and self.persons[0].steps == 0 and self.persons[1].steps == 0:
            self.persons[0].say = "You Lost"
            self.persons[1].say = "You Lost"

        self.endResult.setText(self.persons[self.currentPerson].say)   
    
    def noSteps(self):
        if self.persons[self.currentPerson].steps == 0:
            self.stepsLeft.setVisible(False)
            self.noStepsLeft.setVisible(True)  

        else:
            self.stepsLeft.setVisible(True)
            self.noStepsLeft.setVisible(False) 

    def updateStepsLeft(self):
        if self.persons[self.currentPerson].steps > self.stepsLeft.maximum():
            self.stepsLeft.setMaximum(self.persons[self.currentPerson].steps)

        self.stepsLeft.setValue(self.persons[self.currentPerson].steps)
        self.stepsLeftNum.changeText(self.persons[self.currentPerson].steps)

    def recharging(self):
        self.rechargeSteps += 1
        if self.rechargeSteps < self.stepsRequired:
            self.rechargeProgress.setValue(self.rechargeSteps)
        else:
            self.hint.setVisible(True)
            self.rechargeProgress.setVisible(False)

    def gotEggs(self):
        for egg in self.eggs:
            if not egg.getStatus():
                return False

        return True
            
            


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
window()