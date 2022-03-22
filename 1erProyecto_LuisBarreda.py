import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from threading import Thread
import threading
import random
import sys
import pygame
from pygame import mixer
sys.setrecursionlimit(3000)

"""About Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""
def openaboutw():
    info = Toplevel() #Creates the about window
    info.title("Programmer information") #Gives the window a name
    info.geometry("675x300") #Dimensions of the window
    info.configure(background = "light blue") #About window configuration
    
    """Basic programmer information Labels"""
    country_of_prod = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Country of Production  -->  Costa Rica", fg = "IndianRed1", bg = "light blue"). place(x = 0, y = 55) #Country Label
    university_career = tk.Label(info, font = ("Comic Sans MS", 13), text = "- University/Career  -->  Tecnológico de Costa Rica / Computer Engineering", fg = "IndianRed1", bg = "light blue"). place(x = 0, y = 85) #College and career label
    subject_year_group = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Subject/Year/Group  -->  Taller de Programación, 2nd Year, Group 3", fg = "IndianRed1", bg = "light blue"). place(x = 0, y = 115) #Subject label
    professor = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Professor  -->  Leonardo Araya Martinez", fg = "IndianRed1", bg = "light blue"). place(x = 0, y = 145) #Professor label
    version = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Version  -->  1.0", fg = "IndianRed1", bg = "light blue"). place(x = 0, y = 175) #Version label
    author_name = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Author name  -->  Luis Alejandro Barreda Acevedo", fg = "IndianRed1", bg = "light blue"). place(x = 0, y = 205) #Author label
    module_authors = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Modules' authors  -->  ______", fg = "IndianRed1", bg = "light blue"). place(x = 0, y = 235) #Modules' authors label

    """Buttons______________________________________________________________________________________________________________________________"""
    def destroyabout():
        info.destroy() #finally destroys the window
        
    def showdetails():
        messagebox.showinfo(message = "For the game to save your results, you must start the game by the start button. If you start a level independently your result may be lost or wrong. Shoot only one bullet at a time. If the enemy kicks you out of bounds, return with the arrow keys", title="Important Details") #opens the message box with the important details
        
    destruir = tk.Button(info, text = "Main Menu", font = ("Comic Sans MS", 10), bg = "IndianRed1", fg = "light blue", command = destroyabout). place(x = 0, y = 5) #button with the "about" window destruction command
    details = tk.Button(info, text = "Game Details", font = ("Comic Sans MS", 10), bg = "IndianRed1", fg = "light blue", command = showdetails). place(x = 100, y = 5) #button with the "about" window destruction command
    
    info.mainloop()

"""Top Players Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""
def opentop():
    archive = open('Top5Players.txt', "r")
    data = [line.rstrip('\n').split(':') for line in archive]
        
    messagebox.showinfo(message = data[0][0] + " " +data[1][0] + " " + data[2][0] + " " + data[3][0] + " " + data[4][0] + " " + data[5][0] + " " + data[6][0] + " " + data[7][0] + "1. " + data[8][0] + "  2. " + data[9][0] + "  3. " + data[10][0] + "  4. " +data[11][0] + "  5. " + data[12][0], title = "Top 5 Players") #opens the message box with the top 5 players
    
