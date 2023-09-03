import logging

logging.basicConfig(level=logging.INFO, filename='loger.log', filemode='a',
                    format='%(asctime)s, %(levelname)s, %(message)s')


def log_deco(func):
    def wrapper(x, y):
        try:
            logging.info(f'Result: {x} / {y} = {func(x, y)}')
        except:
            logging.error('ZeroDivisionZero')

    return wrapper


@log_deco
def log_div(x, y):
    return x / y


a, b = map(int, input('Введите два целых числа через пробел: ').split())

log_div(a, b)
