import sys
import os
import logging
from common.variables import LOGGING_LEVEL, CLIENT_FORMATTER
# sys.path.append('../')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

# Создаем обработчик, который выводит сообщения в поток stderr
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setLevel(logging.ERROR)

# Создать обработчик, который выводит сообщения в файл
LOG_FILE = logging.FileHandler(PATH, encoding='utf8')

# подключаем объект Formatter к обработчикам
STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)
LOG_FILE.setFormatter(CLIENT_FORMATTER)

# создаём регистратор
CLIENT_LOG = logging.getLogger('client')

# Добавляем обработчики к регистратору
CLIENT_LOG.addHandler(STREAM_HANDLER)
CLIENT_LOG.addHandler(LOG_FILE)
CLIENT_LOG.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    CLIENT_LOG.critical('Критическая ошибка')
    CLIENT_LOG.error('Ошибка')
    CLIENT_LOG.warning('Предупреждение!')
    CLIENT_LOG.debug('Отладочная информация')
    CLIENT_LOG.info('Информационное сообщение')
