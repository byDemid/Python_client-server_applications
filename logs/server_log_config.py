import sys
import os
import logging
import logging.handlers
from common.variables import LOGGING_LEVEL, SERVER_FORMATTER
sys.path.append('../')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

# Создаем обработчик, который выводит сообщения в поток stderr
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setLevel(logging.INFO)

# Создать обработчик, который выводит сообщения в файл
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')

# подключаем объект Formatter к обработчикам
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
LOG_FILE.setFormatter(SERVER_FORMATTER)

# создаём регистратор
SERVER_LOG = logging.getLogger('server')

# Добавляем обработчики к регистратору
SERVER_LOG.addHandler(STREAM_HANDLER)
SERVER_LOG.addHandler(LOG_FILE)
SERVER_LOG.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    SERVER_LOG.critical('Критическая ошибка')
    SERVER_LOG.error('Ошибка')
    SERVER_LOG.warning('Предупреждение!')
    SERVER_LOG.debug('Отладочная информация')
    SERVER_LOG.info('Информационное сообщение')
