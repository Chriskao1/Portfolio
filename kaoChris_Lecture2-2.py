from vpython import *
#Web VPython 3.2

size=0.05
theta=0.0
r=1.0
omega=2*pi
t=0.0
dt=0.001

scene = canvas(width=600, height=600, center = vector(0,0,0), background=vector(140.0/225, 228.0/225, 204.0/225)) #設定畫面
ball = sphere(radius = size, color=color.red, make_trail=True, interval=1, retain=1000)

ball.pos=vector(r,0,0)

pre_theta=theta
pre_t=0.0

while True:
    rate(1/dt)
    pre_pre_theta=pre_theta
    pre_theta=theta
    theta+=omega*dt
    ball.pos = vector(r*cos(theta), r*sin(theta), 0)
    t += dt

    if pre_theta % (2*pi) > pre_pre_theta % (2*pi) and pre_theta % (2*pi) >  theta % (2*pi):
        print("period=", t-pre_t)
        pre_t=t