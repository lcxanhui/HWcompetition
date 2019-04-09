import logging
import sys
from manage3 import Manage
from load_save_data import *


# logging.basicConfig(level=logging.DEBUG,
#                     filename='../logs/CodeCraft-2019.log',
#                     format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filemode='a')




def main():
    # if len(sys.argv) != 6:
    #     logging.info('please input args: car_path, road_path, cross_path, answerPath')
    #     exit(1)
    #
    # car_path = sys.argv[1]
    # road_path = sys.argv[2]
    # cross_path = sys.argv[3]
    # preset_answer_path = sys.argv[4]
    # answer_path = sys.argv[5]
    #
    # logging.info("car_path is %s" % (car_path))
    # logging.info("road_path is %s" % (road_path))
    # logging.info("cross_path is %s" % (cross_path))
    # logging.info("preset_answer_path is %s" % (preset_answer_path))
    # logging.info("answer_path is %s" % (answer_path))
    car_path = './2-map-training-1/car.txt'
    road_path = './2-map-training-1/road.txt'
    cross_path = './2-map-training-1/cross.txt'
    presetAnswer_path = './2-map-training-1/presetAnswer.txt'
    answer_path = './2-map-training-1/answer.txt'

    # logging.info("car_path is %s" % (car_path))
    # logging.info("road_path is %s" % (road_path))
    # logging.info("cross_path is %s" % (cross_path))
    # logging.info("answer_path is %s" % (answer_path))

    # to read input file

    data_car, data_road, data_cross,data_presetAnswer = load_data(car_path, road_path, cross_path, presetAnswer_path)


    # process

    manage = Manage(data_car, data_road, data_cross, data_presetAnswer)
    results = manage.running()

    # to write output file
    save_data(answer_path, results)


if __name__ == "__main__":
    main()
