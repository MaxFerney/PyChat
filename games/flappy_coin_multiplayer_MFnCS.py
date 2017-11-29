# Max Ferney
# Christopher Soto

# Imports
import pygame
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
PURPLE2 = (200, 10, 200)
TEXT = (225, 125, 0)
FLAPPY = (200, 0, 0)
FLAPPY2 = (0, 0, 200)
BEAK = (255, 255, 125)
SKY = (125, 175, 225)
SUN = (255, 255, 200)
GRASS1 = (0, 175, 0)
GRASS2 = (0, 150, 0)
SAND1 = (225, 225, 150)
SAND2 = (175, 175, 100)
PIPE = (25, 125, 25)
GOLD1 = (218, 153, 3)
GOLD2 = (135, 115, 15)
GOLD3 = (149, 105, 2)
BONUSGOLD = (250, 168, 56)
PLATINUM1 = (190, 191, 183)
PLATINUM2 = (164, 165, 154)
PLATINUM3 = (88, 89, 79)

flappy_pos = [300, 550]
flappy_vel = [0, 0]
facing_right = True

flappy_pos2 = [150, 550]
flappy_vel2 = [0, 0]
facing_right2 = True


coin_pos = [random.randrange(100, 600), random.randrange(100, 500)]
coin_pos2 = [random.randrange(100, 600), random.randrange(100, 500)]
bonus_coin_pos = [random.randrange(100, 600), random.randrange(100, 500)]
bad_coin_pos = [random.randrange(100, 600), random.randrange(100, 500)]
bad_coin_pos2 = [random.randrange(100, 600), random.randrange(100, 500)]
flip_coin_pos = [random.randrange(100, 800), random.randrange(100, 400)]
super_flip_coin_pos = [random.randrange(100, 800), random.randrange(100, 400)]
pipe_pos = [100, 450]
class data:
    
    def draw_flappy(screen, position):
        x = position[0]
        y = position[1]
        
        pygame.draw.rect(screen, FLAPPY, [x, y, 50, 50])
        pygame.draw.rect(screen, BLACK, [x, y, 50, 50], 2)

        if facing_right:
            pygame.draw.polygon(screen, BEAK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]])
            pygame.draw.polygon(screen, BLACK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]], 2)
            pygame.draw.rect(screen, FLAPPY, [x - 10, y + 20, 40, 10])
            pygame.draw.rect(screen, BLACK, [x - 10, y + 20, 40, 10], 2)
            pygame.draw.rect(screen, WHITE, [x + 35, y + 5, 10, 10])
            pygame.draw.rect(screen, BLACK, [x + 35, y + 5, 10, 10], 2)
            pygame.draw.rect(screen, BLACK, [x + 40, y + 10, 5, 5])
        else:
            pygame.draw.polygon(screen, BEAK, [[x, y + 20], [x - 10, y + 25], [x, y + 30]])
            pygame.draw.polygon(screen, BLACK, [[x, y + 20], [x -10, y + 25], [x, y + 30]], 2)
            pygame.draw.rect(screen, FLAPPY, [x + 20, y + 20, 40, 10])
            pygame.draw.rect(screen, BLACK, [x + 20, y + 20, 40, 10], 2)
            pygame.draw.rect(screen, WHITE, [x + 5, y + 5, 10, 10])
            pygame.draw.rect(screen, BLACK, [x + 5, y + 5, 10, 10], 2)
            pygame.draw.rect(screen, BLACK, [x + 5, y + 10, 5, 5])

    def draw_flappy2(screen, position):
        x = position[0]
        y = position[1]
        
        pygame.draw.rect(screen, FLAPPY2, [x, y, 50, 50])
        pygame.draw.rect(screen, BLACK, [x, y, 50, 50], 2)

        if facing_right2:
            pygame.draw.polygon(screen, BEAK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]])
            pygame.draw.polygon(screen, BLACK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]], 2)
            pygame.draw.rect(screen, FLAPPY2, [x - 10, y + 20, 40, 10])
            pygame.draw.rect(screen, BLACK, [x - 10, y + 20, 40, 10], 2)
            pygame.draw.rect(screen, WHITE, [x + 35, y + 5, 10, 10])
            pygame.draw.rect(screen, BLACK, [x + 35, y + 5, 10, 10], 2)
            pygame.draw.rect(screen, BLACK, [x + 40, y + 10, 5, 5])
        else:
            pygame.draw.polygon(screen, BEAK, [[x, y + 20], [x - 10, y + 25], [x, y + 30]])
            pygame.draw.polygon(screen, BLACK, [[x, y + 20], [x -10, y + 25], [x, y + 30]], 2)
            pygame.draw.rect(screen, FLAPPY2, [x + 20, y + 20, 40, 10])
            pygame.draw.rect(screen, BLACK, [x + 20, y + 20, 40, 10], 2)
            pygame.draw.rect(screen, WHITE, [x + 5, y + 5, 10, 10])
            pygame.draw.rect(screen, BLACK, [x + 5, y + 5, 10, 10], 2)
            pygame.draw.rect(screen, BLACK, [x + 5, y + 10, 5, 5])


    def draw_cloud(screen, position):
        x = position[0]
        y = position[1]
        
        pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
        pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
        pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
        pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
        pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])


    def draw_sun(screen, position):
        x = position[0]
        y = position[1]
        
        pygame.draw.ellipse(screen, SUN, [x, y, 75, 75])


    def draw_grass(screen):
        pygame.draw.rect(screen, GRASS1, [0, 600, 1000, 50])
        pygame.draw.line(screen, BLACK, [0, 600], [1000, 600], 2)


    def draw_coin(screen, position):
        x = position[0]
        y = position[1]
        
        pygame.draw.ellipse(screen, BONUSGOLD, [x, y, 50, 50])
        pygame.draw.ellipse(screen, GOLD2, [x, y, 50, 50], 2)
        pygame.draw.rect(screen, GOLD1, [x + 20, y + 10, 10, 30])
        pygame.draw.rect(screen, GOLD3, [x + 20, y + 10, 10, 30], 1)

    def draw_bonus_coin(screen, position):
        x = position[0]
        y = position[1]
        
        pygame.draw.ellipse(screen, PLATINUM1, [x, y, 50, 50])
        pygame.draw.ellipse(screen, GOLD2, [x, y, 50, 50], 2)
        pygame.draw.rect(screen, PLATINUM2, [x + 20, y + 10, 10, 30])
        pygame.draw.rect(screen, PLATINUM3, [x + 20, y + 10, 10, 30], 1)

    def draw_bad_coin(screen, position):
        x = position[0]
        y = position[1]
        
        pygame.draw.ellipse(screen, FLAPPY, [x, y, 50, 50])
        pygame.draw.ellipse(screen, WHITE, [x, y, 50, 50], 2)
        pygame.draw.rect(screen, PLATINUM2, [x + 10, y + 20, 30, 10])
        pygame.draw.rect(screen, PLATINUM3, [x + 10, y + 20, 30, 10], 1)

    def draw_flip_coin(screen, position):
        x = position[0]
        y = position[1]
        
        pygame.draw.ellipse(screen, GRASS1, [x, y, 50, 50])
        pygame.draw.ellipse(screen, GOLD2, [x, y, 50, 50], 2)
        pygame.draw.rect(screen, GRASS2, [x + 10, y + 20, 30, 10])
        pygame.draw.rect(screen, GOLD1, [x + 20, y + 10, 10, 30], 1)

    def draw_super_flip_coin(screen, position):
        x = position[0]
        y = position[1]
        
        pygame.draw.ellipse(screen, PURPLE, [x, y, 50, 50])
        pygame.draw.ellipse(screen, GOLD2, [x, y, 50, 50], 2)
        pygame.draw.rect(screen, PURPLE2, [x + 10, y + 20, 30, 10])
        pygame.draw.rect(screen, GOLD1, [x + 20, y + 10, 10, 30], 1)

    def draw_pipes(screen, position):
        x = position[0]
        y = position[1]

        pygame.draw.rect(screen, PIPE, [x, y, 105, 50])
        pygame.draw.rect(screen, BLACK, [x, y, 105, 50], 3)
        pygame.draw.rect(screen, PIPE, [x+15, y+50, 75, 100])
        pygame.draw.rect(screen, BLACK, [x+15, y+50, 75, 100], 3)
        pygame.draw.rect(screen, PIPE, [x+15, y-450, 75, 200])
        pygame.draw.rect(screen, BLACK, [x+15, y-450, 75, 200], 3)
        pygame.draw.rect(screen, PIPE, [x, y-250, 105, 50])
        pygame.draw.rect(screen, BLACK, [x, y-250, 105, 50], 3)
        

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



