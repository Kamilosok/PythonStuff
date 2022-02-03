import arcade
class Gamer:
    def __init__(self,x,y):
        self.x=x*10
        self.y=y*10
        self.r=10
    def show(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,arcade.color.WHITE)
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800,800,"Class Arrays")
        self.gamer=[]
        for i in range(10):
            self.gamer.append(Gamer(i,i))
        for i in range(10):
            self.gamer[i].show()

def main():
    MyGame()
    arcade.run()
    arcade.close_window()
if __name__ =="__main__":
    main()