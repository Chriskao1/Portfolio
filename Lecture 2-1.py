from vpython import *
#Web VPython 3.2

size=1.5 
scene = canvas(width=600, height=600, center = vector(0,5,0)) #設定畫面
floor = box(length=150, height=0.01, width=50, color=color.green)      #畫地板
bally = sphere(radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=100)
ballr = sphere(radius = size, color=color.red, make_trail=True, trail_type="points", interval=100)

bally.pos = vector(-70, 0, 0)#球初始位置
ballr.pos = vector(-70, 0, 0)#球初始位置
bally.v = vector(10, 10, 0) #球初速 
ballr.v = vector(10, 10, 0) #球初速 
g=9.8
m=10
k=0.05

dt = 0.001	#時間間隔 0.001 秒
t = 0.0		#模擬初始時間為0秒

while bally.v.y != 0:    #模擬直到球落地 即y=球半徑
    rate(1/dt)    #每一秒跑 1000 次
    t = t + dt    #計時器
    bally.v.y -= g * dt       #球的末速度 = 前一刻速度 + 加速度*時間間隔
    bally.pos = bally.pos + bally.v * dt#球的末位置 = 前一刻位置 + 速度*時間間隔
    air_resist = -k * ballr.v
    if ballr.v.y > 0:
        ballr.v.y -= g * dt
        ballr.v += air_resist * dt
    else:
        ballr.v.y -= g * dt
        ballr.v += air_resist * dt
    ballr.pos += ballr.v * dt
    if bally.v.y < 0 and bally.pos.y <= size:
        bally.v.y = -bally.v.y
    if ballr.v.y < 0 and ballr.pos.y <= size:
        ballr.v.y = -ballr.v.y
