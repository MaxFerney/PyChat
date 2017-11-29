# Imports
import pygame
import os
import time
import random

# Colors
WHITE =     ( 255, 255, 255 )
GRAY =      ( 125, 125, 125 )
BLACK =     (   0,   0,   0 )
RED =       ( 255,   0,   0 )
BLUE =      (   0,   0, 255 )

class Player:
    name = ""
    color = BLUE
    chipsLeft = 15
    chipsStandard = 15
    chipsKing = 0
    cp = []
    cpSpawn = []
    chips = []
    
    controls = {"TR":pygame.K_e,
                "TL":pygame.K_q,
                "BR":pygame.K_c,
                "BL":pygame.K_z}
    side = "right"
    occupied = []

    def __init__(self, name, color, cpSpawn, side):
        self.name = name
        self.color = color
        self.cpSpawn = cpSpawn
        self.side = side

        # other initializing variables
        self.spawn()
        self.occupied = list()
        for c in self.chips:
            self.occupied.append(c.pos)
        
    def draw(self, screen):
        for c in self.chips:
            c.draw(screen)

    def makeToChip(self):
        for cpos in self.cp:
            chip = Chip(cpos, self.color)
            self.chips.append(chip)

    def move(self, pos1, pos2):
        #pos3 = [0, 0]
        for c in self.chips:
            index = self.chips.index(c)
            if pos1 == self.chips[index].pos:#exists at chip pos
                if not self.chips[index].isKing:#not king
                    posx = self.chips[index].pos[0]
                    posy = self.chips[index].pos[1]
                    if self.side == "right":
                        if posx-1 == pos2[0] and \
                           (posy-1 == pos2[1] or \
                            posy+1 == pos2[1]):
                            self.chips[index].pos = pos2
                        else:
                            print("invalid")
                    if self.side == "left":
                        if posx+1 == pos2[0] and \
                           (posy+1 == pos2[1] or \
                            posy-1 == pos2[1]):
                            self.chips[index].pos = pos2
                        else:
                            print("invalid")
                else:
                    posx = self.chips[index].pos[0]
                    posy = self.chips[index].pos[1]
                    if posx-1 == pos2[0] and \
                       (posy-1 == pos2[1] or \
                        posy+1 == pos2[1]):
                        self.chips[index].pos = pos2
                        
                    if posx+1 == pos2[0] and \
                       (posy+1 == pos2[1] or \
                        posy-1 == pos2[1]):
                        self.chips[index].pos = pos2
                    else:
                        print("invalid")
        
        self.occupied = list()
        for c in self.chips:
            self.occupied.append(c.pos)
        
    def spawn(self):
        self.cp = self.cpSpawn
        self.chips = list()
        self.makeToChip()
        self.occupied = list()
        for c in self.chips:
            self.occupied.append(c.pos)

    def killTheChip(self, pos):
        for c in self.chips:
            index = self.chips.index(c)
            if pos == c.pos:
                if self.chips[index].isKing:
                    self.chipsLeft-=1
                    self.chipsKing-=1
                    del(self.chips[index])
                else:
                    self.chipsLeft-=1
                    self.chipsStandard-=1
                    del(self.chips[index])

    def takenTiles(self):
        return self.occupied


    def kingMe(self, pos):
        for c in self.chips:
            index = self.chips.index(c)
            if pos == c.pos:
                if self.chips[index].isKing:
                    self.chips[index].isKing = False
                    self.chipsStandard += 1
                    self.chipsKing -= 1
                else:
                    self.chips[index].isKing = True
                    self.chipsStandard -= 1
                    self.chipsKing += 1

    def makeNewChip(self, pos):
        for c in self.chips:
            index = self.chips.index(c)
            if not pos == c.pos:
                chip = Chip(pos, self.color)
                self.chips.append(chip)
                self.chipsStandard+=1
                self.chipsLeft+=1



# Colors
WHITE =     ( 255, 255, 255 )
GRAY =      ( 125, 125, 125 )
BLACK =     (   0,   0,   0 )
RED =       ( 255,   0,   0 )
BLUE =      (   0,   0, 255 )

class Chip:
    color = GRAY
    pos = [0, 0]
    size = [50, 50]
    isValid = True
    askQuestion = False
    mayMove = True
    isKing = False
    canJump = False

    def __init__(self, pos, color=GRAY, isValid=True):
        self.pos = pos
        self.color = color
        self.isValid = isValid

    def draw(self, screen):
        pos = self.pos
        color = self.color
        c = Tile(self.pos, color)
        Cpos = c.getPos()
        rect = [(Cpos[0]*60)+5,
                (Cpos[1]*60)+5,
                int(self.size[0]),
                int(self.size[1])]
        if self.isKing:
            w = 0
        else:
            w = 5
        pygame.draw.ellipse(screen, color, rect, w)

##        if self.isKing:
##            rect = [(Cpos[0]*60)+10,
##                    (Cpos[1]*60)+10,
##                    int(self.size[0]-5),
##                    int(self.size[1]-5)]
##            pygame.draw.ellipse(screen, color, rect)

