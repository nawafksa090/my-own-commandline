import os
import subprocess
import sqlite3, hashlib
from tkinter import *
from tkinter import simpledialog
from functools import partial
import random
def test():
            import turtle as n
            n.speed(20)
            def forward():
                a = int(input("please enter the number of steps you want to move: "))
                n.forward(a)
                test()

            def right():
                a = int(input("please enter the number of steps you want to move to the right: "))
                n.right(a)
                test()
            


            def left():
                a = int(input("please enter the number of steps you want to move to the left: "))
                n.left(a)
                test()


            def backwards():
                a = int(input("please enter the number of steps you want to move backwards: "))
                n.backward(a)
                test()
            def circle():
                a = input("please enter a number (type half circle if you want to do a half circle): ")
                if a == "half circle":
                    b = int(input("please enter the first number"))
                    d = int(input("please enter the second number"))
                    n.circle(b,d)
                elif a >= 1:
                    n.circle(a)
                else:
                    print("please make sure you typed it right")
                test()
            ask = input("please enter a command: ")
            if ask == "forward":
                forward()
            elif ask == "help":
                print("heres all the commands: 1.forward 2.right 3.left 4.backwards 5.penup 6.pendown 7.circle 8.color 9.help 10.exit.")
                test()
            elif ask == "right":
                right()
            elif ask == "left":
                left()
            elif ask == "backwards":
                backwards()
            elif ask == "penup":
                n.penup()
                print("pen is up")
                test()
            elif ask == "circle":
                circle()
            elif ask == "pendown":
                n.pendown()
                print("pen is down")
                test()
            elif ask == "color":
                color = input("please choose a color: ")
                n.color(color)
                print("color " + color + " has been chosen if its still black then the color doesnt exist")
                test()
            elif ask == "exit":
                print("you exited.")
                n.bye()
                commands()
            else:
                print("sorry but the command you typed does not exist please try again")
                test()
def start1():
    print("Welcome to turtle, this will draw anything you want, type exit to leave.")
    print("Check if an app was opened if not please try again later")
    print("if you close the window make sure you type exit and you cant run it back unless you restart the program")
    print("Please enter help for info about the commands!")
    test()
