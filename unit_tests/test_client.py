# import sys
# import os
# import unittest
# sys.path.append(os.path.join(os.getcwd(), '..'))
# from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
# from client import create_presence, process_ans
#
#
# class TestClient(unittest.TestCase):
#
#     def test_def_presence(self):
#         """проверка подключения"""
#         test = create_presence()
#         test[TIME] = 1.1  # принудительно приравниваем время
#         self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})
#
#     def test_200_ans(self):
#         """проверка ответа 200"""
#         self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')
#
#     def test_400_ans(self):
#         """проверка ответа ошибки 400"""
#         self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')
#
#     def test_no_response(self):
#         """тест без поля RESPONSE"""
#         self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})
#
#
# if __name__ == '__main__':
#     unittest.main()