class RunGameFCM_MFCS:
    def main():


        # Initialize game engine
        pygame.init()


        # Window
        SIZE = (1000, 700)
        TITLE = "Flappy Coin Multiplayer"
        screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)


        # Timer
        clock = pygame.time.Clock()
        refresh_rate = 25

        # Score
        score1 = 0
        score2 = 0
        end_score = 60

        # Stages
        start = 0
        playing = 1
        end = 2
        game_help = 3

        # Other important variables
        SPEED = 6


            
        # Initial game state

        sun_pos = [800, 75]

        clouds = []
        for i in range(20):
            x = random.randrange(-200, 2200)
            y = random.randrange(-100, 300)
            clouds.append([x, y])

        bonus_coin_spawn = []
        for i in range(1):
            x = random.randrange(50, 750)
            y = random.randrange(100, 600)
            bonus_coin_spawn.append([x, y])

        bad_coin_spawn = []
        for i in range(3):
            x = random.randrange(50, 750)
            y = random.randrange(100, 600)
            bad_coin_spawn.append([x, y])

        flip_coin_spawn = []
        for i in range(3):
            x = random.randrange(50, 750)
            y = random.randrange(100, 600)
            flip_coin_spawn.append([x, y])

        super_flip_coin_spawn = []
        for i in range(3):
            x = random.randrange(50, 750)
            y = random.randrange(100, 600)
            super_flip_coin_spawn.append([x, y])

        stripes = []
        for i in range(0, 1000, 30):
            stripes.append(i)

        sand = []
        for i in range(250):
            x = random.randrange(0, 1200)
            y = random.randrange(650, 700)
            sand.append([x, y])

        pipes = []
        for i in range(10, 900, 150):
            x = random.randrange(50, 900)
            y = 450
            pipes.append([x, y])
            
        flappy_pos = [300, 550]
        flappy_vel = [0, 0]
        facing_right = True

        flappy_pos2 = [150, 550]
        flappy_vel2 = [0, 0]
        facing_right2 = True


        coin_pos = [random.randrange(100, 600), random.randrange(100, 500)]
        coin_pos2 = [random.randrange(100, 600), random.randrange(100, 500)]
        bonus_coin_pos = [random.randrange(100, 600), random.randrange(100, 500)]
        bad_coin_pos = [random.randrange(100, 600), random.randrange(100, 500)]
        bad_coin_pos2 = [random.randrange(100, 600), random.randrange(100, 500)]
        flip_coin_pos = [random.randrange(100, 800), random.randrange(100, 400)]
        super_flip_coin_pos = [random.randrange(100, 800), random.randrange(100, 400)]
        pipe_pos = [100, 450]


                
        # hide mouse cursor over screen
        pygame.mouse.set_visible(0)

        win = 0
        # Game loop
        done = False
        stage = start

        while not done:
            # Event processing (React to key presses, mouse clicks, etc.)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RCTRL:
                        flappy_vel[1] = 5
                        flappy_vel[0] *= 1.2
                    if event.key == pygame.K_SPACE:
                        flappy_vel2[1] = 5
                        flappy_vel2[0] *= 1.2

                        if stage == start:
                            stage = 1
                    elif event.key == pygame.K_RIGHT:
                        flappy_vel[0] = 5
                        facing_right = True
                    elif event.key == pygame.K_LEFT:
                        flappy_vel[0] = -5
                        facing_right = False
                    elif event.key == pygame.K_PERIOD:
                        flappy_vel2[0] = 5
                        facing_right2 = True
                    elif event.key == pygame.K_COMMA:
                        flappy_vel2[0] = -5
                        facing_right2 = False
                    elif event.key == pygame.K_HOME:
                        score1 = 0
                        score2 = 0
                        
                        flappy_pos = [300, 550]
                        flappy_vel = [0, 0]
                        facing_right = True
                        
                        flappy_pos2 = [150, 550]
                        flappy_vel2 = [0, 0]
                        facing_right2 = True
                        
                        stage = 0
                    elif event.key == pygame.K_h:
                        stage = 3
                    


            # Game logic
            if stage == playing:
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

                ''' move FLAPPY2 '''
                flappy_pos2[0] += flappy_vel2[0]
                
                if flappy_vel2[1] > 0:
                    flappy_pos2[1] -= flappy_vel2[1] ** 2        
                else:
                    flappy_pos2[1] += 0.25 * (flappy_vel2[1] ** 2)

                if flappy_pos2[0] < 0:
                    flappy_pos2[0] = 0  
                elif flappy_pos2[0] > 950:
                    flappy_pos2[0] = 950  

                if flappy_pos2[1] < 0:
                    flappy_pos2[1] = 0  
                elif flappy_pos2[1] > 550:
                    flappy_pos2[1] = 550
                    flappy_vel2 = [0,0]

                flappy_vel2[1] -= 1


                
                ''' check coin hit '''#loop
                if data.intersects(flappy_pos, [50,50], coin_pos, [50, 50]):
                    coin_pos[0] = random.randrange(40,900)
                    coin_pos[1] = random.randrange(40,450)
                    score1+=1
                if data.intersects(flappy_pos2, [50,50], coin_pos, [50, 50]):
                    coin_pos[0] = random.randrange(40,900)
                    coin_pos[1] = random.randrange(40,450)
                    score2+=1
                if data.intersects(flappy_pos, [50,50], coin_pos2, [50, 50]):
                    coin_pos2[0] = random.randrange(40,900)
                    coin_pos2[1] = random.randrange(40,450)
                    score1+=1
                if data.intersects(flappy_pos2, [50,50], coin_pos2, [50, 50]):
                    coin_pos2[0] = random.randrange(40,900)
                    coin_pos2[1] = random.randrange(40,450)
                    score2+=1
                if data.intersects(flappy_pos, [50,50], bonus_coin_pos, [50, 50]):
                    bonus_coin_pos[0] = random.randrange(40,900)
                    bonus_coin_pos[1] = random.randrange(40,450)
                    score1+=2
                if data.intersects(flappy_pos2, [50,50], bonus_coin_pos, [50, 50]):
                    bonus_coin_pos[0] = random.randrange(40,900)
                    bonus_coin_pos[1] = random.randrange(40,450)
                    score2+=2
                if data.intersects(flappy_pos, [50,50], bad_coin_pos, [50, 50]):
                    bad_coin_pos[0] = random.randrange(40,900)
                    bad_coin_pos[1] = random.randrange(40,450)
                    score1-=10
                if data.intersects(flappy_pos2, [50,50], bad_coin_pos, [50, 50]):
                    bad_coin_pos[0] = random.randrange(40,900)
                    bad_coin_pos[1] = random.randrange(40,450)
                    score2-=10
                if data.intersects(flappy_pos, [50,50], bad_coin_pos2, [50, 50]):
                    bad_coin_pos2[0] = random.randrange(40,900)
                    bad_coin_pos2[1] = random.randrange(40,450)
                    score1-=10
                if data.intersects(flappy_pos2, [50,50], bad_coin_pos2, [50, 50]):
                    bad_coin_pos2[0] = random.randrange(40,900)
                    bad_coin_pos2[1] = random.randrange(40,450)
                    score2-=10
                if data.intersects(flappy_pos, [50,50], flip_coin_pos, [50, 50]):
                    flip_coin_pos[0] = random.randrange(40,900)
                    flip_coin_pos[1] = random.randrange(40,450)
                    score2+=5
                    score1-=5
                if data.intersects(flappy_pos2, [50,50], flip_coin_pos, [50, 50]):
                    flip_coin_pos[0] = random.randrange(40,900)
                    flip_coin_pos[1] = random.randrange(40,450)
                    score1+=5
                    score2-=5
                if data.intersects(flappy_pos, [50,50], super_flip_coin_pos, [50, 50]):
                    super_flip_coin_pos[0] = random.randrange(40,900)
                    super_flip_coin_pos[1] = random.randrange(40,450)
                    score2+=15
                    score1-=15
                if data.intersects(flappy_pos2, [50,50], super_flip_coin_pos, [50, 50]):
                    super_flip_coin_pos[0] = random.randrange(40,900)
                    super_flip_coin_pos[1] = random.randrange(40,450)
                    score1+=15
                    score2-=15



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

            ''' pipes background '''
            for p in pipes:
                data.draw_pipes(screen, p)


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
            data.draw_coin(screen, coin_pos)
            data.draw_coin(screen, coin_pos2)
            data.draw_bonus_coin(screen, bonus_coin_pos)
            data.draw_bad_coin(screen, bad_coin_pos)
            data.draw_bad_coin(screen, bad_coin_pos2)
            data.draw_flip_coin(screen, flip_coin_pos)
            data.draw_super_flip_coin(screen, super_flip_coin_pos)
            

            
            ''' flappy '''
            data.draw_flappy(screen, flappy_pos)
            data.draw_flappy2(screen, flappy_pos2)

            ''' score '''
            font = pygame.font.Font(None, 40)
            text1 = font.render("P1 Score: " + str(score1), True, FLAPPY)
            text2 = font.render("P2 Score: " + str(score2), True, FLAPPY2)
            screen.blit(text1, [30, 30])
            screen.blit(text2, [30, 70])

            win1 = "Player 1 Wins!"
            win2 = "Player 2 Wins!"
            if score1 >= end_score:
                stage = end
                win = win1
            if score2 >= end_score:
                stage = end
                win = win2
            if stage == start:
                font1 = pygame.font.Font(None, 75)
                font2 = pygame.font.Font(None, 40)
                text1 = font1.render("Flappy Coin Multiplayer!", True, BLACK)
                text2 = font1.render("Flappy Coin Multiplayer!", True, BONUSGOLD)
                text3 = font2.render("(Press SPACE to play.)", True, BLACK)
                screen.blit(text1, [100, 275])
                screen.blit(text2, [100, 273])
                screen.blit(text3, [115, 355])
            if stage == end:
                font = pygame.font.Font(None, 100)
                text1 = font.render("Game Over", True, BLACK)
                text2 = font.render("Game Over", True, BONUSGOLD)
                text3 = font.render(win, True, BLACK)
                text4 = font.render(win, True, BONUSGOLD)
                screen.blit(text1, [325, 275])
                screen.blit(text2, [323, 273])
                screen.blit(text3, [300, 350])
                screen.blit(text4, [298, 348])
            if stage == game_help:
                pass
            
                
            # Update screen
            pygame.display.flip()
            clock.tick(refresh_rate)


        # Close window on quit
pygame.quit()
