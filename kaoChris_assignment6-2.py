from vpython import *
#Web VPython 3.2
G = 6.67*10**(-11) ; m1 = 1.9891*10**30; m2 = 5.9742*10**24; m3 = 7.342*10**22; r1 = 6.955*10**8; r2 = 6.3728*10**6; r3 = 1.7371*10**6 
R_12 = 1.496*10**11 ;R_23 = 3.84399*10**8; t = 0 ; dt = 100
v2 = (G*m1/R_12)**0.5; v3 = (G*m2/R_23)**0.5 
t1 = 0 ; t2 = 0 ; t3 = 0  #t1給地球算週期 ; t2給月球算週期

#設定前太陽地球相對位置向量
pre_m1m2_rv = vector(0,0,0)
radiavector_12 = vector(0,0,0)

#設定前地球月球相對位置向量
pre_m2m3_rv = vector(0,0,0)
radiavector_23 = vector(0,0,0)

def Fg(x,y1,y2): 
    return -G*y1*y2/(x**2)
"""
    2. 畫面設定
"""
scene = canvas(width=1200, height=800, center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=7*R_23)

ball_m1 = sphere(pos=vector(0,0,0), radius=20*r1, color = color.yellow, make_trail=True)
ball_m2 = sphere(pos=vector(R_12,0,0), radius=20*r2, color = color.blue, make_trail=True)
ball_m3 = sphere(pos=vector(R_12+R_23,0,0), radius=20*r3, color = color.red, make_trail=True)
"""sun = arrow(pos=ball_m3.pos, color=color.yellow, shaftwidth = 0.5)
earth = arrow(pos=ball_m3.pos, color=color.blue, shaftwidth = 0.5)
total = arrow(pos=ball_m3.pos, color=color.black, shaftwidth = 0.5)"""

ball_m1_v = vector(0,0,0) ; ball_m2_v = vector(0,v2,0) ; ball_m3_v = vector(0,v2+v3,0)
"""
    3. 執行迴圈
"""
while True:
    rate(10000)
    # 地球受太陽的力與產生的運動
    scene.center = ball_m2.pos
    pre_pre_m1m2_rv = pre_m1m2_rv
    pre_m1m2_rv = vector(radiavector_12.x , radiavector_12.y,radiavector_12.z)

    #設定前與前前地球月球相對位置向量 
    pre_pre_m2m3_rv = pre_m2m3_rv
    pre_m2m3_rv = vector(radiavector_23.x , radiavector_23.y,radiavector_23.z)
    
    dist_12 = mag(ball_m1.pos-ball_m2.pos) 
    radiavector_12 = (ball_m2.pos-ball_m1.pos)/dist_12
    Fg_12_vector = Fg(dist_12,m1,m2)*radiavector_12
    
    dist_32 = mag(ball_m3.pos - ball_m2.pos)
    radiavector_32 = (ball_m2.pos-ball_m3.pos)/dist_32
    Fg_32_vector = Fg(dist_32,m3,m2)*radiavector_32
    
    ball_m2_v += Fg_12_vector/m2*dt + Fg_32_vector/m2 * dt
    ball_m2.pos = ball_m2.pos + ball_m2_v*dt
    
    dist_23 = mag(ball_m2.pos - ball_m3.pos) 
    radiavector_23 = (ball_m3.pos-ball_m2.pos)/dist_23
    Fg_23_vector = Fg(dist_23,m2,m3)*radiavector_23


    # 月球受太陽的力
    dist_13 = mag(ball_m1.pos - ball_m3.pos) 
    radiavector_13 = (ball_m3.pos - ball_m1.pos)/dist_13
    Fg_13_vector = Fg(dist_13,m1,m3)*radiavector_13
    
    ball_m3_v += (Fg_13_vector+Fg_23_vector)/m3*dt
    ball_m3.pos = ball_m3.pos + ball_m3_v*dt
    ball_m1.pos += ball_m1_v * dt

    t = t+dt ; t1=t1+dt ; t2=t2+dt ; t3+=dt#加入時間t1給地球算週期, 等等t2給月算週期
    
    #找地球相對太陽右端點位置
    if pre_m1m2_rv.x > pre_pre_m1m2_rv.x and pre_m1m2_rv.x > radiavector_12.x :
        earth_T = t1/86400.0 #設定earth_T為地球週期
        print ('earth_t=' , earth_T)
        t1=0 #時間重置

    #找月球相對地球右端點位置
    if pre_m2m3_rv.x > pre_pre_m2m3_rv.x and pre_m2m3_rv.x > radiavector_23.x  :
        moon_T = t2/86400.0 #設定earth_T為地球週期
        print ('moon_T=' , moon_T)
        t2=0 #時間重置
    if mag(pre_m1m2_rv-pre_m2m3_rv) > mag(pre_pre_m1m2_rv-pre_pre_m2m3_rv) and mag(pre_m1m2_rv-pre_m2m3_rv) >  mag(radiavector_12-radiavector_23) :
       moon_T2 = t3/86400.0 #設定moon_T2為月球週期2
       print ('moon_T2=' , moon_T2)
       t3=0 #時間重置