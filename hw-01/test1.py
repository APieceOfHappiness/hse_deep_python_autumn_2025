""" Тестирование task1 """
import unittest

from task1 import predict_message_mood


class TestUser(unittest.TestCase):
    """
    Основной класс для тестирования модели
    """
    def test_predict_message_mood_specific_cases(self):
        """
        Тут оцениваем особенные кейсы
        """
        self.assertEqual("отл", predict_message_mood("Чапаев и пустота"))
        self.assertEqual("норм", predict_message_mood("Чапаев и пустота",
                                                      0.8, 0.99))
        self.assertEqual("неуд", predict_message_mood("Вулкан"))

    def test_predict_message_mood_general(self):
        """
        Тут оцениваем general кейсы
        """
        self.assertEqual("норм", predict_message_mood("aabb"))
        self.assertEqual("неуд", predict_message_mood("aaaaaa"))
        self.assertEqual("отл", predict_message_mood("abcdef"))
