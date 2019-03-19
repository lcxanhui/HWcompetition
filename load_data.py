import os
import re

# 道路类初始化
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

# 车辆类初始化
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

# 路口类初始化
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
                data_car.append(Car(data[0], data[1], data[2], data[3], data[4]))
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
	roadPath = '../config_6/road.txt'
	carPath = '../config_6/car.txt'
	crossPath = '../config_6/cross.txt'
	data = load_data(roadPath, carPath, crossPath)
#	for obj in data.load_cross():
#		print(obj)