"""Game1 Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""

def game1():
    game = Toplevel() #creates the game window
    game.title("Operation Moon Light") #gives the game window a title
    game.geometry("630x750") #gives the game window its dimensions
    game.configure(background = "midnightblue") #configure the window background color
    
    """Canvas widget_______________________________________________________________________________________________________________"""
    gamecanvas = Canvas(game, width = 450, height = 650, bg = 'black') #create the canvas widget where the animation is going to occur 
    spacebg = gamecanvas.create_image(230, 350, image = space)
    enemy1 = gamecanvas.create_oval(15, 15, 80, 80, fill = "IndianRed1") #enemy spaceship
    user = gamecanvas.create_oval(10, 10, 60, 60, fill = "ghostwhite") #user's spaceship
    gamecanvas.move(user, 190, 570) #place the user's spaceship down the canvas    

    """User's life functions_________________________________________________________________________________________________________"""
    def ulifeassignation():
        ulifeindicator.config(text = "Life: " + str(userlife)) #set the actual user life points to the tag that show them
        
    """Enemy's life functions________________________________________________________________________________________________________"""
    def e1lifeassignation():
        e1lifeindicator.config(text = "Enemy: " + str(enemy1life)) #set the actual enemy life points to the tag that show them

    """Score functions_____________________________________________________________________________________________________________"""
    def scoreassignation():
        scoreindicator.config(text = "Score: " + str(score)) #set the actual score to the tag that show them

    """Top 5 Players update_____________________________________________________________________________________________________________"""

    def top5set():
        top5 = top5update()
        with open('Top5Players.txt', 'w') as update:
            for i in top5: #cycle that writes down the information in the .txt
                update.write(i)
                update.write("\n")
    
    def top5update():
        n = name.get() #Gets the user's name
        strusername = str(n) #Produce a tring with the user name for the record
        alltext = [] #list with all the .txt  information
        with open('Top5Players.txt', 'r') as top5:
            for line in top5.readlines():
                alltext.append(line) #adds all the text in a list

        allminusn = [] #takes away the \n string that attaches to the text when it is taken
        for line in alltext: #cycle that makes this possible
            minusn = line.replace("\n", "") #search for the string
            allminusn.append(minusn) #adds all the text in a list

        scoreonly = allminusn
        n = 8
        while n != 0: #takes only the score in a list of strings
            scoreonly = scoreonly[1: ]
            n -= 1

        nameonly = []
        m = 0
        for m in range(1, 6): #takes the 5 names of the top players in a list of strings
            nameonly = nameonly + [allminusn[m]]
            m += 1

        intscores = []
        i = 0
        scores = 5
        while i != scores: #produce a list with the int values of the top scores
            intscores.append(int(scoreonly[i]))
            i += 1

        """
        These lists are the name only mentioned before, but without the 1., 2.,..., 5. label
        """
        nameonly2 = []
        for line in nameonly:
            takedot = line.replace(".", "")
            nameonly2.append(takedot)

        nameonly3 = []
        for line in nameonly2:
            takedot = line.replace("1", "")
            nameonly3.append(takedot)

        nameonly4 = []
        for line in nameonly3:
            takedot = line.replace("2", "")
            nameonly4.append(takedot)

        nameonly5 = []
        for line in nameonly4:
            takedot = line.replace("3", "")
            nameonly5.append(takedot)

        nameonly6 = []
        for line in nameonly5:
            takedot = line.replace("4", "")
            nameonly6.append(takedot)

        nameonly7 = []
        for line in nameonly6:
            takedot = line.replace("5", "")
            nameonly7.append(takedot)

        nameonly8 = []
        for line in nameonly7:
            takedot = line.replace(" ", "")
            nameonly8.append(takedot)

        def count(scoreonly, nameonly8, allminusn, actualscore, actualname, defil, i): #function in charge of eliminating the least score and adding the one of the user
            if scoreonly == []:
                return allminusn
            elif actualscore > int(scoreonly[0]): #condition of the position that belongs to the user if it has more points than anyone in the top
                scoreonly.pop()
                defil = defil + scoreonly + [str(actualscore)]
                defil.sort(reverse = True)
                return count_aux(nameonly8, actualname, defil, i, 0, [])
            else:
                return count(scoreonly[1:], nameonly8, allminusn, actualscore, actualname, defil + [str(scoreonly[0])], i + 1)

        def count_aux(nameonly8, actualname, defil, i, top, definame): #function in charge of eliminating the least score name and adding the one of the user
            if nameonly8 == []:
                definame.sort()
                return ["Top 5 Players by score"] + definame + [""] + ["Respective score"] + defil
            elif top == i: #condition of the position that belongs to the user if it has more points than anyone in the top
                nameonly8.pop()
                return count_aux(nameonly8, actualname, defil, i, top + 1, definame + [str(top + 1) + ". "  + actualname])
            else:
                return count_aux(nameonly8[1: ], actualname, defil, i, top + 1, definame + [str(top + 1) + ". "  + nameonly8[0]])

        
        return count(scoreonly, nameonly8, allminusn, score, strusername, [], 0) #returns a list with the information ready for adding it to the .txt

    """Destruction of the game window_______________________________________________________________________________________________________________"""
    def destroygame():
        #reset all the values for future uses if the window isn't closed
        global second1
        global score
        global enemy1life
        global userlife
        enemy1life = 30
        userlife = 50
        score = 0
        second1 = 0
        game.destroy() #destroy the game window by the "main menu" button

    """Movement of the ammonition__________________________________________________________________________________________________"""
    def move_ammo():
        global second1
        global score
        global score2
        global enemy1life
        global userlife
        ammopos = gamecanvas.coords(ammo) #gets the ammonition coordinates
        enemy1pos = enemy1coords() #gets the enemy coordinates
        if int(ammopos[3]) < 0: #if the ammo surpass the canvas upper edge, the ammo gets destroyed
            time.sleep(0.01)
            gamecanvas.delete(ammo) #deletes the ammo
        elif (int(ammopos[0]) in range(int(enemy1pos[0]), int(enemy1pos[2])) or int(ammopos[2]) in range(int(enemy1pos[0]), int(enemy1pos[2])))  and   (int(ammopos[1]) in range(int(enemy1pos[1]), int(enemy1pos[3])) or int(ammopos[3]) in range(int(enemy1pos[1]), int(enemy1pos[3]))): #if the ammo hits the enemy, gets deleted
            time.sleep(0.01)
            gamecanvas.delete(ammo) #deletes the ammo
            score += 1 #add one point to the score
            scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
            scoreth.start() #starts the score modification thread
            enemy1life -= 1
            e1lifeth = Thread(target = e1lifeassignation, args = ()) #thread that calls the function of the enemy's life modification
            e1lifeth.start() #starts the enemy's life modification thread
            if enemy1life <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                winningtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "LEVEL CLEARED !", fg = "ghostwhite", bg = "midnightblue") #Label with the winning title
                winningtitle.place(x = 215, y = 8) #Place the winning title label
                gamecanvas.delete(enemy1) #deletes the enemy1
                if userlife == 50 and second1 <= 60:
                    score += 30 #add 30 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
                elif userlife == 50:
                    score += 10 #add 10 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
                elif second1 <= 60:
                    score += 20 #add 20 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
                else:
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
        else:
            time.sleep(0.01)
            gamecanvas.move(ammo, 0, -10) #moves the ammo towards the enemy
            return move_ammo() #recursive call to move the ammo continuously

    """Enemy spaceship movement function and timer function thread_________________________________________________________________________"""
    def startthread():
        e1movement = Thread(target = move_enemy1f, args = ()) #thread that calls the function that produces the movement
        e1movement.start() #starts the movement thread
        timer = Thread(target = starttimer, args = ()) #thread that calls the function of the timer
        timer.start() #starts the timer thread
    
    """Timer Functions_______________________________________________________________________________________________________________"""
    def starttimer():
        while True:
            time.sleep(1)
            global second1
            second1 += 1
            countdown.config(text = "Timer: " + str(second1)) #set the actual time to the tag that show them

    """Enemy spaceship movement_______________________________________________________________________________________________________"""
    """FORWARD"""
    def move_enemy1f():
        global second1
        global score
        global enemy1life
        global userlife
        prob = random.randint(1, 99) #chooses a random number for a future decision
        enemy1pos = enemy1coords() #gets the enemy coordinates
        userpos = usercoords() #gets the user coordinates
        if enemy1pos[2] > 430: #if the object reaches the right edge, it moves backward
            time.sleep(0.1)
            gamecanvas.move(enemy1, 0, 0) #stops the object and...
            return move_enemy1b() #calls the funtion that makes the backward movement
        elif (int(userpos[0]) in range(int(enemy1pos[0]), int(enemy1pos[2])) or int(userpos[2]) in range(int(enemy1pos[0]), int(enemy1pos[2])))  and   (int(userpos[1]) in range(int(enemy1pos[1]), int(enemy1pos[3])) or int(userpos[3]) in range(int(enemy1pos[1]), int(enemy1pos[3]))): #if the enemy hits the user
            time.sleep(0.1)
            gamecanvas.move(user, 0, 300) #moves the user out of the enemy range to prevent the extra life loosing
            userlife -= 10 #subtracts 10 life points from the userlife variable
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
            else:
                return move_enemy1f() #calls the function in a recursive way
        elif second1 % 2 == 0 and second1 != 0 and prob % 10 == 0 and prob < 100:
            time.sleep(0.1)
            gamecanvas.move(enemy1, 0, 0) #stops the object and...
            return move_enemy1d() #calls the funtion that makes the down movement
        else:
            time.sleep(0.1)
            gamecanvas.move(enemy1, 20, 0) #moves the object 20 by 20 spaces forward until the spaceship reach the right edge
            return move_enemy1f() #calls the function in a recursive way

    """BACKWARD"""
    def move_enemy1b():
        global second1
        global score
        global enemy1life
        global userlife
        prob = random.randint(1, 99) #chooses a random number for future decisions
        enemy1pos = enemy1coords() #gets the enemy coordinates
        userpos = usercoords() #gets the user coordinates
        if enemy1pos[0] < 30: #if the object reaches the left edge, it moves forward
            time.sleep(0.1)
            gamecanvas.move(enemy1, 0, 0) #stops the object and...
            return move_enemy1f() #calls the funtion that makes the forward movement
        elif (int(userpos[0]) in range(int(enemy1pos[0]), int(enemy1pos[2])) or int(userpos[2]) in range(int(enemy1pos[0]), int(enemy1pos[2])))  and   (int(userpos[1]) in range(int(enemy1pos[1]), int(enemy1pos[3])) or int(userpos[3]) in range(int(enemy1pos[1]), int(enemy1pos[3]))): #if the enemy hits the user
            time.sleep(0.1)
            gamecanvas.move(user, 0, 300) #moves the user out of the enemy range to prevent the extra life loosing
            userlife -= 10 #subtracts 10 life points from the userlife variable
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
            else:
                return move_enemy1b() #calls the function in a recursive way
        elif second1 % 2 == 0 and second1 != 0 and prob % 10 == 0 and prob < 100:
            time.sleep(0.1)
            gamecanvas.move(enemy1, 0, 0) #stops the object and...
            return move_enemy1d() #calls the funtion that makes the down movement
        else:
            time.sleep(0.1)
            gamecanvas.move(enemy1, -20, 0) #moves the object 20 by 20 spaces backward until the spaceship reach the left edge
            return move_enemy1b() #calls the function in a recursive way

    """DOWNWARD"""
    def move_enemy1d():
        global second1
        global score
        global score2
        global enemy1life
        global userlife
        enemy1pos = enemy1coords() #gets the enemy coordinates
        userpos = usercoords() #gets the user coordinates
        if enemy1pos[3] > 620: #if the object reaches the lower edge, it moves upward
            time.sleep(0.1)
            gamecanvas.move(enemy1, 0, 0) #stops the object and...
            enemy1life -= 1 #subtracts 1 life point from the enemy1life variable
            e1lifeth = Thread(target = e1lifeassignation, args = ()) #thread that calls the function of the enemy's life modification
            e1lifeth.start() #starts the enemy's life modification thread
            if enemy1life <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                winningtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "LEVEL CLEARED !", fg = "ghostwhite", bg = "midnightblue") #Label with the winning title
                winningtitle.place(x = 215, y = 8) #Place the winning title label
                gamecanvas.delete(enemy1) #deletes the enemy1
                if userlife == 50 and second1 <= 60:
                    score += 30 #add 30 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score #saves the score before the original gets destroyed
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
                elif userlife == 50:
                    score += 10 #add 10 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score #saves the score before the original gets destroyed
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
                elif second1 <= 60:
                    score += 20 #add 20 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score #saves the score before the original gets destroyed
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the destroygame function
                    level2th.start() #start the thread
                else:
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score #saves the score before the original gets destroyed
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
            else:
                return move_enemy1u() #calls the funtion that makes the upward movement
        elif (int(userpos[0]) in range(int(enemy1pos[0]), int(enemy1pos[2])) or int(userpos[2]) in range(int(enemy1pos[0]), int(enemy1pos[2])))  and   (int(userpos[1]) in range(int(enemy1pos[1]), int(enemy1pos[3])) or int(userpos[3]) in range(int(enemy1pos[1]), int(enemy1pos[3]))): #if the enemy hits the user
            time.sleep(0.1)
            gamecanvas.move(user, -100, 100) #moves the user out of the enemy range to prevent the extra life loosing
            gamecanvas.move(enemy1, 0, -20)  #moves the object 20 by 20 spaces upward until the spaceship reach the upper edge
            enemy1life -= 1 #subtracts 1 life point from the enemy1life variable
            e1lifeth = Thread(target = e1lifeassignation, args = ()) #thread that calls the function of the enemy's life modification
            e1lifeth.start() #starts the enemy's life modification thread
            userlife -= 10 #subtracts 10 life points from the userlife variable
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if enemy1life <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                winningtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "LEVEL CLEARED !", fg = "ghostwhite", bg = "midnightblue") #Label with the winning title
                winningtitle.place(x = 215, y = 8) #Place the winning title label
                gamecanvas.delete(enemy1) #deletes the enemy1
                if userlife == 50 and second1 <= 60:
                    score += 30 #add 30 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score #saves the score before the original gets destroyed
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
                elif userlife == 50:
                    score += 10 #add 10 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score #saves the score before the original gets destroyed
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
                elif second1 <= 60:
                    score += 20 #add 20 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score #saves the score before the original gets destroyed
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
                else:
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score2 = score #saves the score before the original gets destroyed
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level2th = Thread(target = game2, args = ()) #thread that calls the game2 window function
                    level2th.start() #start the thread
            elif userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losing title
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
            else:
                return move_enemy1u() #calls the function in a recursive way
        else:
            time.sleep(0.1)
            gamecanvas.move(enemy1, 0, 30) #moves the object 30 by 30 spaces downward until the spaceship reach the lower edge
            return move_enemy1d() #calls the function in a recursive way

    """UPWARD"""
    def move_enemy1u():
        global second1
        global score
        global enemy1life
        global userlife
        enemy1pos = enemy1coords() #gets the enemy coordinates
        userpos = usercoords() #gets the user coordinates
        if enemy1pos[1] < 30: #if the object reaches the upper edge, it moves forward or backward depending of its position
            time.sleep(0.1)
            gamecanvas.move(enemy1, 0, 0) #stops the object and...
            if enemy1pos[0] > 215:
                return move_enemy1b() #calls the funtion that makes the backward movement
            else:
                return move_enemy1f() #calls the funtion that makes the forward movement
        elif (int(userpos[0]) in range(int(enemy1pos[0]), int(enemy1pos[2])) or int(userpos[2]) in range(int(enemy1pos[0]), int(enemy1pos[2])))  and   (int(userpos[1]) in range(int(enemy1pos[1]), int(enemy1pos[3])) or int(userpos[3]) in range(int(enemy1pos[1]), int(enemy1pos[3]))): #if the enemy hits the user
            time.sleep(0.1)
            gamecanvas.move(user, 100, -100) #moves the user out of the enemy range to prevent the extra life loosing
            gamecanvas.move(enemy1, 0, -20) #moves the object 20 by 20 spaces upward until the spaceship reach the upper edge
            userlife -= 10 #subtracts 10 life points from the userlife variable
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
            else:
                return move_enemy1u() #calls the function in a recursive way
        else:
            time.sleep(0.1)
            gamecanvas.move(enemy1, 0, -20) #moves the object 20 by 20 spaces upward until the spaceship reach the upper edge
            return move_enemy1u() #calls the function in a recursive way

    """Position of the spaceships_______________________________________________________________________________________________________________"""
    def usercoords():
        return gamecanvas.coords(user) #canvas function that receives the coordinates of the user's spaceship

    def enemy1coords():
        return gamecanvas.coords(enemy1) #canvas function that receives the coordinates of the enemy spaceship

    """Keys functions________________________________________________________________________________________________________________________"""
    #x and y are the number of positions the user's spaceship is going to move from its original position
    def left(event):
        x = -20 
        y = 0
        gamecanvas.move(user, x, y) #moves the ship -20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def right(event):
        x = 20
        y = 0
        gamecanvas.move(user, x, y) #moves the ship 20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def up(event):
        x = 0
        y = -20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and -20 spaces in the y direction, from its original position

    def down(event):
        x = 0
        y = 20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and 20 spaces in the y direction, from its original position

    def shoot(event):
        userposition = usercoords() #Receives the tuple of the coordinates of the user space ship
        global ammo
        ammo = gamecanvas.create_oval(5, 5, 15, 15, fill = "gold") #creates the ammo that the spaceship shoot
        gamecanvas.move(ammo, userposition[0] + 15, userposition[1] - 15) #place the ammo in spaceship
        pygame.mixer.init() #initialize the mixer
        mixer.music.load('lasersound.wav') #loads the laser sound
        mixer.music.play() #plays the sound
        ammomove = Thread(target = move_ammo, args = ()) #thread that calls the function that produces the movement
        ammomove.start() #start the thread
                        
    """Keys Binding______________________________________________________________________________________________________________________"""

    game.bind("<Left>", left) #binds the left key to the left movement function
    game.bind("<Right>", right) #binds the right key to the left movement function
    game.bind("<Up>", up) #binds the up key to the left movement function
    game.bind("<Down>", down) #binds the down key to the left movement function
    game.bind("<space>", shoot) #binds the space bar to the shooting function
    
    """Buttons of the game window___________________________________________________________________________________________________________"""
    startgame = tk.Button(game, text = "Start", font = ("Comic Sans MS", 10), bg = "white", fg = "midnightblue", command = startthread)
    startgame.place(x = 50, y = 10) #start the game
    
    game_mainnmenu = tk.Button(game, text = "Main Menu", font = ("Comic Sans MS", 10), bg = "white", fg = "midnightblue", command = destroygame)
    game_mainnmenu.place(x = 110, y = 10) #return to the main menu, losing the user's record
    
    """Labels of the game window___________________________________________________________________________________________________________"""    
    n = name.get() #Gets the user's name
    username = tk.Label(game, text = "User: " + n, font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue")
    username.place(x = 510, y = 100) #Label where the user's name is written

    countdown = tk.Label(game, text = "Timer: " + str(second1), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the time is written
    countdown.place(x = 510, y = 140) #place the timer label

    scoreindicator = tk.Label(game, text = "Score: " + str(score), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the score is written
    scoreindicator.place(x = 510, y = 180) #place the score label
    
    ulifeindicator = tk.Label(game, text = "Life: " + str(userlife), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the user's life is written
    ulifeindicator.place(x = 510, y = 220) #place the user's life label
    
    e1lifeindicator = tk.Label(game, text = "Enemy: " + str(enemy1life), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the enemy's life is written
    e1lifeindicator.place(x = 510, y = 260) #place the enemy's life label
    
    """Canvas configuration_________________________________________________________________________________________________________________"""
    gamecanvas.place(x = 50, y = 50) #place the canvas widget  
    game.mainloop()

"""Game 2 Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""
def game2():
    game = Toplevel() #creates the game window
    game.title("Operation Moon Light") #gives the game window a title
    game.geometry("630x750") #gives the game window its dimensions
    game.configure(background = "midnightblue") #configure the window background color
    
    """Canvas widget_______________________________________________________________________________________________________________"""
    gamecanvas = Canvas(game, width = 450, height = 650, bg = "black") #create the canvas widget where the animation is going to occur
    spacebg = gamecanvas.create_image(230, 350, image = space)
    enemy2 = gamecanvas.create_oval(15, 15, 80, 80, fill = "lime") #enemy spaceship
    user = gamecanvas.create_oval(10, 10, 60, 60, fill = "ghostwhite") #user's spaceship
    gamecanvas.move(enemy2, 175, 15) #place the enemy's spaceship down the canvas
    gamecanvas.move(user, 190, 570) #place the user's spaceship down the canvas

    """User's life functions_________________________________________________________________________________________________________"""
    def ulifeassignation():
        ulifeindicator.config(text = "Life: " + str(userlife)) #set the actual user life points to the tag that show them
        
    """Enemy's life functions________________________________________________________________________________________________________"""
    def e2lifeassignation():
        e2lifeindicator.config(text = "Enemy: " + str(enemy2life)) #set the actual enemy life points to the tag that show them

    """Score functions_____________________________________________________________________________________________________________"""
    def scoreassignation():
        scoreindicator.config(text = "Score: " + str(score2)) #set the actual score to the tag that show them

    """Top5 Functions"""
    def top5set():
        top5 = top5update()
        with open('Top5Players.txt', 'w') as update:
            for i in top5: #cycle that writes down the information in the .txt
                update.write(i)
                update.write("\n")
    
    def top5update():
        n = name.get() #Gets the user's name
        strusername = str(n) #Produce a tring with the user name for the record
        alltext = [] #list with all the .txt  information
        with open('Top5Players.txt', 'r') as top5:
            for line in top5.readlines():
                alltext.append(line) #adds all the text in a list

        allminusn = [] #takes away the \n string that attaches to the text when it is taken
        for line in alltext: #cycle that makes this possible
            minusn = line.replace("\n", "") #search for the string
            allminusn.append(minusn) #adds all the text in a list

        scoreonly = allminusn
        n = 8
        while n != 0: #takes only the score in a list of strings
            scoreonly = scoreonly[1: ]
            n -= 1

        nameonly = []
        m = 0
        for m in range(1, 6): #takes the 5 names of the top players in a list of strings
            nameonly = nameonly + [allminusn[m]]
            m += 1

        intscores = []
        i = 0
        scores = 5
        while i != scores: #produce a list with the int values of the top scores
            intscores.append(int(scoreonly[i]))
            i += 1

        """
        These lists are the name only mentioned before, but without the 1., 2.,..., 5. label
        """
        nameonly2 = []
        for line in nameonly:
            takedot = line.replace(".", "")
            nameonly2.append(takedot)

        nameonly3 = []
        for line in nameonly2:
            takedot = line.replace("1", "")
            nameonly3.append(takedot)

        nameonly4 = []
        for line in nameonly3:
            takedot = line.replace("2", "")
            nameonly4.append(takedot)

        nameonly5 = []
        for line in nameonly4:
            takedot = line.replace("3", "")
            nameonly5.append(takedot)

        nameonly6 = []
        for line in nameonly5:
            takedot = line.replace("4", "")
            nameonly6.append(takedot)

        nameonly7 = []
        for line in nameonly6:
            takedot = line.replace("5", "")
            nameonly7.append(takedot)

        nameonly8 = []
        for line in nameonly7:
            takedot = line.replace(" ", "")
            nameonly8.append(takedot)

        def count(scoreonly, nameonly8, allminusn, actualscore, actualname, defil, i): #function in charge of eliminating the least score and adding the one of the user
            if scoreonly == []:
                return allminusn
            elif actualscore > int(scoreonly[0]): #condition of the position that belongs to the user if it has more points than anyone in the top
                scoreonly.pop()
                defil = defil + scoreonly + [str(actualscore)]
                defil.sort(reverse = True)
                return count_aux(nameonly8, actualname, defil, i, 0, [])
            else:
                return count(scoreonly[1:], nameonly8, allminusn, actualscore, actualname, defil + [str(scoreonly[0])], i + 1)

        def count_aux(nameonly8, actualname, defil, i, top, definame): #function in charge of eliminating the least score name and adding the one of the user
            if nameonly8 == []:
                definame.sort()
                return ["Top 5 Players by score"] + definame + [""] + ["Respective score"] + defil
            elif top == i: #condition of the position that belongs to the user if it has more points than anyone in the top
                nameonly8.pop()
                return count_aux(nameonly8, actualname, defil, i, top + 1, definame + [str(top + 1) + ". "  + actualname])
            else:
                return count_aux(nameonly8[1: ], actualname, defil, i, top + 1, definame + [str(top + 1) + ". "  + nameonly8[0]])

        
        return count(scoreonly, nameonly8, allminusn, score2, strusername, [], 0) #returns a list with the information ready for adding it to the .txt
    
    """Destruction of the game window_______________________________________________________________________________________________________________"""
    def destroygame():
        #reset all the values for future uses if the window isn't closed
        global second1
        global score2
        global enemy2life
        global userlife
        enemy2life = 40
        userlife = 50
        score2 = 0
        second1 = 0
        game.destroy() #destroy the game window by the "main menu" button

    """Movement of the ammonition__________________________________________________________________________________________________"""
    def move_ammo():
        global second1
        global score2
        global score3
        global enemy2life
        global userlife
        ammopos = gamecanvas.coords(ammo) #gets the ammonition coordinates
        enemy2pos = enemy2coords() #gets the enemy coordinates
        if int(ammopos[3]) < 0: #if the ammo surpass the canvas upper edge, the ammo gets destroyed
            time.sleep(0.01)
            gamecanvas.delete(ammo) #deletes the ammo
        elif (int(ammopos[0]) in range(int(enemy2pos[0]), int(enemy2pos[2])) or int(ammopos[2]) in range(int(enemy2pos[0]), int(enemy2pos[2])))  and   (int(ammopos[1]) in range(int(enemy2pos[1]), int(enemy2pos[3])) or int(ammopos[3]) in range(int(enemy2pos[1]), int(enemy2pos[3]))): #if the ammo hits the enemy, gets deleted
            time.sleep(0.01)
            gamecanvas.delete(ammo) #deletes the ammo
            score2 += 1 #add one point to the score
            scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
            scoreth.start() #starts the score modification thread
            enemy2life -= 1
            e2lifeth = Thread(target = e2lifeassignation, args = ()) #thread that calls the function of the enemy's life modification
            e2lifeth.start() #starts the enemy's life modification thread
            if enemy2life <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                winningtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "LEVEL CLEARED !", fg = "ghostwhite", bg = "midnightblue") #Label with the winning title
                winningtitle.place(x = 215, y = 8) #Place the winning title label
                gamecanvas.delete(enemy2) #deletes the enemy1
                if userlife == 50 and second1 <= 90:
                    score2 += 30 #add 30 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score3 = score2
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level3th = Thread(target = game3, args = ()) #thread that calls the destroygame function
                    level3th.start() #start the thread
                elif userlife == 50:
                    score2 += 10 #add 10 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score3 = score2
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level3th = Thread(target = game3, args = ()) #thread that calls the destroygame function
                    level3th.start() #start the thread
                elif second1 <= 90:
                    score2 += 20 #add 20 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score3 = score2
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level3th = Thread(target = game3, args = ()) #thread that calls the destroygame function
                    level3th.start() #start the thread
                else:
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    score3 = score2
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                    time.sleep(3)
                    level3th = Thread(target = game3, args = ()) #thread that calls the destroygame function
                    level3th.start() #start the thread
        else:
            time.sleep(0.01)
            gamecanvas.move(ammo, 0, -10) #moves the ammo towards the enemy
            return move_ammo() #recursive call to move the ammo continuously

    """Movement of the enemy attacks__________________________________________________________________________________________________"""
    def move_attack1():
        global userlife
        atta1pos = gamecanvas.coords(atta1) #gets the attack 1 coordinates
        userpos = usercoords() #gets the user coordinates
        if int(atta1pos[3]) > 650: #if the attack1 surpass the canvas lower edge, the ammo gets destroyed
            time.sleep(0.01)
            gamecanvas.delete(atta1) #deletes the attack 1
        elif (int(atta1pos[0]) in range(int(userpos[0]), int(userpos[2])) or int(atta1pos[2]) in range(int(userpos[0]), int(userpos[2])))  and   (int(atta1pos[1]) in range(int(userpos[1]), int(userpos[3])) or int(atta1pos[3]) in range(int(userpos[1]), int(userpos[3]))): #if the attack 1 hits the user, gets deleted
            time.sleep(0.01)
            gamecanvas.delete(atta1) #deletes the attack 1
            userlife -= 3
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
        else:
            time.sleep(0.01)
            gamecanvas.move(atta1, 0, 6) #moves the attack 1 towards the user
            return move_attack1() #recursive call to move the attack1 continuously

    def move_attack2():
        global userlife
        atta2pos = gamecanvas.coords(atta2) #gets the attack 2 coordinates
        userpos = usercoords() #gets the user coordinates
        if int(atta2pos[3]) > 650: #if the attack 2 surpass the canvas lower edge, the ammo gets destroyed
            time.sleep(0.01)
            gamecanvas.delete(atta2) #deletes the attack 2
        elif (int(atta2pos[0]) in range(int(userpos[0]), int(userpos[2])) or int(atta2pos[2]) in range(int(userpos[0]), int(userpos[2])))  and   (int(atta2pos[1]) in range(int(userpos[1]), int(userpos[3])) or int(atta2pos[3]) in range(int(userpos[1]), int(userpos[3]))): #if the attack 1 hits the user, gets deleted
            time.sleep(0.01)
            gamecanvas.delete(atta2) #deletes the attack 2
            userlife -= 3
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
        else:
            time.sleep(0.01)
            gamecanvas.move(atta2, 0, 6) #moves the attack 2 towards the user
            return move_attack2() #recursive call to move the attack2 continuously

    def move_attack3():
        global userlife
        atta3pos = gamecanvas.coords(atta3) #gets the ammonition coordinates
        userpos = usercoords() #gets the enemy coordinates
        if int(atta3pos[3]) > 650: #if the attack3 surpass the canvas lower edge, the ammo gets destroyed
            time.sleep(0.01)
            gamecanvas.delete(atta3) #deletes the atta3
        elif (int(atta3pos[0]) in range(int(userpos[0]), int(userpos[2])) or int(atta3pos[2]) in range(int(userpos[0]), int(userpos[2])))  and   (int(atta3pos[1]) in range(int(userpos[1]), int(userpos[3])) or int(atta3pos[3]) in range(int(userpos[1]), int(userpos[3]))): #if the attack 1 hits the user, gets deleted
            time.sleep(0.01)
            gamecanvas.delete(atta3) #deletes the atta3
            userlife -= 3
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
        else:
            time.sleep(0.01)
            gamecanvas.move(atta3, 0, 6) #moves the attack 3 towards the user
            return move_attack3() #recursive call to move the attack3 continuously
    
    """Enemy spaceship movement function and timer function thread_________________________________________________________________________"""
    def startthread():
        e2movement = Thread(target = move_enemy2, args = ()) #thread that calls the function that produces the movement
        e2movement.start() #starts the movement thread
        timer = Thread(target = starttimer, args = ()) #thread that calls the function of the timer
        timer.start() #starts the timer thread
    
    """Timer Functions_______________________________________________________________________________________________________________"""
    def starttimer():
        while True:
            time.sleep(1)
            global second1
            second1 += 1
            countdown.config(text = "Timer: " + str(second1)) #set the actual time to the tag that show them

    """Enemy spaceship movement_______________________________________________________________________________________________________"""
    def move_enemy2():
        while True:
            time.sleep(1)
            enemy2pos = enemy2coords() #Receives the tuple of the coordinates of the enemy2 space ship
            global atta1
            global atta2
            global atta3
            
            atta1 = gamecanvas.create_oval(5, 5, 15, 15, fill = "darkorange") #creates the attack that the enemy spaceship shoot
            gamecanvas.move(atta1, enemy2pos[0] + 25, enemy2pos[1] + 70) #place the attack in enemy's spaceship

            atta2 = gamecanvas.create_oval(5, 5, 15, 15, fill = "darkorange") #creates the attack that the enemy spaceship shoot
            gamecanvas.move(atta2, enemy2pos[0] + 25, enemy2pos[1] + 110) #place the attack in enemy's spaceship
            
            atta3 = gamecanvas.create_oval(5, 5, 15, 15, fill = "darkorange") #creates the attack that the enemy spaceship shoot
            gamecanvas.move(atta3, enemy2pos[0] + 25, enemy2pos[1] + 150) #place the attack in enemy's spaceship

            pygame.mixer.init() #initialize the mixer
            mixer.music.load('lasersound.wav') #loads the laser sound
            mixer.music.play() #plays the sound
            atta1move = Thread(target = move_attack1, args = ()) #thread that calls the function that produces the movement
            atta1move.start() #start the thread

            pygame.mixer.init() #initialize the mixer
            mixer.music.load('lasersound.wav') #loads the laser sound
            mixer.music.play() #plays the sound
            atta2move = Thread(target = move_attack2, args = ()) #thread that calls the function that produces the movement
            atta2move.start() #start the thread

            pygame.mixer.init() #initialize the mixer
            mixer.music.load('lasersound.wav') #loads the laser sound
            mixer.music.play() #plays the sound
            atta3move = Thread(target = move_attack3, args = ()) #thread that calls the function that produces the movement
            atta3move.start() #start the thread

            time.sleep(1)
            randpos = random.randint(15, 350)
            gamecanvas.move(enemy2, (randpos - int(enemy2pos[0])), 0) #moves the enemy in a random way along the x axis
            
        
    """Position of the spaceships_______________________________________________________________________________________________________________"""
    def usercoords():
        return gamecanvas.coords(user) #canvas function that receives the coordinates of the user's spaceship

    def enemy2coords():
        return gamecanvas.coords(enemy2) #canvas function that receives the coordinates of the enemy spaceship

    """Keys functions________________________________________________________________________________________________________________________"""
        #x and y are the number of positions the user's spaceship is going to move from its original position
    def left(event):
        x = -20 
        y = 0
        gamecanvas.move(user, x, y) #moves the ship -20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def right(event):
        x = 20
        y = 0
        gamecanvas.move(user, x, y) #moves the ship 20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def up(event):
        x = 0
        y = -20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and -20 spaces in the y direction, from its original position

    def down(event):
        x = 0
        y = 20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and 20 spaces in the y direction, from its original position

    def shoot(event):
        userposition = usercoords() #Receives the tuple of the coordinates of the user space ship
        global ammo
        ammo = gamecanvas.create_oval(5, 5, 15, 15, fill = "gold") #creates the ammo that the spaceship shoot
        gamecanvas.move(ammo, userposition[0] + 15, userposition[1] - 15) #place the ammo in spaceship
        pygame.mixer.init() #initialize the mixer
        mixer.music.load('lasersound.wav') #loads the laser sound
        mixer.music.play() #plays the sound
        ammomove = Thread(target = move_ammo, args = ()) #thread that calls the function that produces the movement
        ammomove.start() #start the thread
                        
    """Keys Binding______________________________________________________________________________________________________________________"""

    game.bind("<Left>", left) #binds the left key to the left movement function
    game.bind("<Right>", right) #binds the right key to the left movement function
    game.bind("<Up>", up) #binds the up key to the left movement function
    game.bind("<Down>", down) #binds the down key to the left movement function
    game.bind("<space>", shoot) #binds the space bar to the shooting function
    
    """Buttons of the game window___________________________________________________________________________________________________________"""
    startgame = tk.Button(game, text = "Start", font = ("Comic Sans MS", 10), bg = "ghostwhite", fg = "midnightblue", command = startthread)
    startgame.place(x = 50, y = 10) #start the game
    
    game_mainnmenu = tk.Button(game, text = "Main Menu", font = ("Comic Sans MS", 10), bg = "ghostwhite", fg = "midnightblue", command = destroygame)
    game_mainnmenu.place(x = 110, y = 10) #return to the main menu, losing the user's record
    
    """Labels of the game window___________________________________________________________________________________________________________"""    
    n = name.get() #Gets the user's name
    username = tk.Label(game, text = "User: " + n, font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue")
    username.place(x = 510, y = 100) #Label where the user's name is written

    countdown = tk.Label(game, text = "Timer: " + str(second1), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the time is written
    countdown.place(x = 510, y = 140) #place the timer label

    scoreindicator = tk.Label(game, text = "Score: " + str(score2), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the score is written
    scoreindicator.place(x = 510, y = 180) #place the score label
    
    ulifeindicator = tk.Label(game, text = "Life: " + str(userlife), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the user's life is written
    ulifeindicator.place(x = 510, y = 220) #place the user's life label
    
    e2lifeindicator = tk.Label(game, text = "Enemy: " + str(enemy2life), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the enemy's life is written
    e2lifeindicator.place(x = 510, y = 260) #place the enemy's life label
    
    """Canvas configuration_________________________________________________________________________________________________________________"""
    gamecanvas.place(x = 50, y = 50) #place the canvas widget  
    game.mainloop()

"""Game 3 Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""
def game3():
    game = Toplevel() #creates the game window
    game.title("Operation Moon Light") #gives the game window a title
    game.geometry("630x750") #gives the game window its dimensions
    game.configure(background = "midnightblue") #configure the window background color
    
    """Canvas widget_______________________________________________________________________________________________________________"""
    gamecanvas = Canvas(game, width = 450, height = 650, bg = "black") #create the canvas widget where the animation is going to occur 
    spacebg = gamecanvas.create_image(230, 350, image = space)
    enemy3 = gamecanvas.create_oval(15, 15, 80, 80, fill = "mediumturquoise") #enemy spaceship
    user = gamecanvas.create_oval(10, 10, 60, 60, fill = "ghostwhite") #user's spaceship
    gamecanvas.move(user, 190, 570) #place the user's spaceship down the canvas

    """User's life functions_________________________________________________________________________________________________________"""
    def ulifeassignation():
        ulifeindicator.config(text = "Life: " + str(userlife)) #set the actual user life points to the tag that show them
        
    """Enemy's life functions________________________________________________________________________________________________________"""
    def e3lifeassignation():
        e3lifeindicator.config(text = "Enemy: " + str(enemy3life)) #set the actual enemy life points to the tag that show them

    """Score functions_____________________________________________________________________________________________________________"""
    def scoreassignation():
        scoreindicator.config(text = "Score: " + str(score3)) #set the actual score to the tag that show them

    """Top5 Functions"""
    def top5set():
        top5 = top5update()
        with open('Top5Players.txt', 'w') as update:
            for i in top5: #cycle that writes down the information in the .txt
                update.write(i)
                update.write("\n")
    
    def top5update():
        n = name.get() #Gets the user's name
        strusername = str(n) #Produce a tring with the user name for the record
        alltext = [] #list with all the .txt  information
        with open('Top5Players.txt', 'r') as top5:
            for line in top5.readlines():
                alltext.append(line) #adds all the text in a list

        allminusn = [] #takes away the \n string that attaches to the text when it is taken
        for line in alltext: #cycle that makes this possible
            minusn = line.replace("\n", "") #search for the string
            allminusn.append(minusn) #adds all the text in a list

        scoreonly = allminusn
        n = 8
        while n != 0: #takes only the score in a list of strings
            scoreonly = scoreonly[1: ]
            n -= 1

        nameonly = []
        m = 0
        for m in range(1, 6): #takes the 5 names of the top players in a list of strings
            nameonly = nameonly + [allminusn[m]]
            m += 1

        intscores = []
        i = 0
        scores = 5
        while i != scores: #produce a list with the int values of the top scores
            intscores.append(int(scoreonly[i]))
            i += 1

        """
        These lists are the name only mentioned before, but without the 1., 2.,..., 5. label
        """
        nameonly2 = []
        for line in nameonly:
            takedot = line.replace(".", "")
            nameonly2.append(takedot)

        nameonly3 = []
        for line in nameonly2:
            takedot = line.replace("1", "")
            nameonly3.append(takedot)

        nameonly4 = []
        for line in nameonly3:
            takedot = line.replace("2", "")
            nameonly4.append(takedot)

        nameonly5 = []
        for line in nameonly4:
            takedot = line.replace("3", "")
            nameonly5.append(takedot)

        nameonly6 = []
        for line in nameonly5:
            takedot = line.replace("4", "")
            nameonly6.append(takedot)

        nameonly7 = []
        for line in nameonly6:
            takedot = line.replace("5", "")
            nameonly7.append(takedot)

        nameonly8 = []
        for line in nameonly7:
            takedot = line.replace(" ", "")
            nameonly8.append(takedot)

        def count(scoreonly, nameonly8, allminusn, actualscore, actualname, defil, i): #function in charge of eliminating the least score and adding the one of the user
            if scoreonly == []:
                return allminusn
            elif actualscore > int(scoreonly[0]): #condition of the position that belongs to the user if it has more points than anyone in the top
                scoreonly.pop()
                defil = defil + scoreonly + [str(actualscore)]
                defil.sort(reverse = True)
                return count_aux(nameonly8, actualname, defil, i, 0, [])
            else:
                return count(scoreonly[1:], nameonly8, allminusn, actualscore, actualname, defil + [str(scoreonly[0])], i + 1)

        def count_aux(nameonly8, actualname, defil, i, top, definame): #function in charge of eliminating the least score name and adding the one of the user
            if nameonly8 == []:
                definame.sort()
                return ["Top 5 Players by score"] + definame + [""] + ["Respective score"] + defil
            elif top == i: #condition of the position that belongs to the user if it has more points than anyone in the top
                nameonly8.pop()
                return count_aux(nameonly8, actualname, defil, i, top + 1, definame + [str(top + 1) + ". "  + actualname])
            else:
                return count_aux(nameonly8[1: ], actualname, defil, i, top + 1, definame + [str(top + 1) + ". "  + nameonly8[0]])

        
        return count(scoreonly, nameonly8, allminusn, score3, strusername, [], 0) #returns a list with the information ready for adding it to the .txt

    """Destruction of the game window_______________________________________________________________________________________________________________"""
    def destroygame():
        #reset all the values for future uses if the window isn't closed
        global second1
        global score3
        global enemy3life
        global userlife
        enemy3life = 50
        userlife = 50
        score3 = 0
        second1 = 0
        game.destroy() #destroy the game window by the "main menu" button

    """Movement of the ammonition__________________________________________________________________________________________________"""
    def move_ammo():
        global second1
        global score3
        global enemy3life
        global userlife
        ammopos = gamecanvas.coords(ammo) #gets the ammonition coordinates
        enemy3pos = enemy3coords() #gets the enemy coordinates
        if int(ammopos[3]) < 0: #if the ammo surpass the canvas upper edge, the ammo gets destroyed
            time.sleep(0.01)
            gamecanvas.delete(ammo) #deletes the ammo
        elif (int(ammopos[0]) in range(int(enemy3pos[0]), int(enemy3pos[2])) or int(ammopos[2]) in range(int(enemy3pos[0]), int(enemy3pos[2])))  and   (int(ammopos[1]) in range(int(enemy3pos[1]), int(enemy3pos[3])) or int(ammopos[3]) in range(int(enemy3pos[1]), int(enemy3pos[3]))): #if the ammo hits the enemy, gets deleted
            time.sleep(0.01)
            gamecanvas.delete(ammo) #deletes the ammo
            score3 += 1 #add one point to the score
            scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
            scoreth.start() #starts the score modification thread
            enemy3life -= 1
            e3lifeth = Thread(target = e3lifeassignation, args = ()) #thread that calls the function of the enemy's life modification
            e3lifeth.start() #starts the enemy's life modification thread
            if enemy3life <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                winningtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "LEVEL CLEARED !", fg = "ghostwhite", bg = "midnightblue") #Label with the winning title
                winningtitle.place(x = 215, y = 8) #Place the winning title label
                gamecanvas.delete(enemy3) #deletes the enemy1
                if userlife == 50 and second1 <= 120:
                    score3 += 30 #add 30 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                elif userlife == 50:
                    score3 += 10 #add 10 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                elif second1 <= 120:
                    score3 += 20 #add 20 point to the score
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    scoreth = Thread(target = scoreassignation, args = ()) #thread that calls the function of the score modification
                    scoreth.start() #starts the score modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
                else:
                    top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                    top5th.start() #starts the top5 modification thread
                    time.sleep(3)
                    nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    nextth.start() #start the thread
        else:
            time.sleep(0.01)
            gamecanvas.move(ammo, 0, -10) #moves the ammo towards the enemy
            return move_ammo() #recursive call to move the ammo continuously

    """Movement of the enemy attacks__________________________________________________________________________________________________"""
    def move_attack1():
        global userlife
        atta1pos = gamecanvas.coords(atta1) #gets the attack 1 coordinates
        userpos = usercoords() #gets the user coordinates
        if int(atta1pos[3]) > 650: #if the attack1 surpass the canvas lower edge, the ammo gets destroyed
            time.sleep(0.01)
            gamecanvas.delete(atta1) #deletes the attack 1
        elif (int(atta1pos[0]) in range(int(userpos[0]), int(userpos[2])) or int(atta1pos[2]) in range(int(userpos[0]), int(userpos[2])))  and   (int(atta1pos[1]) in range(int(userpos[1]), int(userpos[3])) or int(atta1pos[3]) in range(int(userpos[1]), int(userpos[3]))): #if the attack 1 hits the user, gets deleted
            time.sleep(0.01)
            gamecanvas.delete(atta1) #deletes the attack 1
            userlife -= 3
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
        else:
            time.sleep(0.01)
            gamecanvas.move(atta1, 0, 10) #moves the attack 1 towards the user
            return move_attack1() #recursive call to move the attack1 continuously

    def move_attack2():
        global userlife
        atta2pos = gamecanvas.coords(atta2) #gets the attack 2 coordinates
        userpos = usercoords() #gets the user coordinates
        if int(atta2pos[3]) > 650: #if the attack 2 surpass the canvas lower edge, the ammo gets destroyed
            time.sleep(0.01)
            gamecanvas.delete(atta2) #deletes the attack 2
        elif (int(atta2pos[0]) in range(int(userpos[0]), int(userpos[2])) or int(atta2pos[2]) in range(int(userpos[0]), int(userpos[2])))  and   (int(atta2pos[1]) in range(int(userpos[1]), int(userpos[3])) or int(atta2pos[3]) in range(int(userpos[1]), int(userpos[3]))): #if the attack 1 hits the user, gets deleted
            time.sleep(0.01)
            gamecanvas.delete(atta2) #deletes the attack 2
            userlife -= 3
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
        else:
            time.sleep(0.01)
            gamecanvas.move(atta2, 0, 10) #moves the attack 2 towards the user
            return move_attack2() #recursive call to move the attack2 continuously

    def move_attack3():
        global userlife
        atta3pos = gamecanvas.coords(atta3) #gets the ammonition coordinates
        userpos = usercoords() #gets the enemy coordinates
        if int(atta3pos[3]) > 650: #if the attack3 surpass the canvas lower edge, the ammo gets destroyed
            time.sleep(0.01)
            gamecanvas.delete(atta3) #deletes the atta3
        elif (int(atta3pos[0]) in range(int(userpos[0]), int(userpos[2])) or int(atta3pos[2]) in range(int(userpos[0]), int(userpos[2])))  and   (int(atta3pos[1]) in range(int(userpos[1]), int(userpos[3])) or int(atta3pos[3]) in range(int(userpos[1]), int(userpos[3]))): #if the attack 1 hits the user, gets deleted
            time.sleep(0.01)
            gamecanvas.delete(atta3) #deletes the atta3
            userlife -= 3
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
        else:
            time.sleep(0.01)
            gamecanvas.move(atta3, 0, 10) #moves the attack 3 towards the user
            return move_attack3() #recursive call to move the attack3 continuously
    
    """Enemy spaceship movement function and timer function thread_________________________________________________________________________"""
    def startthread():
        e3shooting = Thread(target = shoot_enemy3, args = ()) #thread that calls the function that produces the shooting
        e3shooting.start() #starts the shooting thread
        e3movement = Thread(target = move_enemy3f, args = ()) #thread that calls the function that produces the movement
        e3movement.start() #starts the movement thread
        timer = Thread(target = starttimer, args = ()) #thread that calls the function of the timer
        timer.start() #starts the timer thread
    
    """Timer Functions_______________________________________________________________________________________________________________"""
    def starttimer():
        while True:
            time.sleep(1)
            global second1
            second1 += 1
            countdown.config(text = "Timer: " + str(second1)) #set the actual time to the tag that show them

    """Enemy spaceship movement and functions_____________________________________________________________________________________________"""
    """FORWARD"""
    def move_enemy3f():
        global second1
        global enemy3life
        global userlife
        enemy3pos = enemy3coords() #gets the enemy coordinates
        userpos = usercoords() #gets the user coordinates
        if enemy3pos[2] > 430: #if the object reaches the right edge, it moves backward
            time.sleep(0.1)
            gamecanvas.move(enemy3, 0, 0) #stops the object and...
            return move_enemy3b() #calls the funtion that makes the backward movement
        elif (int(userpos[0]) in range(int(enemy3pos[0]), int(enemy3pos[2])) or int(userpos[2]) in range(int(enemy3pos[0]), int(enemy3pos[2])))  and   (int(userpos[1]) in range(int(enemy3pos[1]), int(enemy3pos[3])) or int(userpos[3]) in range(int(enemy3pos[1]), int(enemy3pos[3]))): #if the enemy hits the user
            time.sleep(0.1)
            gamecanvas.move(user, 0, 300) #moves the user out of the enemy range to prevent the extra life loosing
            userlife -= 10 #subtracts 10 life points from the userlife variable
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
            else:
                return move_enemy3f() #calls the function in a recursive way
        elif second1 % 10 == 0 and second1 != 0:
            time.sleep(0.1)
            gamecanvas.move(enemy3, 0, 0) #stops the object and...
            return move_enemy3d() #calls the funtion that makes the down movement
        else:
            time.sleep(0.1)
            gamecanvas.move(enemy3, 20, 0) #moves the object 20 by 20 spaces forward until the spaceship reach the right edge
            return move_enemy3f() #calls the function in a recursive way

    """BACKWARD"""
    def move_enemy3b():
        global second1
        global enemy3life
        global userlife
        enemy3pos = enemy3coords() #gets the enemy coordinates
        userpos = usercoords() #gets the user coordinates
        if enemy3pos[0] < 30: #if the object reaches the left edge, it moves forward
            time.sleep(0.1)
            gamecanvas.move(enemy3, 0, 0) #stops the object and...
            return move_enemy3f() #calls the funtion that makes the forward movement
        elif (int(userpos[0]) in range(int(enemy3pos[0]), int(enemy3pos[2])) or int(userpos[2]) in range(int(enemy3pos[0]), int(enemy3pos[2])))  and   (int(userpos[1]) in range(int(enemy3pos[1]), int(enemy3pos[3])) or int(userpos[3]) in range(int(enemy3pos[1]), int(enemy3pos[3]))): #if the enemy hits the user
            time.sleep(0.1)
            gamecanvas.move(user, 0, 300) #moves the user out of the enemy range to prevent the extra life loosing
            userlife -= 10 #subtracts 10 life points from the userlife variable
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
            else:
                return move_enemy3b() #calls the function in a recursive way
        elif second1 % 10 == 0 and second1 != 0:
            time.sleep(0.1)
            gamecanvas.move(enemy3, 0, 0) #stops the object and...
            return move_enemy3d() #calls the funtion that makes the down movement
        else:
            time.sleep(0.1)
            gamecanvas.move(enemy3, -20, 0) #moves the object 20 by 20 spaces backward until the spaceship reach the left edge
            return move_enemy3b() #calls the function in a recursive way

    """DOWNWARD"""
    def move_enemy3d():
        global second1
        global enemy3life
        global userlife
        enemy3pos = enemy3coords() #gets the enemy coordinates
        userpos = usercoords() #gets the user coordinates
        if enemy3pos[3] > 620: #if the object reaches the lower edge, it moves upward
            time.sleep(0.1)
            gamecanvas.move(enemy3, 0, 0) #stops the object and...
            return move_enemy3u() #calls the funtion that makes the upward movement
        elif (int(userpos[0]) in range(int(enemy3pos[0]), int(enemy3pos[2])) or int(userpos[2]) in range(int(enemy3pos[0]), int(enemy3pos[2])))  and   (int(userpos[1]) in range(int(enemy3pos[1]), int(enemy3pos[3])) or int(userpos[3]) in range(int(enemy3pos[1]), int(enemy3pos[3]))): #if the enemy hits the user
            time.sleep(0.1)
            gamecanvas.move(user, -100, 100) #moves the user out of the enemy range to prevent the extra life loosing
            gamecanvas.move(enemy3, 0, -20)  #moves the object 20 by 20 spaces upward until the spaceship reach the upper edge
            userlife -= 10 #subtracts 10 life points from the userlife variable
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losing title
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
            else:
                return move_enemy3u() #calls the function in a recursive way
        else:
            time.sleep(0.1)
            gamecanvas.move(enemy3, 0, 30) #moves the object 30 by 30 spaces downward until the spaceship reach the lower edge
            return move_enemy3d() #calls the function in a recursive way

    """UPWARD"""
    def move_enemy3u():
        global second1
        global enemy3life
        global userlife
        enemy3pos = enemy3coords() #gets the enemy coordinates
        userpos = usercoords() #gets the user coordinates
        if enemy3pos[1] < 30: #if the object reaches the upper edge, it moves forward or backward depending of its position
            time.sleep(0.1)
            gamecanvas.move(enemy3, 0, 0) #stops the object and...
            prob = random.randint(0,1)
            randpos = random.randint(15, 350)
            if prob == 1:
                time.sleep(0.1)
                gamecanvas.move(enemy3, (randpos - int(enemy3pos[0])), 0) #moves the enemy in a random way along the x axis
                return move_enemy3d() #calls the funtion that makes the downward movement
            else:
                time.sleep(0.1)
                gamecanvas.move(enemy3, 15 - int(enemy3pos[0]), 0) #moves the enemy to its initial position
                return move_enemy3f() #calls the funtion that makes the downward movement
        elif (int(userpos[0]) in range(int(enemy3pos[0]), int(enemy3pos[2])) or int(userpos[2]) in range(int(enemy3pos[0]), int(enemy3pos[2])))  and   (int(userpos[1]) in range(int(enemy3pos[1]), int(enemy3pos[3])) or int(userpos[3]) in range(int(enemy3pos[1]), int(enemy3pos[3]))): #if the enemy hits the user
            time.sleep(0.1)
            gamecanvas.move(user, 100, -100) #moves the user out of the enemy range to prevent the extra life loosing
            gamecanvas.move(enemy3, 0, -20) #moves the object 20 by 20 spaces upward until the spaceship reach the upper edge
            userlife -= 10 #subtracts 10 life points from the userlife variable
            ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
            ulifeth.start() #starts the user's life modification thread
            if userlife <= 0:
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('explosionsound.wav') #loads the explosion sound
                mixer.music.play() #plays the sound
                top5th = Thread(target = top5set, args = ()) #thread that calls the function of the top5 modification
                top5th.start() #starts the top5 modification thread
                losingtitle = tk.Label(game, font = ("Comic Sans MS", 16), text = "YOU LOST...", fg = "ghostwhite", bg = "midnightblue")
                losingtitle.place(x = 215, y = 8) #Label with the losingtitle
                gamecanvas.delete(user) #deletes the user
                time.sleep(2)
                loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                loseth.start() #start the thread
            else:
                return move_enemy3u() #calls the function in a recursive way
        else:
            time.sleep(0.1)
            gamecanvas.move(enemy3, 0, -20) #moves the object 20 by 20 spaces upward until the spaceship reach the upper edge
            return move_enemy3u() #calls the function in a recursive way

    """Enemy shooting functions"""
    def shoot_enemy3():
        while True:
            global atta1
            global atta2
            global atta3
            enemy3pos = enemy3coords() #gets the enemy coordinates
            time.sleep(1.5)
            if enemy3pos[3] <= 90:
                enemy3pos = enemy3coords() #Receives the tuple of the coordinates of the enemy2 space ship

                atta1 = gamecanvas.create_oval(5, 5, 15, 15, fill = "darkorange") #creates the attack that the enemy spaceship shoot
                gamecanvas.move(atta1, enemy3pos[0] + 25, enemy3pos[1] + 70) #place the attack in enemy's spaceship
            
                atta2 = gamecanvas.create_oval(5, 5, 15, 15, fill = "darkorange") #creates the attack that the enemy spaceship shoot
                gamecanvas.move(atta2, enemy3pos[0] + 25, enemy3pos[1] + 110) #place the attack in enemy's spaceship
            
                atta3 = gamecanvas.create_oval(5, 5, 15, 15, fill = "darkorange") #creates the attack that the enemy spaceship shoot
                gamecanvas.move(atta3, enemy3pos[0] + 25, enemy3pos[1] + 150) #place the attack in enemy's spaceship
            
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('lasersound.wav') #loads the laser sound
                mixer.music.play() #plays the sound
                atta1move = Thread(target = move_attack1, args = ()) #thread that calls the function that produces the movement
                atta1move.start() #start the thread

                pygame.mixer.init() #initialize the mixer
                mixer.music.load('lasersound.wav') #loads the laser sound
                mixer.music.play() #plays the sound
                atta2move = Thread(target = move_attack2, args = ()) #thread that calls the function that produces the movement
                atta2move.start() #start the thread

                pygame.mixer.init() #initialize the mixer
                mixer.music.load('lasersound.wav') #loads the laser sound
                mixer.music.play() #plays the sound
                atta3move = Thread(target = move_attack3, args = ()) #thread that calls the function that produces the movement
                atta3move.start() #start the thread            
        
    """Position of the spaceships_______________________________________________________________________________________________________________"""
    def usercoords():
        return gamecanvas.coords(user) #canvas function that receives the coordinates of the user's spaceship

    def enemy3coords():
        return gamecanvas.coords(enemy3) #canvas function that receives the coordinates of the enemy spaceship

    """Keys functions________________________________________________________________________________________________________________________"""
        #x and y are the number of positions the user's spaceship is going to move from its original position
    def left(event):
        x = -20 
        y = 0
        gamecanvas.move(user, x, y) #moves the ship -20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def right(event):
        x = 20
        y = 0
        gamecanvas.move(user, x, y) #moves the ship 20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def up(event):
        x = 0
        y = -20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and -20 spaces in the y direction, from its original position

    def down(event):
        x = 0
        y = 20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and 20 spaces in the y direction, from its original position

    def shoot(event):
        userposition = usercoords() #Receives the tuple of the coordinates of the user space ship
        global ammo
        ammo = gamecanvas.create_oval(5, 5, 15, 15, fill = "gold") #creates the ammo that the spaceship shoot
        gamecanvas.move(ammo, userposition[0] + 15, userposition[1] - 15) #place the ammo in spaceship
        pygame.mixer.init() #initialize the mixer
        mixer.music.load('lasersound.wav') #loads the laser sound
        mixer.music.play() #plays the sound
        ammomove = Thread(target = move_ammo, args = ()) #thread that calls the function that produces the movement
        ammomove.start() #start the thread
                        
    """Keys Binding______________________________________________________________________________________________________________________"""

    game.bind("<Left>", left) #binds the left key to the left movement function
    game.bind("<Right>", right) #binds the right key to the left movement function
    game.bind("<Up>", up) #binds the up key to the left movement function
    game.bind("<Down>", down) #binds the down key to the left movement function
    game.bind("<space>", shoot) #binds the space bar to the shooting function
    
    """Buttons of the game window___________________________________________________________________________________________________________"""
    startgame = tk.Button(game, text = "Start", font = ("Comic Sans MS", 10), bg = "ghostwhite", fg = "midnightblue", command = startthread)
    startgame.place(x = 50, y = 10) #start the game
    
    game_mainnmenu = tk.Button(game, text = "Main Menu", font = ("Comic Sans MS", 10), bg = "ghostwhite", fg = "midnightblue", command = destroygame)
    game_mainnmenu.place(x = 110, y = 10) #return to the main menu, losing the user's record
    
    """Labels of the game window___________________________________________________________________________________________________________"""    
    n = name.get() #Gets the user's name
    username = tk.Label(game, text = "User: " + n, font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue")
    username.place(x = 510, y = 100) #Label where the user's name is written

    countdown = tk.Label(game, text = "Timer: " + str(second1), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the time is written
    countdown.place(x = 510, y = 140) #place the timer label

    scoreindicator = tk.Label(game, text = "Score: " + str(score3), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the score is written
    scoreindicator.place(x = 510, y = 180) #place the score label
    
    ulifeindicator = tk.Label(game, text = "Life: " + str(userlife), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the user's life is written
    ulifeindicator.place(x = 510, y = 220) #place the user's life label
    
    e3lifeindicator = tk.Label(game, text = "Enemy: " + str(enemy3life), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the enemy's life is written
    e3lifeindicator.place(x = 510, y = 260) #place the enemy's life label
    
    """Canvas configuration_________________________________________________________________________________________________________________"""
    gamecanvas.place(x = 50, y = 50) #place the canvas widget  
    game.mainloop()

"""Main Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""
mw = tk.Tk() #Creates the main window
name = StringVar() #Takes the name of the user for the top 5 list

mw.title("Operation Moon Light") #Title of the principal window
mw.geometry("500x300") #Size of the principal window
mw.configure(background = "midnightblue") #Modifies the window background color

"""Entries___________________________________________________________________________________________________________"""
user_name = tk.Entry(mw, textvariable = name, font = ("Comic Sans MS", 14), width = 10) .place(x=185, y=85) #Entry widget for the user to write his/her name

"""Labels___________________________________________________________________________________________________________"""
videogame_name = tk.Label(mw, font = ("Comic Sans MS", 22), text = "Operation Moon Light", fg = "ghostwhite", bg = "midnightblue")
videogame_name.place(x = 105, y = 5) #Label with the title of the game
usernameinstruction = tk.Label(mw, font = ("Comic Sans MS", 12), text = "Enter your name to save your results", fg = "ghostwhite", bg = "midnightblue"). place(x = 115, y = 125) #Label with the title of the game
space = PhotoImage(file = 'background.gif')
space = space.subsample(1)
space = space.zoom(2)

"""Buttons___________________________________________________________________________________________________________"""
level1 = tk.Button(mw, text = "Level 1", font = ("Comic Sans MS", 10), bg = "ghostwhite", fg = "midnightblue", command = game1) .place(x=135, y=170) #Opens the level 1 window
level2 = tk.Button(mw, text = "Level 2", font = ("Comic Sans MS", 10), bg = "ghostwhite", fg = "midnightblue", command = game2) .place(x=215, y=170) #Opens the level 2 window
level3 = tk.Button(mw, text = "Level 3", font = ("Comic Sans MS", 10), bg = "ghostwhite", fg = "midnightblue", command = game3) .place(x=295, y=170) #Opens the level 3 window
aboutb = tk.Button(mw, text = "About the Creator", font = ("Comic Sans MS", 10), bg = "ghostwhite", fg = "midnightblue", command = openaboutw) .place(x=120, y=265) #Opens the creator information window
topplayersb = tk.Button(mw, text = "Best 5 Players", font = ("Comic Sans MS", 10), bg = "ghostwhite", fg = "midnightblue", command = opentop) .place(x=260, y=265) #Opens the top 5 player window

second1 = 0
userlife = 50
enemy1life = 30
enemy2life = 40
enemy3life = 50
score = 0
score2 = 0
score3 = 0

mw.mainloop()
