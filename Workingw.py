import arcade
import random
MS=10
class Shot:
    def __init__(self):
        self.x=random.randint(10,790)
        self.y=random.randint(10,790)
        self.r=4
        self.c=arcade.color.GOLD
    def wywal(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,self.c)
    def update(self):
            self.x=random.randint(10,790)
            self.y=random.randint(10,790)
class Shat:
    def __init__(self):
        self.x=random.randint(10,790)
        self.y=random.randint(10,790)
        self.r=20
        self.c=arcade.color.RED
    def wywal(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.r,self.r,self.c)
    def update(self):
        self.x=random.randint(10,790)
        self.y=random.randint(10,790)
class Ball:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
        self.c=arcade.color.WHITE
        self.zx=0
        self.zy=0
    def rys(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,self.c)
    def update(self):
        self.x=self.x+self.zx
        self.y=self.y+self.zy
        if self.x < self.r:
            self.x = self.r

        if self.x>800-self.r:
            self.x=800-self.r

        if self.y<self.r:
            self.y=self.r

        if self.y>800-self.r:
            self.y=800-self.r
    def big(self):
        self.r+=2
    def small(self):
        self.r-=4

class Gra(arcade.Window):
    def __init__(self,wys,szer,nazw):
        super().__init__(wys,szer,nazw)
        self.set_mouse_visible(True)
        self.ball=Ball(400,400,20)
        self.moneta=Shot()
        self.wrog=Shat()
        self.background=arcade.load_texture("Alpaka.jpg",0,0)
    def on_draw(self):
        arcade.draw_lrwh_rectangle_textured (0, 0,800,800 ,self.background)
        arcade.start_render()
        self.ball.rys()
        self.moneta.wywal()
        self.wrog.wywal()
        arcade.draw_text ("Score: "+str(self.ball.r), 10, 20, arcade.color.WHITE, 14)
        if self.ball.r==0:
            arcade.draw_text("U lost u n00b",400,400,arcade.color.WHITE,20)
    def on_update(self, delta_time=1/60):
        self.ball.update()
        if (self.moneta.x>self.ball.x-self.ball.r and self.moneta.x<self.ball.x+self.ball.r) and\
           (self.moneta.y>self.ball.y-self.ball.r and self.moneta.y<self.ball.y+self.ball.r):
            self.wrog.update()
            self.moneta.update()
            self.ball.big()
        if (self.wrog.x > self.ball.x - self.ball.r and self.wrog.x < self.ball.x + self.ball.r) and \
                (self.wrog.y > self.ball.y - self.ball.r and self.wrog.y < self.ball.y + self.ball.r):
            self.wrog.update ()
            self.ball.small()
    def on_key_press(self,key,modifiers):
        if key==arcade.key.UP:
            self.ball.zy=MS
        elif key==arcade.key.DOWN:
            self.ball.zy=-MS
        elif key==arcade.key.LEFT:
            self.ball.zx=-MS
        elif key==arcade.key.RIGHT:
            self.ball.zx=MS
    def on_key_release(self,key,modifiers):
        if key==arcade.key.UP or key==arcade.key.DOWN:
            self.ball.zy=0
        if key==arcade.key.LEFT or key==arcade.key.RIGHT:
            self.ball.zx=0
def main():
    Gra(800,800,"Oh boy")
    arcade.run()
if __name__=="__main__":
    main()


