
from shortest_path import Path
from load_data import load_data

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

		self.__path = Path(self.__road_list, self.__cross_list)

		self.crossIdsToRoad = {}
		for road in self.__road_list:
			cross_ids = road.startId + '_' + road.endId
			self.crossIdsToRoad[cross_ids] = road
			if road.isDuplex == '1':
				cross_ids = road.endId + '_' + road.startId
				self.crossIdsToRoad[cross_ids] = road

	def running(self):
		time_list = list()
		numberOfCarEveryTime= 14

		i = 0   # schedule_counter
		while i < len(self.__car_list) // numberOfCarEveryTime:
			if i + 1 == len(self.__car_list) // numberOfCarEveryTime:
				movingCars = self.__car_list[numberOfCarEveryTime * i : ]
			else:
				movingCars = self.__car_list[numberOfCarEveryTime * i : numberOfCarEveryTime * (i + 1)]
			for car in movingCars:
				cross_id_start = car.startId
				cross_id_end = car.endId
				crossList = self.__path.dijkstra(cross_id_start, cross_id_end)
				roadList = list()
				for j in range(len(crossList) - 1):
					crossIds = crossList[j].crossId + '_' + crossList[j+1].crossId
					roadList.append(self.crossIdsToRoad[crossIds])
				timeScheduling = TimeScheduling(car, i + car.startTime, roadList)
				time_list.append(timeScheduling)
			i += 1
		return time_list

	def make_car_list(self):
		car_list_made = []
		self.carDictionary = {}
		for car in self.__car_list:
			if str(car.startTime) in self.carDictionary.keys():
				self.carDictionary[str(car.startTime)].append(car)
			else:
				self.carDictionary[str(car.startTime)] = [car]
		keyList = list(self.carDictionary.keys())
		for key in keyList:
			for car in self.carDictionary[key]:
				car_list_made.append(car)
		self.__car_list = car_list_made


