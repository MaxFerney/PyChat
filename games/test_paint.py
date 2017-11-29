import pygame
class PaintGame:
        

    # Initial Variables
    def main():
        pygame.init()
        
        # Window
        SIZE = (800, 600)
        TITLE = "Paint"
        screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)


        # Timer
        clock = pygame.time.Clock()
        refresh_rate = 250


        # Colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)

        current_color = RED

        # Brush
        radius = 5;
        SIZE1 = 1
        SIZE2 = 2
        SIZE3 = 3
        SIZE4 = 4
        SIZE5 = 5
        SIZE6 = 6
        SIZE7 = 7
        SIZE8 = 8
        SIZE9 = 9
        SIZE = 5

        # Palete Location
        RED_BOX = (10, 560, 30, 30)
        GREEN_BOX = (50, 560, 30, 30)
        BLUE_BOX = (90, 560, 30, 30)

        # Game loop
        done = False

        while not done:
            # Event processing (React to key presses, mouse clicks, etc.)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        SIZE = SIZE1
                    if event.key == pygame.K_2:
                        SIZE = SIZE2
                    if event.key == pygame.K_3:
                        SIZE = SIZE3
                    if event.key == pygame.K_4:
                        SIZE = SIZE4
                    if event.key == pygame.K_5:
                        SIZE = SIZE5
                    if event.key == pygame.K_6:
                        SIZE = SIZE6
                    if event.key == pygame.K_7:
                        SIZE = SIZE7
                    if event.key == pygame.K_8:
                        SIZE = SIZE8
                    if event.key == pygame.K_9:
                        SIZE = SIZE9
                        
                        
                    
                

            # Game logic
            clicks = pygame.mouse.get_pressed()

            if clicks[0]:
                click_pos = pygame.mouse.get_pos()
                x = click_pos[0]
                y = click_pos[1]
##                print('click!', x, y)
                
                if RED_BOX[0] < x < RED_BOX[0] + RED_BOX[2] and \
                   RED_BOX[1] < y < RED_BOX[1] + RED_BOX[3]:
                    current_color = RED
##                    print('Red')
                elif GREEN_BOX[0] < x < GREEN_BOX[0] + GREEN_BOX[2] and \
                     GREEN_BOX[1] < y < GREEN_BOX[1] + GREEN_BOX[3]:
                    current_color = GREEN
##                    print('Green')
                elif BLUE_BOX[0] < x < BLUE_BOX[0] + BLUE_BOX[2] and \
                     BLUE_BOX[1] < y < BLUE_BOX[1] + BLUE_BOX[3]:
                    current_color = BLUE
##                    print('Blue')
                else:
##                    print('draw')
                    pygame.draw.circle(screen, current_color, [x, y], SIZE)
                    

            ''' draw palette '''
            pygame.draw.rect(screen, RED, RED_BOX)
            pygame.draw.rect(screen, WHITE, RED_BOX, 2)
            pygame.draw.rect(screen, GREEN, GREEN_BOX)
            pygame.draw.rect(screen, WHITE, GREEN_BOX, 2)
            pygame.draw.rect(screen, BLUE, BLUE_BOX)
            pygame.draw.rect(screen, WHITE, BLUE_BOX, 2)
                             
            # Update screen
            pygame.display.flip()
            clock.tick(refresh_rate)


        # Close window on quit
        pygame.quit()
