from vpython import*

size=0.2
scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))
x = arrow(pos=vector(0,10,0), axis=vector(10,0,0), shaftwidth=0.1, color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,20,0), shaftwidth=0.1, color=color.red)
z = arrow(pos=vector(0,10,0), axis=vector(0,0,10), shaftwidth=0.1, color=color.blue)

ball = sphere(radius=size, color=color.yellow, pos=vector(0,10,0), v=vector(3,0,0))


dt = 0.001    
t = 0.0        
ax = -1
ay = -0.5

while t<=6:          
    rate(1/dt)      
    t = t+dt  
    plot_t = t % 0.4
    ball.v.x += ax*dt
    ball.v.y += ay*dt
    ball.pos = ball.pos + ball.v*dt 
    if ball.v.x > 0 and ball.v.x + ax*dt < 0:
        print ("x max point time=", t)
        print ("x max point position=(", ball.pos.x, ",", ball.pos.y, ")")
        print ("x max point velocity=(", ball.v.x, ",", ball.v.y, ",", ball.v.z, ")")
    if plot_t + dt >= 0.4 and plot_t < 0.4:
        v=arrow(pos=vector(ball.pos.x,ball.pos.y,ball.pos.z), axis=vector(ball.v.x,ball.v.y,ball.v.z), shaftwidth=0.05, color=color.green)
        a=arrow(pos=vector(ball.pos.x,ball.pos.y,ball.pos.z), axis=vector(-1, -0.5, 0), shaftwidth=0.05, color=color.red)
        ball1 = sphere(radius=size, color=color.yellow, pos=vector(ball.pos.x, ball.pos.y, ball.pos.z))
