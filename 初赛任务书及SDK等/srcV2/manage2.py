from shortest_path import *
#from load_data import load_data
# from load_data import Car

class TimeScheduling(object):

	def __init__(self, car, startTime, roadlist):
		self.roadList = roadlist
		self.car = car
		self.startTime = startTime

	def __str__(self):
		roadIds = ''
		for i in range(len(self.roadList) - 1):
			roadIds += self.roadList[i].roadId + ','
		roadIds += self.roadList[-1].roadId
		return str('(' + self.car.carId + ',' + str(self.startTime)+ ','  + roadIds +')')



class Manage(object):

	def __init__(self, carList, roadList, crossList):

		self.__car_list = carList
		self.__road_list = roadList
		self.__cross_list = crossList

		self.make_car_list()
		self.use_roadnum = dict()
		self.crossIds = ''

		self.path, self.id2index = floyd(self.__road_list, self.__cross_list, self.crossIds)

		self.crossIdsToRoad = {}
		for road in self.__road_list:
			cross_ids = road.startId + '_' + road.endId
			self.crossIdsToRoad[cross_ids] = road
			if road.isDuplex == '1':
				cross_ids = road.endId + '_' + road.startId
				self.crossIdsToRoad[cross_ids] = road

	def running(self):
		time_list = list()

		num = 400
		for i in range(10):
			for car in self.__car_list[num//10*i : num//10*(i+1)]:
				cross_id_start = car.startId
				cross_id_end = car.endId
				crossList = shorest_path(self.__cross_list, self.path, self.id2index[cross_id_start], self.id2index[cross_id_end])
				roadList = list()
				for j in range(len(crossList) - 1):
					self.crossIds = crossList[j].crossId + '_' + crossList[j + 1].crossId
					if self.crossIds in self.use_roadnum.keys():
						self.use_roadnum[self.crossIds] += 1
					else:
						self.use_roadnum[self.crossIds] = 0
					if self.use_roadnum[self.crossIds] > 300:
						self.path, self.id2index = floyd(self.__road_list, self.__cross_list, self.crossIds)
						self.use_roadnum[self.crossIds] = 0
					roadList.append(self.crossIdsToRoad[self.crossIds])
				timeScheduling = TimeScheduling(car, car.startTime + i, roadList)
				# print(timeScheduling)
				time_list.append(timeScheduling)

		# everyTime = 28
		everyTime = 29
		long = (len(self.__car_list) - num) // everyTime
		for i in range(long):
			if i + 1 == long:
				movingCars = self.__car_list[everyTime * i + num:]
			else:
				movingCars = self.__car_list[everyTime * i + num: everyTime * (i + 1) + num]
			for car in movingCars:
				cross_id_start = car.startId
				cross_id_end = car.endId
				crossList = shorest_path(self.__cross_list, self.path, self.id2index[cross_id_start], self.id2index[cross_id_end])
				roadList = list()
				for j in range(len(crossList) - 1):
					self.crossIds = crossList[j].crossId + '_' + crossList[j + 1].crossId
					if self.crossIds in self.use_roadnum.keys():
						self.use_roadnum[self.crossIds] += 1
					else:
						self.use_roadnum[self.crossIds] = 0
					if self.use_roadnum[self.crossIds] > 300:
						self.path, self.id2index = floyd(self.__road_list, self.__cross_list, self.crossIds)
						self.use_roadnum[self.crossIds] = 0
					roadList.append(self.crossIdsToRoad[self.crossIds])

				timeScheduling = TimeScheduling(car, 10 + i, roadList)
				time_list.append(timeScheduling)
		results = ""
		for result in time_list:
			results += str(result) + '\n'
		return results

		# while i < len(self.__car_list) // numberOfCarEveryTime:
		# 	if i + 1 == len(self.__car_list) // numberOfCarEveryTime:
		# 		movingCars = self.__car_list[numberOfCarEveryTime * i : ]
		# 	else:
		# 		movingCars = self.__car_list[numberOfCarEveryTime * i : numberOfCarEveryTime * (i + 1)]
		# 	for car in movingCars:
		# 		cross_id_start = car.startId
		# 		cross_id_end = car.endId
		# 		crossList = self.__path.dijkstra(cross_id_start, cross_id_end)
		# 		roadList = list()
		# 		for j in range(len(crossList) - 1):
		# 			crossIds = crossList[j].crossId + '_' + crossList[j + 1].crossId
		# 			roadList.append(self.crossIdsToRoad[crossIds])
		# 		if i <= long//10:
		# 			timeScheduling = TimeScheduling(car, car.startTime, roadList)
		# 		elif i > long//10 and i <= long*2//10:
		# 			timeScheduling = TimeScheduling(car, car.startTime + i, roadList)
		# 		elif i > long*2//10 and i <= long*3//10:
		# 			timeScheduling = TimeScheduling(car, car.startTime + i, roadList)
		# 		elif i > long*3//10 and i <= long * 4 // 10:
		# 			timeScheduling = TimeScheduling(car, car.startTime + i, roadList)
		# 		elif i > long*4//10 and i <= long*5//10:
		# 			timeScheduling = TimeScheduling(car, car.startTime + i, roadList)
		# 		elif i > long*5//10 and i <= long*6//10:
		# 			timeScheduling = TimeScheduling(car, car.startTime + i, roadList)
		# 		elif i > long*6//10 and i <= long*7//10:
		# 			timeScheduling = TimeScheduling(car, car.startTime + i, roadList)
		# 		elif i > long*7//10 and i <= long*8//10:
		# 			timeScheduling = TimeScheduling(car, car.startTime + i, roadList)
		# 		else:
		# 			timeScheduling = TimeScheduling(car, car.startTime + long*8//10 + i//10, roadList)
		# 		time_list.append(timeScheduling)
		# 	i += 1
		# return time_list


		# while i < len(self.__car_list) // numberOfCarEveryTime:
		# 	if i + 1 == len(self.__car_list) // numberOfCarEveryTime:
		# 		movingCars = self.__car_list[numberOfCarEveryTime * i : ]
		# 	else:
		# 		movingCars = self.__car_list[numberOfCarEveryTime * i : numberOfCarEveryTime * (i + 1)]
		# 	for car in movingCars:
		# 		cross_id_start = car.startId
		# 		cross_id_end = car.endId
		# 		crossList = self.__path.dijkstra(cross_id_start, cross_id_end)
		# 		roadList = list()
		# 		for j in range(len(crossList) - 1):
		# 			crossIds = crossList[j].crossId + '_' + crossList[j+1].crossId
		# 			roadList.append(self.crossIdsToRoad[crossIds])
		# 		if i<len(self.__car_list) // numberOfCarEveryTime / 10:
		# 			timeScheduling = TimeScheduling(car, car.startTime, roadList)
		# 		elif i>len(self.__car_list) // numberOfCarEveryTime *9/ 10:
		# 			timeScheduling = TimeScheduling(car, car.startTime + i//2, roadList)
		# 		else:
		# 			timeScheduling = TimeScheduling(car, i + car.startTime, roadList)
		# 		time_list.append(timeScheduling)
		# 	i += 1
		# return time_list

	def make_car_list(self):
		car_list_made = []
		self.carDictionary = {}
		for car in self.__car_list:
			if str(car.maxSpeed) in self.carDictionary.keys():
				self.carDictionary[str(car.maxSpeed)].append(car)
			else:
				self.carDictionary[str(car.maxSpeed)] = [car]
		#按字符串排序有问题，因此先转为int排序，再换回来
		keyList = list(self.carDictionary.keys())
		keyList = [int(x) for x in keyList]
		keyList.sort(reverse=True)
		keyList = [str(x) for x in keyList]

		for key in keyList:
			# self.carDictionary[key].sort(key=Car.getStartTime, reverse=False)
			for car in self.carDictionary[key]:
				car_list_made.append(car)
		self.__car_list = car_list_made


