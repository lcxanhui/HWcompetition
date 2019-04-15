import numpy as np
inf = 999999

class Path():
    def __init__(self, data_road, data_cross):
        self.data_road = data_road
        self.data_cross = data_cross
#        self.road_num = len(data_road)
        self.cross_num = len(data_cross)
        #建立路径字典
        self.cross_path = dict()
        #建立邻接表，初始化为inf
        self.adj = np.empty([self.cross_num, self.cross_num], dtype='int32')
        self.adj.fill(inf)
        #对角线值为0
        for num in range(self.cross_num):
            self.adj[num][num] = 0
        #路口Id到index映射
        self.id2index = dict()
        for index in range(self.cross_num):
            self.id2index[self.data_cross[index].crossId] = index
        for data in data_road:
            self.adj[self.id2index[data.startId]][self.id2index[data.endId]] = data.roadLength
            if data.isDuplex == '1':
                self.adj[self.id2index[data.endId]][self.id2index[data.startId]] = data.roadLength


    def dijkstra(self, cross_startId, cross_endId):
        start2end = cross_startId + 'to' + cross_endId
        if start2end in self.cross_path.keys():
            return self.cross_path[start2end]
        start_index = self.id2index[cross_startId]
        end_index = self.id2index[cross_endId]
        distance = self.adj[start_index].tolist()         #与cross_startId距离矩阵
        temp_distance = distance.copy()
        temp_distance[start_index] = inf
        min_distance = min(temp_distance)
        temp_path = list(range(self.cross_num))           #存储最小路径经过的路口
        while min_distance != inf:
            min_index = temp_distance.index(min_distance)
            if min_index == end_index:
                break
            for index in range(self.cross_num):
                if distance[index] > min_distance + self.adj[min_index][index]:
                    distance[index] = min_distance + self.adj[min_index][index]
                    temp_path[index] = min_index
                    temp_distance[index]= distance[index]
                    # print(index, min_index)
            temp_distance[min_index] = inf
            min_distance = min(temp_distance)
        # min_path = np.array([self.data_cross[end_index]])
        min_path = [self.data_cross[end_index]]
        through_path = temp_path[end_index]
        while through_path != temp_path[through_path]:
            min_path.append(self.data_cross[through_path])
            # np.append(min_path, self.data_cross[through_path])
            through_path = temp_path[through_path]
        min_path.append(self.data_cross[through_path])
        min_path.append(self.data_cross[start_index])
        # np.append(min_path, self.data_cross[through_path])
        # np.append(min_path, self.data_cross[start_index])
        min_path = min_path[::-1]
        self.cross_path[start2end] = min_path
        return min_path

