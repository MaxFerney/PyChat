import pygame
import random
#from FC2048functions import data
# Colors

#updated on 1.15.2016
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (220, 20, 220)
TEXT = (225, 125, 0)
FLAPPY = (200, 0 , 0)
BEAK = (255, 255, 125)
SKY = (125, 175, 225)
SUN = (255, 255, 200)
GRASS1 = (0, 175, 0)
GRASS2 = (0, 150, 0)
SAND1 = (225, 225, 150)
SAND2 = (175, 175, 100)
PIPE = (25, 125, 25)
GOLD1 = (230, 200, 90)
GOLD2 = (135, 115, 15)
COLOR = FLAPPY
colorlst = [BLACK,  #0
            WHITE,  #1
            PURPLE, #2
            TEXT,   #3
            FLAPPY, #4
            BEAK,   #5
            SKY,    #6
            SUN,    #7
            GRASS1, #8
            GRASS2, #9
            SAND1,  #10
            SAND2,  #11
            PIPE,   #12
            GOLD1,  #13
            GOLD2,  #14
            COLOR]  #15
            
DISC1 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
DISC2 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
DISC3 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
DISC4 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
DISC5 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
DISC6 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
DISC7 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
DISC8 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
DISC9 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
DISCO = []
DISCO.append(DISC1)
DISCO.append(DISC2)
DISCO.append(DISC3)
DISCO.append(DISC4)
DISCO.append(DISC5)
DISCO.append(DISC6)
DISCO.append(DISC7)
DISCO.append(DISC8)
DISCO.append(DISC9)
DISCO_COL = DISCO[random.randrange(0, 9)]


class data:


    

    def disco():
        global col
        col = ((random.randrange(0, 255),
                random.randrange(0, 255),
                random.randrange(0, 255)))
        
    def draw_flappy(facing, screen, position):
        global colorlst
        x = position[0]
        y = position[1]
        
        pygame.draw.rect(screen, colorlst[15], [x, y, 50, 50])
        pygame.draw.rect(screen, colorlst[0], [x, y, 50, 50], 2)

        if facing:
            pygame.draw.polygon(screen, colorlst[5], [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]])
            pygame.draw.polygon(screen, colorlst[0], [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]], 2)
            pygame.draw.rect(screen, colorlst[15], [x - 10, y + 20, 40, 10])
            pygame.draw.rect(screen, colorlst[0], [x - 10, y + 20, 40, 10], 2)
            pygame.draw.rect(screen, colorlst[1], [x + 35, y + 5, 10, 10])
            pygame.draw.rect(screen, colorlst[0], [x + 35, y + 5, 10, 10], 2)
            pygame.draw.rect(screen, colorlst[0], [x + 40, y + 10, 5, 5])
        else:
            pygame.draw.polygon(screen, colorlst[5], [[x, y + 20], [x - 10, y + 25], [x, y + 30]])
            pygame.draw.polygon(screen, colorlst[0], [[x, y + 20], [x -10, y + 25], [x, y + 30]], 2)
            pygame.draw.rect(screen, colorlst[15], [x + 20, y + 20, 40, 10])
            pygame.draw.rect(screen, colorlst[0], [x + 20, y + 20, 40, 10], 2)
            pygame.draw.rect(screen, colorlst[1], [x + 5, y + 5, 10, 10])
            pygame.draw.rect(screen, colorlst[0], [x + 5, y + 5, 10, 10], 2)
            pygame.draw.rect(screen, colorlst[0], [x + 5, y + 10, 5, 5])

    def draw_cloud(screen, position):
        global colorlst
        x = position[0]
        y = position[1]
        pygame.draw.ellipse(screen, colorlst[1], [x, y + 20, 40 , 40])
        pygame.draw.ellipse(screen, colorlst[1], [x + 60, y + 20, 40 , 40])
        pygame.draw.ellipse(screen, colorlst[1], [x + 20, y + 10, 25, 25])
        pygame.draw.ellipse(screen, colorlst[1], [x + 35, y, 50, 50])
        pygame.draw.rect(screen, colorlst[1], [x + 20, y + 20, 60, 40])

    def draw_sun(screen, position):
        global colorlst
        x = position[0]
        y = position[1]
        
        pygame.draw.ellipse(screen, colorlst[7], [x, y, 75, 75])


    def draw_grass(screen):
        global colorlst
        pygame.draw.rect(screen, colorlst[8], [0, 600, 1000, 50])
        pygame.draw.line(screen, colorlst[0], [0, 600], [1000, 600], 2)


    def draw_coin(screen, position):
        global colorlst
        x = position[0]
        y = position[1]
        
        pygame.draw.ellipse(screen, colorlst[13], [x, y, 50, 50])
        pygame.draw.ellipse(screen, colorlst[14], [x, y, 50, 50], 2)

    def draw_reset_coin(screen, position):
        global colorlst
        x = position[0]
        y = position[1]
        
        pygame.draw.ellipse(screen, colorlst[4], [x, y, 50, 50])
        pygame.draw.ellipse(screen, colorlst[1], [x, y, 50, 50], 2)

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




