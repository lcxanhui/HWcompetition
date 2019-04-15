import logging
import sys
from manage2 import *
from load_save_data import *
import time

# logging.basicConfig(level=logging.DEBUG,
#                     filename='../logs/CodeCraft-2019.log',
#                     format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filemode='a')




def main():
#    if len(sys.argv) != 5:
        # logging.info('please input args: car_path, road_path, cross_path, answerPath')
 #       exit(1)

    # car_path = sys.argv[1]
    # road_path = sys.argv[2]
    # cross_path = sys.argv[3]
    # answer_path = sys.argv[4]
    since = time.time()
    car_path = './1-map-training-2/car.txt'
    road_path = './1-map-training-2/road.txt'
    cross_path = './1-map-training-2/cross.txt'
    answer_path = './1-map-training-2/answer.txt'

    # logging.info("car_path is %s" % (car_path))
    # logging.info("road_path is %s" % (road_path))
    # logging.info("cross_path is %s" % (cross_path))
    # logging.info("answer_path is %s" % (answer_path))

    # to read input file
    # reader = Reader(car_path, cross_path, road_path)
    # car_list = reader.get_cars()
    # road_list = reader.get_roads()
    # cross_list = reader.get_crosses()


    data_road, data_car, data_cross = load_data(road_path, car_path, cross_path)
    # reader = load_data(roadPath, carPath, crossPath)
    # data_car = reader.load_car()
    # data_road = reader.load_road()
    # data_cross = reader.load_cross()

    # for road in road_list:
    #     print(road)
    # for cross in cross_list:
    #     print(cross)

    # process
    # dispatcher = Dispatcher(car_list, data_road, cross_list)
    # schedule_list = dispatcher.run()


    manage = Manage(data_car, data_road, data_cross)
    results = manage.running()

    # for schedule in schedule_list:
    #     print(schedule)

    # to write output file
    save_data(answer_path, results)
    print(time.time()-since,'s cost')

if __name__ == "__main__":
    main()
