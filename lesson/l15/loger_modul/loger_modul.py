import logging
from other import log_all

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(filename='matrix_log.log', filemode='w', encoding='utf-8',
                    level=logging.INFO, format=FORMAT, style='{')
logger = logging.getLogger('main')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
