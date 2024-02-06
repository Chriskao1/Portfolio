from vpython import *
#Web VPython 3.2

g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 100000              #彈簧力常數 100000 N/m
m = 0.1                 #球質量 0.1 kg
theta = 30 * pi/180     #初始擺角
Fg = m*vector(0,-g,0)   #球所受重力向量

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball = sphere(radius = size,  color=color.yellow, make_trail = True, retain = 1000, interval=1)#畫球
ball_2 = sphere(radius = size,  color=color.green, make_trail = True, retain = 1000, interval=1)#畫球
rod = cylinder(radius=size/10)#畫棒子
rod_2 = cylinder(radius=size/10)#畫棒子
    
figure = graph(align='left',     #畫x-t圖                                  
              title='E', xtitle='t', ytitle='e2-black,e1-green,E-red',
              foreground=color.black,background=color.white)
f1_1 = gcurve(color=color.red)       
f1_2 = gcurve(color=color.black)
f1_3 = gcurve(color=color.green)
    
ball.pos = vector(L, 0, 0)   #球的初始位置
ball.v = vector(0, 0, 0)                            #球初速
rod.pos = vector(0, 0, 0)                           #棒子頭端的位置

ball_2.pos = vector(2*L, 0, 0)   #球的初始位置
ball_2.v = vector(0, 0, 0)                            #球初速
rod_2.pos = vector(L, 0, 0)                           #棒子頭端的位置

dt = 0.001    #時間間隔
t = 0.0       #初始時間


while True:
    rate(1/dt)
    
    rod_2.pos = ball.pos                 #外棒的位子在紅球處
    rod.axis = ball.pos                #內棒的軸方向由原點指向紅球
    rod_2.axis = ball_2.pos - ball.pos   #外棒的軸方向由紅球指向綠球
    ball.a = (Fg + SpringForce(rod.axis,L)- SpringForce(rod_2.axis,L))/m    #牛頓第二定律：加速度＝合力/質量
    ball_2.a = (Fg + SpringForce(rod_2.axis,L))/m    #牛頓第二定律：加速度＝合力/質量

    ball.v += ball.a*dt    #速度
    ball.pos += ball.v*dt  #三點記錄法，現在時刻x座標
    ball_2.v += ball_2.a*dt    #速度
    ball_2.pos += ball_2.v*dt  #三點記錄法，現在時刻x座標
    
    k_1=0.5*(m*mag(ball.v)**2)
    u=m*g*ball.pos.y
    e=k_1+u
    
    k_2=0.5*(m*mag(ball_2.v)**2)
    u_2=m*g*ball_2.pos.y
    e_2=k_2+u_2
    
    E=e+e_2
    
    f1_1.plot( pos=(t,E))
    f1_2.plot( pos=(t,e_2))
    f1_3.plot( pos=(t,e))
    
    t += dt