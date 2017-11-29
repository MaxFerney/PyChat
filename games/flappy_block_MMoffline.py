
# by Max Ferney
# Imports
import pygame
import random



# Initialize game engine
pygame.init()


# Window
SIZE = (1000, 700)
TITLE = "Flappy Block Multiplayer(8 Players)"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 20


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TEXT = (225, 125, 0)
FLAPPY = (200, 0 , 0)
FLAPPY2 = (50, 50, 225)
FLAPPY3 = (27, 216, 174)
FLAPPY4 = (101, 0, 155)
FLAPPY5 = (255, 252 , 1)
FLAPPY6 = (254, 138, 14)
FLAPPY7 = (32, 192, 0)
FLAPPY8 = (220, 100, 173)
BEAK = (255, 255, 125)
SKY = (125, 175, 225)
SUN = (255, 255, 200)
GRASS1 = (0, 175, 0)
GRASS2 = (0, 150, 0)
SAND1 = (225, 225, 150)
SAND2 = (175, 175, 100)
PIPE = (25, 125, 25)
POWER_UP1 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
POWER_UP2 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
POWER_UP3 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
POWER_UP4 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
FLAPPYCOL1=FLAPPY
FLAPPYCOL2=FLAPPY2
FLAPPYCOL3=FLAPPY3
FLAPPYCOL4=FLAPPY4
FLAPPYCOL5=FLAPPY5
FLAPPYCOL6=FLAPPY6
FLAPPYCOL7=FLAPPY7
FLAPPYCOL8=FLAPPY8
'''
# Player colors
p1_color=FLAPPYCOL1
p2_color=FLAPPYCOL2
p3_color=FLAPPYCOL3
p4_color=FLAPPYCOL4
p5_color=FLAPPYCOL5
p6_color=FLAPPYCOL6
p7_color=FLAPPYCOL7
p8_color=FLAPPYCOL8
'''



POWER_UP = []
POWER_UP.append(POWER_UP1)
POWER_UP.append(POWER_UP2)
POWER_UP.append(POWER_UP3)
POWER_UP.append(POWER_UP4)
# Speed
SPEED = 6
NEAR = 2 / 3 * SPEED
FAR = 1 / 3 * SPEED

# Initial game state
flappy = [300, 200]
flappy2 = [275, 200]
flappy3 = [250, 200]
flappy4 = [225, 200]
flappy5 = [200, 200]
flappy6 = [175, 200]
flappy7 = [150, 200]
flappy8 = [125, 200]
ups = 0
ups2 = 0
ups3 = 0
ups4 = 0
ups5 = 0
ups6 = 0
ups7 = 0
ups8 = 0
score = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0
score7 = 0
score8 = 0


cheat = False
cheat2 = False
cheat3 = False
cheat4 = False
cheat5 = False
cheat6 = False
cheat7 = False
cheat8 = False
auto = False
pause = False
unpause = False


# cheat function
cheats=[]
cheats.append(cheat)
cheats.append(cheat2)
cheats.append(cheat3)
cheats.append(cheat4)
cheats.append(cheat5)
cheats.append(cheat6)
cheats.append(cheat7)
cheats.append(cheat8)
# stages
START = 0 
PLAYING = 1
END = 2
PAUSE = 3

pipes = []
gap = 175
distance = 450;

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


for i in range(5):
    pipes.append( [700 + distance*i, random.randrange(75, 400 - gap)] )

clouds = []
for i in range(5):
    x = random.randrange(-200, 2000)
    y = random.randrange(-100, 200)
    w = random.randrange(125, 200)
    h = random.randrange(75,100)
    clouds.append([x, y, w, h])

powerUps = []
for i in range(1):
    x = random.randrange(-200, 1500)
    y = random.randrange(200, 400)
    powerUps.append([x, y])
    

stripes = []
for i in range(0, 1000, 30):
    stripes.append(i)

sand = []
for i in range(250):
    x = random.randrange(0, 1200)
    y = random.randrange(650, 700)
    sand.append([x, y])

sun = [800, 75, 75]

hills = []
for i in range(3):
    x = random.randrange(-200, 2000)
    w = random.randrange(200, 300)
    h = random.randrange(75, 150)
    y = 600 - h + 2
    hills.append([x, y, w, h])
    
