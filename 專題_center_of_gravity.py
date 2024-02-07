from vpython import*
def calculate_g_1(boxlist):
    return [sum([b.pos.x for b in boxlist if b.texture!=textures.wood])/(len(boxlist)-1),
            sum([b.pos.y for b in boxlist if b.texture!=textures.wood])/(len(boxlist)-1),
            sum([b.pos.z for b in boxlist if b.texture!=textures.wood])/(len(boxlist)-1)]

def calculate_g_2(boxlist):
    return [sum([b.pos.x for b in boxlist])/len(boxlist),
            sum([b.pos.y for b in boxlist])/len(boxlist)-1,
            sum([b.pos.z for b in boxlist])/len(boxlist)-1]

def check(boxlist):
    totalheight=boxlist[len(boxlist)-1].pos.y
    startpoint=len(boxlist)-1
    flag=0
    while startpoint>=0 and flag==0:
        while boxlist[startpoint].pos.y>=totalheight-10:
            startpoint-=1
        stoppoint=startpoint
        try:
            while boxlist[stoppoint].pos.y==boxlist[startpoint].pos.y:
                stoppoint-=1
        except:
            stoppoint=-1
        stoppoint+=1
        g1=calculate_g_1(boxlist[startpoint+1:])
        g2=calculate_g_2(boxlist[startpoint+1:])
        if boxlist[startpoint].length<boxlist[startpoint].width:
            if boxlist[stoppoint].pos.x-5<g1[0]<boxlist[startpoint].pos.x+5:
                flag=0
            else:
                flag=1
                break
            if boxlist[stoppoint].pos.x-5<g2[0]<boxlist[startpoint].pos.x+5:
                flag=0
            else:
                flag=2
                break
        elif boxlist[startpoint].length>boxlist[startpoint].width:
            if boxlist[stoppoint].pos.z-5<g1[2]<boxlist[startpoint].pos.z+5:
                flag=0
            else:
                flag=1
                break
            if boxlist[stoppoint].pos.z-5<g2[2]<boxlist[startpoint].pos.z+5:
                flag=0
            else:
                flag=2
                break
        startpoint=stoppoint-1
    if flag==0:
        return 'True'
    elif flag==1:
        return 'False1'
    elif flag==2:
        return 'False2'
'''
for i in range(len(boxlist)-1,0,-1):
    if boxlist[i].texture!=textures.granite:
        boxlist[i].texture=textures.granite
        break

while check(boxlist)=='False1' or check(boxlist)=='False2':
    move_place=0
    for i in range(len(boxlist))-1,0,-1):
        if boxlist[i].texture!=textures.granite:
            move_place=i
            break
    if boxlist[move_place].length<boxlist[move_place].width:
        boxlist[move_place].pos.x=0
    elif boxlist[move_place].length>boxlist[move+place].width:
        boxlist[(move_place].pos.z=0
'''
