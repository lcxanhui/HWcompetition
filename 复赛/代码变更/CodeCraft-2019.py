import logging
import sys
from manage4 import Manage
from load_save_data import *


def main():
    car_path = './map/car.txt'
    road_path = './map/road.txt'
    cross_path = './map/cross.txt'
    preset_answer_path = './map/presetAnswer.txt'
    answer_path = './map/answer.txt'

    # logging.info("car_path is %s" % (car_path))
    # logging.info("road_path is %s" % (road_path))
    # logging.info("cross_path is %s" % (cross_path))
    # logging.info("answer_path is %s" % (answer_path))

    # to read input file
    # reader = Reader(car_path, cross_path, road_path)
    # car_list = reader.get_cars()
    # road_list = reader.get_roads()
    # cross_list = reader.get_crosses()

    # reader = load_data(roadPath, carPath, crossPath)
    # data_car = reader.load_car()
    # data_road = reader.load_road()
    # data_cross = reader.load_cross()
    # print("read finished")

    # for road in road_list:
    #     print(road)
    # for cross in cross_list:
    #     print(cross)

    # process
    # dispatcher = Dispatcher(car_list, data_road, cross_list)
    # schedule_list = dispatcher.run()
    data_car, data_road, data_cross = load_data(car_path, road_path, cross_path)
    data_preset, preset_time = load_preset(preset_answer_path)
    # process

    manage = Manage(data_car, data_road, data_cross, data_preset, preset_time)
    results = manage.running()

    # to write output file
    save_data(answer_path, results)

    print("over")

if __name__ == "__main__":
    main()