bushes = []
for i in range(4):
    x = random.randrange(-200, 2000)
    w = random.randrange(75, 125)
    h = w
    y = 600 - h + 2
    bushes.append([x, y, w, h])
    

# Game loop
stage = START
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_COMMA:
                ups8 = 5
            if event.key == pygame.K_u:
                ups7 = 5
            if event.key == pygame.K_n:
                ups6 = 5
            if event.key == pygame.K_t:
                ups5 = 5
            if event.key == pygame.K_v:
                ups4 = 5
            if event.key == pygame.K_e:
                ups3 = 5
            if event.key == pygame.K_x:
                ups2 = 5
            if event.key == pygame.K_q:
                ups = 5

                if stage == START:
                    stage = 1
            elif event.key == pygame.K_1:
                cheat = not cheat
            elif event.key == pygame.K_2:
                cheat2 = not cheat2
            elif event.key == pygame.K_3:
                cheat3 = not cheat3
            elif event.key == pygame.K_4:
                cheat4 = not cheat4
            elif event.key == pygame.K_5:
                cheat5 = not cheat5
            elif event.key == pygame.K_6:
                cheat6 = not cheat6
            elif event.key == pygame.K_7:
                cheat7 = not cheat7
            elif event.key == pygame.K_8:
                cheat8 = not cheat8

            elif event.key == pygame.K_a:
                auto = not auto
            '''
            elif event.key == pygame.K_ESCAPE:
                pause = not pause
                print("key pressed paused")
            elif event.key == pygame.K_TAB:
                unpause = not unpause
                print("key pressed unpaused")
            '''    


    # Game logic
    if stage == PLAYING:
        if auto:
            for p in pipes:
                if -150 < p[0] - flappy[0] < distance - 150:
                    if flappy[1] > p[1] + gap - 75 or flappy[1] > 525:
                        ups = 5
                if -150 < p[0] - flappy2[0] < distance - 150:
                    if flappy2[1] > p[1] + gap - 75 or flappy2[1] > 525:
                        ups2 = 5
                if -150 < p[0] - flappy3[0] < distance - 150:
                    if flappy3[1] > p[1] + gap - 75 or flappy3[1] > 525:
                        ups3 = 5
                if -150 < p[0] - flappy4[0] < distance - 150:
                    if flappy4[1] > p[1] + gap - 75 or flappy4[1] > 525:
                        ups4 = 5
                if -150 < p[0] - flappy5[0] < distance - 150:
                    if flappy5[1] > p[1] + gap - 75 or flappy5[1] > 525:
                        ups5 = 5
                if -150 < p[0] - flappy6[0] < distance - 150:
                    if flappy6[1] > p[1] + gap - 75 or flappy6[1] > 525:
                        ups6 = 5
                if -150 < p[0] - flappy7[0] < distance - 150:
                    if flappy7[1] > p[1] + gap - 75 or flappy7[1] > 525:
                        ups7 = 5
                if -150 < p[0] - flappy8[0] < distance - 150:
                    if flappy8[1] > p[1] + gap - 75 or flappy8[1] > 525:
                        ups8 = 5


        #if unpause:
            #stage = 1
        ''' move FLAPPY '''
        if ups > 0:
            flappy[1] -= ups ** 2
        if ups2 > 0:
            flappy2[1] -= ups2 ** 2
        if ups3 > 0:
            flappy3[1] -= ups3 ** 2
        if ups4 > 0:
            flappy4[1] -= ups4 ** 2
        if ups5 > 0:
            flappy5[1] -= ups5 ** 2
        if ups6 > 0:
            flappy6[1] -= ups6 ** 2
        if ups7 > 0:
            flappy7[1] -= ups7 ** 2
        if ups8 > 0:
            flappy8[1] -= ups8 ** 2

        else:
            flappy[1] += 0.25*(ups ** 2)
            flappy2[1] += 0.25*(ups2 ** 2)
            flappy3[1] += 0.25*(ups3 ** 2)
            flappy4[1] += 0.25*(ups4 ** 2)
            flappy5[1] += 0.25*(ups5 ** 2)
            flappy6[1] += 0.25*(ups6 ** 2)
            flappy7[1] += 0.25*(ups7 ** 2)
            flappy8[1] += 0.25*(ups8 ** 2)

            
            if cheat and flappy[1] > 550:
                flappy[1] = 548

            if flappy[1] > 550:
                flappy[1] = 550
                
            if cheat2 and flappy2[1] > 550:
                flappy2[1] = 548

            if flappy2[1] > 550:
                flappy2[1] = 550

            if cheat3 and flappy3[1] > 550:
                flappy3[1] = 548

            if flappy3[1] > 550:
                flappy3[1] = 550

            if cheat4 and flappy4[1] > 550:
                flappy4[1] = 548

            if flappy4[1] > 550:
                flappy4[1] = 550
                
            if cheat5 and flappy5[1] > 550:
                flappy5[1] = 548

            if flappy5[1] > 550:
                flappy5[1] = 550

            if cheat6 and flappy6[1] > 550:
                flappy6[1] = 548

            if flappy6[1] > 550:
                flappy6[1] = 550

            if cheat7 and flappy7[1] > 550:
                flappy7[1] = 548

            if flappy7[1] > 550:
                flappy7[1] = 550

            if cheat8 and flappy8[1] > 550:
                flappy8[1] = 548

            if flappy8[1] > 550:
                flappy8[1] = 550

        
        ups -= 2
        ups2 -= 2
        ups3 -= 2
        ups4 -= 2
        ups5 -= 2
        ups6 -= 2
        ups7 -= 2
        ups8 -= 2

        
        ''' move clouds '''
        for c in clouds:
            c[0] -= FAR
            if c[0] + 200 < 0:
                c[0] += random.randrange(1000, 3200)
                c[1] = random.randrange(-100, 200)
                
        ''' move pipes '''
        for p in pipes:
            p[0] -= SPEED

            if p[0] + 150 < 0:
                p[0] += len(pipes) * distance
                p[1] = random.randrange(75, 325)

        ''' move POWER UPS!'''
        for u in powerUps:
            u[0] -= SPEED

            if u[0] + 150 < 0:
                u[0] += len(pipes) * distance
                u[1] = random.randrange(75, 275)
            
        ''' move sand specs '''
        for s in sand:
            s[0] -= SPEED

            if s[0] < 0:
                s[0] = random.randrange(1000, 1200)
                s[1] = random.randrange(650, 700)
        
        ''' move grass stripes '''
        n = 0
        while n < len(stripes):
            stripes[n] -= SPEED

            if stripes[n] + 10 < 0:
                stripes[n] += 1020

            n += 1
            
        ''' move hills '''
        for h in hills:
            h[0] -= NEAR

            if  h[0] + h[2] < 0:
                h[0] = random.randrange(1000, 3200)
                h[2] = random.randrange(200, 300)
                h[3] = random.randrange(75, 150)
                h[1] = 600 - h[3] + 2

        ''' move bushes '''
        for b in bushes:
            b[0] -= SPEED

            if  b[0] + h[2] < 0:
                b[0] = random.randrange(1000, 3200)
                b[2] = random.randrange(75, 125)
                b[3] = w
                b[1] = 600 - b[3] + 2


        ''' collision testing '''
        if not cheat:
            score += .02675
            ''' ground'''
            if flappy[1] >= 550:
                stage = PLAYING
            ''' pipes '''
            for p in pipes:
                if flappy[0] + 50 > p[0] and flappy[0] < p[0] + 150:
                    if flappy[1] < p[1] or flappy[1] + 50 > p[1] + 200:
                        stage = PLAYING
                        score -= 1
                        FLAPPYCOL = FLAPPY
                        
            ''' POWER UPS!'''
            for u in powerUps:
                if intersects(flappy, [50, 50], u, [95, 95]):
                    stage = PLAYING
                    score += 2
                    FLAPPYCOL1 = POWER_UP[random.randrange(0, 3)]
            
        if not cheat2:
            score2 += .02675
            ''' ground'''
            if flappy2[1] >= 550:
                stage = PLAYING
            ''' pipes '''
            for p in pipes:
                if flappy2[0] + 50 > p[0] and flappy2[0] < p[0] + 150:
                    if flappy2[1] < p[1] or flappy2[1] + 50 > p[1] + 200:
                        stage = PLAYING
                        score2 -= 1
                        FLAPPYCOL2 = FLAPPY2
                        

            ''' POWER UPS!'''
            for u in powerUps:
                if flappy2[0] + 50 > u[0] and flappy2[0] < u[0] + 75:
                    if flappy2[1] < u[1] or flappy2[1] + 50 > u[1] + 75:
                        stage = PLAYING
                        score2 += 2
                        FLAPPYCOL2 = POWER_UP[random.randrange(0, 3)]
                        
                        
        if not cheat3:
            score3 += .02675
            ''' ground'''
            if flappy3[1] >= 550:
                stage = PLAYING
            ''' pipes '''
            for p in pipes:
                if flappy3[0] + 50 > p[0] and flappy3[0] < p[0] + 150:
                    if flappy3[1] < p[1] or flappy3[1] + 50 > p[1] + 200:
                        stage = PLAYING
                        score3 -= 1
                        FLAPPYCOL3 = FLAPPY3

            ''' POWER UPS!'''
            for u in powerUps:
                if flappy3[0] + 50 > u[0] and flappy3[0] < u[0] + 75:
                    if flappy3[1] < u[1] or flappy3[1] + 50 > u[1] + 75:
                        stage = PLAYING
                        score3 += 2
                        FLAPPYCOL3 = POWER_UP[random.randrange(0, 3)]
                        
                        
                        
        if not cheat4:
            score4 += .02675
            ''' ground'''
            if flappy4[1] >= 550:
                stage = PLAYING
            ''' pipes '''
            for p in pipes:
                if flappy4[0] + 50 > p[0] and flappy4[0] < p[0] + 150:
                    if flappy4[1] < p[1] or flappy4[1] + 50 > p[1] + 200:
                        stage = PLAYING
                        score4 -= 1
                        FLAPPYCOL4 = FLAPPY4

            ''' POWER UPS!'''
            for u in powerUps:
                if flappy4[0] + 50 > u[0] and flappy4[0] < u[0] + 75:
                    if flappy4[1] < u[1] or flappy4[1] + 50 > u[1] + 75:
                        stage = PLAYING
                        score4 += 2
                        FLAPPYCOL4 = POWER_UP[random.randrange(0, 3)]

        if not cheat5:
            score5 += .02675
            ''' ground'''
            if flappy5[1] >= 550:
                stage = PLAYING
            ''' pipes '''
            for p in pipes:
                if flappy5[0] + 50 > p[0] and flappy5[0] < p[0] + 150:
                    if flappy5[1] < p[1] or flappy5[1] + 50 > p[1] + 200:
                        stage = PLAYING
                        score5 -= 1
                        FLAPPYCOL5 = FLAPPY5

            ''' POWER UPS!'''
            for u in powerUps:
                if flappy5[0] + 50 > u[0] and flappy5[0] < u[0] + 75:
                    if flappy5[1] < u[1] or flappy5[1] + 50 > u[1] + 75:
                        stage = PLAYING
                        score5 += 2
                        FLAPPYCOL5 = POWER_UP[random.randrange(0, 3)]
                        

        if not cheat6:
            score6 += .02675
            ''' ground'''
            if flappy6[1] >= 550:
                stage = PLAYING
            ''' pipes '''
            for p in pipes:
                if flappy6[0] + 50 > p[0] and flappy6[0] < p[0] + 150:
                    if flappy6[1] < p[1] or flappy6[1] + 50 > p[1] + 200:
                        stage = PLAYING
                        score6 -= 1
                        FLAPPYCOL6 = FLAPPY6
                        

            ''' POWER UPS!'''
            for u in powerUps:
                if flappy6[0] + 50 > u[0] and flappy6[0] < u[0] + 75:
                    if flappy6[1] < u[1] or flappy6[1] + 50 > u[1] + 75:
                        stage = PLAYING
                        score6 += 2
                        FLAPPYCOL6 = POWER_UP[random.randrange(0, 3)]
                        
                        
        if not cheat7:
            score7 += .02675
            ''' ground'''
            if flappy7[1] >= 550:
                stage = PLAYING
            ''' pipes '''
            for p in pipes:
                if flappy7[0] + 50 > p[0] and flappy7[0] < p[0] + 150:
                    if flappy7[1] < p[1] or flappy7[1] + 50 > p[1] + 200:
                        stage = PLAYING
                        score7 -= 1
                        FLAPPYCOL7 = FLAPPY7

            ''' POWER UPS!'''
            for u in powerUps:
                if flappy7[0] + 50 > u[0] and flappy7[0] < u[0] + 75:
                    if flappy7[1] < u[1] or flappy7[1] + 50 > u[1] + 75:
                        stage = PLAYING
                        score7 += 2
                        FLAPPYCOL7 = POWER_UP[random.randrange(0, 3)]
                        
                        
                        
        if not cheat8:
            score8 += .02675
            ''' ground'''
            if flappy8[1] >= 550:
                stage = PLAYING
            ''' pipes '''
            for p in pipes:
                if flappy8[0] + 50 > p[0] and flappy8[0] < p[0] + 150:
                    if flappy8[1] < p[1] or flappy8[1] + 50 > p[1] + 200:
                        stage = PLAYING
                        score8 -= 1
                        FLAPPYCOL8 = FLAPPY8

            ''' POWER UPS!'''
            for u in powerUps:
                if flappy8[0] + 50 > u[0] and flappy8[0] < u[0] + 75:
                    if flappy8[1] < u[1] or flappy8[1] + 50 > u[1] + 75:
                        stage = PLAYING
                        score8 += 2
                        FLAPPYCOL8 = POWER_UP[random.randrange(0, 3)]

            

        
        ''' update score '''
        if cheat:
            score+=0
        if cheat2:
            score2+=0
        if cheat3:
            score3+=0
        if cheat4:
            score4+=0
        if cheat5:
            score5+=0
        if cheat6:
            score6+=0
        if cheat7:
            score7+=0
        if cheat8:
            score8+=0
        '''
        score += .02675
        score2 += .02675
        score3 += .02675
        score4 += .02625
        score5 += .02675
        score6 += .02675
        score7 += .02675
        score8 += .02625
        '''

    

    # Drawing code
    ''' sky '''
    screen.fill(SKY)

    ''' sun '''
    x = sun[0]
    y = sun[1]
    r = sun[2]
    pygame.draw.rect(screen, SUN, [x, y, r, r])

    ''' draw clouds '''
    for c in clouds:
        x = c[0]
        y = c[1]
        w = c[2]
        h = c[3]
        pygame.draw.rect(screen, WHITE, [x, y, w, h])
        pygame.draw.rect(screen, BLACK, [x, y, w, h], 2)

    '''POWER UPS!'''
    for p in powerUps:
        x = p[0]
        y = p[1]
        pygame.draw.ellipse(screen, FLAPPY4, [x + 90, y + 90, 95, 95])
        pygame.draw.ellipse(screen, FLAPPY, [x + 100, y + 100, 75, 75])
        pygame.draw.ellipse(screen, FLAPPY4, [x + 125, y + 125, 25, 25])
    
    ''' hills '''
    for h in hills:
        pygame.draw.rect(screen, GRASS1, h)
        pygame.draw.rect(screen, BLACK, h, 2)

    ''' flappy '''
    x = flappy[0]
    y = flappy[1]
    pygame.draw.rect(screen, FLAPPYCOL1, [x, y, 50, 50])
    pygame.draw.rect(screen, BLACK, [x, y, 50, 50], 2)
    pygame.draw.polygon(screen, BEAK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]])
    pygame.draw.polygon(screen, BLACK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]], 2)
    pygame.draw.rect(screen, FLAPPYCOL1, [x - 10, y + 20, 40, 10])
    pygame.draw.rect(screen, BLACK, [x - 10, y + 20, 40, 10], 2)
    pygame.draw.rect(screen, WHITE, [x + 35, y + 5, 10, 10])
    pygame.draw.rect(screen, BLACK, [x + 35, y + 5, 10, 10], 2)
    pygame.draw.rect(screen, BLACK, [x + 40, y + 10, 5, 5])

    x2 = flappy2[0]
    y2 = flappy2[1]
    pygame.draw.rect(screen, FLAPPYCOL2, [x2, y2, 50, 50])
    pygame.draw.rect(screen, BLACK, [x2, y2, 50, 50], 2)
    pygame.draw.polygon(screen, BEAK, [[x2 + 50, y2 + 20], [x2 + 60, y2 + 25], [x2 + 50, y2 + 30]])
    pygame.draw.polygon(screen, BLACK, [[x2 + 50, y2 + 20], [x2 + 60, y2 + 25], [x2 + 50, y2 + 30]], 2)
    pygame.draw.rect(screen, FLAPPYCOL2, [x2 - 10, y2 + 20, 40, 10])
    pygame.draw.rect(screen, BLACK, [x2 - 10, y2 + 20, 40, 10], 2)
    pygame.draw.rect(screen, WHITE, [x2 + 35, y2 + 5, 10, 10])
    pygame.draw.rect(screen, BLACK, [x2 + 35, y2 + 5, 10, 10], 2)
    pygame.draw.rect(screen, BLACK, [x2 + 40, y2 + 10, 5, 5])

    x3 = flappy3[0]
    y3 = flappy3[1]
    pygame.draw.rect(screen, FLAPPYCOL3, [x3, y3, 50, 50])
    pygame.draw.rect(screen, BLACK, [x3, y3, 50, 50], 2)
    pygame.draw.polygon(screen, BEAK, [[x3 + 50, y3 + 20], [x3 + 60, y3 + 25], [x3 + 50, y3 + 30]])
    pygame.draw.polygon(screen, BLACK, [[x3 + 50, y3 + 20], [x3 + 60, y3 + 25], [x3 + 50, y3 + 30]], 2)
    pygame.draw.rect(screen, FLAPPYCOL3, [x3 - 10, y3 + 20, 40, 10])
    pygame.draw.rect(screen, BLACK, [x3 - 10, y3 + 20, 40, 10], 2)
    pygame.draw.rect(screen, WHITE, [x3 + 35, y3 + 5, 10, 10])
    pygame.draw.rect(screen, BLACK, [x3 + 35, y3 + 5, 10, 10], 2)
    pygame.draw.rect(screen, BLACK, [x3 + 40, y3 + 10, 5, 5])

    x4 = flappy4[0]
    y4 = flappy4[1]
    pygame.draw.rect(screen, FLAPPYCOL4, [x4, y4, 50, 50])
    pygame.draw.rect(screen, BLACK, [x4, y4, 50, 50], 2)
    pygame.draw.polygon(screen, BEAK, [[x4 + 50, y4 + 20], [x4 + 60, y4 + 25], [x4 + 50, y4 + 30]])
    pygame.draw.polygon(screen, BLACK, [[x4 + 50, y4 + 20], [x4 + 60, y4 + 25], [x4 + 50, y4 + 30]], 2)
    pygame.draw.rect(screen, FLAPPYCOL4, [x4 - 10, y4 + 20, 40, 10])
    pygame.draw.rect(screen, BLACK, [x4 - 10, y4 + 20, 40, 10], 2)
    pygame.draw.rect(screen, WHITE, [x4 + 35, y4 + 5, 10, 10])
    pygame.draw.rect(screen, BLACK, [x4 + 35, y4 + 5, 10, 10], 2)
    pygame.draw.rect(screen, BLACK, [x4 + 40, y4 + 10, 5, 5])

    x5 = flappy5[0]
    y5 = flappy5[1]
    pygame.draw.rect(screen, FLAPPYCOL5, [x5, y5, 50, 50])
    pygame.draw.rect(screen, BLACK, [x5, y5, 50, 50], 2)
    pygame.draw.polygon(screen, BEAK, [[x5 + 50, y5 + 20], [x5 + 60, y5 + 25], [x5 + 50, y5 + 30]])
    pygame.draw.polygon(screen, BLACK, [[x5 + 50, y5 + 20], [x5 + 60, y5 + 25], [x5 + 50, y5 + 30]], 2)
    pygame.draw.rect(screen, FLAPPYCOL5, [x5 - 10, y5 + 20, 40, 10])
    pygame.draw.rect(screen, BLACK, [x5 - 10, y5 + 20, 40, 10], 2)
    pygame.draw.rect(screen, WHITE, [x5 + 35, y5 + 5, 10, 10])
    pygame.draw.rect(screen, BLACK, [x5 + 35, y5 + 5, 10, 10], 2)
    pygame.draw.rect(screen, BLACK, [x5 + 40, y5 + 10, 5, 5])

    x6 = flappy6[0]
    y6 = flappy6[1]
    pygame.draw.rect(screen, FLAPPYCOL6, [x6, y6, 50, 50])
    pygame.draw.rect(screen, BLACK, [x6, y6, 50, 50], 2)
    pygame.draw.polygon(screen, BEAK, [[x6 + 50, y6 + 20], [x6 + 60, y6 + 25], [x6 + 50, y6 + 30]])
    pygame.draw.polygon(screen, BLACK, [[x6 + 50, y6 + 20], [x6 + 60, y6 + 25], [x6 + 50, y6 + 30]], 2)
    pygame.draw.rect(screen, FLAPPYCOL6, [x6 - 10, y6 + 20, 40, 10])
    pygame.draw.rect(screen, BLACK, [x6 - 10, y6 + 20, 40, 10], 2)
    pygame.draw.rect(screen, WHITE, [x6 + 35, y6 + 5, 10, 10])
    pygame.draw.rect(screen, BLACK, [x6 + 35, y6 + 5, 10, 10], 2)
    pygame.draw.rect(screen, BLACK, [x6 + 40, y6 + 10, 5, 5])

    x7 = flappy7[0]
    y7 = flappy7[1]
    pygame.draw.rect(screen, FLAPPYCOL7, [x7, y7, 50, 50])
    pygame.draw.rect(screen, BLACK, [x7, y7, 50, 50], 2)
    pygame.draw.polygon(screen, BEAK, [[x7 + 50, y7 + 20], [x7 + 60, y7 + 25], [x7 + 50, y7 + 30]])
    pygame.draw.polygon(screen, BLACK, [[x7 + 50, y7 + 20], [x7 + 60, y7 + 25], [x7 + 50, y7 + 30]], 2)
    pygame.draw.rect(screen, FLAPPYCOL7, [x7 - 10, y7 + 20, 40, 10])
    pygame.draw.rect(screen, BLACK, [x7 - 10, y7 + 20, 40, 10], 2)
    pygame.draw.rect(screen, WHITE, [x7 + 35, y7 + 5, 10, 10])
    pygame.draw.rect(screen, BLACK, [x7 + 35, y7 + 5, 10, 10], 2)
    pygame.draw.rect(screen, BLACK, [x7 + 40, y7 + 10, 5, 5])

    x8 = flappy8[0]
    y8 = flappy8[1]
    pygame.draw.rect(screen, FLAPPYCOL8, [x8, y8, 50, 50])
    pygame.draw.rect(screen, BLACK, [x8, y8, 50, 50], 2)
    pygame.draw.polygon(screen, BEAK, [[x8 + 50, y8 + 20], [x8 + 60, y8 + 25], [x8 + 50, y8 + 30]])
    pygame.draw.polygon(screen, BLACK, [[x8 + 50, y8 + 20], [x8 + 60, y8 + 25], [x8 + 50, y8 + 30]], 2)
    pygame.draw.rect(screen, FLAPPYCOL8, [x8 - 10, y8 + 20, 40, 10])
    pygame.draw.rect(screen, BLACK, [x8 - 10, y8 + 20, 40, 10], 2)
    pygame.draw.rect(screen, WHITE, [x8 + 35, y8 + 5, 10, 10])
    pygame.draw.rect(screen, BLACK, [x8 + 35, y8 + 5, 10, 10], 2)
    pygame.draw.rect(screen, BLACK, [x8 + 40, y8 + 10, 5, 5])

    
    ''' grass '''
    pygame.draw.rect(screen, GRASS1, [0, 600, 1000, 50])

    for s in stripes:
        pygame.draw.line(screen, GRASS2, [s, 600], [s - 20, 650], 10)

    pygame.draw.line(screen, BLACK, [0, 600], [1000, 600], 2)

    ''' sand '''
    pygame.draw.rect(screen, SAND1, [0, 650, 1000, 50])

    for s in sand:
        pygame.draw.rect(screen, SAND2, [s[0], s[1], 2, 2])
    
    pygame.draw.line(screen, BLACK, [0, 650], [1000, 650], 2)


    ''' pipes '''
    for p in pipes:
        x = p[0]
        y = p[1]
        
        pygame.draw.rect(screen, PIPE, [x + 10, 0, 130, y])
        pygame.draw.rect(screen, BLACK, [x + 10, 0, 130, y], 2)
        pygame.draw.rect(screen, PIPE, [x, y - 75, 150, 75])
        pygame.draw.rect(screen, BLACK, [x, y - 75, 150, 75], 2)
        
        pygame.draw.rect(screen, PIPE, [x + 10, p[1] + gap, 130, 600 - y - gap])
        pygame.draw.rect(screen, BLACK, [x + 10, p[1] + gap, 130, 601 - y - gap], 2)
        pygame.draw.rect(screen, PIPE, [x, y + gap, 150, 75])
        pygame.draw.rect(screen, BLACK, [x, y + gap, 150, 75], 2)

    for b in bushes:
        pygame.draw.rect(screen, GRASS2, h)
        pygame.draw.rect(screen, BLACK, h, 2)

    ''' score '''
    font = pygame.font.Font(None, 40)
    text1 = font.render("P1 Score: " + str(score // 2), True, FLAPPY)
    text2 = font.render("P2 Score: " + str(score2 // 2), True, FLAPPY2)
    text3 = font.render("P3 Score: " + str(score3 // 2), True, FLAPPY3)
    text4 = font.render("P4 Score: " + str(score4 // 2), True, FLAPPY4)
    text5 = font.render("P5 Score: " + str(score5 // 2), True, FLAPPY5)
    text6 = font.render("P6 Score: " + str(score6 // 2), True, FLAPPY6)
    text7 = font.render("P7 Score: " + str(score7 // 2), True, FLAPPY7)
    text8 = font.render("P8 Score: " + str(score8 // 2), True, FLAPPY8)

    screen.blit(text1, [30, 30])
    screen.blit(text2, [30, 70])
    screen.blit(text3, [30, 110])
    screen.blit(text4, [30, 150])
    screen.blit(text5, [300, 30])
    screen.blit(text6, [300, 70])
    screen.blit(text7, [300, 110])
    screen.blit(text8, [300, 150])


    ''' auto '''
    if auto:
        font = pygame.font.Font(None, 30)
        text = font.render("Auto play: On", True, FLAPPY)
        screen.blit(text, [30, 450])
        


    ''' cheat '''
    if cheat:
        font = pygame.font.Font(None, 30)
        text = font.render("Cheat mode P1: On", True, FLAPPY)
        screen.blit(text, [30, 480])
        score+=0
    if cheat2:
        font = pygame.font.Font(None, 30)
        text = font.render("Cheat mode P2: On", True, FLAPPY2)
        screen.blit(text, [30, 510])
        score2+=0
    if cheat3:
        font = pygame.font.Font(None, 30)
        text = font.render("Cheat mode P3: On", True, FLAPPY3)
        screen.blit(text, [30, 540])
        score3+=0
    if cheat4:
        font = pygame.font.Font(None, 30)
        text = font.render("Cheat mode P4: On", True, FLAPPY4)
        screen.blit(text, [30, 570])
        score4+=0
    if cheat5:
        font = pygame.font.Font(None, 30)
        text = font.render("Cheat mode P5: On", True, FLAPPY5)
        screen.blit(text, [600, 480])
        score5+=0
    if cheat6:
        font = pygame.font.Font(None, 30)
        text = font.render("Cheat mode P6: On", True, FLAPPY6)
        screen.blit(text, [600, 510])
        score6+=0
    if cheat7:
        font = pygame.font.Font(None, 30)
        text = font.render("Cheat mode P7: On", True, FLAPPY7)
        screen.blit(text, [600, 540])
        score7+=0
    if cheat8:
        font = pygame.font.Font(None, 30)
        text = font.render("Cheat mode P8: On", True, FLAPPY8)
        screen.blit(text, [600, 570])
        score8+=0


    #if pause:
        #stage = 3
    
        
    ''' begin/end game text '''
    if stage == START:
        font1 = pygame.font.Font(None, 75)
        font2 = pygame.font.Font(None, 40)
        text1 = font1.render("Flappy Block Multiplayer!", True, BLACK)
        text2 = font1.render("Flappy Block Multiplayer!", True, TEXT)
        text3 = font2.render("(press q to play. P1: Q. P2: X. P3: E)", True, BLACK)
        text4 = font2.render("(P4: V. P5: T. P6: N. P7: U. P8: COMMA.)", True, BLACK)
        screen.blit(text1, [100, 275])
        screen.blit(text2, [100, 273])
        screen.blit(text3, [100, 355])
        screen.blit(text4, [100, 395])
    elif stage == END:
        font = pygame.font.Font(None, 100)
        text1 = font.render("Game Over", True, BLACK)
        text2 = font.render("Game Over", True, TEXT)
        screen.blit(text1, [325, 275])
        screen.blit(text2, [323, 273])
    '''
    elif stage == PAUSE:
        font = pygame.font.Font(None, 100)
        text1 = font.render("Game Paused", True, BLACK)
        text2 = font.render("Game Paused", True, TEXT)
        screen.blit(text1, [325, 275])
        screen.blit(text2, [323, 273])
    '''
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()

print("ended game")
print()
