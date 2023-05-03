class Egg:
    def __init__(self, name, picture, roomId):
        self._room = roomId
        self.picture = picture
        self._name = name
        self._pickedup = False
    

    def getId(self):
        return self._room

    def pickup(self):
        self._pickedup = True

    def getStatus(self):
        return self._pickedup

    def getName(self):
        return self._name


class Room:
    def __init__(self, roomId, picture, name):
        self._roomId = roomId
        self.picture = picture
        self.name = name
        self.north = True
        self.east = True
        self.south = True
        self.west = True
        self.isVisited = False


    def getName(self):
        return self.name

    def getPic(self):
        return self.picture

    def setSurroundings(self, north, east, south, west):
        self.northSur = north
        self.southSur = south
        self.eastSur = east
        self.westSur = west
        

    def setAround(self):
        self.northEastSur = self.eastSur.northSur
        self.southEastSur = self.eastSur.southSur
        self.northWestSur = self.westSur.northSur
        self.southWestSur = self.westSur.southSur

    def getSurroundings(self):
        return (self.northSur, self.eastSur, self.southSur, self.westSur, self.northEastSur, self.southEastSur, self.northWestSur, self.southWestSur)

    def getId(self):
        return self._roomId

    def setDir(self, roomX, roomY):
        self.roomX = roomX
        self.roomY = roomY

    def getDirection(self):
        return (self.roomX, self.roomY)

    def setDirections(self, north, east, south, west):
        self.north = north
        self.east = east
        self.south = south
        self.west = west


class Person:
    def __init__(self, picture, name, currentRoom):
        self._name = "{n:.15}".format(n=name)
        self._currentRoom = currentRoom
        self.picture = picture
        self.canGo = True
        self.steps = 20
        self.say = ""
        self.hitWall = 0
        self.stepsUsed = 0
        self.objectsGot = 0


    def getRoom(self):
        return self._currentRoom

    def getName(self):
        return self._name


    def setName(self, newName):
        self._name = "{n:.15}".format(n=newName)

    def move(self, where, includeSteps=True):
        if not includeSteps:
            self.steps = 1
        if self.steps > 0:
            if where == 'w':
                if self._currentRoom.north.getId() == -1:
                    self.hitWall += 1
                    self.say = "You cannot go there"
                    self.canGo = False
                
                else:
                    self.stepsUsed += 1
                    self.say = ""
                    self.canGo = True
                    self._currentRoom = self._currentRoom.north


            elif where == 's':
                if self._currentRoom.south.getId() == -1:
                    self.hitWall += 1
                    self.say = "You cannot go there"
                    self.canGo = False
                
                else:
                    self.stepsUsed += 1
                    self.say = ""
                    self.canGo = True
                    self._currentRoom = self._currentRoom.south


            elif where == 'd':
                if self._currentRoom.east.getId() == -1:
                    self.hitWall += 1
                    self.say = "You cannot go there"
                    self.canGo = False
                
                else:
                    self.stepsUsed += 1
                    self.say = ""
                    self.canGo = True
                    self._currentRoom = self._currentRoom.east


            elif where == 'a':
                if self._currentRoom.west.getId() == -1:
                    self.hitWall += 1
                    self.say = "You cannot go there"
                    self.canGo = False
                
                else:
                    self.stepsUsed += 1
                    self.say = ""
                    self.canGo = True
                    self._currentRoom = self._currentRoom.west


            else:
                self.say = "That is the end"
                self.canGo = False

            if includeSteps:
                self.steps -= 1

        else:
            self.say = "This person does not have enough steps to move"
            self.canGo = False
        