class RunGameFC2048:
    def main():
        # By Max Ferney
        # Imports
        


        # Initialize game engine
        pygame.init()


        # Window
        SIZE = (1000, 700)
        TITLE = "Flappy Coin 2048"
        screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)


        # Timer
        clock = pygame.time.Clock()
        refresh_rate = 25

        score = 2
        score1 = 2
        score2 = 2
        score3 = 2
        score4 = 2
        high_score = 0
        high_score_1 = 0
        high_score_2 = 0
        high_score_3 = 0
        high_score_4 = 0
        m = 2

        play = 1
        end = 2
        control = 3

        # Difficulty
        easy = "Easy"
        normal = "Normal"
        hard = "Hard"
        insane = "INSANE"

        # Colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        PURPLE = (220, 20, 220)
        TEXT = (225, 125, 0)
        FLAPPY = (200, 0 , 0)
        BEAK = (255, 255, 125)
        SKY = (125, 175, 225)
        SUN = (255, 255, 200)
        GRASS1 = (0, 175, 0)
        GRASS2 = (0, 150, 0)
        SAND1 = (225, 225, 150)
        SAND2 = (175, 175, 100)
        PIPE = (25, 125, 25)
        GOLD1 = (230, 200, 90)
        GOLD2 = (135, 115, 15)
        COLOR = FLAPPY
        DISC1 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        DISC2 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        DISC3 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        DISC4 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        DISC5 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        DISC6 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        DISC7 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        DISC8 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        DISC9 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        DISCO = []
        DISCO.append(DISC1)
        DISCO.append(DISC2)
        DISCO.append(DISC3)
        DISCO.append(DISC4)
        DISCO.append(DISC5)
        DISCO.append(DISC6)
        DISCO.append(DISC7)
        DISCO.append(DISC8)
        DISCO.append(DISC9)
        DISCO_COL = DISCO[random.randrange(0, 9)]


