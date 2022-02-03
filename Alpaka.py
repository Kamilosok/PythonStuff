import arcade
import os
class MyGame(arcade.Window):
    def __init__(self,wys,szer,nazw):
        super().__init__(wys,szer,nazw)
        file_path = os.path.dirname (os.path.abspath (__file__))
        os.chdir(file_path)
        self.background=arcade.load_texture("Alpaka.jpg")
    def on_draw(self):
        arcade.draw_lrwh_rectangle_textured (0,0,800,800,self.background)
def main():
    """ Main method """
    window = MyGame(800,800,"U Boo")
    arcade.run()


if __name__ == "__main__":
    main()

