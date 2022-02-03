"""Программа-сервер"""
import argparse
import socket
import sys
import json
import logging
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, IP_ADDRESS, PORT
from common.utils import get_message, send_message
from errors import IncorrectDataRecivedError
from logs import server_log_config
from decor import log

# Инициализация логирования сервера.
SERVER_LOGGER = logging.getLogger('server')


@log
def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    '''
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


@log
def create_arg_parser():
    """
    Парсер аргументов коммандной строки
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    return parser


def main():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    :return:
    '''
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p
    # проверка получения корретного номера порта для работы сервера.
    if not 1023 < listen_port < 65536:
        SERVER_LOGGER.critical(
            f'{listen_port} В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    SERVER_LOGGER.info(f'Запущен сервер, порт для подключений: {listen_port}, '
                       f'адрес с которого принимаются подключения: {listen_address}. '
                       f'Если адрес не указан, принимаются соединения с любых адресов.')

    # Загружаем какой адрес слушать

    try:
        listen_address = sys.argv[sys.argv.index(IP_ADDRESS) + 1] if IP_ADDRESS in sys.argv else ''
    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_ip = transport.accept()
        SERVER_LOGGER.info(f'Установлено соедение с ПК {client_ip}')
        try:
            message_from_client = get_message(client)
            SERVER_LOGGER.debug(f'Получено сообщение {message_from_client}')
            response = process_client_message(message_from_client)
            SERVER_LOGGER.info(f'Cформирован ответ клиенту {response}')
            send_message(client, response)
            SERVER_LOGGER.debug(f'Соединение с клиентом {client_ip} закрывается.')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать JSON строку, полученную от '
                                f'клиента {client_ip}. Соединение закрывается.')
            client.close()
        except IncorrectDataRecivedError:
            SERVER_LOGGER.error(f'От клиента {client_ip} приняты некорректные данные. '
                                f'Соединение закрывается.')
            client.close()


if __name__ == '__main__':
    main()
