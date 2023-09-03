import logging

logging.basicConfig(level=logging.INFO, filename='loger.log', filemode='a',
                    format='%(asctime)s, %(levelname)s, %(message)s')

x, y = map(int, input('Введите два целых числа через пробел: ').split())
try:
    print((x / y))
    logging.info('Ok')
except:
    logging.error('ZeroDivisionZero')
