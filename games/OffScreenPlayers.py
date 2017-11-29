# Imports
import pygame

class Player:
    SPEED = 2
    name = 'Player... forgot to insert name'
    x = 0
    y = 0
    w = 10
    h = 10
    v_x = 0
    v_y = -SPEED
    d = 0
    left = None
    right = None
    color = (255,255,255)
    qua = 5
    distance = 0

    def __init__(self, name, x, y, left, right, color=(255,255,255)):
        self.name = name
        self.x = x
        self.y = y
        self.left = left
        self.right = right
        self.color = color

    def draw_player(self, Scrn):
        pos = [self.x, self.y]
        size = [self.w, self.h]
        pygame.draw.rect(Scrn, self.color, [pos, size])

    def display(self, Scrn):
        if self.qua != 5:
            font = pygame.font.Font(None, 30)
            text = font.render(str(self.name)+\
                               " Distance="+\
                               str(self.distance)+\
                               "px", True, self.color)
            
            if self.qua == 4:      #left
                Scrn.blit(text, [10, self.y])
            elif self.qua == 6:    #right
                Scrn.blit(text, [650, self.y])
            elif self.qua == 8:    #top
                Scrn.blit(text, [self.x, 10])
            elif self.qua == 2:    #bottom
                Scrn.blit(text, [self.x, 590])

    def intersects(pos1, size1, pos2, size2):
        x1_min = pos1[0]
        y1_min = pos1[1]
        x1_max = pos1[0] + size1[0]
        y1_max = pos1[1] + size1[1]

        x2_min = pos2[0]
        y2_min = pos2[1]
        x2_max = pos2[0] + size2[0]
        y2_max = pos2[1] + size2[1]

        if x1_max < x2_min or x1_min > x2_max or \
           y1_max < y2_min or y1_min > y2_max:
            return False
        else:
            return True


    

class RunGameOSP:
    def main():

        # Initialize game engine
        pygame.init()


        # Window
        SIZE = (800, 600)
        TITLE = "TESTING... kinda"
        screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)


        # Timer
        clock = pygame.time.Clock()
        refresh_rate = 30


        # Colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        YELLOW = (255, 255, 0)
        # Variables
        SPEED = 2

        # Locations
        corners = {'upleft':[-5000, 0],
                   'upright':[800,0],
                   'downleft':[0,600],
                   'downright':[800,600]}

        borders = {'left':0,#x
                   'right':SIZE[0],#x
                   'top':0,#y
                   'bottom':SIZE[1]}#y

        # Players

            

        p1 = Player('Player 1', 200, 300, pygame.K_LEFT, pygame.K_RIGHT, RED)
        p2 = Player('Player 2', 600, 300, pygame.K_a, pygame.K_d, BLUE)
        #p3 = Player('Player 3', 300, 300, pygame.K_q, pygame.K_e, (255, 255, 0))

            

        # Initial Variables
        players = [p1, p2]#, p3]


        # Game loop
        done = False

        while not done:
            # Event processing (React to key presses, mouse clicks, etc.)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    for p in players:
                        if event.key == p.right:
                            p.d += 1
                            if p.d > 3:
                                p.d = 0
                        elif event.key == p.left:
                            p.d -= 1
                            if p.d < 0:
                                p.d = 3

                
            # Game logic
            ''' offscreen '''
            for p in players:
        ##        if p['x']>borders['left'] or p['x']<borders['right'] or \
        ##           p['y']>borders['top'] or p['y']<borders['bottom']:
        ##            p['qua'] = 5
                if p.x < borders['left']:
                    p.qua = 4
                    p.distance = p.x*-1
                elif p.x > borders['right']:
                    p.qua = 6
                    p.distance = p.x-800
                elif p.y < borders['top']:
                    p.qua = 8
                    p.distance = p.y*-1
                elif p.y > borders['bottom']:
                    p.qua = 2
                    p.distance = p.y-600
                else:
                    p.qua = 5
                    p.distance = 0
                
            
            ''' direction '''
            for p in players:
                if p.d==0:
                    p.v_y=-SPEED
                    p.v_x=0
                elif p.d==1:
                    p.v_y=0
                    p.v_x=SPEED
                elif p.d==2:
                    p.v_y=SPEED
                    p.v_x=0
                elif p.d==3:
                    p.v_y=0
                    p.v_x=-SPEED

            ''' move '''
            for p in players:
                p.x += p.v_x
                p.y += p.v_y


                
            ''' fill '''
            screen.fill(BLACK) #alt+(3/4)
            
            ''' drawing code '''
            for p in players:
                p.draw_player(screen)

            ''' distance display '''
            for p in players:
                p.display(screen)

            
            # Update screen
            pygame.display.flip()
            clock.tick(refresh_rate)


        # Close window on quit
        pygame.quit()

