import pygame
import os

#games

from games.test_paint import PaintGame
##from games.flappy_coin_2048 import RunGameFC2048
from games.flappy_block import RunGameFBC
from games.US_flag import RunGameUSF
from games.OffScreenPlayers import RunGameOSP
from games.flappy_coin_multiplayer_MFnCS import RunGameFCM_MFCS
from games.Checkers import RunGameEC
def GameMenu():
    while True:
        print("""
        \n###################################################\n
        \t\tWhat game do you want to play?\n
        --apps--
        [1]US Flag
        [2]Paint

        --games--
        [3]flappy Coin 2048
        [4]Flappy Block Classic
        [5]Off Screen Players
        [6]Flappy Coin Multiplayer MF&CS
        [7]Executive Checkers
        

        """)
        askGame = input('\t\t\t')

        if askGame == "1":          #US Flag
            RunGameUSF.main()
        elif askGame == "2":        #Paint
            PaintGame.main()
##        elif askGame == "3":        #Flappy Coin 2048
##            RunGameFC2048.main()
        elif askGame == "4":        #Flappy Block Classic
            RunGameFBC.main()
        elif askGame == "5":        #Off Screen Players
            RunGameOSP.main()
        elif askGame == "6":        #My flappy coin multiplayer project
            RunGameFCM_MFCS.main()
        elif askGame == "7":        #Executive Checkers 
            RunGameEC.main()
            
        else:
            print("GoodBye")
            break

GameMenu()
print("GameMenu closed")
print()
print()
            

