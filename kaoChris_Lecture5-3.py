from vpython import *
#Web VPython 3.2

G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1; T=0; record = 0
v0 = (G * M / H)**0.5
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)

"""
    2. 畫面設定
"""
scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
materv = vec(0,0.7*v0,0) #衛星速率=0
Fe = G*M*m/Re**2 #定義地球表面重力強度
pre_mater_pos = vector(0,0,0)
"""
    3. 執行迴圈
"""
while True:  #執行迴圈
    rate(5000)
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector = (mater.pos-earth.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量
    pre_pre_mater_pos = pre_mater_pos
    pre_mater_pos = mater.pos
    materv += Fg_vector/m*dt   #Δv = F/m *dt
    mater.pos = mater.pos + materv*dt  # S = S0 + v *dt
    U = -G * M *m / dist
    K = 0.5 * m * mag(materv)**2
    """f1.plot( pos=(t, U))
    f2.plot(pos=(t, K))
    total.plot(pos=(t, U+K))"""
    t = t+dt
    T += dt
    if pre_mater_pos.x > pre_pre_mater_pos.x and pre_mater_pos.x > mater.pos.x :
        if record == 0:
            record = T
        else:
            print(T-record)
            T=0
            record=0
    """if pre_mater_pos.x < pre_pre_mater_pos.x and pre_mater_pos.x < mater.pos.x : 
      print (mater.pos) #印出左端點
    if pre_mater_pos.y > pre_pre_mater_pos.y and pre_mater_pos.y > mater.pos.y :
      print (mater.pos) #印出上端點
    if pre_mater_pos.y < pre_pre_mater_pos.y and pre_mater_pos.y < mater.pos.y :
      print (mater.pos) #印出下端點"""
