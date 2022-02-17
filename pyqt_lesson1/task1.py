'''Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться
с помощью функции ip_address().'''

from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(list_ip_adresses, timeout=5, request=1):
    result = {'Доступные узлы': '', 'Недоступные узлы': ''}
    for address in list_ip_adresses:
        try:
            address = ip_address(address)
        except ValueError:
            pass
        proc = Popen(f'ping {address} -w {timeout} -n {request}', shell=False, stdout=PIPE)
        proc.wait()

        if proc.returncode == 0:
            result['Доступные узлы'] += f'{str(address)}\n'
            res_string = f'{address}- Узел досутпен'

        else:
            result['Недоступные узлы'] += f'{str(address)}\n'
            res_string = f'{address}- Узел недоступен'
        print(res_string)

    return result


if __name__ == '__main__':
    ip_adresses = ['mail.ru', '3.3.3.3', '192.168.0.17', '192.168.0.100', '192.168.0.1']
    host_ping(ip_adresses)

""" Оезультат
mail.ru- Узел досутпен
3.3.3.3- Узел недоступен
192.168.0.17- Узел досутпен (мой)
192.168.0.100- Узел недоступен
192.168.0.1- Узел досутпен
"""