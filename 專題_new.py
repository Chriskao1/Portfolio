from vpython import *
#Web VPython 3.2
from 專題_center_of_gravity import*
from 專題_operating_laws import*
from 專題_place import*
'''1.設定&蓋塔'''
L=10;W=30;H=10;t=0;dt=0.00001;do_times=0
scene = canvas(width=600, height=600,background=color.white,center=vector(0,150,0))
floor = box(pos=vector(0,(-H/2)-2.5,0),length=100, height=5, width=100, texture=textures.granite)
local_light(pos=vec(-100,150,100), color=color.white)
boxlist=[]
for i in range(0,10):
    for j in range(-1,2):
        if i%2==0:
            boxlist.append(box(pos=vector(j*L,i*H,0),length=L,height=H,width=W, texture=textures.wood))
        elif i%2==1:
            boxlist.append(box(pos=vector(0,i*H,j*L),length=W,height=H,width=L, texture=textures.wood))
            
'''2.迴圈'''
while True:
    rate(1)
    if check(boxlist)=='False1' or check(boxlist)=='False2':
        move_place=0
        for i in range(len(boxlist)-1,len(boxlist)-4,-1):
            if boxlist[i].texture!=textures.wood:
                move_place=i
                break
        if boxlist[move_place].length<boxlist[move_place].width:
            boxlist[move_place].pos.x=0
        elif boxlist[move_place].length>boxlist[move_place].width:
            boxlist[move_place].pos.z=0
    else:
        for i in range(len(boxlist)-1,len(boxlist)-4,-1):
            if boxlist[i].texture!=textures.wood:
                boxlist[i].texture=textures.wood
                break
        toplayer = layer_move(do_times,10)
        place = placement(toplayer,boxlist,H)
        take = take_place(boxlist,H,toplayer)
        if take==-1:
            break
        else:
            put_place(boxlist,take,place,toplayer)
            do_times+=1
            t+=dt
print(do_times)