def pygame():
    try:
        import pygame
        import os
        pygame.font.init()
        pygame.mixer.init()
        print("\tthis game is 2 player only")
        print("\tmade by nawaf and youtube :')")
        print("\tcontrols:" + "\n\tL, quits the game")
        print("\tyellow(on the left): left ctrl, shoots, W, up, d, right, a, left, s, down")
        print("\tred(on the right): right ctrl, shoots, up arrow, up, down arrow, down, left arrow, left, right arrow, right")
        print("\tthe max bullets you have is 3 if you hit the other player or if your bullets miss you will get them back")
        print("\tpress n to stop background sounds") 
        print("\tcheck if an app opened if not please try again")
        print("\tremember the left one is the yellow and the right one is the red")
        #this game is 2 player only
        #controls: L, quits the game
        #yellow(on the left): left ctrl, shoots, W, up, d, right, a, left, s, down
        #red(on the right): right ctrl, shoots, up arrow, up, down arrow, down, left arrow, left, right arrow, right
        #the max bullets you have is 3 if you hit the other player or if your bullets miss you will get them back

        WIDTH, HEIGHT = 900,500
        WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        ICON = pygame.image.load('Assets/Icon.png')
        pygame.display.set_caption("Space shooter (2PLAYERS ONLY)")

        WHITE = (255,255,255)
        BLACK = (0,0,0)
        RED = (255,0,0)
        YELLOW = (255,255,0)

        BORDER = pygame.Rect(WIDTH//2 - 30, 0, 10,HEIGHT)

        BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
        BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')
        WINNER_SOUND = pygame.mixer.Sound('Assets/Winner+2.wav')
        BACK_GROUND_SOUND = pygame.mixer.Sound('Assets/Space+Sound.wav')

        HEALTH_FONT = pygame.font.SysFont('comicsans', 30)
        WINNER_FONT = pygame.font.SysFont('comicsans', 40)
        BACK_GROUND_SOUND_FONT = pygame.font.SysFont('comicsans', 20)

        FPS = 60
        VEL = 5
        MAX_BULLETS = 3
        BULLET_VEL = 7

        SPACE_WIDTH, SPACE_HEIGHT =   55,40  

        YELLOW_HIT = pygame.USEREVENT + 1
        RED_HIT = pygame.USEREVENT + 2

        #yellow space ship
        YELLOW_S_IM = pygame.image.load(
            os.path.join('Assets', 'spaceship_yellow.png'))
        YELLOW_S = pygame.transform.rotate(pygame.transform.scale(
            YELLOW_S_IM, (SPACE_WIDTH,SPACE_HEIGHT)), 90)
        #red space ship
        RED_S_IM = pygame.image.load(
            os.path.join('Assets', 'spaceship_red.png'))
        RED_S = pygame.transform.rotate(pygame.transform.scale(
            RED_S_IM, (SPACE_WIDTH,SPACE_HEIGHT)),-90)

        SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
        #draws in the window
        def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, on_or_off_text):
            WIN.blit(SPACE, (0,0))
            pygame.display.set_icon(ICON)
            pygame.draw.rect(WIN, BLACK, BORDER)

            back_ground_text = BACK_GROUND_SOUND_FONT.render("Music is "+ on_or_off_text, 1, WHITE)
            red_health_text = HEALTH_FONT.render("Red's Health: " + str(red_health), 1, WHITE) 
            yellow_health_text = HEALTH_FONT.render("Yellow's Health: " + str(yellow_health), 1, WHITE)

            WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
            WIN.blit(yellow_health_text, (10,10))
            WIN.blit(back_ground_text, (WIDTH/2 - back_ground_text.get_width() + 15,15))

            WIN.blit(YELLOW_S, (yellow.x, yellow.y))
        
            WIN.blit(RED_S, (red.x, red.y))

            for bullet in red_bullets:
                pygame.draw.rect(WIN, RED, bullet)
            
            for bullet in yellow_bullets:
                pygame.draw.rect(WIN, YELLOW, bullet)

            pygame.display.update()
        #yellow keys
        def yellow_keys(keys_pressed, yellow):
            if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
                yellow.x -= VEL
            if keys_pressed[pygame.K_d] and yellow.x + VEL  + yellow.width < BORDER.x: #right
                yellow.x += VEL
            if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
                yellow.y -= VEL
            if keys_pressed[pygame.K_s] and yellow.y + VEL  + yellow.height < HEIGHT - 15: #down
                yellow.y += VEL
        #red keys
        def red_keys(keys_pressed, red):
            if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
                red.x -= VEL
            if keys_pressed[pygame.K_RIGHT] and red.x + VEL  + red.width < WIDTH: #right
                red.x += VEL
            if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #up
                red.y -= VEL
            if keys_pressed[pygame.K_DOWN] and red.y + VEL  + red.height < HEIGHT - 15: #down
                red.y += VEL
        def handle_bullets(yellow_bullets, red_bullets, yellow, red):
            for bullet in yellow_bullets:
                bullet.x += BULLET_VEL
                if red.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(RED_HIT))
                    yellow_bullets.remove(bullet)
                elif bullet.x > WIDTH:
                    yellow_bullets.remove(bullet)
            for bullet in red_bullets:
                bullet.x -= BULLET_VEL
                if yellow.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(YELLOW_HIT))
                    red_bullets.remove(bullet)
                elif bullet.x < 0:
                    red_bullets.remove(bullet)
        def draw_winner(text):
            draw_text = WINNER_FONT.render(text + ", The game will restart in 5 seconds", 1, WHITE)
            WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
            WINNER_SOUND.play()
            pygame.display.update()
            pygame.time.delay(5000)
        def main():
            too_many_ms = True
            too_many_ns = False
            on_or_off_text = "On"
            BACK_GROUND_SOUND.play()
            red = pygame.Rect(700,300, SPACE_WIDTH, SPACE_HEIGHT)
            yellow = pygame.Rect(100,300, SPACE_WIDTH, SPACE_HEIGHT)

            red_bullets = []
            yellow_bullets = []

            red_health = 10
            yellow_health = 10

            clock = pygame.time.Clock()
            run = True
            while run: 
                keys_pressed2 = pygame.key.get_pressed()
                if keys_pressed2[pygame.K_m] and too_many_ms == False:
                    BACK_GROUND_SOUND.play()
                    on_or_off_text = "On"
                    too_many_ms = True
                    too_many_ns = False
                    print("\tPress N to stop back ground sound")
                if keys_pressed2[pygame.K_n] and too_many_ns == False:
                    BACK_GROUND_SOUND.stop()
                    on_or_off_text = "Off"
                    too_many_ms = False
                    too_many_ns = True
                    print("\tPress M to start back ground sound")
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LSHIFT and len(yellow_bullets) < MAX_BULLETS:
                            bullet = pygame.Rect(
                                yellow.x + yellow.width - 5, yellow.y + yellow.height//2 - 2, 10, 5)
                            yellow_bullets.append(bullet)
                            BACK_GROUND_SOUND.set_volume(0.0)
                            BULLET_FIRE_SOUND.play()
                            BACK_GROUND_SOUND.set_volume(100.0)

                        if event.key == pygame.K_RSHIFT and len(red_bullets) < MAX_BULLETS:
                            bullet = pygame.Rect(
                                red.x, red.y + red.height//2 - 2, 10, 5)
                            red_bullets.append(bullet)
                            BACK_GROUND_SOUND.set_volume(0.0)
                            BULLET_FIRE_SOUND.play()
                            BACK_GROUND_SOUND.set_volume(100.0)
                    if event.type == RED_HIT:
                        red_health -= 1
                        BACK_GROUND_SOUND.set_volume(0.0)
                        BULLET_HIT_SOUND.play()
                        BACK_GROUND_SOUND.set_volume(100.0)
                    if event.type == YELLOW_HIT:
                        yellow_health -= 1
                        BACK_GROUND_SOUND.set_volume(0.0)
                        BULLET_HIT_SOUND.play()
                        BACK_GROUND_SOUND.set_volume(100.0)
                winner_text = ""
                if red_health <=0:
                    winner_text = "Yellow wins!"
                if yellow_health <=0:
                    winner_text = "Reds wins!"
                if winner_text !="":
                    draw_winner(winner_text)
                    break
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_l]: #quits
                    run = False
                    pygame.quit()           
                yellow_keys(keys_pressed, yellow)
                red_keys(keys_pressed,red)
                handle_bullets(yellow_bullets, red_bullets, yellow, red)
                draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, on_or_off_text)

            
            main()

        if __name__ == "__main__":
            main()
    except pygame.error:
        commands()

