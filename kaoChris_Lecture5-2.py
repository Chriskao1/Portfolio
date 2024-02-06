from vpython import *
#Web VPython 3.2

G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1
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
mater1 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.blue, make_trail=True) #放置物件衛星
mater1v = vec(0,0.9*v0,0) #衛星速率=0
mater2 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.green, make_trail=True) #放置物件衛星
mater2v = vec(0,0.8*v0,0) #衛星速率=0
gd = graph(align='left',width=400,height=400,  #設定X-t繪圖視窗
              title='U+K=E', xtitle='t', ytitle='E)',
              foreground=color.black,background=color.white)
f1 = gcurve(color=color.red)  #定義曲線
f2 = gcurve(color=color.green)
total = gcurve(color=color.black)
Fe = G*M*m/Re**2 #定義地球表面重力強度
"""
    3. 執行迴圈
"""
while True:  #執行迴圈
    rate(5000)
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector = (mater.pos-earth.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量
    dist1 = ((mater1.pos.x-earth.pos.x)**2+(mater1.pos.y-earth.pos.y)**2+(mater1.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector1 = (mater1.pos-earth.pos)/dist1 #距離單位向量
    Fg1_vector = Fg(dist1)*radiavector1 # 萬有引力向量=萬有引力量值*單位向量
    dist2 = ((mater2.pos.x-earth.pos.x)**2+(mater2.pos.y-earth.pos.y)**2+(mater2.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector2 = (mater2.pos-earth.pos)/dist2#距離單位向量
    Fg2_vector = Fg(dist2)*radiavector2 # 萬有引力向量=萬有引力量值*單位向量
    materv += Fg_vector/m*dt   #Δv = F/m *dt
    mater.pos = mater.pos + materv*dt  # S = S0 + v *dt
    mater1v += Fg1_vector/m*dt   #Δv = F/m *dt
    mater1.pos = mater1.pos + mater1v*dt  # S = S0 + v *dt    
    mater2v += Fg2_vector/m*dt   #Δv = F/m *dt
    mater2.pos = mater2.pos + mater2v*dt  # S = S0 + v *dt
    """U = -G * M *m / dist
    K = 0.5 * m * mag(materv)**2
    f1.plot( pos=(t, U))
    f2.plot(pos=(t, K))
    total.plot(pos=(t, U+K))
    t = t+dt"""
"""
    4.當衛星碰觸地球表面，則衛星停止不動
"""
while True:  
    rate(1000)
    materv = vector(0,0,0)
    mater.pos = mater.pos