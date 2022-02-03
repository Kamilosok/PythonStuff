import arcade
import random
class Character:
    def __init__(self):
        self.x=10
        self.y=10
        self.r=10
        self.l=40
        self.MX=0
        self.MY=0
        self.MS=5
        self.shoot=False
        self.bshoot=False
        self.c1=arcade.color.RED
        self.c2=arcade.color.AMBER
    def wywal(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,self.c1)
        arcade.draw_circle_outline(self.x,self.y,self.r,self.c2)
        arcade.draw_point(self.x,self.y,self.c2,self.r/2)
    def updatex(self):
        self.x+=self.MX
        if self.x<self.r:
            self.x=self.r
        if self.x+self.r>800:
            self.x=self.x-self.MX
    def updatey(self):
        self.y+=self.MY
        if self.y<self.r:
            self.y=self.r
        if self.y+self.r>800:
            self.y=self.y-self.MY
    def shot(self):
        arcade.draw_line(self.x,self.y+self.r,self.x,self.y+self.r+self.l,self.c2)
    def bshot(self):
        arcade.draw_circle_outline(self.x, self.y, self.r+3, self.c2)


class Enemy:
    def __init__(self):
        self.x=random.randint(20,780)
        self.y=random.randint(100,760)
        self.Y=self.y
        self.r=20
        self.MX=8
        self.shoot=True
        self.c1=arcade.color.AIR_SUPERIORITY_BLUE
        self.c2=arcade.color.BLUE
    def wywal(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,self.c1)
        arcade.draw_circle_outline(self.x,self.y,self.r,self.c2,2)
        arcade.draw_rectangle_filled(self.x,self.y,self.r,self.r,self.c2,45)
    def updatex(self):
        self.x+=self.MX
        if self.x<self.r and self.y!=self.Y:
            self.y=self.y+10
            self.MX=8
        if self.x+self.r>800 and self.y==self.Y:
            self.y=self.y-10
            self.MX=-8

