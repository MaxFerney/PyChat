import pygame
import random
class RunGameUSF:
    def main():
        pygame.init()

        #Window
        SIZE=(800, 600)
        TITLE="THE FLAG"
        screen=pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)

        #Timer
        clock = pygame.time.Clock()
        refresh_rate = 30

        #COLOR
        RED=(255,0,0)
        WHITE=(255,255,255)
        BLUE=(0,0,255)

        #Variables
        distance=46.15
        distancey=29.37
        distancex=19.05

            


            
        done = False

        while not done:
            # Event processing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            ''' stripes '''
            pygame.draw.rect(screen, RED, [0, 0, 800, 600])
            pygame.draw.rect(screen, WHITE, [0, distance * 1, 800, distance])
            pygame.draw.rect(screen, WHITE, [0, distance * 3, 800, distance])
            pygame.draw.rect(screen, WHITE, [0, distance * 5, 800, distance])
            pygame.draw.rect(screen, WHITE, [0, distance * 7, 800, distance])
            pygame.draw.rect(screen, WHITE, [0, distance * 9, 800, distance])
            pygame.draw.rect(screen, WHITE, [0, distance * 11, 800, distance])
            ''' stars '''
            pygame.draw.rect(screen, BLUE, [0, 0, 400, 323.05])
            pygame.draw.rect(screen, WHITE, [0, distancey*1, 400, distancey])
            pygame.draw.rect(screen, WHITE, [0, distancey*3, 400, distancey])
            pygame.draw.rect(screen, WHITE, [0, distancey*5, 400, distancey])
            pygame.draw.rect(screen, WHITE, [0, distancey*7, 400, distancey])
            pygame.draw.rect(screen, WHITE, [0, distancey*9, 400, distancey])
            
            pygame.draw.rect(screen, BLUE, [0, 0, distancex*1, 323.05])
            pygame.draw.rect(screen, BLUE, [distancex*2, 0, distancex*1, 323.05])
            pygame.draw.rect(screen, BLUE, [distancex*4, 0, distancex*1, 323.05])
            pygame.draw.rect(screen, BLUE, [distancex*6, 0, distancex*1, 323.05])
            pygame.draw.rect(screen, BLUE, [distancex*8, 0, distancex*1, 323.05])
            pygame.draw.rect(screen, BLUE, [distancex*10, 0, distancex*1, 323.05])
            pygame.draw.rect(screen, BLUE, [distancex*12, 0, distancex*1, 323.05])
            pygame.draw.rect(screen, BLUE, [distancex*14, 0, distancex*1, 323.05])
            pygame.draw.rect(screen, BLUE, [distancex*16, 0, distancex*1, 323.05])
            pygame.draw.rect(screen, BLUE, [distancex*18, 0, distancex*1, 323.05])
            pygame.draw.rect(screen, BLUE, [distancex*20, 0, distancex*1, 323.05])
            
            pygame.display.flip()
            clock.tick(refresh_rate)
            
        pygame.quit()