##        def draw_flappy(position):
##            x = position[0]
##            y = position[1]
##            
##            pygame.draw.rect(screen, COLOR, [x, y, 50, 50])
##            pygame.draw.rect(screen, BLACK, [x, y, 50, 50], 2)
##
##            if facing_right:
##                pygame.draw.polygon(screen, BEAK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]])
##                pygame.draw.polygon(screen, BLACK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]], 2)
##                pygame.draw.rect(screen, COLOR, [x - 10, y + 20, 40, 10])
##                pygame.draw.rect(screen, BLACK, [x - 10, y + 20, 40, 10], 2)
##                pygame.draw.rect(screen, WHITE, [x + 35, y + 5, 10, 10])
##                pygame.draw.rect(screen, BLACK, [x + 35, y + 5, 10, 10], 2)
##                pygame.draw.rect(screen, BLACK, [x + 40, y + 10, 5, 5])
##            else:
##                pygame.draw.polygon(screen, BEAK, [[x, y + 20], [x - 10, y + 25], [x, y + 30]])
##                pygame.draw.polygon(screen, BLACK, [[x, y + 20], [x -10, y + 25], [x, y + 30]], 2)
##                pygame.draw.rect(screen, COLOR, [x + 20, y + 20, 40, 10])
##                pygame.draw.rect(screen, BLACK, [x + 20, y + 20, 40, 10], 2)
##                pygame.draw.rect(screen, WHITE, [x + 5, y + 5, 10, 10])
##                pygame.draw.rect(screen, BLACK, [x + 5, y + 5, 10, 10], 2)
##                pygame.draw.rect(screen, BLACK, [x + 5, y + 10, 5, 5])
##
##
##        def draw_cloud(position):
##            x = position[0]
##            y = position[1]
##            
##            pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
##            pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
##            pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
##            pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
##            pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])
##
##
##        def draw_sun(position):
##            x = position[0]
##            y = position[1]
##            
##            pygame.draw.ellipse(screen, SUN, [x, y, 75, 75])
##
##
##        def draw_grass():
##            pygame.draw.rect(screen, GRASS1, [0, 600, 1000, 50])
##            pygame.draw.line(screen, BLACK, [0, 600], [1000, 600], 2)
##
##
##        def draw_coin(position):
##            x = position[0]
##            y = position[1]
##            
##            pygame.draw.ellipse(screen, GOLD1, [x, y, 50, 50])
##            pygame.draw.ellipse(screen, GOLD2, [x, y, 50, 50], 2)
##
##        def draw_reset_coin(position):
##            x = position[0]
##            y = position[1]
##            
##            pygame.draw.ellipse(screen, FLAPPY, [x, y, 50, 50])
##            pygame.draw.ellipse(screen, WHITE, [x, y, 50, 50], 2)
##
##        def intersects(pos1, size1, pos2, size2):
##            x1_min = pos1[0]
##            y1_min = pos1[1]
##            x1_max = pos1[0] + size1[0]
##            y1_max = pos1[1] + size1[1]
##
##            x2_min = pos2[0]
##            y2_min = pos2[1]
##            x2_max = pos2[0] + size2[0]
##            y2_max = pos2[1] + size2[1]
##
##            if x1_max < x2_min or x1_min > x2_max or \
##               y1_max < y2_min or y1_min > y2_max:
##                return False
##            else:
##                return True

            
        # Initial game state

        sun_pos = [800, 75]

        clouds = []
        for i in range(20):
            x = random.randrange(-200, 2200)
            y = random.randrange(-100, 300)
            clouds.append([x, y])

        stripes = []
        for i in range(0, 1000, 30):
            stripes.append(i)

        sand = []
        for i in range(250):
            x = random.randrange(0, 1200)
            y = random.randrange(650, 700)
            sand.append([x, y])
            
        flappy_pos = [300, 550]
        flappy_vel = [0, 0]
        facing_right = True


        coin_pos = [random.randrange(100, 800), random.randrange(100, 500)]
        reset_coin_pos_list = []
        for pos in range(15):
            pos = [random.randrange(100, 800), random.randrange(100, 500)]
            reset_coin_pos_list.append(pos)

                
        # hide mouse cursor over screen
        pygame.mouse.set_visible(0)


        # Game loop
        done = False
        stage = play
        difficulty = normal
        while not done:
            # Event processing (React to key presses, mouse clicks, etc.)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flappy_vel[1] = 5
                        flappy_vel[0] *= 1.2
                    elif event.key == pygame.K_RIGHT:
                        flappy_vel[0] = 5
                        facing_right = True
                    elif event.key == pygame.K_LEFT:
                        flappy_vel[0] = -5
                        facing_right = False
                    # In-Game Keys
                    elif event.key == pygame.K_c:
                        m = 8
                    elif event.key == pygame.K_g:
                        m = 256
                    elif event.key == pygame.K_n:
                        m = 2
                        COLOR = FLAPPY
                    elif event.key == pygame.K_END:
                        stage = end
                    elif event.key == pygame.K_HOME:
                        stage = play
                    elif event.key == pygame.K_d:
                        data.disco()
                        COLOR = col
                    elif event.key == pygame.K_h:
                        stage = control
                    # Difficulty
                    elif event.key == pygame.K_1:
                        difficulty = easy
                    elif event.key == pygame.K_2:
                        difficulty = normal
                    elif event.key == pygame.K_3:
                        difficulty = hard
                    elif event.key == pygame.K_4:
                        difficulty = insane
                        


            # Game logic
            
            ''' move FLAPPY '''
            flappy_pos[0] += flappy_vel[0]
            
            if flappy_vel[1] > 0:
                flappy_pos[1] -= flappy_vel[1] ** 2        
            else:
                flappy_pos[1] += 0.25 * (flappy_vel[1] ** 2)

            if flappy_pos[0] < 0:
                flappy_pos[0] = 0  
            elif flappy_pos[0] > 950:
                flappy_pos[0] = 950  

            if flappy_pos[1] < 0:
                flappy_pos[1] = 0  
            elif flappy_pos[1] > 550:
                flappy_pos[1] = 550
                flappy_vel = [0,0]

            flappy_vel[1] -= 1


            ''' check coin hit '''
            if data.intersects(flappy_pos, [50,50], coin_pos, [50, 50]):
                coin_pos[0] = random.randrange(40,900)
                coin_pos[1] = random.randrange(40,450)
                score = score * m
                if difficulty == easy:
                    score1 = score1 * m
                if difficulty == normal:
                    score2 = score2 * m
                if difficulty == hard:
                    score3 = score3 * m
                if difficulty == insane:
                    score4 = score4 * m
                
                if score >= high_score:
                    high_score = score
                
                if score1 >= high_score_1:
                    high_score_1 = score1
                if score2 >= high_score_2:
                    high_score_2 = score2
                if score3 >= high_score_3:
                    high_score_3 = score3
                if score4 >= high_score_4:
                    high_score_4 = score4
                

            ''' Difficulty spawns '''
            if difficulty == easy:
                    if data.intersects(flappy_pos, [50,50], reset_coin_pos_list[i], [50, 50]):
                        reset_coin_pos_list[i][0] = random.randrange(40,900)
                        reset_coin_pos_list[i][1] = random.randrange(40,450)
                        score = 2
                        score1 = 2
                        score2 = 2
                        score3 = 2
                        score4 = 4
                    
            if difficulty == normal:
                for i in range(5):
                    if data.intersects(flappy_pos, [50,50], reset_coin_pos_list[i], [50, 50]):
                        reset_coin_pos_list[i][0] = random.randrange(40,900)
                        reset_coin_pos_list[i][1] = random.randrange(40,450)
                        score = 2
                        score1 = 2
                        score2 = 2
                        score3 = 2
                        score4 = 4
                    
            if difficulty == hard:

                for i in range(10):
                    if data.intersects(flappy_pos, [50,50], reset_coin_pos_list[i], [50, 50]):
                        reset_coin_pos_list[i][0] = random.randrange(40,900)
                        reset_coin_pos_list[i][1] = random.randrange(40,450)
                        score = 2
                        score1 = 2
                        score2 = 2
                        score3 = 2
                        score4 = 4
                    
            if difficulty == insane:
                for i in range(15):
                    if data.intersects(flappy_pos, [50,50], reset_coin_pos_list[i], [50, 50]):
                        reset_coin_pos_list[i][0] = random.randrange(40,900)
                        reset_coin_pos_list[i][1] = random.randrange(40,450)
                        score = 2
                        score1 = 2
                        score2 = 2
                        score3 = 2
                        score4 = 4
                         
            

            ''' move clouds '''
            for c in clouds:
                c[0] -= 1

                if c[0] < -200:
                    c[0] = random.randrange(1000,2000)
                    c[1] = random.randrange(-100, 300)


            # Drawing code
            screen.fill(SKY)

            ''' sun '''
            data.draw_sun(screen, sun_pos)


            ''' clouds ''' 
            for c in clouds:
                data.draw_cloud(screen, c)
            
            ''' grass '''
            data.draw_grass(screen)

            for s in stripes:
                pygame.draw.line(screen, GRASS2, [s, 602], [s - 20, 650], 10)


            ''' sand '''
            pygame.draw.rect(screen, SAND1, [0, 650, 1000, 50])

            for s in sand:
                pygame.draw.rect(screen, SAND2, [s[0], s[1], 2, 2])
            
            pygame.draw.line(screen, BLACK, [0, 650], [1000, 650], 2)


            ''' coins '''
            '''
            draw_coin(coin_pos)
            draw_reset_coin(reset_coin_pos1)
            draw_reset_coin(reset_coin_pos2)
            draw_reset_coin(reset_coin_pos3)
            draw_reset_coin(reset_coin_pos4)
            draw_reset_coin(reset_coin_pos5)
            '''
            ''' Draw Difficulty '''
            if difficulty == easy:
                data.draw_coin(screen, coin_pos)
                for i in range(3):
                    data.draw_reset_coin(screen, reset_coin_pos_list[i])
