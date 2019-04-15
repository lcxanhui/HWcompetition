from shortest_path import *


class Manage(object):
	def __init__(self, data_car, data_road, data_cross):
		self.data_car = data_car
		self.data_road = data_road
		self.data_cross = data_cross

		self.use_roadNum = dict()
		self.crossId2roadId = dict()
		self.crossIds = ''
		self.route = dict()  # 开始结束路口到最小路径映射
		self.path, self.id2index = floyd(self.data_road, self.data_cross, self.crossIds)

		for road in self.data_road:
			start2end = road.startId + '_' + road.endId
			self.crossId2roadId[start2end] = road
			if road.isDuplex == '1':
				cross_ids = road.endId + '_' + road.startId
				self.crossId2roadId[cross_ids] = road

		# 车辆按速度排序
		sort_carByv = list()
		car_dictionary = dict()

		for car in self.data_car:
			if car.startId in car_dictionary.keys():
				car_dictionary[car.startId].append(car)
			else:
				car_dictionary[car.startId] = [car]

		key_car = list(car_dictionary.keys())
		max_length = 0
		for key in key_car:
			car_dictionary[key].sort(key=lambda x:(x.planTime, -x.maxSpeed))
			car_num = len(car_dictionary[key])
			if car_num > max_length:
				max_length = car_num

		for i in range(max_length):
			for key in key_car:
				if len(car_dictionary[key]) > i:
					sort_carByv.append(car_dictionary[key][i])
		self.data_car = sort_carByv


	def running(self):
		results = ''
		num = 1230
		block_road = 6200
		everyTime = 32
		for i in range(10):
			for car in self.data_car[num//10*i : num//10*(i+1)]:

				cross_idStart = car.startId
				cross_idEnd = car.endId
				min_path = shortest_path(self.data_cross, self.path, self.id2index[cross_idStart], self.id2index[cross_idEnd])
				road_data = list()
				for j in range(len(min_path) - 1):
					self.crossIds = min_path[j] + '_' + min_path[j + 1]
					if self.crossIds in self.use_roadNum.keys():
						self.use_roadNum[self.crossIds] += 1
					else:
						self.use_roadNum[self.crossIds] = 0
					if self.use_roadNum[self.crossIds] > block_road:
						self.path, self.id2index = floyd(self.data_road, self.data_cross, self.crossIds)
						self.use_roadNum[self.crossIds] = 0
					road_data.append(self.crossId2roadId[self.crossIds])
				road_ids = ''
				for k in range(len(road_data) - 1):
					road_ids += road_data[k].roadId + ','
				road_ids += road_data[-1].roadId
				result = str('(' + car.carId + ',' + str(car.planTime + i) + ',' + road_ids + ')')
				results += str(result) + '\n'

		long = (len(self.data_car) - num) // everyTime
		for i in range(long):
			if i + 1 == long:
				movingCars = self.data_car[everyTime * i + num:]
			else:
				movingCars = self.data_car[everyTime * i + num: everyTime * (i + 1) + num]
			for car in movingCars:
				cross_idStart = car.startId
				cross_idEnd = car.endId
				min_path = shortest_path(self.data_cross, self.path, self.id2index[cross_idStart], self.id2index[cross_idEnd])
				road_data = list()
				for j in range(len(min_path) - 1):
					self.crossIds = min_path[j] + '_' + min_path[j + 1]
					if self.crossIds in self.use_roadNum.keys():
						self.use_roadNum[self.crossIds] += 1
					else:
						self.use_roadNum[self.crossIds] = 0
					if self.use_roadNum[self.crossIds] > block_road:
						self.path, self.id2index = floyd(self.data_road, self.data_cross, self.crossIds)
						self.use_roadNum[self.crossIds] = 0
					road_data.append(self.crossId2roadId[self.crossIds])
				road_ids = ''
				for k in range(len(road_data) - 1):
					road_ids += road_data[k].roadId + ','
				road_ids += road_data[-1].roadId
				result = str('(' + car.carId + ',' + str(car.planTime + 11 + i) + ',' + road_ids + ')')
				results += str(result) + '\n'
		return results



