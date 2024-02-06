from vpython import *
#Web VPython 3.2

size=0.05
theta=0.0
r=1.0
omega=2*pi
t=0.0
dt=0.001
back = False
redo = True

scene = canvas(width=600, height=600, center = vector(0,0,0), background=vector(140.0/225, 228.0/225, 204.0/225)) #設定畫面
ball = sphere(radius = size, color=color.red, make_trail=True, interval=1, retain=1000)

ball.pos=vector(r,0,0)

pre_theta=theta
pre_t=0.0
record = 0.0
while True:
    rate(1/dt)
    pre_pre_theta=pre_theta
    pre_theta=theta
    theta+=omega*dt
    ball.pos = vector(r*cos(theta), r*sin(theta), 0)
    t += dt
    if back and redo:
        plot_t = t % (record/20) #將週期切成N等分，並用餘數除法設定畫圖時間點
        if plot_t + dt >= record/20 and plot_t < record/20 : #畫圖時間判斷點
            cylinder(radius=size/50, color=color.black, pos=vector(0,0,0) , axis= ball.pos) #畫細線
        if pre_theta % (2*pi) > pre_pre_theta % (2*pi) and pre_theta % (2*pi) >  theta % (2*pi):
            redo = False
    if pre_theta % (2*pi) > pre_pre_theta % (2*pi) and pre_theta % (2*pi) >  theta % (2*pi):
        back = True
        record = t
        t=0
