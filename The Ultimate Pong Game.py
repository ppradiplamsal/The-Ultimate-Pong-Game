import simplegui

height = 800
width = 1300
pad_wid = 25
pad_hei = 115
ball_rad = 10
velx = 5
vely = 2
ball_pos = [width / 2, height / 2]
pad1_pos = [[0, height / 2 - pad_hei / 2],[pad_wid, height / 2 - pad_hei / 2],
            [pad_wid, height / 2 + pad_hei / 2], [0, height / 2 + pad_hei /2]]
pad2_pos = [[width - pad_wid, height / 2 - pad_hei / 2],[width, height / 2 - pad_hei / 2],
            [width, height / 2 + pad_hei / 2], [width -pad_wid, height / 2 + pad_hei /2]]
slider = 130
p1pts = 0
p2pts = 0

def draw_handler(p):
    global ball_pos, velx, vely, p1pts, p2pts
    ball_pos[0] += velx
    ball_pos[1] += vely
    
    if (ball_pos[1]-ball_rad<=0) or (ball_pos[1]+ball_rad>=height):
        vely=-vely

    #for bouncing the ball off the paddle
    if (ball_pos[0]-ball_rad<=pad_wid):
        if (ball_pos[1]+ball_rad>=pad1_pos[1][1])and(ball_pos[1]+ball_rad<=pad1_pos[2][1]):
            velx=-velx
        else:
            p2pts+=10
            ball_pos = [width / 2, height / 2]
            p.draw_text ("PLR 2", [150,400], 450, "Blue")
                       
    
    if (ball_pos[0]+ball_rad>=width-pad_wid):
        if (ball_pos[1]+ball_rad>=pad2_pos[0][1])and(ball_pos[1]+ball_rad<=pad2_pos[3][1]):
            velx=-velx
        else:
            p1pts+=10
            ball_pos = [width / 2, height / 2]
            p.draw_text ("PLR 1", [150,400], 450, "Yellow")
            
        
    p.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    p.draw_line([pad_wid, 0], [pad_wid, height], 1.5, "White")
    p.draw_line([width - pad_wid, 0], [width - pad_wid, height], 1.5, "White")
    p.draw_polygon(pad1_pos, 1, "White")
    p.draw_polygon(pad2_pos, 2, "White")
    p.draw_circle(ball_pos, ball_rad, 2, "Red", "White")
    p.draw_text ("Player1", [347,60], 40, "Red")
    p.draw_text ("Player2", [823,60], 40, "Red")
    p.draw_text (str(p1pts), [375,120], 55, "Red")
    p.draw_text (str(p2pts), [850,120], 55, "Red")


def key_handler (q):
    global pad1_pos, pad2_pos
    if q == simplegui.KEY_MAP["up"]:
        pad1_pos[0][1] -= slider
        pad1_pos[1][1] -= slider
        pad1_pos[2][1] -= slider
        pad1_pos[3][1] -= slider
        if pad1_pos[0][1]<0 and pad1_pos[1][1]<0: 
            pad1_pos[0][1]=0 
            pad1_pos[1][1]=0 
            pad1_pos[2][1]=pad_hei
            pad1_pos[3][1]=pad_hei 
        
    if q == simplegui.KEY_MAP["down"]:
        pad1_pos[0][1] += slider
        pad1_pos[1][1] += slider
        pad1_pos[2][1] += slider
        pad1_pos[3][1] += slider
        if pad1_pos[2][1] > height and pad1_pos[3][1] > height:
            pad1_pos[2][1] = height
            pad1_pos[3][1] = height
            pad1_pos[0][1] = height-pad_hei
            pad1_pos[1][1] = height-pad_hei

    if q == simplegui.KEY_MAP["w"]:
        pad2_pos[0][1] -= slider
        pad2_pos[1][1] -= slider
        pad2_pos[2][1] -= slider
        pad2_pos[3][1] -= slider
        if pad2_pos[0][1]<0 and pad2_pos[1][1]<0: 
            pad2_pos[0][1]=0 
            pad2_pos[1][1]=0 
            pad2_pos[2][1]=pad_hei
            pad2_pos[3][1]=pad_hei 
        
    if q == simplegui.KEY_MAP["s"]:
        pad2_pos[0][1] += slider
        pad2_pos[1][1] += slider
        pad2_pos[2][1] += slider
        pad2_pos[3][1] += slider
        if pad2_pos[2][1] > height and pad2_pos[3][1] > height:
            pad2_pos[2][1] = height
            pad2_pos[3][1] = height
            pad2_pos[0][1] = height-pad_hei
            pad2_pos[1][1] = height-pad_hei 


        
                                     
frame = simplegui.create_frame("The Ultimate Pong Game", width, height)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handler)

frame.start()