##                data.draw_reset_coin(screen, reset_coin_pos1)
##                data.draw_reset_coin(screen, reset_coin_pos2)
##                data.draw_reset_coin(screen, reset_coin_pos3)
                
            if difficulty == normal:
                data.draw_coin(screen, coin_pos)
                for i in range(5):
                    data.draw_reset_coin(screen, reset_coin_pos_list[i])
##                data.draw_reset_coin(screen, reset_coin_pos1)
##                data.draw_reset_coin(screen, reset_coin_pos2)
##                data.draw_reset_coin(screen, reset_coin_pos3)
##                data.draw_reset_coin(screen, reset_coin_pos4)
##                data.draw_reset_coin(screen, reset_coin_pos5)
                
            if difficulty == hard:
                data.draw_coin(screen, coin_pos)
                for i in range(10):
                    data.draw_reset_coin(screen, reset_coin_pos_list[i])
##                data.draw_reset_coin(screen, reset_coin_pos1)
##                data.draw_reset_coin(screen, reset_coin_pos2)
##                data.draw_reset_coin(screen, reset_coin_pos3)
##                data.draw_reset_coin(screen, reset_coin_pos4)
##                data.draw_reset_coin(screen, reset_coin_pos5)
##                data.draw_reset_coin(screen, reset_coin_pos6)
##                data.draw_reset_coin(screen, reset_coin_pos7)
##                data.draw_reset_coin(screen, reset_coin_pos8)
##                data.draw_reset_coin(screen, reset_coin_pos9)
##                data.draw_reset_coin(screen, reset_coin_pos10)

                
            if difficulty == insane:
                data.draw_coin(screen, coin_pos)
                for i in range(15):
                    data.draw_reset_coin(screen, reset_coin_pos_list[i])
