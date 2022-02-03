import arcade
import time
import random
arcade.open_window(1000,1000,'Animation')
arcade.set_background_color(arcade.color.BLACK)
while True:
    CenterY = 400
    CenterX = 10
    while CenterX>9 and CenterX<390 or CenterY<790 and CenterY>399:
        arcade.start_render()
        CenterX+=10+random.randint(-15,15)
        CenterY+=10+random.randint(-15,15)
        arcade.draw_line(CenterX,CenterY,CenterX-20+random.randint(-15,0),CenterY-20+random.randint(-15,0),arcade.color.AIR_SUPERIORITY_BLUE)
        arcade.draw_circle_filled (CenterX, CenterY, 10, arcade.color.ALABAMA_CRIMSON)
        arcade.finish_render()
        time.sleep(0.01)
    while CenterX>399 and CenterX<790 or CenterY<790 and CenterY>399:
        arcade.start_render()
        CenterX+=10+random.randint(-15,15)
        CenterY-=10+random.randint(-15,15)
        arcade.draw_line (CenterX,CenterY,CenterX-20+random.randint(-15,0),CenterY+20+random.randint (0,15),arcade.color.AIR_SUPERIORITY_BLUE)
        arcade.draw_circle_filled (CenterX, CenterY, 10, arcade.color.ALABAMA_CRIMSON)
        arcade.finish_render()
        time.sleep(0.01)
        arcade.finish_render()
    while CenterX>399 and CenterX<799 or CenterY<399 and CenterY>19:
        arcade.start_render()
        CenterX-=10+random.randint(-15,15)
        CenterY-=10+random.randint(-15,15)
        arcade.draw_line (CenterX,CenterY,CenterX+20+random.randint(0,15),CenterY+20+random.randint(0, 15),arcade.color.AIR_SUPERIORITY_BLUE)
        arcade.draw_circle_filled (CenterX, CenterY, 10, arcade.color.ALABAMA_CRIMSON)
        arcade.finish_render()
        time.sleep(0.01)
    while CenterX>19 and CenterX<399 or CenterY<399 and CenterY>9:
        arcade.start_render()
        CenterX-=10+random.randint(-15,15)
        CenterY+=10+random.randint(-15,15)
        arcade.draw_line (CenterX,CenterY,CenterX+20+random.randint(0,15),CenterY-20+random.randint(-15,0),arcade.color.AIR_SUPERIORITY_BLUE)
        arcade.draw_circle_filled (CenterX, CenterY, 10, arcade.color.ALABAMA_CRIMSON)
        arcade.finish_render()
        time.sleep(0.01)