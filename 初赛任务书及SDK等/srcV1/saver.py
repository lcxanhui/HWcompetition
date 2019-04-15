
class Saver(object):

	def __init__(self, answer_file, schedule_list):
		self.__answer_file = answer_file
		self.__schedule_list = schedule_list

	def save(self):
		with open(self.__answer_file, 'w', encoding='utf-8') as answer_file:
			lines = list()
			for schedule in self.__schedule_list:
				lines.append(str(schedule)+'\n')
			answer_file.writelines(lines)