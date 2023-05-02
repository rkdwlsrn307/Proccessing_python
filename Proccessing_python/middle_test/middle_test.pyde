

ball_color = [0xffff0000, 0xffffff00, 0xffff00ff, 0xff0000ff, 0xff556600]

ball_data = []

ball_diam = 100

color_cnt = 0

diry = 3


def setup():
    size(800, 800)
    background(255)
    for i in range(100):
        ball_data.append([random(width-50), random(height-50), i+5, 0])
    
def draw():
    background(255)
    global ball_color, ball_diam, color_cnt, diry
    for ball in ball_data:
        color_cnt += 1
        #fill(ball_color[i])
        x = ball[0]
        y = ball[1]
        diry = ball[2]
        cnt = ball[3]
        if color_cnt >= 5:
            color_cnt = 0
        fill(ball_color[color_cnt])
        if cnt <= 10:
            if cnt == 10:
                continue
            ellipse(x, y, ball_diam, ball_diam)
            textSize(20)
            fill(255)
            text(cnt, x, y)
        
        newy = y + diry
        newdiry = diry
        newcnt = cnt
        
        if newy >= height - ball_diam / 2:
            newdiry *= -1
            newcnt = cnt + 1
        if newy <= ball_diam / 2:
            newdiry *= -1
            newcnt = cnt + 1
            
            
        ball[1] = newy
        ball[2] = newdiry
        ball[3] = newcnt
