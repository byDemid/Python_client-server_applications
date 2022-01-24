"""Программа-сервер"""

import socket
import sys
import json
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, IP_ADDRESS, PORT
from common.utils import get_message, send_message


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


def main():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    :return:
    '''

    try:
        listen_port = int(sys.argv[sys.argv.index(PORT) + 1]) if PORT in sys.argv else DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

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
        print(client_ip)
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
