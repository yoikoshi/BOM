import pyxel
import random
import math

#画面遷移
SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2
SCENE_CLEAR = 3
SCENE_EXPLANATION = 4

# プレイヤーの大きさ、動きの速さ
PLAYER_WIDTH = 25
PLAYER_HEIGHT = 16
PLAYER_SPEED = 2

def text(text):
    pyxel.text(72, 10, "STAGE", 7)

#プレイヤー  
class Player:
    def __init__(self):
        self.x = 12
        self.y = 168
        self.w = PLAYER_WIDTH
        self.h = PLAYER_HEIGHT

    def update(self):

        if pyxel.btn(pyxel.KEY_RIGHT) :
           if not 145 < self.y < 160 and not 110 < self.y < 135 and not 78 < self.y < 100 and not 48 < self.y < 68:
            self.x += PLAYER_SPEED

        if pyxel.btn(pyxel.KEY_UP):
            if not 145 < self.x < 165 and not 112 < self.x < 135  and not 78 < self.x < 103 and not 48 < self.x < 70 and not 18 < self.x < 38:
             self.y -= PLAYER_SPEED

        self.x = max(self.x, 0)
        self.x = min(self.x, pyxel.width - self.w)
        self.y = max(self.y, 40)
        self.y = min(self.y, pyxel.height - self.h)

    def draw(self):
        pyxel.blt(172, 42, 0, 16, 0, 16, 16, 0)
        pyxel.rect(self.x, self.y, 16, 16, 7)

class Bom:
    def __init__(self):
        self.x = [12, 44, 76, 108, 140 ,172]
        self.y = [42, 74, 106, 138 ,170]
        self.random = random.randint(1, 1)
        self.bom_update = 0
        self.bom_level = 1
        self.bom_level_least = 1

    def update(self):
        random.shuffle(self.x)
        random.shuffle(self.y)
        self.random = random.randint(self.bom_level_least, self.bom_level)

    def draw(self):
     pass


class Treasure:
    def __init__(self):
        self.x = [12, 44, 76, 108, 140 ,172]
        self.y = [42, 74,106, 138 ,170]
        self.random = random.randint(0, 3)
        self.t = 0
        self.t_update = 0

    def update(self):
        random.shuffle(self.x)
        random.shuffle(self.y)
        self.random = random.randint(0, 3)

    def draw(self):
      pass


class App:
    def __init__(self):
        pyxel.init(200, 200, fps=60)
        pyxel.load("app.pyxres")
        self.hp_color1 = 11
        self.hp_color2 = 11
        self.hp_color3 = 11
        self.sp_color1 = 9
        self.sp_color2 = 9
        self.sp_color3 = 9
        self.c = 0
        self.c2 = 0
        self.stage = 1
        self.treasure = 0
        self.rect = 16
        self.limit = 1
        self.text_color = 7
        self.player = Player()
        self.bom = Bom()
        self.t = Treasure()
        self.scene = SCENE_TITLE

        pyxel.run(self.update, self.draw)

    def update(self):
