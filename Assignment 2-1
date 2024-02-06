from vpython import *
#Web VPython 3.2

size=0.5
scene = canvas(width=600, height=600, center = vector(0,5,0)) #設定畫面
floor = box(length=50, height=0.01, width=10, color=color.blue)      #畫地板
bally = sphere(radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=100)
ballr = sphere(radius = size, color=color.red, make_trail=True, trail_type="points", interval=100)
ballg = sphere(radius = size, color=color.green, make_trail=True, trail_type="points", interval=100)

bally.pos = vector(-10, 0, 0)#球初始位置
ballr.pos = vector(-10, 0, 0)#球初始位置
ballg.pos = vector(-10, 0, 0)
bally.v = vector(10, 10, 0) #球初速 
ballr.v = vector(10, 10, 0) #球初速
ballg.v = vector(10, 10, 0)

g=9.8
m=1
k=0.999999

dt = 0.001    #時間間隔 0.001 秒
t = 0.0		#模擬初始時間為0秒

while bally.pos.y >= 0:
    rate(1/dt)
    t += dt
    bally.v.y -= g*dt
    airresist = -k * ballr.v
    ballr.a = (airresist + vector(0, -g*m, 0)) / m
    if ballr.pos.y >= 0:
        ballr.v += ballr.a * dt
    else:
        ballr.v.x=0
        ballr.v.y=0
    bally.pos += bally.v*dt
    ballr.pos += ballr.v*dt

t = 0.0

while ballg.pos.y >= 0:
    rate(1/dt)
    t += dt
    ballg.pos.x = ballg.v.x * (1 - exp(-k*t))/k -10
    ballg.pos.y = - g*t/k + (k*ballg.v.y + g) * (1 - exp(-k*t))/k**2
    ballg.pos.z = 0
