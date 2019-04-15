import numpy as np
inf = 999999
from load_save_data import *


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
        adj[id2index[data.startId]][id2index[data.endId]] = 3
        if data.isDuplex == '1':
            adj[id2index[data.startId]][id2index[data.endId]] = 2
            adj[id2index[data.endId]][id2index[data.startId]] = 2
            if data.laneNum == 1:
                adj[id2index[data.startId]][id2index[data.endId]] = 3
                adj[id2index[data.endId]][id2index[data.startId]] = 3

            if data.laneNum > 3:
                adj[id2index[data.startId]][id2index[data.endId]] = 1
                adj[id2index[data.endId]][id2index[data.startId]] = 1
    if crossId != '':
        id = crossId.split('_')
        adj[id2index[id[0]]][id2index[id[1]]] = 3
        # if data.laneNum > 3:
        #     adj[id2index[data.startId]][id2index[data.endId]] = 1
        #     if data.isDuplex == '1':
        #         adj[id2index[data.endId]][id2index[data.startId]] = 1
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



def shorest_path(data_cross, path, start_index, end_index):
    temp_path = path[start_index][end_index]
    min_path = list()
    min_path.append(data_cross[start_index])
    while temp_path != end_index:
        min_path.append(data_cross[temp_path])
        temp_path = path[temp_path][end_index]
    min_path.append(data_cross[temp_path])
    return min_path

if __name__ == "__main__":
    car_path = './1-map-training-1/car.txt'
    road_path = './1-map-training-1/road.txt'
    cross_path = './1-map-training-1/cross.txt'
    answer_path = './1-map-training-1/answer.txt'
    data_road, data_car, data_cross = load_data(road_path, car_path, cross_path)
    path, id2index = dijkstra(data_road, data_cross)
    start_index = id2index['12']
    end_index = id2index['54']
    min_path = shorest_path(data_cross, path, start_index, end_index)
    print('over')
    # start_index = id2index['1']
    # end_index = id2index['51']
    # start_path = start_index
    # # temp_path = path[start_index]
    # # min_path = list()
    # # min_path.append(data_cross[end_index])
    # # through_path = temp_path[end_index]
    # # while temp_path[through_path] != through_path:
    # #     min_path.append(data_cross[through_path])
    # #
    # # min_path.append(data_cross[start_index])
    # # min_path.append(data_cross[start_index])
    # # min_path = min_path[::-1]
    # temp_path = path[start_index][end_index]
    # min_path = list()
    # min_path.append(data_cross[start_index])
    # temp_road = []
    # # flag = 0
    # while temp_path != end_index:
    #     # for i in data_cross[start_path].allRoad:
    #     #     for j in data_cross[temp_path].allRoad:
    #     #         if i is not '-1':
    #     #             if i == j:
    #     #                 temp_road = i
    #     #                 flag = 1
    #     #                 break
    #     #     if flag == 1:
    #     #         flag =0
    #     #         break
    #     # min_path.append(temp_road)
    #     # start_path = temp_path
    #     # temp_path = path[temp_path][end_index]
    #     min_path.append(data_cross[temp_path])
    #     temp_path = path[temp_path][end_index]
    # # for i in data_cross[start_path].allRoad:
    # #     #     for j in data_cross[temp_path].allRoad:
    # #     #         if i is not '-1':
    # #     #             if i == j:
    # #     #                 temp_road = i
    # #     #                 flag = 1
    # #     #                 break
    # #     #     if flag == 1:
    # #     #         flag = 0
    # #     #         break
    # #     # min_path.append(temp_road)
    # min_path.append(data_cross[temp_path])
    # print('over')
