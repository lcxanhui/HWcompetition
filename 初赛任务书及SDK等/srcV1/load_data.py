#import os
import re
from shortest_path import  Path

class kindError(Exception):   #自定义异常类,所有与车辆状态错误导致的异常
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo


# 道路类
class Road(object):
    def __init__(self, roadId, roadLength, maxSpeed, laneNum, startId, endId, isDuplex):
        self.roadId = roadId
        self.roadLength = roadLength
        self.maxSpeed = maxSpeed
        self.laneNum = laneNum
        self.startId = startId
        self.endId = endId
        self.isDuplex = isDuplex
    def __str__(self):
        return str('(' + self.roadId + ','
                   + str(self.roadLength) + ','
                   + str(self.maxSpeed) + ','
                   + str(self.laneNum) + ','
                   + self.startId + ','
                   + self.endId + ','
                   + self.isDuplex + ')')

# 车辆类
class Car(object):
    def __init__(self, carId, startId, endId, maxSpeed, startTime):
        self.carId = carId
        self.startId = startId
        self.endId = endId
        self.maxSpeed = maxSpeed
        self.startTime = startTime
    def __str__(self):
        return str('(' + self.carId + ','
                   + self.startId + ','
                   + self.endId + ','
                   + str(self.maxSpeed) + ','
                   + str(self.startTime) + ')')

# 路口类
class Cross(object):
    def __init__(self, crossId, upId, rightId, downId, leftId):
        self.crossId = crossId
        self.upId = upId
        self.rightId = rightId
        self.downId = downId
        self.leftId = leftId

    def __str__(self):
        return str('(' + self.crossId + ','
                   + self.upId + ','
                   + self.rightId + ','
                   + self.downId + ','
                   + self.leftId + ')')

# 读取数据
class load_data(object):
    def __init__(self, road, car, cross):
        self.__road = road #os.path.join('./', road)
        self.__car = car #os.path.join('./', car)
        self.__cross = cross #os.path.join('./', cross)
    
    def load_road(self):
        with open(self.__road, 'r') as road_file:
            pattern = r'.*?([0-9]+).*?([0-9]+).*?([0-9]+).*?([0-9]+).*?([0-9]+).*?([0-9]+).*?([0-9]+).*?'
            road_read = road_file.read()
            result = re.findall(pattern, road_read)
            data_road = list()
            for data in result:
                data_road.append(Road(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
            return data_road
        
    def load_car(self):
        with open(self.__car, 'r') as car_file:
            pattern = r'.*?([0-9]+).*?([0-9]+).*?([0-9]+).*?([0-9]+).*?([0-9]+).*?'
            car_read = car_file.read()
            result = re.findall(pattern, car_read)
            data_car = list()
            for data in result:
                data_car.append(Car(data[0], data[1], data[2], int(data[3]), int(data[4])))
            return data_car

    def load_cross(self):
        with open(self.__cross, 'r') as cross_file:
            pattern = r'.*?([0-9]+).*?([0-9\-]+).*?([0-9\-]+).*?([0-9\-]+).*?([0-9\-]+).*?'
            cross_read = cross_file.read()
            result = re.findall(pattern, cross_read)
            data_cross = list()
            for data in result:
                data_cross.append(Cross(data[0], data[1], data[2], data[3], data[4]))
            return data_cross

if __name__ == '__main__':
    carPath = './config-4/car.txt'
    roadPath = './config-4/road.txt'
    crossPath = './config-4/cross.txt'
# reader = load_data(roadPath, carPath, crossPath)
# car_list = reader.load_car()
# road_list = reader.load_road()
# cross_list = reader.load_cross()
# shorestPath = Path(road_list, cross_list)
# path_temp = shorestPath.dijkstra('13','54')
# print(path_temp)

