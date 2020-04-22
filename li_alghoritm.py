from queue import *
#Start vars
length=5
start=(0, 0)
finish=(2, 4)
barriers=[(2, 4), (3, 3), (1, 2)]

#build field function
def build(length,start,barriers):
        field = [[0 for i in range(length)] for i in range(length)]
        for b in barriers:
            field[b[0]][b[1]] = -1
        field[start[0]][start[1]] = 1
        print('Current field:')
        for row in field:
            print(*row)

#find path function
def find_path(field,start,finish,length):
        q = Queue()
        q.put(start)
        while not q.empty():
            index = q.get()
            l = (index[0]-1, index[1])
            r = (index[0]+1, index[1])
            u = (index[0], index[1]-1)
            d = (index[0], index[1]+1)

            if l[0] >= 0 and field[l[0]][l[1]] == 0:
                field[l[0]][l[1]] += field[index[0]][index[1]] + 1
                q.put(l)
            if r[0] < length and field[r[0]][r[1]] == 0:
                field[r[0]][r[1]] += field[index[0]][index[1]] + 1
                q.put(r)
            if u[1] >= 0 and field[u[0]][u[1]] == 0:
                field[u[0]][u[1]] += field[index[0]][index[1]] + 1
                q.put(u)
            if d[1] < length and field[d[0]][d[1]] == 0:
                field[d[0]][d[1]] += field[index[0]][index[1]] + 1
                q.put(d)

#function which returns result info about path
def get_path(field,finish):
    if field[finish[0]][finish[1]] == 0 or \
            field[finish[0]][finish[1]] == -1:
        print('Path not found')
        return
    path = []
    item = finish
    while not path.append(item) and item != start:
        l = (item[0]-1, item[1])
        if l[0] >= 0 and field[l[0]][l[1]] == field[item[0]][item[1]] - 1:
            item = l
            continue
        r = (item[0]+1, item[1])
        if r[0] < length and field[r[0]][r[1]] == field[item[0]][item[1]] - 1:
            item = r
            continue
        u = (item[0], item[1]-1)
        if u[1] >= 0 and field[u[0]][u[1]] == field[item[0]][item[1]] - 1:
            item = u
            continue
        d = (item[0], item[1]+1)
        if d[1] < length and field[d[0]][d[1]] == field[item[0]][item[1]] - 1:
            item = d
            continue
    print('Path to finish cell:')
    for p in reversed(path):
        print (p)

build(length,start,barriers)
find_path(field,start,finish,length)
path = get_path(field,finish)
