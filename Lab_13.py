def ford_belman(N,W):
    '''

    :param N: number of vertices
    :param W: dictionary {(start,end):weight}
    :return:
    '''

    INF = 30000
    F = [INF] * N
    F[0] = 0
    Stop = False
    k = 1
    while k < N and not Stop:
        k += 1
        Stop = True
        for j, i in W.keys():
            if F[j] + W[(j, i)] < F[i]:
                F[i] = F[j] + W[(j, i)]
                Stop = False
    return F

def eolymp():
    tmp = input()
    vertices = int(tmp.split()[0])
    verge = int(tmp.split()[1])
    W = {}
    for i in range(verge):
        tmp = input().split()
        start = int(tmp[0])-1
        end = int(tmp[1])-1
        weight = int(tmp[2])
        if start < vertices and end < vertices:
            W[(start,end)] = weight
        else:
            raise Exception
    res = ford_belman(vertices,W)
    prnt = '{} '*vertices
    print(prnt.format(*res))


eolymp()