class Shop:
    def __init__(self):
        self.score=0
        self.ups = [0, 0, 0, 0, 0, 0]
        self.poor=0
        self.pro1=0
        self.pro2=0
        self.BS=False
        self.active=False
    def openshop(self):
        arcade.start_render()
        arcade.draw_text ("Score: " + str (self.score), 330, 740, arcade.color.WHITE, 40)
        arcade.draw_rectangle_filled(200,700,365,50,arcade.color.AMBER)
        arcade.draw_rectangle_filled (600,700,365,50,arcade.color.AMBER)
        arcade.draw_rectangle_filled (200,500,365,50,arcade.color.AMBER)
        arcade.draw_rectangle_filled (600,500,365,50,arcade.color.AMBER)
        arcade.draw_rectangle_filled (200,300,365,50,arcade.color.AMBER)
        arcade.draw_rectangle_filled (600,300,365,50,arcade.color.AMBER)
        arcade.draw_rectangle_filled (400,100,400,60,arcade.color.RED)
        arcade.draw_text ("EXIT", 350, 65, arcade.color.WHITE, 50)
        arcade.draw_text ("Speed +1 - 10 points", 45, 680, arcade.color.WHITE, 30)
        arcade.draw_text ("Speed +2 - 18 points", 445, 680, arcade.color.WHITE, 30)
        arcade.draw_text ("Laser L +10 - 10 points", 45, 480, arcade.color.WHITE, 30)
        arcade.draw_text ("Laser L +20 - 18 points", 430, 480, arcade.color.WHITE, 30)
        arcade.draw_text ("Body Shot - 30 points", 40, 280, arcade.color.WHITE, 30)
        arcade.draw_text ("Enemy starting speed -1 \n           - 15 points", 480, 275, arcade.color.WHITE, 22)
        if self.ups[0]>0:
            arcade.draw_rectangle_filled (400, 400, 440, 300, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_rectangle_outline (400, 400, 440, 300,arcade.color.BLUE)
            arcade.draw_text("Successfully bought +1 speed upgrade!",225,400,arcade.color.BLUE,20)
            self.ups[0]-=1
        if self.ups[1]>0:
            arcade.draw_rectangle_filled (400, 400, 440, 300, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_rectangle_outline (400, 400, 440, 300, arcade.color.BLUE)
            arcade.draw_text ("Successfully bought +2 speed upgrade!", 225, 400, arcade.color.BLUE, 20)
            self.ups[1] -= 1
        if self.ups[2]>0:
            arcade.draw_rectangle_filled (400, 400, 440, 300, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_rectangle_outline (400, 400, 440, 300, arcade.color.BLUE)
            arcade.draw_text ("Successfully bought\n+10 laser length upgrade!", 315, 400, arcade.color.BLUE, 20)
            self.ups[2] -= 1
        if self.ups[3]>0:
            arcade.draw_rectangle_filled (400, 400, 440, 300, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_rectangle_outline (400, 400, 440, 300, arcade.color.BLUE)
            arcade.draw_text ("Successfully bought\n+20 laser length upgrade!", 315, 400, arcade.color.BLUE, 20)
            self.ups[3] -= 1
        if self.ups[4]>0:
            arcade.draw_rectangle_filled (400, 400, 440, 300, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_rectangle_outline (400, 400, 440, 300, arcade.color.BLUE)
            arcade.draw_text ("Successfully bought\nBody Shot speed upgrade!", 285, 400, arcade.color.BLUE, 20)
            self.ups[4] -= 1
        if self.ups[5]>0:
            arcade.draw_rectangle_filled (400, 400, 440, 300, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_rectangle_outline (400, 400, 440, 300, arcade.color.BLUE)
            arcade.draw_text ("Successfully bought\n-1 enemy starting speed\nupgrade!", 295, 380, arcade.color.BLUE, 20)
            self.ups[5] -= 1
        if self.poor>0:
            arcade.draw_rectangle_filled (400, 400, 440, 300, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_rectangle_outline (400, 400, 440, 300, arcade.color.BLUE)
            arcade.draw_text ("Not enough points!", 315, 400, arcade.color.BLUE,20)
            self.poor-=1
        if self.pro1>0:
            arcade.draw_rectangle_filled (400, 400, 440, 300, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_rectangle_outline (400, 400, 440, 300, arcade.color.BLUE)
            arcade.draw_text ("Body Shot already bought!", 275, 400, arcade.color.BLUE,20)
            self.pro1-=1
        if self.pro2>0:
            arcade.draw_rectangle_filled (400, 400, 440, 300, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_rectangle_outline (400, 400, 440, 300, arcade.color.BLUE)
            arcade.draw_text ("Enemy starting speed already 0!", 245, 400, arcade.color.BLUE,20)
            self.pro2-=1


class Mygame(arcade.Window):
    def __init__(self):
        self.wwidth=800
        self.hheight=800
        self.ttitle="Shooter Game"
        self.espeed=8
        self.t=0
        self.resp=0
        super().__init__(self.wwidth,self.hheight,self.ttitle)
        self.Pog=Character()
        self.Shoppy=Shop()
        self.Enemy=Enemy()
        self.Enemy1=Enemy()
        self.Enemy2=Enemy()
        self.Enemy3=Enemy()
    def on_draw(self):
        if self.Shoppy.active==False:
            arcade.start_render()
            self.Pog.wywal()
            if self.Enemy.shoot:
                self.Enemy.wywal()
            if self.Enemy1.shoot:
                self.Enemy1.wywal()
            if self.Enemy2.shoot:
                self.Enemy2.wywal()
            if self.Enemy3.shoot:
                self.Enemy3.wywal()
            if self.Pog.shoot:
                self.Pog.shot()
            if self.Pog.bshoot:
                self.Pog.bshot()
            arcade.draw_rectangle_filled(20,790,530,40,arcade.color.AMBER)
            arcade.draw_rectangle_outline(20,790,190,40,arcade.color.WHITE)
            arcade.draw_rectangle_outline(200,790,170,40,arcade.color.WHITE)
            arcade.draw_text ("Score: " + str (self.Shoppy.score), 10, 770, arcade.color.WHITE, 20)
            arcade.draw_text("SHOP",170,770,arcade.color.WHITE,20)
        else:
            self.Shoppy.openshop()

    def on_update(self, delta_time=1/60):
        self.Pog.updatex()
        self.Pog.updatey()
        if self.Enemy.shoot:
            self.Enemy.updatex()
        if self.Enemy1.shoot:
            self.Enemy1.updatex()
        if self.Enemy2.shoot:
            self.Enemy2.updatex()
        if self.Enemy3.shoot:
            self.Enemy3.updatex()
        if self.resp==300:
            self.resp=0
            self.Enemy.shoot=True
            self.Enemy1.shoot=True
            self.Enemy2.shoot=True
            self.Enemy3.shoot=True
            self.Enemy.x = random.randint (20, 780)
            self.Enemy1.x = random.randint (20, 780)
            self.Enemy2.x = random.randint (20, 780)
            self.Enemy3.x = random.randint (20, 780)
            self.Enemy.y = random.randint (100, 760)
            self.Enemy1.y = random.randint (100, 760)
            self.Enemy2.y = random.randint (100, 760)
            self.Enemy3.y = random.randint (100, 760)
            self.Enemy.Y = self.Enemy.y+10
            self.Enemy1.Y = self.Enemy1.y+10
            self.Enemy.MX=-self.espeed
            self.Enemy1.MX=-self.espeed
            self.Enemy2.Y = self.Enemy2.y
            self.Enemy3.Y = self.Enemy3.y
            self.Enemy2.MX = self.espeed
            self.Enemy3.MX = self.espeed
        if self.t==5:
            self.Pog.shoot=False
            self.Pog.bshoot=False
            self.t=0
        self.t+=1
        self.resp+=1
    def on_key_press(self,key,modifiers):
        if key==arcade.key.UP:
            self.Pog.MY=self.Pog.MS
        if key==arcade.key.DOWN:
            self.Pog.MY=-self.Pog.MS
        if key==arcade.key.RIGHT:
            self.Pog.MX=self.Pog.MS
        if key==arcade.key.LEFT:
            self.Pog.MX=-self.Pog.MS
        if key == arcade.key.A:
            self.Pog.shoot=True
            if self.Shoppy.BS==True:
                self.Pog.bshoot=True
            self.t=0
            self.ifshot()
    def on_key_release(self,key,modifiers):
        if key==arcade.key.UP or key==arcade.key.DOWN:
            self.Pog.MY=0
        if key==arcade.key.RIGHT or key==arcade.key.LEFT:
            self.Pog.MX=0

    def on_mouse_press(self, x, y, button, modifiers):
        if x>110 and x<290 and y>765 and y<800 and self.Shoppy.active==False:
            self.Shoppy.active=True
        if x>200 and x<600 and y>70 and y<130 and self.Shoppy.active==True:
            self.Shoppy.active=False

        if x>20 and x<385 and y>675 and y<725 and self.Shoppy.active==True:
            if self.Shoppy.score>=10:
                self.Shoppy.score-=10
                self.Pog.MS+=1
                self.Shoppy.ups[0] = 90
            else:
                self.Shoppy.poor=90
        if x>420 and x<785 and y>675 and y<725 and self.Shoppy.active==True:
            if self.Shoppy.score>=18:
                self.Shoppy.score-=18
                self.Pog.MS+=2
                self.Shoppy.ups[1] = 90
            else:
                self.Shoppy.poor = 90

        if x>20 and x<385 and y>475 and y<525 and self.Shoppy.active==True:
            if self.Shoppy.score>=10:
                self.Shoppy.score-=10
                self.Pog.l+=10
                self.Shoppy.ups[2] = 90
            else:
                self.Shoppy.poor = 90
        if x>420 and x<785 and y>475 and y<525 and self.Shoppy.active==True:
            if self.Shoppy.score>=18:
                self.Shoppy.score-=18
                self.Pog.l+=20
                self.Shoppy.ups[3] = 90
            else:
                self.Shoppy.poor = 90

        if x>20 and x<385 and y>275 and y<325 and self.Shoppy.active==True:
            if self.Shoppy.score>=30:
                if self.Shoppy.BS==False:
                    self.Shoppy.score-=30
                    self.Shoppy.BS=True
                    self.Shoppy.ups[4] = 90
                else:
                    self.Shoppy.pro1 = 90
            else:
                self.Shoppy.poor = 90
        if x>420 and x<785 and y>275 and y<325 and self.Shoppy.active==True:
            if self.Shoppy.score>=15:
                if self.espeed>0:
                    self.Shoppy.score-=15
                    self.espeed-=1
                    self.Shoppy.ups[5] = 90
                else:
                    self.Shoppy.pro2 = 90
            else:
                self.Shoppy.poor = 90

    def ifshot(self):
        if (self.Pog.x>self.Enemy.x-self.Enemy.r and self.Pog.x<self.Enemy.x+self.Enemy.r) and\
                (self.Pog.y+self.Pog.l+5>self.Enemy.y-self.Enemy.r and self.Pog.y+self.Pog.l+5<self.Enemy.y+self.Enemy.r):
            self.Shoppy.score+=1
            self.Enemy.x=820
            self.Enemy.shoot = False
        if (self.Pog.x > self.Enemy1.x - self.Enemy1.r and self.Pog.x < self.Enemy1.x + self.Enemy1.r) and \
                (self.Pog.y + self.Pog.l+5 > self.Enemy1.y - self.Enemy1.r and self.Pog.y + self.Pog.l+5 < self.Enemy1.y + self.Enemy1.r):
            self.Shoppy.score += 1
            self.Enemy1.x = 820
            self.Enemy1.shoot=False
        if (self.Pog.x > self.Enemy2.x - self.Enemy2.r and self.Pog.x < self.Enemy2.x + self.Enemy2.r) and \
                (self.Pog.y + self.Pog.l+5 > self.Enemy2.y - self.Enemy2.r and self.Pog.y + self.Pog.l+5 < self.Enemy2.y + self.Enemy2.r):
            self.Shoppy.score += 1
            self.Enemy2.x = 820
            self.Enemy2.shoot = False
        if (self.Pog.x > self.Enemy3.x - self.Enemy3.r and self.Pog.x < self.Enemy3.x + self.Enemy3.r) and \
                (self.Pog.y + self.Pog.l+5 > self.Enemy3.y - self.Enemy3.r and self.Pog.y + self.Pog.l+5 < self.Enemy3.y + self.Enemy3.r):
            self.Shoppy.score += 1
            self.Enemy3.x = 820
            self.Enemy3.shoot = False
        if self.Pog.bshoot:
            if (self.Enemy.x > self.Pog.x - self.Pog.r-20 and self.Enemy.x < self.Pog.x + self.Pog.r+20) and \
                    (self.Enemy.y > self.Pog.y - self.Pog.r-20 and self.Enemy.y < self.Pog.y + self.Pog.r+20):
                self.Shoppy.score += 1
                self.Enemy.x = 820
                self.Enemy.shoot = False
            if (self.Enemy1.x > self.Pog.x - self.Pog.r-20 and self.Enemy1.x < self.Pog.x + self.Pog.r+20) and \
                    (self.Enemy1.y > self.Pog.y - self.Pog.r-20 and self.Enemy1.y < self.Pog.y + self.Pog.r+20):
                self.Shoppy.score += 1
                self.Enemy1.x = 820
                self.Enemy1.shoot = False
            if (self.Enemy2.x > self.Pog.x - self.Pog.r-20 and self.Enemy2.x < self.Pog.x + self.Pog.r+20) and \
                    (self.Enemy2.y > self.Pog.y - self.Pog.r-20 and self.Enemy2.y < self.Pog.y + self.Pog.r+20):
                self.Shoppy.score += 1
                self.Enemy2.x = 820
                self.Enemy2.shoot = False
            if (self.Enemy3.x > self.Pog.x - self.Pog.r-20 and self.Enemy3.x < self.Pog.x + self.Pog.r+20) and \
                    (self.Enemy3.y > self.Pog.y - self.Pog.r-20 and self.Enemy3.y < self.Pog.y + self.Pog.r+20):
                self.Shoppy.score += 1
                self.Enemy3.x = 820
                self.Enemy3.shoot = False


def main():
    Mygame()
    arcade.run()
    arcade.close_window()
if __name__ =="__main__":
    main()
