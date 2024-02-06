from vpython import *
#Web VPython 3.2

G = 6.67*10**(-11) ; M = 6*10**31 ; m = 1000  ; t1=0
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 0.001; judge=False; judge1=False; recordv=0; record=0; record1=0; recordv1=0; repose=vector(0,0,0); reposv=vector(0,0,0)
v0 = (G * M / H)**0.5
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)

"""
    2. 畫面設定
"""
scene = canvas(align = 'left', width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
sun = sphere(pos=vec(0,0,0), radius=Re, color=color.yellow) #放置物件地球 
earth= sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
earthv = vec(0,0.7*((G*M/H)**0.5),0) #衛星速率=0
venus = sphere(pos=vec(0.7*H,0,0), radius=0.1*Re,color=color.blue, make_trail=True) #放置物件衛星
venusv = vec(0,0.7*((G*M/H/0.7)**0.5),0) #衛星速率=0
Fe = G*M*m/Re**2 #定義地球表面重力強度
pre_earth_pos = earth.pos
pre_venus_pos = venus.pos
"""
    3. 執行迴圈
"""
while True:  #執行迴圈
    rate(5000)
    """print(earthv)
    print(venusv)"""
    dist = ((earth.pos.x-sun.pos.x)**2+(earth.pos.y-sun.pos.y)**2+(earth.pos.z-sun.pos.z)**2)**0.5 #距離純量
    radiavector = (earth.pos-sun.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量

    dist1 = ((venus.pos.x-sun.pos.x)**2+(venus.pos.y-sun.pos.y)**2+(venus.pos.z-sun.pos.z)**2)**0.5 #距離純量
    radiavector1 = (venus.pos-sun.pos)/dist1 #距離單位向量
    Fg1_vector = Fg(dist1)*radiavector1 # 萬有引力向量=萬有引力量值*單位向量
    
    pre_pre_earth_pos = pre_earth_pos
    pre_earth_pos = earth.pos
    earthv += Fg_vector/m*dt   #Δv = F/m *dt
    earth.pos = earth.pos + earthv*dt  # S = S0 + v *dt
    
    pre_pre_venus_pos = pre_venus_pos
    pre_venus_pos = venus.pos
    venusv += Fg1_vector/m*dt   #Δv = F/m *dt
    venus.pos = venus.pos + venusv*dt  # S = S0 + v *dt    
    if pre_earth_pos.x > pre_pre_earth_pos.x and pre_earth_pos.x > earth.pos.x :
        record=t1
        judge=True
        repose = pre_earth_pos
    if pre_earth_pos.x < pre_pre_earth_pos.x and pre_earth_pos.x < earth.pos.x and judge:
        record1=t1
        T = (record1-record)*2
        print('earth T:', T)
        a=pre_earth_pos - repose
        print('earth a**3/T**2:', mag(a)**3/(record1-record)**2)
    if pre_venus_pos.x > pre_pre_venus_pos.x and pre_venus_pos.x > venus.pos.x :
        recordv=t1
        judge1=True
        reposv = pre_venus_pos
    if pre_venus_pos.x < pre_pre_venus_pos.x and pre_venus_pos.x < venus.pos.x and judge1:
        recordv1=t1
        T = (recordv1-recordv)*2
        print('venus:', T)
        a=pre_venus_pos - reposv
        print('venus a**3/T**2:', mag(a)**3/(recordv1-recordv)**2)
    t1 += dt
    t+=dt