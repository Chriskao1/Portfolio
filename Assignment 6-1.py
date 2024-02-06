from vpython import *
#Web VPython 3.2

G = 6.67 ; m = 10 ; R = 20 ; v = (G*m/R)**0.5 ; t = 0 ; dt = 0.001; F = G * (m**2) * (3**0.5) / (R**2) ; v0 = (G * m / R)**0.5

def Fg(x): #定義萬有引力函數
    return -G*m**2/(x**2)
"""
    2. 畫面設定
"""
 
scene = canvas(width=1200, height=800, center=vec(0,0,0),
                background=vec(0.6,0.8,0.8),range=2*R)

ballright = sphere(pos=vector(0.5*R,-0.5/(3**0.5)*R,0), radius=0.3, color = color.blue, make_trail=True)
ballleft = sphere(pos=vector(-0.5*R,-0.5/(3**0.5)*R,0), radius=0.3, color = color.red, make_trail=True)
balltop = sphere(pos=vector(0,R/(3**0.5),0), radius = 0.3, color=color.black, make_trail=True)
ball_top_v = vector(v0,0,0)
ball_left_v = vector(-0.5*v0,(3**0.5) / 2 * v0,0)
ball_right_v = vector(-0.5*v0,-(3**0.5 / 2 * v0),0)

"""atop = vector(0,-F/m,0)
aright = vector(-F*cos(pi/6)/m, F*sin(pi/6)/m, 0)
aleft = vector(F*cos(pi/6)/m, F*sin(pi/6)/m, 0)"""

while True:
    rate(1/dt)
    distopright = mag(balltop.pos - ballright.pos)
    topright = (balltop.pos-ballright.pos)/distopright
    Ftopright = Fg(distopright) * topright
    
    distopleft = mag(balltop.pos - ballright.pos)
    topleft = (balltop.pos - ballleft.pos)/distopleft
    Ftopleft = Fg(distopleft) * topleft
    
    disleftright = mag(ballleft.pos - ballright.pos)
    leftright = (ballleft.pos - ballright.pos)/distopright
    Fleftright = Fg(disleftright) * leftright
    
    atop = (Ftopright / m + Ftopleft / m)
    aleft = (-Ftopleft / m + Fleftright / m)
    aright = (-Ftopright / m - Fleftright / m)
    
    ball_right_v += aright*dt
    ball_left_v += aleft*dt
    ball_top_v += atop*dt
    
    balltop.pos += ball_top_v*dt
    ballright.pos += ball_right_v*dt
    ballleft.pos += ball_left_v*dt