##    def canJump(self, chips, Otiles, pos1, pos2):
##        for c in chips:
##            index = chips.index(c)
##            if pos

        
                           
    def __str__(self):
        return str(self.pos[0]) + "," + str(self.pos[1])


# Colors
WHITE =     ( 255, 255, 255 )
BLACK =     (   0,   0,   0 )
GRAY =      ( 125, 125, 125 )
RED =       ( 255,   0,   0 )
GREEN =     (   0, 255,   0 )
BLUE =      (   0,   0, 255 )


class Tile:
    color = BLUE
    size = [60, 60]
    pos = [0, 0]
    name = ["A", "1"]

    def __init__(self, pos=[0, 0], color=GRAY):
        self.pos = pos
        self.color = color

    def posnamex(self):
        if self.pos[1] == 0:
            self.name[0] = "A"
        if self.pos[1] == 1:
            self.name[0] = "B"
        if self.pos[1] == 2:
            self.name[0] = "C"
        if self.pos[1] == 3:
            self.name[0] = "D"
        if self.pos[1] == 4:
            self.name[0] = "E"
        if self.pos[1] == 5:
            self.name[0] = "F"
        if self.pos[1] == 6:
            self.name[0] = "G"
        if self.pos[1] == 7:
            self.name[0] = "H"
        if self.pos[1] == 8:
            self.name[0] = "I"
        if self.pos[1] == 9:
            self.name[0] = "J"
    def posnamey(self):
        self.name[1] = str( (self.pos[0])+1 )

    def values(self):
        self.posnamex()
        self.posnamey()
        return {"name":     self.name,
                "pos":      self.pos,
                "color":    self.color,
                "size":     self.size}

    def getText(self):
        self.values()
        return str(self.name[0] + self.name[1])

    def getPos(self):
        self.values()
        return self.pos
        
    def __str__(self):
        self.values()
        return "Name: " + self.name[0] + self.name[1]



class Board:
    size = [10, 10]
    primary = RED
    secondary = BLACK
    tile_size = [60, 60]

    def __init__(self,
                 size=[10, 10],
                 primary=RED,
                 secondary=BLACK,
                 tile_size=[60, 60]):
        
        self.size = size
        self.primary = primary
        self.secondary = secondary
        self.tile_size = tile_size

    def draw(self, screen):
        color = {"prim": self.primary,
                 "sec" : self.secondary}
        size = self.size
        tile_size = self.tile_size
        
        font = pygame.font.Font(None, 30)
        
        # row odd
        x = 0
        y = 0
        while x < (size[0]):
            y = 0
            while y < (size[1]):
                pygame.draw.rect(screen, color["prim"], [x*60, y*60, tile_size[0], tile_size[1]])
                text = font.render(Tile([x, y]).getText(), True, Tile([x, y]).color)
                screen.blit(text, [x*60, y*60])
                y+=2
            
            x+=2

        x = 1
        y = 0
        while x < (size[0]):
            y = 0
            while y < (size[1]):
                pygame.draw.rect(screen, color["sec"], [x*60, y*60, tile_size[0], tile_size[1]])
                text = font.render(Tile([x, y]).getText(), True, Tile([x, y]).color)
                screen.blit(text, [x*60, y*60])
                y+=2
            x+=2

        # row even

        x = 1
        y = 1
        while x < (size[0]):
            y = 1
            while y < (size[1]):
                pygame.draw.rect(screen, color["prim"], [x*60, y*60, tile_size[0], tile_size[1]])
                text = font.render(Tile([x, y]).getText(), True, Tile([x, y]).color)
                screen.blit(text, [x*60, y*60])
                y+=2
            
            x+=2

        x = 0
        y = 1
        while x < (size[0]):
            y = 1
            while y < (size[1]):
                pygame.draw.rect(screen, color["sec"], [x*60, y*60, tile_size[0], tile_size[1]])
                text = font.render(Tile([x, y]).getText(), True, Tile([x, y]).color)
                screen.blit(text, [x*60, y*60])
                y+=2
            x+=2

            
                

