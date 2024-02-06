from vpython import *
#Web VPython 3.2

size = 0.5               
scene = canvas(width=600, height=600, center=vector(0, 5, 0))  # 設定畫面
floor = box(length=50, height=0.01, width=10, color=color.blue)  # 畫地板
ball = sphere(radius=size, color=color.yellow, make_trail=True, trail_type="points")
r = graph(title="theta-R plot", width=600, height=400, xtitle="theta", ytitle="R")
liner = gcurve(color=color.blue)
time_graph = graph(title="theta-T plot", width=600, height=400, xtitle="theta", ytitle="T")
linet = gcurve(color=color.blue)
show_angle = label(pos=vector(0, -7 * size, 0), box=False, height=20, color=color.yellow)

ball.pos = vector(0, size, 0)
theta = 3 * pi / 180
ball.v = vector(10 * cos(theta), 10 * sin(theta), 0)
dt = 0.001
time = 0

while theta <= pi:
    show_angle.text = f'Theta: {theta/pi*180:.2f} degrees'
    while ball.pos.y >= size:
        rate(1/dt)
        ball.pos += ball.v * dt
        ball.v.y -= 9.8 * dt
        time += dt
    liner.plot(pos=(theta, ball.pos.x))
    linet.plot(pos=(theta, time))
    print('T=', time, 'theta=', theta * 180 / pi, 'R=', ball.pos.x)
    theta += 3 * pi / 180
    ball.pos = vector(0, size, 0)
    ball.v = vector(10 * cos(theta), 10 * sin(theta), 0)
