# Imports
import pygame
import random

class RunGameFBC:
    def main():
        # Initialize game engine
        pygame.init()


        # Window
        SIZE = (1000, 700)
        TITLE = "Flappy Block"
        screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)

        # Timer
        clock = pygame.time.Clock()
        refresh_rate = 25


        # Colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
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

        # Speed
        SPEED = 6
        NEAR = 2 / 3 * SPEED
        FAR = 1 / 3 * SPEED

        # Initial game state
        flappy = [300, 200]
        ups = 0
        score = 0

        cheat = False
        auto = False

        # stages
        START = 0
        PLAYING = 1
        END = 2

        pipes = []
        gap = 175
        distance = 450;

        for i in range(5):
            pipes.append( [700 + distance*i, random.randrange(75, 400 - gap)] )

        clouds = []
        for i in range(5):
            x = random.randrange(-200, 2000)
            y = random.randrange(-100, 200)
            w = random.randrange(125, 200)
            h = random.randrange(75,100)
            clouds.append([x, y, w, h])

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
                    if event.key == pygame.K_SPACE:
                        ups = 5

                        if stage == START:
                            stage = 1
                    elif event.key == pygame.K_c:
                        cheat = not cheat
                    elif event.key == pygame.K_a:
                        auto = not auto

            # Game logic
            if stage == PLAYING:
                if auto:
                    for p in pipes:
                        if -150 < p[0] - flappy[0] < distance - 150:
                            if flappy[1] > p[1] + gap - 75 or flappy[1] > 525:
                                ups = 5
                    
                ''' move FLAPPY '''
                if ups > 0:
                    flappy[1] -= ups ** 2
                        
                else:
                    flappy[1] += 0.25*(ups ** 2)
                    
                    if cheat and flappy[1] > 550:
                        flappy[1] = 548

                    if flappy[1] > 550:
                        flappy[1] = 550
            
                ups -= 1
                
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
                    ''' ground'''
                    if flappy[1] >= 550:
                        stage = END

                    ''' pipes '''
                    for p in pipes:
                        if flappy[0] + 50 > p[0] and flappy[0] < p[0] + 150:
                            if flappy[1] < p[1] or flappy[1] + 50 > p[1] + 200:
                                stage = END
                
                ''' update score ''' 
                score += 1
            

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

            ''' hills '''
            for h in hills:
                pygame.draw.rect(screen, GRASS1, h)
                pygame.draw.rect(screen, BLACK, h, 2)

            ''' flappy '''
            x = flappy[0]
            y = flappy[1]
            pygame.draw.rect(screen, FLAPPY, [x, y, 50, 50])
            pygame.draw.rect(screen, BLACK, [x, y, 50, 50], 2)
            pygame.draw.polygon(screen, BEAK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]])
            pygame.draw.polygon(screen, BLACK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]], 2)
            pygame.draw.rect(screen, FLAPPY, [x - 10, y + 20, 40, 10])
            pygame.draw.rect(screen, BLACK, [x - 10, y + 20, 40, 10], 2)
            pygame.draw.rect(screen, WHITE, [x + 35, y + 5, 10, 10])
            pygame.draw.rect(screen, BLACK, [x + 35, y + 5, 10, 10], 2)
            pygame.draw.rect(screen, BLACK, [x + 40, y + 10, 5, 5])
            
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
            font = pygame.font.Font(None, 50)
            text = font.render("Score: " + str(score), True, BLACK)
            screen.blit(text, [30, 30])

            ''' auto '''
            if auto:
                font = pygame.font.Font(None, 30)
                text = font.render("Auto play: On", True, FLAPPY)
                screen.blit(text, [30, 510])

            ''' cheat '''
            if cheat:
                font = pygame.font.Font(None, 30)
                text = font.render("Cheat mode: On", True, FLAPPY)
                screen.blit(text, [30, 550])

            ''' begin/end game text '''
            if stage == START:
                font1 = pygame.font.Font(None, 100)
                font2 = pygame.font.Font(None, 40)
                text1 = font1.render("Flappy Block!", True, BLACK)
                text2 = font1.render("Flappy Block!", True, TEXT)
                text3 = font2.render("(Press SPACE to play.)", True, BLACK)
                screen.blit(text1, [225, 275])
                screen.blit(text2, [224, 273])
                screen.blit(text3, [310, 355])
            elif stage == END:
                font = pygame.font.Font(None, 100)
                text1 = font.render("Game Over", True, BLACK)
                text2 = font.render("Game Over", True, TEXT)
                screen.blit(text1, [325, 275])
                screen.blit(text2, [323, 273])

            # Update screen
            pygame.display.flip()
            clock.tick(refresh_rate)


        # Close window on quit
        pygame.quit()

