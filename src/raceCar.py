import pygame
import time
import random
import os
from dotenv import load_dotenv



class Racey:

    def __init__(self):
        # Window Properties
        self.display_width      = 800
        self.display_height     = 600
        self.gameDisplay        = pygame.display.set_mode((self.display_width, self.display_height))# Set up window(Surface or Frame)
        self.clock              = pygame.time.Clock()# Set game clock
        self.carImg             = pygame.image.load('images/racecar.png')# display car Image
        self.gameIcon           = pygame.image.load('images/racecaricon.png')
        self.car_width          = 73# car width

        # Color Properties
        self.black              = (0,0,0)
        self.white              = (255,255,255)
        self.red                = (255, 0, 0)
        self.thick_red          = (200, 0, 0)
        self.block_color        = (102, 204, 0)
        self.green              = (0, 255, 0)
        
        # Sound and MUSIC pROPERTIES
        self.crash_sound     = pygame.mixer.Sound("music/crash_1.wav")
        pygame.mixer.music.load("music/jazz.mp3")

        # Global Variables
        self.paused          = False
        load_dotenv(".env")
        self.Best_score      = os.getenv("BEST_SCORE")
        
        # Set Window Title and Icon
        pygame.display.set_caption('Racey')
        pygame.display.set_icon(self.gameIcon)


    def quit_game(self):
        pygame.quit()
        quit()


    def unpause(self):

        self.paused = False
        print(self.paused)
        pygame.mixer.music.unpause()


    def car(self, x, y):
        self.gameDisplay.blit(self.carImg, (x, y))


    def text_objects(self, text, font, color):
        textSurface         = font.render(text, True, color)
        return textSurface, textSurface.get_rect()


    def message_display(self, text, font_size, color, position):
        largeText               = pygame.font.SysFont("comicsansms", font_size)
        TextSurf, TextRect      = self.text_objects(text, largeText, color) 
        TextRect.center         = position
        self.gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        #display message for 2 seconds
        

    def crash(self, score):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(self.crash_sound)
        crash   = True
        db_bx   = 100
        db_by   = 70
        db_bh   = 300
        db_bw   = 600
        db_x    = db_bx + 5
        db_y    = db_by + 5
        db_h    = db_bh - 10
        db_w    = db_bw - 10
        rec_w   = 140
        rec_h   = 70
        pa_x    = (db_x + 40)
        rec_y   = ((db_y + db_h) - 100)
        qt_x    = ((db_x + db_w) - 170)# 130 + 40
        pa_bt_x = (pa_x + (rec_w/2))
        qt_bt_x = (qt_x + (rec_w/2))
        pa_bt_y = (rec_y + (rec_h/2))
        qt_bt_y = (rec_y + (rec_h/2))

        pygame.draw.rect(self.gameDisplay, self.black, (db_bx, db_by, db_bw, db_bh))
        pygame.draw.rect(self.gameDisplay, self.white, (db_x, db_y, db_w, db_h))
        self.message_display("YOU CRASHED", 50, self.black, ((db_x + (db_w/2)), (db_y + 70)))

        if score > int(self.Best_score):
            self.Best_score = score
            with open(".env", "w") as f:
                f.write("export BEST_SCORE=" + str(self.Best_score))
            self.message_display("Best Score : " + str(score), 60, self.black, ((db_x + (db_w/2)), (db_y + (db_h/2))))
        else:
            self.message_display("Score : " + str(score), 60, self.black, ((db_x + (db_w/2)), (db_y + (db_h/2))))



        while crash:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.button("Play Again", 25, (pa_bt_x, pa_bt_y), self.white, (pa_x, rec_y, rec_w, rec_h), self.block_color, self.green, self.game_loop)

            self.button("Quit", 25, (qt_bt_x, qt_bt_y), self.white, ( qt_x, rec_y, rec_w, rec_h), self.red, self.thick_red, self.quit_game)

            pygame.display.update()
            self.clock.tick(15)


    def pause(self):
        pygame.mixer.music.pause()
        db_bx   = 100
        db_by   = 70
        db_bh   = 300
        db_bw   = 600
        db_x    = db_bx + 5
        db_y    = db_by + 5
        db_h    = db_bh - 10
        db_w    = db_bw - 10
        rec_w   = 140
        rec_h   = 70
        pa_x    = (db_x + 40)
        rec_y   = ((db_y + db_h) - 100)
        qt_x    = ((db_x + db_w) - 170)# 130 + 40
        pa_bt_x = (pa_x + (rec_w/2))
        qt_bt_x = (qt_x + (rec_w/2))
        pa_bt_y = (rec_y + (rec_h/2))
        qt_bt_y = (rec_y + (rec_h/2))
        print(self.paused)

        pygame.draw.rect(self.gameDisplay, self.black, (db_bx, db_by, db_bw, db_bh))
        pygame.draw.rect(self.gameDisplay, self.white, (db_x, db_y, db_w, db_h))
        self.message_display("PAUSED", 50, self.black, ((db_x + (db_w/2)), (db_y + 70)))

        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.button("Continue", 25, (pa_bt_x, pa_bt_y), self.white, (pa_x, rec_y, rec_w, rec_h), self.block_color, self.green, self.unpause)

            self.button("Quit", 25, (qt_bt_x, qt_bt_y), self.white, ( qt_x, rec_y, rec_w, rec_h), self.red, self.thick_red, self.quit_game)

            pygame.display.update()
            self.clock.tick(15)

            
    def things(self, thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(self.gameDisplay, color, [thingx, thingy, thingw, thingh])


    def things_dodged(self, count):
        font    = pygame.font.SysFont("comicsansms", 25)
        text    = font.render("Score: " + str(count), True, self.black)
        self.gameDisplay.blit(text, (0, 0))


    def pause_game(self):
        self.paused = True
        self.button("", 10, (800, 0), self.white, ( 740, 0, 40, 40), self.thick_red, self.red, self.pause)
        pygame.draw.line(self.gameDisplay, self.white, (750, 10), (750, 30), 8)
        pygame.draw.line(self.gameDisplay, self.white, (770, 10), (770, 30), 8)
        # pygame.display.update()


    def button(self, text, text_font, text_pos, text_color, btn_pos, btn_color_1, btn_color_2=None, action=None):
        mouse       = pygame.mouse.get_pos()
        click       = pygame.mouse.get_pressed()
        
        if (mouse[0] < (btn_pos[0] + btn_pos[2])  and  mouse[0] > btn_pos[0] and mouse[1] < (btn_pos[1] + btn_pos[3])  and  mouse[1] > btn_pos[1]):
            if btn_color_2 is not None:
                pygame.draw.rect(self.gameDisplay, btn_color_2, btn_pos)
            else:
                pygame.draw.rect(self.gameDisplay, btn_color_1, btn_pos)
            if click[0] == 1 and action is not None:
                action()
        else: 
            pygame.draw.rect(self.gameDisplay, btn_color_1, btn_pos)

        self.message_display(text, text_font, text_color, text_pos)


    def game_intro(self):
        # pygame.mixer.music.play(-1)
        intro = True
        rec_x = (self.display_width - 500)
        rec_y = (self.display_height - 200)
        rec_w = 200
        rec_h = 90
        a     = ((self.display_width - 500) + (rec_w/2))
        a2    = ((self.display_width - 500) + (180/2))
        b     = ((self.display_height - 200) + (rec_h - 63))
        c     = ((self.display_height - 200) + (rec_h/2))
        d     = ((self.display_height - 200) + (rec_h - 10))
        e     = ((self.display_width - 500) + (rec_w - 80))
        f     =  ( (c + d)/ 2)

        self.gameDisplay.fill(self.white)   
        self.message_display("A BIT RACEY", 40, self.red, ((self.display_width/2), (self.display_height - 560)))
        self.message_display("Ready to get your racey on !!", 30, self.black, ((self.display_width/2), (self.display_height - 500)))
        self.message_display("BEST SCORE :", 30, self.black, ((self.display_width/2), (self.display_height - 430)))
        self.message_display(str(self.Best_score), 90, self.red, ((self.display_width/2), (self.display_height/2)))

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.game_loop()

            self.button("GO!", 25, (a, b), self.white, ( rec_x, rec_y, rec_w, rec_h), self.block_color, self.green, self.game_loop)
            pygame.draw.polygon(self.gameDisplay, self.white, ( (a2, c), (a2, d), (e, f) ))

            pygame.display.update()
            self.clock.tick(15)


    def game_loop(self):
        pygame.mixer.music.play(-1)

        x               = (self.display_width * 0.45)
        y               = (self.display_height * 0.8)
        x_chnage        = 0
        thing_startx    = random.randrange(0, self.display_width-100)
        thing_startxs   = thing_startx + 406
        thing_starty    = -600
        thing_speed     = 4
        thing_width     = 100
        thing_height    = 100
        gameExit        = False
        dodged          = 0
        self.gameDisplay.fill(self.white)
        
        



        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_chnage = -7
                    elif event.key == pygame.K_RIGHT:
                        x_chnage = 7
                    if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                        self.paused = True
                        self.pause()
                    if event.key == pygame.K_m:
                        pygame.mixer.music.stop()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_chnage = 0

            x += x_chnage

            self.gameDisplay.fill(self.white)

            
            self.things(thing_startx, thing_starty, thing_width, thing_height, self.block_color)

            

            if thing_speed > 9 and thing_startxs + thing_width < self.display_width - 1:
                self.things(thing_startxs, thing_starty, thing_width, thing_height, self.block_color)

            thing_starty += thing_speed

            self.car(x,y)
            self.things_dodged(dodged)
            self.pause_game()
            

            
            
            if thing_starty > self.display_height:
                thing_starty    = 0 - thing_height
                thing_startx    = random.randrange(0, self.display_width-100)
                thing_startxs   = thing_startx + 354
                dodged          += 1
                
                if thing_speed <= 11:
                    thing_width     += (dodged * 1.2)
                    thing_speed     += 1


            if y < thing_starty + thing_height:
                if x > thing_startx and x < thing_startx + thing_width or x + self.car_width > thing_startx and x + self.car_width < thing_startx + thing_width:
                    self.crash(dodged)

                if thing_speed > 9:
                    if x > thing_startxs and x < thing_startxs + thing_width or x + self.car_width > thing_startxs and x + self.car_width < thing_startxs + thing_width:
                        self.crash(dodged)
            
            if x > self.display_width - self.car_width or x < 0:
                self.crash(dodged)


            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    rc          = Racey()
    rc.game_intro()



