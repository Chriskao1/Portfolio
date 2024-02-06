from vpython import *
#Web VPython 3.2

m1 = 1
m2 = 5
m3 = 30
g=9.8                 #重力加速度 9.8 m/s^2            
dt = 0.001 
redo = True
redo1 = True
"""
    2. 畫面設定
"""
scene = canvas(width=400, height=600, center = vec(0,20,0), background=vec(0.6,0.8,0.8)) #設定畫面
floor = box(length=15, height=0.01, width=10, color=color.blue)                         #畫地板
ball_1 = sphere(radius = 1, color=color.yellow ) #畫球
ball_2 = sphere(radius = 2, color=color.green ) #畫球
ball_3 = sphere(radius = 3, color=color.red )

ball_1.pos = vector( 0, 20, 0)        #球初始位置       
ball_1.v = vector( 0, 0, 0)                    #球初速 
ball_2.pos = vector( 0, 17, 0)        #球初始位置       
ball_2.v = vector( 0, 0, 0)   
ball_3.pos = vector( 0, 12, 0)        #球初始位置       
ball_3.v = vector( 0, 0, 0)   #球初速 
"""
    3. 執行迴圈
"""
pre_height = ball_1.pos.y
while True:             
    rate(1000)                          #每一秒跑 1000 次
    pre_pre_height = pre_height
    pre_height = ball_1.pos.y
    ball_1.pos += ball_1.v*dt
    ball_1.v.y += - g*dt
    
    if ball_1.pos.y <= 1 and ball_1.v.y < 0:     
        ball_1.v.y = - 1* ball_1.v.y

    ball_2.pos += ball_2.v*dt
    ball_2.v.y += - g*dt
    
    if ball_2.pos.y <= 2 and ball_2.v.y < 0:     
        ball_2.v.y = - 1* ball_2.v.y
        
    ball_3.pos += ball_3.v*dt
    ball_3.v.y += - g*dt
    if ball_3.pos.y <= 3 and ball_3.v.y < 0:
        ball_3.v.y *= -1
        
    if ball_3.v.y > 0 and redo:
        v3y = (m3-m2) / (m3+m2) * ball_3.v.y+ 2*m2 / (m2+m3) * ball_2.v.y
        v2y = (m2-m3) / (m3+m2) * ball_2.v.y+ 2*m3 / (m3+m2) * ball_3.v.y
        ball_3.v = vector(0,v3y,0)
        ball_2.v = vector(0,v2y,0)
        redo = False
    if ball_2.v.y > 0 and redo1:
        v2y = (m2-m1) / (m1+m2) * ball_2.v.y+ 2*m1 / (m1+m2) * ball_1.v.y 
        v1y = (m1-m2) / (m1+m2) * ball_1.v.y+ 2*m2 / (m1+m2) * ball_2.v.y
        ball_2.v = vector(0,v2y,0)
        ball_1.v = vector(0,v1y,0)
        redo1 = False
    if pre_height > pre_pre_height and pre_height > ball_1.pos.y:
        print(pre_height)
