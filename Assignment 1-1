from vpython import*

size=1
scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))
x = arrow(pos=vector(0,0,0), axis=vector(10,0,0), shaftwidth=1, color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,25,0), shaftwidth=1, color=color.red)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,10), shaftwidth=1, color=color.blue)

gdx=graph(title="x-t plot", width=600, height=400, xtitle="t", ytitle="x")
linex = gcurve(color=color.blue)
gdv=graph(title="v-t plot", width=600, height=400, xtitle="t", ytitle="v")
linev = gcurve(color=color.blue)
gda=graph(title="a-t plot", width=600, height=400, xtitle="t", ytitle="a")
linea = gcurve(color=color.blue)

ball = sphere(radius=size, color=color.yellow, pos=vector(0,0,0), v=vector(1,0,0))

dt = 0.001    
t = 0.0    	
a=0

while t<=6:          
    rate(1/dt)      
    t = t+dt  
    if t < 2:
        a=5
    else:
        a=-5
    ball.v.y += a*dt
    ball.pos = ball.pos + ball.v*dt 
    linex.plot(pos=(t,ball.pos.y))
    linev.plot(pos=(t,ball.v.y))
    linea.plot(pos=(t,a))
    if ball.v.y > 0 and ball.v.y + a*dt < 0:
        print ("turning point time=", t)
        print ("turning point position=", ball.pos.y)
        print ("turning point velocity=", ball.v.y)
