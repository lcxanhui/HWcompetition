import numpy as np
inf = 999999

# 创建邻接矩阵
def floyd(data_road, data_cross, crossId):
    cross_num = len(data_cross)
    adj = np.empty([cross_num, cross_num], dtype='int32')
    adj.fill(inf)
    # 对角线值为0
    for num in range(cross_num):
        adj[num][num] = 0
    # 路口Id到index映射
    id2index = dict()
    for index in range(cross_num):
        id2index[data_cross[index].crossId] = index
    for data in data_road:

        if data.isDuplex == '1':
            if data.laneNum == 1:
                adj[id2index[data.startId]][id2index[data.endId]] = 3
                adj[id2index[data.endId]][id2index[data.startId]] = 3
            elif data.laneNum > 2:
                adj[id2index[data.startId]][id2index[data.endId]] = 1
                adj[id2index[data.endId]][id2index[data.startId]] = 1
            else:
                adj[id2index[data.startId]][id2index[data.endId]] = 2
                adj[id2index[data.endId]][id2index[data.startId]] = 2
        else:
            adj[id2index[data.startId]][id2index[data.endId]] = 3
    if crossId != '':
        id = crossId.split('_')
        adj[id2index[id[0]]][id2index[id[1]]] = 3
    # 创建路径矩阵
    path = np.array([range(cross_num)])
    for i in range(cross_num - 1):
        path = np.append(path, [range(cross_num)], axis=0)
    # 求最短路径
    for i in range(cross_num):
        for j in range(cross_num):
            for k in range(cross_num):
                if adj[j][k] > adj[j][i] + adj[i][k]:
                    adj[j][k] = adj[j][i] + adj[i][k]
                    path[j][k] = path[j][i]
    return path, id2index


def shortest_path(data_cross, path, start_index, end_index):
    temp_path = path[start_index][end_index]
    min_path = list()
    min_path.append(data_cross[start_index].crossId)
    while temp_path != end_index:
        min_path.append(data_cross[temp_path].crossId)
        temp_path = path[temp_path][end_index]
    min_path.append(data_cross[temp_path].crossId)
    return min_path
