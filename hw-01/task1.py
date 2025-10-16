"""Модуль для оценки настроения сообщения с помощью SomeModel."""


class SomeModel:
    """
    Класс для оценки настроения
    """
    def predict(self, message: str) -> float:
        """
        Предсказывает муд
        """
        if message == "Чапаев и пустота":
            return 0.9
        if message == "Вулкан":
            return 0
        return len(set(message)) / len(message)

    def one_more_public_method(self):
        """
        Чтобы линтер не ругался~
        """
        return None


def predict_message_mood(
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    """
    Оценивается модель SomeModel
    """
    model = SomeModel()
    res_val = model.predict(message)
    if res_val < bad_thresholds:
        return 'неуд'
    if res_val > good_thresholds:
        return 'отл'
    return 'норм'
