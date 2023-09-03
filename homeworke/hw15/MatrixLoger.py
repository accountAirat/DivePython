import logging

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" в строке {lineno:03d}: {msg}'
logging.basicConfig(filename='matrix.log', filemode='w', encoding='utf-8',
                    level=logging.INFO, format=FORMAT, style='{')


def init_log(func):
    def wrapper(*args, **kwargs):
        try:
            logging.info(f'Старт инициализация')
            func(*args, **kwargs)
            logging.info(f'Успешная инициализация матрицы с параметрами: {args, kwargs}')
        except Exception as e:
            logging.error(e)

    return wrapper


def operation_log(func):
    def wrapper(*args, **kwargs):
        logging.info(f'Старт метода {func.__name__}')
        try:
            res = func(*args, **kwargs)
            logging.info(f'Успешная операция {func.__name__} с матрицей: {args, kwargs}')
            return res
        except Exception as e:
            logging.error(e)

    return wrapper
