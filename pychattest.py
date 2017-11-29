import os
import sys
#import time

print("input name:\n")
name = input()

class chat:
    name = None
    text = None
    c_group = 'testing_chat'

    def __init__(self, name, c_group='testing_chat'):
        self.name = name
        self.c_group = c_group

        self.readF()

    def readF(self):
        c_group = self.c_group
        text = self.text
        FileName = 'chat_groups/' + str(c_group) + '.txt'

        
        with open(FileName, 'r') as f:
            text = f.read()
            self.text = text
        f.close()
        
    def speak(self, system=False, message=""):
        #print("to stop typing, press ENTER, then press CONTROL + C")
                
        name = self.name
        c_group = self.c_group
        text = self.text

        file = 'chat_groups/'+str(c_group)+'.txt'

        
        with open(file) as f:
            t = f.read()
        f.close()
        if not system:
            while 1:
                try:
                    line = sys.stdin.readline()
                    
                except KeyboardInterrupt:
                    break

                if not line:
                    break

                t += (name+': '+line)

        else:
            t += 'SYSTEM\t'+message+'\n'
            
         
        with open(file, 'w') as f:
            f.write(t)
        f.close()

        with open(file) as f:
            text = f.read()
            self.text = text
        f.close()


    def update(self):
        c_group = self.c_group

        file = 'chat_groups/'+str(c_group)+'.txt'
        with open(file) as f:
            display = f.read()
        f.close()

        print(display)
        #print()
        #print()

    def __str__(self):
        self.readF()
        return "nothing here...yet..."


def start():
    global name

    user = chat(name)
    user.speak(True, "USER: ["+user.name+"] HAS JOINED THE CHAT")
    
    
    
    while 1:
        print()
        print("------Main Menu------")
        print("type in chat[0]")
        print("update chat[1]")
        print("leave chat[2]")
        try:
            print()
            option = int(input())
            if option == 0:
                user.update()
                print("Typing...")
                print("to stop typing, press ENTER, then press CONTROL + C")
                user.speak()
            if option == 1:
                print("Updating...")
                user.update()
                print("Updated!")
            if option == 2:
                print("Goodbye, "+str(user.name)+".")
                print("to restart, type: start()\n")
                user.speak(True, "USER: ["+user.name+"] HAS LEFT THE CHAT")
                break
        except ValueError:
            print("INVALID TYPE. please input a (valid) number.")
        except KeyboardInterrupt:
            print("this is the main menu...")


#print("\n\t\ttype: start()\n")

start()

        
            
        

    
