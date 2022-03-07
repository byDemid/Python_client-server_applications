# import sys
# import os
# import unittest
# sys.path.append(os.path.join(os.getcwd(), '..'))
# from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
# from server import process_client_message
#
#
# class TestServer(unittest.TestCase):
#     err_dict = {
#         RESPONSE: 400,
#         ERROR: 'Bad Request'
#     }
#     ok_dict = {RESPONSE: 200}
#
#     def test_no_action(self):
#         """Ошибка если нет действия (ACTION:)"""
#         self.assertEqual(process_client_message(
#             {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)
#
#     def test_wrong_action(self):
#         """Ошибка если неизвестное действие (Wrong)"""
#         self.assertEqual(process_client_message(
#             {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)
#
#     def test_no_time(self):
#         """Ошибка, если  запрос не содержит штампа времени (TIME)"""
#         self.assertEqual(process_client_message(
#             {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)
#
#     def test_no_user(self):
#         """Ошибка - нет пользователя (USER:)"""
#         self.assertEqual(process_client_message(
#             {ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)
#
#     def test_unknown_user(self):
#         """Ошибка - не тот пользователь (ожидает Guest1 а зашел Guest)"""
#         self.assertEqual(process_client_message(
#             {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.err_dict)
#
#     def test_ok_check(self):
#         """Корректный запрос, ожидаемое совподает с пришедшим, отправляем 200 - успешно завершено """
#         self.assertEqual(process_client_message(
#             {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)
#
#
# if __name__ == '__main__':
#     unittest.main()