def rps():
    a = random.randint(1,3)


    ask = int(input("\tenter a number (1. rock 2. paper 3.scissors): "))
    b = str(a)
    if ask == "exit":
        exit()
    if a == 1:
        if ask == 1:
            print("\ttie!")
            print("\t the robot chose '" + b + "'")
            ask2 = input("\tdo you want to play again: ")
            if ask2 == "yes":
                rps()
            else:
                commands()
        elif ask ==2:
            print("\tyou won!")
            print("\t the robot chose '" + b + "'")
            ask2 = input("\tdo you want to play again: ")
            if ask2 == "yes":
                rps()
            else:
                commands()
        else:
            print("\tyou lost!")
            print("\t the robot chose '" + b + "'")
            ask2 = input("\tdo you want to play again: ")
            if ask2 == "yes":
                rps()
            else:
                commands()
    elif a == 3:
        if ask == 3:
            print("\ttie!")
            print("\tthe robot chose '" + b + "'")
            ask2 = input("\tdo you want to play again: ")
            if ask2 == "yes":
                rps()
            else:
                commands()
        elif ask == 1:
            print("\tyou won!")
            print("\tthe robot chose '" + b + "'")
            ask2 = input("\tdo you want to play again: ")
            if ask2 == "yes":
                rps()
            else:
                commands()
        else:
            print("\tyou lost!")
            print("\tthe robot chose '" + b + "'")
            ask2 = input("\tdo you want to play again: ")
            if ask2 == "yes":
                rps()
            else:
                commands()
    elif a == 2:
        if ask == 2:
            print("\ttie!")
            print("\tthe robot chose '" + b + "'")
            ask2 = input("\tdo you want to play again: ")
            if ask2 == "yes":
                rps()
            else:
                commands()
        elif ask ==3:
            print("\tyou won!")
            print("\tthe robot chose '" + b + "'")
            ask2 = input("\tdo you want to play again: ")
            if ask2 == "yes":
                rps()
            else:
                commands()
        else:
            print("\tyou lost!")
            print("\tthe robot chose '" + b + "'")
            ask2 = input("\tdo you want to play again: ")
            if ask2 == "yes":
                rps()
            else:
                commands()