#ゴール判定
        if 150 < self.player.x < 180 and 30 < self.player.y < 60:
           self.player.x = 12
           self.player.y = 168
           self.stage += 1
           self.limit = 1
           pyxel.cls(0)
           self.bom.update()
           self.t.update()


        if self.scene == SCENE_TITLE:
           self.update_title_scene()
        elif self.scene == SCENE_PLAY:
             self.update_play_scene()
        elif self.scene == SCENE_GAMEOVER:
             self.update_gameover_scene()
        elif self.scene == SCENE_EXPLANATION:
             self.update_explanation_scene()

        if pyxel.btnp(pyxel.KEY_DOWN) and self.treasure > 0 and self.hp_color1 == 0:
           self.treasure -= 1
           if self.hp_color1 == 0 and self.hp_color2 == 0:
                self.hp_color3 = 11
                self.hp_color2 = 11
                self.c = 1
           elif self.hp_color1 == 0:
                self.hp_color1 = 11
                self.c = 0

        if pyxel.btnp(pyxel.KEY_LEFT) and self.c2 < 3:
           if self.sp_color1 == 0 and self.sp_color2 == 0:
                self.c2 = 3
                self.update_bom_sp()
           elif self.sp_color1 == 0:
                self.c2 = 2
                self.update_bom_sp()
           elif self.sp_color1 == 9:
                self.c2 = 1
                self.update_bom_sp()

        if self.stage == 100:
           self.scene = SCENE_CLEAR

        if self.stage == 10:
           self.bom.bom_level = 2
        elif self.stage == 20:
             self.bom.bom_level_least = 2
        elif self.stage == 30:
             self.bom.bom_level = 3
        elif self.stage == 50:
             self.bom.bom_level = 4
        elif self.stage == 90:
             self.bom.bom_level = 5


    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
           pyxel.cls(0)
           self.scene = SCENE_PLAY

        if  58 < pyxel.mouse_x < 158 and 140 < pyxel.mouse_y < 150:
            self.text_color = 8
        else:
            self.text_color = 7

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 58 < pyxel.mouse_x < 158 and 140 < pyxel.mouse_y < 150:
           pyxel.cls(0)
           self.scene = SCENE_EXPLANATION

    def update_gameover_scene(self):
         if pyxel.btnp(pyxel.KEY_SPACE):
            self.hp_color1 = 11
            self.hp_color2 = 11
            self.hp_color3 = 11
            self.sp_color1 = 9
            self.sp_color2 = 9
            self.sp_color3 = 9
            self.c = 0
            self.c2 = 0
            self.stage = 1
            self.treasure = 0
            self.limit = 1
            self.bom.bom_update = 1
            self.bom.bom_level = 1
            self.bom.bom_level_least = 1
            pyxel.cls(0)
            self.scene = SCENE_PLAY

    def update_play_scene(self):
        self.player.update()
        self.update_hp_bar()
        self.update_sp_bar()
        if self.bom.bom_update == 1:
           self.update_bom()

        if self.t.t_update == 1:
           self.update_t()

    def update_explanation_scene(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
           pyxel.cls(0)
           self.scene = SCENE_TITLE

    def update_bom_sp(self):
           self.bom.bom_update = 1
           self.player.x = 12
           self.player.y = 168
           self.limit = 1

    def update_hp_bar(self):
        if self.c == 1:
           self.hp_color1 = 0
        if self.c == 2:
             self.hp_color2 = 0
             self.hp_color3 = 8
        if self.c == 3:
             self.hp_color3 = 0
             self.scene = SCENE_GAMEOVER

    def update_sp_bar(self):
        if self.c2 == 1:
           self.sp_color1 = 0
        if self.c2 == 2:
             self.sp_color2 = 0
        if self.c2 == 3:
             self.sp_color3 = 0

    def update_bom(self):
        self.bom.update()
        self.bom.bom_update = 0
        pyxel.cls(0)
        self.draw_bom()

    def update_t(self):
         self.t.update()
         self.t.t_update = 0
         pyxel.cls(0)
         self.draw_treasure()

    def draw(self):
        s = " {:>4} / 100".format(self.stage)
        pyxel.text(85, 10, s, 7)
        pyxel.text(85, 20, "BOM lv.", 7)
        s = " {:>4}".format(self.bom.bom_level)
        pyxel.text(100, 20, s, 8)
        self.draw_hp_bar()
        self.draw_sp_bar()
        text(text)
        self.draw_treasure_num()
        pyxel.blt(140, 2, 0, 48, 32, 16, 16, 0)
        s = " :{:>4}".format(self.limit)
        pyxel.text(160, 8, s, 7)

        if self.scene == SCENE_TITLE:
           self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
           self.draw_play_scene()
        elif self.scene == SCENE_GAMEOVER:
           pyxel.cls(0)
           self.draw_gameover_scene()
        elif self.scene == SCENE_CLEAR:
             pyxel.cls(0)
             self.draw_clear_scene()
        elif self.scene == SCENE_EXPLANATION:
             pyxel.cls(0)
             self.draw_explanation_scene()

    def draw_title_scene(self):
        pyxel.mouse(True)
        pyxel.cls(0)
        pyxel.blt(63, 55, 0, 0, 48, 16, 16, 0)
        pyxel.blt(89, 54, 0, 16, 48, 16, 16, 0)
        pyxel.blt(115, 55, 0, 32, 48, 16, 16, 0)
        pyxel.text(80, 75, "-GO HOME-", 7)
        pyxel.text(90, 110, "START", pyxel.frame_count % 12)
        pyxel.text(78, 120, "PRESS SPACE", 7)
        pyxel.text(78, 140, "HOW TO PLAY", self.text_color)

    def draw_play_scene(self):
        pyxel.mouse(False)
        self.player.draw()
        self.draw_bom()
        self.draw_treasure()
        pyxel.bltm(0, 4, 0, 0, 0, 32, 32, 0)

    def draw_gameover_scene(self):
        pyxel.text(85, 100, "GAMEOVER", 8)
        pyxel.text(78, 110, "PRESS SPACE", 7)

    def draw_explanation_scene(self):
        pyxel.text(70, 50, "--HOW TO PLAY--", 8)
        pyxel.text(50, 70, "UP KEY : PLAYER UP", 7)
        pyxel.text(50, 80, "DOWN KEY : HEAL -1TREASURE", 7)
        pyxel.text(50, 90, "RIGHT KEY : PLAYER RIGHT", 7)
        pyxel.text(50, 100, "LEFT KEY : BOM REDRAW -1SP", 7)
        pyxel.text(50, 110, "SPACE KEY : SEARCH BOMS", 7)
        pyxel.blt(50, 124, 0, 32, 0, 16, 16, 0)
        pyxel.blt(40, 125, 0, 48, 48, 16, 16, 0)
        pyxel.text(68, 130, ":-1HP", 7)
        pyxel.blt(112, 125, 0, 40, 16, 16, 16, 0)
        pyxel.blt(100, 125, 0, 48, 48, 16, 16, 0)
        pyxel.text(130, 130, ":+1SP", 7)
        pyxel.text(40, 150, "PRESS SPACE KEY TO RETURN TITLE", 7)

    def draw_clear_scene(self):
        pyxel.text(85, 90, "CLEAR!", 7)
        pyxel.text(65, 100, "CONGRATULATIONS!!", pyxel.frame_count % 12)

    def draw_hp_bar(self):
        pyxel.text(20,10,"HP:",7)
        pyxel.rect(35, 10, 5, 5, self.hp_color3)
        pyxel.rect(42, 10, 5, 5, self.hp_color2)
        pyxel.rect(49, 10, 5, 5, self.hp_color1)

    def draw_sp_bar(self):
        pyxel.text(20,20,"SP:",7)
        pyxel.rect(35, 20, 5, 5, self.sp_color3)
        pyxel.rect(42, 20, 5, 5, self.sp_color2)
        pyxel.rect(49, 20, 5, 5, self.sp_color1)

    def draw_treasure_num(self):
        s = " :{:>4}".format(self.treasure)
        pyxel.text(160, 22, s, 7)
        pyxel.blt(140, 17, 0, 40, 16, 16, 16, 0)


    def draw_bom(self):
        for i in range(0, self.bom.random):
         if self.bom.x[i] == 172 and self.bom.y[i] == 42:
            self.bom.bom_update = 1
         elif self.bom.x[i] == 12 and self.bom.y[i] == 170:
            self.bom.bom_update = 1
         else:
            pyxel.blt(self.bom.x[i], self.bom.y[i], 0, 32, 0, 16, 16, 0)

         if self.bom.x[i] == 44 and self.bom.y[i] == 170 and self.bom.x[i] == 12 and self.bom.y[i] == 138:
           self.bom.bom_update = 1
         if self.bom.x[i] == 172 and self.bom.y[i] == 74 and self.bom.x[i] == 140 and self.bom.y[i] == 42:
           self.bom.bom_update = 1

        for i in range(0, self.bom.random):
         if self.bom.x[i] - 15 < self.player.x < self.bom.x[i] + 15 and self.bom.y[i] - 15 < self.player.y < self.bom.y[i] + 15:
           self.c += 1
           self.rect = 0

           self.player.x = 12
           self.player.y = 168
           pyxel.cls(0)


         pyxel.rect(self.bom.x[i], self.bom.y[i], self.rect, self.rect, 0)

         if pyxel.btn(pyxel.KEY_SPACE) and self.limit == 1:
            self.rect = 0
            self.limit -= 1

         if pyxel.btn(pyxel.KEY_UP) and self.rect == 0:
            self.rect = 16

         if pyxel.btn(pyxel.KEY_RIGHT) and self.rect == 0:
            self.rect = 16

    def draw_treasure(self):
            if self.t.random == 0:
                   self.t.t = 1

            for i in range(0, self.t.t):
             if self.t.x[i] == 172 and self.t.y[i] == 42:
                self.t.t_update = 1
             elif self.t.x[i] == 12 and self.t.y[i] == 170:
                self.t.t_update = 1
             else:
                pyxel.blt(self.t.x[i], self.t.y[i], 0, 48, 0, 16, 16, 0)
                self.t.t = 0

             if self.t.x[i] == self.bom.x[i] and self.t.y[i] == self.bom.y[i]:
                self.t.t_update = 1

             for i in range(0, 1):
              if self.t.x[i] - 15 < self.player.x < self.t.x[i] + 15 and self.t.y[i] - 15 < self.player.y < self.t.y[i] + 15:
               self.player.x = 12
               self.player.y = 168
               self.treasure += 1
               self.t.random = 1

               if self.c2 == 1:
                  self.sp_color1 = 9
                  self.c2 = 0
               elif self.c2 == 2:
                    self.sp_color2 = 9
                    self.c2 = 1
               elif self.c2 == 3:
                    self.sp_color3 = 9
                    self.c2 = 2

               pyxel.cls(0)


App()


