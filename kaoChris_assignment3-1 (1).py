from vpython import *
#Web VPython 3.2

g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 10                  #彈簧力常數 10 N/m
m = 0.1                 #球質量 0.1 kg
Fg = m*vector(0,-g,0)   #球所受重力向量

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball = sphere(radius = size,  color=color.yellow)#畫球
spring = helix(radius=0.02, thickness =0.01)#畫彈簧
a = graph(width=600, height=500, title='Energy check: green for K, red for Uk, blue for Ug', xtitle='t', ytitle='E')
K = gcurve(color=color.green)
Uk = gcurve(color=color.red)
Ug = gcurve(color=color.blue)
total = gcurve(color=color.black)
    
ball.pos = vector(0, -L, 0)     #球在t=0時的位置
ball.v = vector(0, 0, 0)        #球初速
spring.pos = vector(0, 0, 0)    #彈簧頭端的位置

v_vector = arrow(shaftwidth = 0.02, color=color.green)
Ftot_vector = arrow(shaftwidth = 0.02, color=color.red)
mg_vector = arrow(shaftwidth = 0.02, color=color.yellow)
Fs_vector = arrow(shaftwidth = 0.02, color=color.white)
X = 0.2
v_text = label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')
Fs_text = label(box = False, opacity = 0, height = 25, color=color.white, text = 'Fs')
mg_text = label(box = False, opacity = 0, height = 25, color=color.yellow, text = 'Fg')
Ftot_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'F_tot')

dt = 0.001
t=0

while True:
    rate(1/dt)
    spring.axis = ball.pos - spring.pos           #彈簧的軸方向，由頭端指向尾端的距離向量
    ball.a = (Fg + SpringForce(spring.axis,L))/m  #球的加速度由重力和彈力所造成
    ball.v += ball.a*dt      #球的速度
    ball.pos += ball.v*dt    #球的位置
    
    v_vector.pos = ball.pos + vector(2.5*size,0,0)      #將速度箭頭設定在球的右方2.5size處
    Ftot_vector.pos = ball.pos + vector(-2.5*size,0,0)  #將合力箭頭設定在球的左方2.5size處
    mg_vector.pos = ball.pos    #將重力箭頭設定在球上
    Fs_vector.pos = ball.pos    #將彈力箭頭設定在球上

    v_vector.axis = ball.v * X                                #設定速度箭頭，將軸方向設定為速度向量
    Ftot_vector.axis = (Fg + SpringForce(spring.axis,L)) * X  #設定合力箭頭，將軸方向設定為合力向量
    mg_vector.axis = Fg * X                                   #設定重力箭頭，將軸方向設定為重力向量
    Fs_vector.axis = SpringForce(spring.axis,L) * X    
    
    v_text.pos = v_vector.pos + v_vector.axis*1.2
    Ftot_text.pos = Ftot_vector.pos + Ftot_vector.axis*1.2
    mg_text.pos = mg_vector.pos + mg_vector.axis*1.2
    Fs_text.pos = Fs_vector.pos + Fs_vector.axis*1.2
    
    k1=0.5 * m * mag(ball.v)**2
    uk=0.5 * k * (mag(spring.axis) - L)**2
    K.plot(pos=(t, k1))
    Uk.plot(pos=(t, uk))
    Ug.plot(pos=(t, m*g*(ball.pos.y+L)))
    total.plot(pos=(t, k1+uk+m*g*(ball.pos.y+L)))
    t+=dt