def odd_or_even():
    a = random.randint(1,1000)
    b = str(a)
    if a % 2 == 0:
        even = True
        odd = False
    else:
        odd = True
        even = False
    user = input("\tGuess if '"+ b + "' is even or odd: ")
    if user == "even":
        if even == True:
            print("\tcorrect!")
        else:
            print("\tsorry but your wrong!")
    elif user == "odd":
        if odd == True:
            print("\tcorrect!")
        else:
            print("\tsorry but your wrong!")
    else:
        print("\tplease type even or odd next time.")
    ask = input("\tdo you want to try again: ")
    if ask == "yes":
        odd_or_even()
    else:
        commands()


def window():



    with sqlite3.connect("password_vault.db") as db:
        cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS masterpassword(
    id INTEGER PRIMARY KEY,
    password TEXT NOT NULL);
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vault(
    id INTEGER PRIMARY KEY,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    );
    """)


    def popUp(text):
        answer = simpledialog.askstring("input string", text)

        return answer

    wd = Tk()

    wd.title("Password Vault")

    def hashPassword(input):
        hash = hashlib.md5(input)
        hash = hash.hexdigest()

        return hash

    def firstScreen():
        wd.geometry("250x150")

        lbl = Label(wd, text="Create Master Password")
        lbl.config(anchor=CENTER)
        lbl.pack()

        txt = Entry(wd, width=20, show="*")
        txt.pack()
        txt.focus()

        lbl1 = Label(wd, text="Re-enter password")
        lbl1.pack()

        txt1 = Entry(wd, width=20, show="*")
        txt1.pack()
        txt1.focus()

        lbl2 = Label(wd)
        lbl2.pack()

        def savePassword():
            if txt.get() == txt1.get():
                hashedPassword = hashPassword(txt.get().encode('utf-8'))

                insert_password = """INSERT INTO masterpassword(password) 
                VALUES(?)"""
                cursor.execute(insert_password, [(hashedPassword)])
                db.commit()

                passwordVault()
            else:
                lbl2.config(text="Passwords do no match")

        btn = Button(wd, text="Save", command=savePassword)
        btn.pack(pady=10)
    def loginScreen():
        wd.geometry("250x100")

        lbl = Label(wd, text="Enter Master Password")
        lbl.config(anchor=CENTER)
        lbl.pack()

        txt = Entry(wd, width=20, show="*")
        txt.pack()
        txt.focus()

        lbl1 = Label(wd)
        lbl1.pack()

        def getMasterPassword():
            checkHashedPassword = hashPassword(txt.get().encode('utf-8'))
            cursor.execute(" SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(checkHashedPassword)])
            return cursor.fetchall()

        def checkPassword():
            match = getMasterPassword()

            if match:
                passwordVault()
            else:
                txt.delete(0, "end")
                lbl1.config(text="Wrong Password")

        btn = Button(wd, text="Submit", command=checkPassword)
        btn.pack(pady=10)

    def passwordVault():
        for widget in wd.winfo_children():
            widget.destroy()

        def addEntry():
            text1 = "Website/App"
            text2 = "Username/Email"
            text3 = "Password"

            website = popUp(text1)
            username = popUp(text2)
            password = popUp(text3)

            insert_fields = """INSERT INTO vault(website,username,password)
            VALUES(?, ?, ?)"""

            cursor.execute(insert_fields, (website, username, password))
            db.commit()

            passwordVault()

        def removeEntry(input):
            cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
            db.commit()

            passwordVault()

        wd.geometry("750x350")

        lbl = Label(wd, text="Password vault")
        lbl.grid(column=1)

        btn = Button(wd, text="+", command=addEntry)
        btn.grid(column=1, pady=10)

        lbl = Label(wd, text="Website/App")
        lbl.grid(row=2, column=0, padx=80)
        lbl = Label(wd, text="Username/Email")
        lbl.grid(row=2, column=1, padx=80)
        lbl = Label(wd, text="Password")
        lbl.grid(row=2, column=2, padx=80)

        cursor.execute(("SELECT * FROM vault"))
        if(cursor.fetchall() != None):
            i = 0
            while True:
                cursor.execute(("SELECT * FROM vault"))
                array = cursor.fetchall()

                lbl1 = Label(wd, text=(array[i][1]), font=("Helvetica", 12))
                lbl1.grid(column=0, row=i+3)
                lbl1 = Label(wd, text=(array[i][2]), font=("Helvetica", 12))
                lbl1.grid(column=1, row=i+3)
                lbl1 = Label(wd, text=(array[i][3]), font=("Helvetica", 12))
                lbl1.grid(column=2, row=i+3)

                btn = Button(wd, text="-", command=partial(removeEntry, array[i][0]))
                btn.grid(column=3, row=i+3, pady=10)

                i = i+1

                cursor.execute("SELECT * FROM vault")
                if (len(cursor.fetchall()) <= i):
                    break
    cursor.execute(" SELECT * FROM masterpassword")
    if cursor.fetchall():
        loginScreen()
    else:
        firstScreen()
    wd.mainloop()
    print("\tdone")
    commands()


def main():
    try:
        host = input("\tEnter website: ")
        packet = 4
        print("\tPlease wait.. we are trying to ping the website (press ctrl + c to stop)")
        ping = subprocess. getoutput(f"ping -w {packet} {host}")
        print(ping)
        commands()
    except KeyboardInterrupt:
        print("\tStopped pinging!")
        commands()
def main2():
    try:
        host = input("\tEnter website: ")
        packet = input("\tEnter packets: ")
        print("\tPlease wait.. we are trying to ping the website (press ctrl + c to stop)")
        ping = subprocess. getoutput(f"ping -n {packet} {host}")
        print(ping)
        commands()
    except KeyboardInterrupt:
        print("\tStopped pinging!")
        commands()


def play():
    print("\t1. math, 2. random number guessing, 3. even or odd, 4.rock paper scissors, 5.space shooter(2PLAYERS), 6.drawing, 0.exit")
    
    choose = input("\tplease choose one of the games above ^: ")
    if choose.isnumeric():
        if choose == "1":
            num1 = float(input("\tEnter first number: "))
            op = input("\tEnter operator: ")
            num2 = float(input("\tEnter second number: "))

            if op == "+":
                print("\t", num1 + num2)
            elif op == "-":
                print("\t",num1 - num2)
            elif op == "/":
                print("\t",num1 / num2)
            elif op == "*":
                print("\t",num1 * num2)
            else:
                print("\tinvalid operator")
            play_again = input("\tdo you wanna play something else?: ")
            if play_again == "yes":
                play()
            else:
                commands()
        elif choose == "5":
            pygame()
        elif choose == "3":
            odd_or_even()
        elif choose == "4":
            rps()
        elif choose == "6":
            start1()
        elif choose == "2":
                def again():
                    import random
                    from unittest import result
                    def again1():
                        try:
                            if diff == 1:
                                b = int(input("\tGuess a number between 1, 10(0 to exit, -1 to change the difficulty): "))
                                a = random.randint(1, 10)
                            elif diff == 2:
                                b=int(input("\tGuess a number between 1, 50 (0 to exit, -1 to change the difficulty): "))
                                a = random.randint(1, 50)
                            elif diff == 3:
                                b=int(input("\tGuess a number between 1, 100(0 to exit, -1 to change the difficulty): "))
                                a= random.randint(1, 100)
                            elif diff == 0:
                                commands()
                            else:
                                pass
                            if a == b:
                                print("\tYou won!")
                                again1()
                            elif b == 0:
                                commands()
                            elif b == -1:
                                again()
                            else:
                                print("\tyou lost!")
                                print("\tthe number was '"+ str(a) +"'")
                                again1()
                        except ValueError:
                            print("\tPlease enter a number")
                            again()
                    print("\t1.easy (1-10), 2.medium (1-50),  3. hard (1-100), 0. exit")
                    try:
                        diff = int(input("\tchoose a difficulty shown above: "))
                        if diff == 1:
                            a = random.randint(1, 10)
                            again1()
                        elif diff == 2:
                            a = random.randint(1, 50)
                            again1()
                        elif diff == 3:
                            a= random.randint(1, 100)
                            again1()
                        elif diff == 0:
                            commands()
                        else:
                            print("\tPlease enter a difficulty")
                            again()
                    except ValueError:
                        print("\tPlease enter a number")
                        again()
                again()


        elif choose == "0":
            commands()
        elif choose == "000":
            print("\ttheres 6 games, 4 of them are actually games and the others are a math thingy and drawing stuff")
            play()
        else:
            print("\terror no number chosen please choose a number next time.")
            commands()
    else:
        print("\tplease enter a number, you entered '" + choose + "'")
        play()

print("\tWelcome to the best commands (this is still new and is still in beta).")
print("\tmade by nawaf(version 1.3.0)")
print("\n\ttype help or /? to see all of the commands")

def commands():
    user = input("\tEnter command: ")
    if user == "help" or  user == "/?":
        print("\thelp or /? witch shows all the commands and what it does")
        print("\tping, pings any website you type in")
        print("\tbping, does the same as ping but you can ping any packets you want (recommended for people that know what packets are)")
        print("\texit, exits the cmd")
        print("\tplay, start playing")
        print("\tprint, to print anything you want")
        print("\tabout,tells you who made the program")
        print("\tstart, starts any app you put.")
        print("\tpython, starts the program python (you need to download it)")
        print("\tnode, starts node (you need to have it downloaded)")
        print("\tthats it for now..")
        commands()
    elif user == "ping":
        main()
    elif user == "print":
        usr = input("\tplease enter the word you want to print: ")
        print("\t"+usr)
        print("\tdone")
        commands()
    elif user == "bping":
        main2()
    elif user == "exit":
        exit()
    elif user == "play":
        play()
    elif user == "commands":
        print("\theres all the commands i know.. node,python,start,window,commands,play,exit,ping,bping,print,about,help or /?, version. and thats it, if we add any more commands we will put it here")
        commands()
    elif user == "window":
        window()
    elif user == "start":
        ask1 = input("\tplease enter what you want to start (has to be a file): ")
        os.system("start "+ ask1)
        commands()
    elif user == "version":
        print("\tthis is version 1.3.0")
        commands()
    elif user == "about":
        print("\tthe programmer: nawaf")
        print("\tand also its nawaf's idea")
        print("\talso he did all the scripting (some of it from youtube)")
        commands()
    elif user == "node":
        try:
            os.system("start node")
            commands()
        except Exception:
            print("Please make sure you have node")
            commands()
    elif user == "python":
        try:
            os.system("start python")
            commands()
        except Exception:
            try:
                os.system("start python3 ")
                commands()
            except Exception:
                print("Please make sure you have python")
                commands()
    else:
        print("\tim sorry but i dont see any command with the name '"+ user + "'  you can type help for the commands")
        commands()
commands()
