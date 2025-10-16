from task1 import predict_message_mood


def test_predict_specific_cases():
    assert predict_message_mood("Чапаев и пустота") == "отл"
    assert predict_message_mood("Чапаев и пустота", 0.8, 0.99) == "норм"
    assert predict_message_mood("Вулкан") == "неуд"


def test_predict_general_cases():
    assert predict_message_mood("aabb") == "норм"
    assert predict_message_mood("aaaaaa") == "неуд"
    assert predict_message_mood("abcdef") == "отл"
