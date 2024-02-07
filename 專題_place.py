from vpython import *
#Web VPython 3.2
def layer_move(do_times, origin_toplayer):
    a = int((do_times)/3)
    origin_toplayer += a+1
    return origin_toplayer

def placement(toplayer,boxlist,H):
    height = (toplayer-1)*H
    record_index = []
    record_num = 0
    index_list = [-10,0,10]
    for i in range(29,-1,-1):
        if toplayer%2 == 1:
            if boxlist[i].pos.y == height:
                record_index.append(boxlist[i].pos.x)
                record_num += 1
            else:
                break
        else:
            if boxlist[i].pos.y == height:
                record_index.append(boxlist[i].pos.z)
                record_num += 1
            else:
                break
    
    for i in range(record_num):
        index_list.remove(record_index[i])
    if index_list == []:
        index_list = [-10,0,10]
        toplayer += 1
    return index_list, toplayer
 