##                data.draw_reset_coin(screen, reset_coin_pos1)
##                data.draw_reset_coin(screen, reset_coin_pos2)
##                data.draw_reset_coin(screen, reset_coin_pos3)
##                data.draw_reset_coin(screen, reset_coin_pos4)
##                data.draw_reset_coin(screen, reset_coin_pos5)
##                data.draw_reset_coin(screen, reset_coin_pos6)
##                data.draw_reset_coin(screen, reset_coin_pos7)
##                data.draw_reset_coin(screen, reset_coin_pos8)
##                data.draw_reset_coin(screen, reset_coin_pos9)
##                data.draw_reset_coin(screen, reset_coin_pos10)
##                data.draw_reset_coin(screen, reset_coin_pos11)
##                data.draw_reset_coin(screen, reset_coin_pos12)
##                data.draw_reset_coin(screen, reset_coin_pos13)
##                data.draw_reset_coin(screen, reset_coin_pos14)
##                data.draw_reset_coin(screen, reset_coin_pos15)
                
                

                

            
            ''' flappy '''
            data.draw_flappy(facing_right, screen, flappy_pos)
            
            ''' score '''
            font = pygame.font.Font(None, 40)
            text1 = font.render("P1 Score: " + str(score), True, FLAPPY)
            text2 = font.render("Difficulty: " + str(difficulty), True, FLAPPY)
            screen.blit(text1, [30, 30])
            screen.blit(text2, [30, 70])

            ''' end '''
            if stage == end:
                font = pygame.font.Font(None, 60)
                text1 = font.render("HIGH SCORES:", True, BLACK)
                text2 = font.render("HIGH SCORES:", True, PURPLE)
                text3 = font.render("Easy: " + str(high_score_1), True, PURPLE)
                text4 = font.render("Normal: " + str(high_score_2), True, PURPLE)
                text5 = font.render("Hard: " + str(high_score_3), True, PURPLE)
                text6 = font.render("Insane: " + str(high_score_4), True, PURPLE)
                screen.blit(text1, [325, 125])
                screen.blit(text2, [323, 123])
                screen.blit(text3, [325, 180])
                screen.blit(text4, [325, 225])
                screen.blit(text5, [325, 270])
                screen.blit(text6, [325, 315])
            if stage == control:
                font = pygame.font.Font(None, 50)
                text1 = font.render("HELP:", True, BLACK)
                text2 = font.render("HELP:", True, PURPLE)
                text3 = font.render("Press HOME to close high score and help screen.", True, TEXT)
                text4 = font.render("left and right arrows to go left and right", True, TEXT)
                text5 = font.render("spacebar to go up. END key to open high scores ", True, TEXT)
                text6 = font.render("and h for help. press 1 for easy, 2 for normal, ", True, TEXT)
                text7 = font.render("3 for hard, and 4 for INSANE.", True, TEXT)
                screen.blit(text1, [325, 125])
                screen.blit(text2, [323, 123])
                screen.blit(text3, [150, 180])
                screen.blit(text4, [150, 225])
                screen.blit(text5, [150, 270])
                screen.blit(text6, [150, 315])
                screen.blit(text7, [150, 360])

            # Update screen
            pygame.display.flip()
            clock.tick(refresh_rate)


        # Close window on quit
        pygame.quit()

