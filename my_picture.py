import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""
    
    # Fill the background
    sg.fill_background("white")
    
    # make some variables available
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    
    draw_ear_and_ribbon(width, height)

def draw_ear_and_ribbon(width, height):
    sg.set_fill_color("#000000")
    sg.fill_rectangle((width/30)*15, (height/20)*3, (width/30), (height/20))
    sg.fill_rectangle((width/30)*16, (height/20)*2, (width/30)*2, (height/20))
    sg.fill_rectangle((width/30)*18, (height/20)*3, (width/30), (height/20))
    sg.fill_rectangle((width/30)*19, (height/20)*4, (width/30), (height/20))
    sg.fill_rectangle((width/30)*15, (height/20)*7, (width/30)*3, (height/20))
    sg.fill_rectangle((width/30)*17, (height/20)*6, (width/30), (height/20))
    sg.fill_rectangle((width/30)*18, (height/20)*8, (width/30)*3, (height/20))
    sg.fill_rectangle((width/30)*18, (height/20)*5, (width/30)*3, (height/20))
    sg.fill_rectangle((width/30)*20, (height/20)*3, (width/30)*3, (height/20))
    sg.fill_rectangle((width/30)*20, (height/20)*8, (width/30), (height/20)*2)
    sg.fill_rectangle((width/30)*16, (height/20)*2, (width/30)*2, (height/20))
    sg.fill_rectangle((width/30)*23, (height/20)*4, (width/30), (height/20)*3)
    sg.fill_rectangle((width/30)*21, (height/20)*6, (width/30)*2, (height/20))
    sg.fill_rectangle((width/30)*21, (height/20)*7, (width/30), (height/20))
    sg.fill_rectangle((width/30)*23, (height/20)*9, (width/30), (height/20))
    sg.fill_rectangle((width/30)*24, (height/20)*7, (width/30), (height/20)*2)
    
    sg.set_fill_color("red")
    sg.set_outline_color("red")
    
    sg.fill_rectangle((width/30)*21, (height/20)*8, (width/30)*2, (height/20)*2)
    sg.fill_rectangle((width/30)*22, (height/20)*7, (width/30)*2, (height/20)*2)
    sg.fill_rectangle((width/30)*18, (height/20)*6, (width/30*3), (height/20)*2)
    sg.fill_rectangle((width/30)*15, (height/20)*4, (width/30)*2, (height/20)*3)
    sg.fill_rectangle((width/30)*16, (height/20)*3, (width/30)*2, (height/20)*3)
    sg.fill_rectangle((width/30)*18, (height/20)*4, (width/30), (height/20))
    
if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
