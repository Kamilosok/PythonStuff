import arcade
import time
Screen_W=800
Screen_H=800
Screen_T="Future"
arcade.open_window(Screen_W,Screen_H,Screen_T,True,True)
arcade.set_background_color(arcade.color.BLACK)
CenterX=10
CenterY=800
for i in range(101):
    arcade.start_render()
    arcade.draw_circle_filled(CenterX,CenterY,10,arcade.color.GOLD)
    while CenterY>0 and CenterX>0:
        arcade.draw_circle_outline(CenterX,CenterY,10,arcade.color.GOLD)
        CenterX=CenterX-10
        CenterY=CenterY-10
    CenterX=CenterX+8
    CenterY=CenterY-8
    arcade.finish_render()
    time.sleep(0.05)
    arcade.start_render()
    arcade.draw_circle_filled(CenterX,CenterY,10,arcade.color.GOLD)
    while CenterY<Screen_H and CenterX<Screen_W:
        arcade.draw_circle_outline(CenterX,CenterY,10,arcade.color.GOLD)
        CenterX=CenterX+10
        CenterY=CenterY+10
    arcade.finish_render()
arcade.run()
arcade.close_window()