class RunGameEC:
    def main():





        # Initialize game engine
        pygame.init()


        # Window
        SIZE = (900, 600)
        TITLE = "Executive Checkers"
        screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)


        # Timer
        clock = pygame.time.Clock()
        refresh_rate = 250


        # Colors
        WHITE =     ( 255, 255, 255 )
        GRAY =      ( 125, 125, 125 )
        BLACK =     (   0,   0,   0 )
        RED =       ( 255,   0,   0 )
        BLUE =      (   0,   0, 255 )

        # Functions
        ##def isOccupied(plist, pos):
        ##    #param pos: position trying to move to
        ##    for player in plist:
        ##        indexp = plist.index(player)
        ##        for o in player.chips.pos:
        ##            indexo = player.takenTiles().index(o)
        ##            if pos == o:
        ##                print("Taken By: "+str(plist[indexp].name))
        ##                return True
        ##            else:
        ##                print("Empty Tile!")
        ##                return False
        ##


        # Initial Variables
        CheckerBoard = Board([10, 10], BLACK, WHITE, [60, 60])

        redchips = [[0, 0], [0, 2], [0, 4], [0, 6], [0, 8],
                    [1, 1], [1, 3], [1, 5], [1, 7], [1, 9],
                    [2, 0], [2, 2], [2, 4], [2, 6], [2, 8]]

        bluechips = [[7, 1], [7, 3], [7, 5], [7, 7], [7, 9],
                     [8, 0], [8, 2], [8, 4], [8, 6], [8, 8],
                     [9, 1], [9, 3], [9, 5], [9, 7], [9, 9]]

        p1 = Player("Player 1", RED, redchips, "left")
        p2 = Player("Player 2", BLUE, bluechips, "right")

        players = [p1, p2]

        selectedpos1=[]
        selectedpos2=[]
        kingpos=[]
        newredpos=[]
        newbluepos=[]

        madeSelection = False
        madeSelection2 = False
        kinging=False
        redding=False
        bluing=False

        occupiedTiles = []

        # Game loop

        done = False

        while not done:
            # Event processing (React to key presses, mouse clicks, etc.)
            mousepos1 = pygame.mouse.get_pos()
            mousepos = list(mousepos1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                

                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not madeSelection:
                        selectedpos1 = mousepos
                        print(selectedpos1)
                        selectedpos1[0] = selectedpos1[0]//60
                        selectedpos1[1] = selectedpos1[1]//60
                        
                        madeSelection = True
                        print("1")
                        
                    else:
                        selectedpos2 = mousepos
                        print(selectedpos2)
                        selectedpos2[0] = selectedpos2[0]//60
                        selectedpos2[1] = selectedpos2[1]//60
                        
                        madeSelection2 = True
                        print("2")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:         #Kinging
                    
                        kingpos = mousepos
                        kingpos[0] = kingpos[0]//60
                        kingpos[1] = kingpos[1]//60
                        kinging = True
                        print("Kinging: True")

                    elif event.key == pygame.K_r:       #Redding

                        newredpos = mousepos
                        newredpos[0] = newredpos[0]//60
                        newredpos[1] = newredpos[1]//60
                        redding = True
                        print("Redding: True")

                    elif event.key == pygame.K_b:       #Bluing

                        newbluepos = mousepos
                        newbluepos[0] = newbluepos[0]//60
                        newbluepos[1] = newbluepos[1]//60
                        bluing = True
                        print("Bluing: True")


            # Game logic
            clicks = pygame.mouse.get_pressed()
            if clicks[0]:
                pass

            occupiedTiles = list()
            for p in players:
                for c in p.chips:
                    occupiedTiles.append(c.pos)
            
            
            ''' moving '''
            if madeSelection2:
                for p in players:
                    index = players.index(p)
        ##            if not isOccupied(players, selectedpos2):
        ##            for o in occupiedTiles:
                    if not selectedpos2 in occupiedTiles:
                        p.move(selectedpos1, selectedpos2)
                    elif selectedpos2 == selectedpos1:
                        p.killTheChip(selectedpos1)
                            
                            
                print("pos1: "+str(selectedpos1[0]),str(selectedpos1[1]))
                print("pos2: "+str(selectedpos2[0]),str(selectedpos2[1]))
                selectedpos1 = list()
                selectedpos2 = list()
                madeSelection = False
                madeSelection2 = False
                
                print("---------------------")
            ''' making king '''
            if kinging:
                for p in players:
                    index = players.index(p)
                    if kingpos in occupiedTiles:
                        players[index].kingMe(kingpos)
                kinging = False
                kingpos = list()

            ''' making blue chip '''
            if bluing:
                for p in players:
                    index = players.index(p)
                    if not newbluepos in occupiedTiles:
                        if p.color == BLUE:
                            players[index].makeNewChip(newbluepos)
                bluing = False
                newbluepos = list()

            ''' making red chip '''
            if redding:
                for p in players:
                    index = players.index(p)
                    if not newredpos in occupiedTiles:
                        if p.color == RED:
                            players[index].makeNewChip(newredpos)
                redding = False
                newredpos = list()


            
            occupiedTiles = list()
            for p in players:
                for c in p.chips:
                    occupiedTiles.append(c.pos)

            ''' fill '''
            screen.fill(BLACK)
            CheckerBoard.draw(screen)
            
            for p in players:
                p.draw(screen)

            if madeSelection:
                for p in players:
                    indexp = players.index(p)
                    for c in p.chips:
                        indexc = p.chips.index(c)
                        if selectedpos1 == c.pos:
                            font = pygame.font.Font(None, 40)
                            txtstr= ("Selected Position 1:")
                            txtpos= Tile(selectedpos1).getText()
                            text1 = font.render(txtstr, True, players[indexp].color)
                            text2 = font.render(txtpos, True, players[indexp].color)
                            text3 = font.render((str(players[indexp].name)), True, players[indexp].color)
                            screen.blit(text1, [650, 20])
                            screen.blit(text2, [650, 60])
                            screen.blit(text3, [650, 100])
            

            # Update screen
            pygame.display.flip()
            clock.tick(refresh_rate)


        # Close window on quit
        pygame.quit()
