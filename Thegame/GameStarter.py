from house import Room

junk = Room(-2, "nothing", "nothing")
wall = Room(-1, "nothing", "nothing")
wall.setSurroundings(junk, junk, junk, junk)
wall.setDirections(junk, junk, junk, junk)
room = ['']*30

directory = "Pics/"

room[0] = Room(0, directory + "Background 0.png","Home World")
room[1] = Room(1, directory + "Background 1.png", "Hydro World")
room[2] = Room(2, directory + "Background 2.png", "Flame Thrower")
room[3] = wall
room[4] = Room(4, directory + "Background 3.png", "Ice World")
room[5] = Room(5, directory + "Background 4.png", " Space")
room[6] = Room(6, directory + "Background 5.png", "Alien World")
room[7] = Room(7, directory + "Background 6.png", "Lights Shining")
room[8] = wall
room[9] = Room(9, directory + "Background 7.png", "Forest Leaves")
room[10] = Room(10, directory + "Background 8.png", "Snow Flake")
room[11] = Room(11, directory + "Background 9.png", "Heavy Clouds")
room[12] = Room(12, directory + "Background 10.png", "World of Worlds")
room[13] = wall
room[14] = Room(14, directory + "Background 11.png", "Graveyard")
room[15] = wall
room[16] = Room(16, directory + "Background 12.png", "Green Vision")
room[17] = Room(17, directory + "Background 13.png", "Prodigy Room")
room[18] = wall
room[19] = Room(19, directory + "Background 14.png", "Diamond")
room[20] = wall
room[21] = Room(21, directory + "Background 15.png", "Forest Ground")
room[22] = Room(22, directory + "Background 16.png", "Water Drop")
room[23] = Room(23, directory + "Background 17.png", "Floral")
room[24] = Room(24, directory + "Background 18.png", "Universal Disk")
room[25] = Room(25, directory + "Background 19.png", "Infinity Globe")
room[26] = Room(26, directory + "Background 20.png", "Red Timeline")
room[27] = Room(27, directory + "Background 21.png", "Silly World")
room[28] = Room(28, directory + "Background 22.png", "Mixed World")
room[29] = Room(29, directory + "Background 14.png", "Cloud Mountains")

y = 511/5
y2 = int(y+7.8)
fory = 2
x = int(711/6)
x2 = int(x-63)
forx = 2
for i in range(0, 30):
    room[i].setDir(x2, y2)
    
    if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
        fory = 1
        x2 = (x*forx)-63
        forx += 1
    y2 = (y*fory) + 7.8
    fory += 1
    if i == 3 or i == 8 or i == 13 or i == 18:
        y2 -= 48.8
    
    y2 = int(y2)
    x2 = int(x2)

for i in range(4, 28):
    nums = [3,3,3,3,0,1,2,4,5,6,7,9,10,11,12,14,16,17,19,21,22,23,24,25,26,27,28,29,3,3,3,3,3]
    indexN = nums[i-1]
    indexE = nums[i+4]
    indexS = nums[i+1]
    indexW = nums[i-4]
    if nums[i] >= 11 and nums[i] <= 19:
        indexE = nums[i+3]
    if nums[i] >= 16 and nums[i] <= 23:
        indexW = nums[i-3]
    if nums[i] >= 21 and nums[i] <= 29:
        indexE = nums[i+5]
    if nums[i] >= 25 and nums[i] <= 29:
        indexW = nums[i-5]
    if nums[i] == 0 or nums[i] == 1 or nums[i] == 2 or nums[i] == 4 or nums[i] == 25:
        indexW = 3
    if nums[i] == 0 or nums[i] == 5 or nums[i] == 10 or nums[i] == 16 or nums[i] == 21 or nums[i] == 25:
        indexN = 3
    if nums[i] == 10 or nums[i] == 25 or nums[i] == 26 or nums[i] == 27 or nums[i] == 28 or nums[i] == 29:
        indexE = 3
    if nums[i] == 4 or nums[i] == 9 or nums[i] == 14 or nums[i] == 19 or nums[i] == 24 or nums[i] == 29:
        indexS = 3


    room[nums[i]].setSurroundings(room[indexN], room[indexE], room[indexS], room[indexW])

for r in room:
    if r.getId() != -1:
        r.setAround()



room[0].setDirections(wall, wall, room[1], wall)
room[1].setDirections(room[0], room[6], room[2], wall)
room[2].setDirections(room[1], wall, room[4], wall)
room[4].setDirections(room[2], room[9], wall, wall)
room[5].setDirections(wall, room[10], room[6], wall) 
room[6].setDirections(room[5], wall, wall, room[1])
room[7].setDirections(wall, room[12], wall, wall)
room[9].setDirections(wall, room[14], wall, room[4])
room[10].setDirections(wall, wall, room[11], room[5])
room[11].setDirections(room[10], wall, room[12], wall)
room[12].setDirections(room[11], room[17], room[14], room[7])
room[14].setDirections(room[12], room[19], wall, room[9])
room[16].setDirections(wall, room[21], room[17], wall)
room[17].setDirections(room[16], wall, wall, room[12])
room[19].setDirections(wall, wall, wall, room[14])
room[21].setDirections(wall, room[26], room[22], room[16])
room[22].setDirections(room[21], wall, room[23], wall)
room[23].setDirections(room[22], room[28], room[24], wall)
room[24].setDirections(room[23], wall, wall, wall)
room[25].setDirections(wall, wall, room[26], wall)
room[26].setDirections(room[25], wall, room[27], room[21])
room[27].setDirections(room[26], wall, wall, wall)
room[28].setDirections(wall, wall, room[29], room[23])
room[29].setDirections(room[28], wall, wall, wall)