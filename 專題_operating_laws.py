from vpython import *
#Web VPython 3.2
def g_special(boxlist,take_layer,third):
    return [(sum([b.pos.x for b in boxlist[third+1:]])+boxlist[take_layer].pos.x)/(len(boxlist[third+1:])+1),
                (sum([b.pos.z for b in boxlist[third+1:]])+boxlist[take_layer].pos.z)/(len(boxlist[third+1:])+1)]
'''
    if len(toplayer_list) == 3:
        start_layer -= 2
    else:
    '''
def take_place(boxlist,H,toplayer):
    layer_list = []
    toplayer_list = []
    for i in range(30):
        layer_list.append(boxlist[i].pos.y / H)
        if layer_list[i] == toplayer-1:
            toplayer_list.append(layer_list[i])
    start_layer = toplayer-1
    start_layer -= 2
    while start_layer != -1:
        judge = []
        for i in range(30):
            if layer_list[i] == start_layer:
                judge.append(i)
        if len(judge) == 3:
            return judge[0]
            break
        elif len(judge) == 2:
            return judge[1]
            break
        else:
            start_layer -= 1
    if start_layer == -1:
        return -1

def put_place(boxlist,take_layer,placement,toplayer):
    if take_layer == -1:
        return 0
    else:
        right = 0
        if (toplayer-1)%2 != (boxlist[take_layer].pos.y/10)%2:
            a = boxlist[take_layer].length
            boxlist[take_layer].length = boxlist[take_layer].width
            boxlist[take_layer].width = a
        if toplayer%2 == 1:
            if len(placement[0]) == 1:
                boxlist[take_layer].pos = vec(placement[0][0],(toplayer-1)*10,0)
            elif len(placement[0]) == 2:
                distance=dict()
                for i in range(2):
                    boxlist[take_layer].pos = vec(placement[0][i],(toplayer-1)*10,0)
                    third=0
                    fourth=0
                    for m in range(len(boxlist)-1,0,-1):
                        if boxlist[m].pos.y<(toplayer-3)*10:
                            fourth=m
                            break
                        elif boxlist[m].pos.y<(toplayer-2)*10 and third==0:
                            third=m
                    if third+1!=take_layer:
                        g=g_special(boxlist,take_layer,third)
                    else:
                        g=g_special(boxlist,take_layer,third+1)
                    if fourth+1!=take_layer:
                        x_middle=(boxlist[fourth+1].pos.x+boxlist[third].pos.x)/2
                    else:
                        x_middle=(boxlist[fourth+2].pos.x+boxlist[third].pos.x)/2
                    distance[round(abs(g[0]-x_middle))]=placement[0][i]
                if len(list(distance.keys()))==1:
                     boxlist[take_layer].pos = vec(placement[0][0],(toplayer-1)*10,0)
                else:
                    short=min(list(distance.keys()))
                    boxlist[take_layer].pos = vec(distance[short],(toplayer-1)*10,0)
            else:
                find = []
                for i in range(30):
                    if boxlist[i].pos.y == (toplayer-3)*10 and i != take_layer:
                        if (toplayer-3)%2 == 0:
                            find.append(boxlist[i].pos.x)
                        else:
                            find.append(boxlist[i].pos.z)
                if -10 in find:
                    boxlist[take_layer].pos = vec(-10,(toplayer-1)*10,0)
                elif 10 in find:
                    boxlist[take_layer].pos = vec(10,(toplayer-1)*10,0)
            for i in range(30):
                if boxlist[i].pos.y == boxlist[take_layer].pos.y and boxlist[i].pos.x > boxlist[take_layer].pos.x:
                    right +=1
        else:
            if len(placement[0]) == 1:
                boxlist[take_layer].pos = vec(0,(toplayer-1)*10,placement[0][0])
            elif len(placement[0]) == 2:
                distance=dict()
                for i in range(2):
                    boxlist[take_layer].pos = vec(0,(toplayer-1)*10,placement[0][i])
                    third=0
                    fourth=0
                    for m in range(29,0,-1):
                        if boxlist[m].pos.y<(toplayer-3)*10:
                            fourth=m
                            break
                        elif boxlist[m].pos.y<(toplayer-2)*10 and third==0:
                            third=m
                    if third+1!=take_layer:
                        g=g_special(boxlist,take_layer,third)
                    else:
                        g=g_special(boxlist,take_layer,third+1)
                    if fourth+1!=take_layer:
                        z_middle=(boxlist[fourth+1].pos.z+boxlist[third].pos.z)/2
                    else:
                        z_middle=(boxlist[fourth+2].pos.z+boxlist[third].pos.z)/2
                    distance[round(abs(g[1]-z_middle))]=placement[0][i]
                if len(list(distance.keys()))==1:
                     boxlist[take_layer].pos = vec(0,(toplayer-1)*10,placement[0][0])
                else:
                    short=min(list(distance.keys()))
                    boxlist[take_layer].pos = vec(0,(toplayer-1)*10,distance[short]) 
            else:
                find = []
                for i in range(30):
                    if boxlist[i].pos.y == (toplayer-3)*10 and i != take_layer:
                        if (toplayer-3)%2 == 0:
                            find.append(boxlist[i].pos.x)
                        else:
                            find.append(boxlist[i].pos.z)
                if -10 in find:
                    boxlist[take_layer].pos = vec(0,(toplayer-1)*10,-10)
                elif 10 in find:
                    boxlist[take_layer].pos = vec(0,(toplayer-1)*10,10)
            for i in range(30):
                if boxlist[i].pos.y == boxlist[take_layer].pos.y and boxlist[i].pos.z > boxlist[take_layer].pos.z:
                    right +=1
        boxlist[take_layer].texture = textures.wood_old
        move_box = boxlist.pop(take_layer)
        boxlist.insert(29-right,move_box)
        '''print(take_layer, boxlist[29-right].pos)'''
