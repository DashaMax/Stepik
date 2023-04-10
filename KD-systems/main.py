class NeuroNetLibrary:
    def __init__(self, *args, **kwargs):
        pass


class NeuroVoiceLibrary:
    def __init__(self, *args, **kwargs):
        pass


class NeuroNluLibrary:
    def __init__(self, *args, **kwargs):
        pass


# Создаем объекты
nn = NeuroNetLibrary(nlu_call, event_loop)
nv = NeuroVoiceLibrary(nlu_call, loop)
nlu = NeuroNluLibrary(nlu_call, event_loop)


# Создание/обнуление внутренних счетчиков
def counter():
    global hello_count, recommend_null_count, recommend_default_count
    hello_count = nn.counter('hello_null')
    recommend_null_count = nn.counter('recommend_null')
    recommend_default_count = nn.counter('recommend_default')


# hello_logic

def hello_listen():
    with nv.listen(5000) as r:
        if not r:                                                                       # не сказано ни одного слова
            global hello_count
            hello_count = nn.counter('hello_null', '+')                                 # Увеличиваем внутренний счетчик
            return hello_logic('hello_null')

        else:
            result = nlu.extract(r, entities=['confirm', 'wrong_time', 'repeat'])       # Выделяем переданные сущности

            if not result.has_entities() or result.entity('confirm'):                   # Если нет подходящих сущностей или confirm=True
                return main_logic('recommend_main')

            elif result.has_entity('confirm') and not result.entity('confirm') or result.entity('wrong_time'):
                return hangup_logic('hangup_wrong_time', 'нет времени для разговора')

            elif result.entity('repeat'):
                return hello_logic('repeat')


def hello_logic(file: str):
    # Проверяем счетчик
    if file == 'hello_null' and hello_count == 2:
        return hangup_logic('hangup_null', 'проблемы с распознаванием')

    nv.say(file)                   # Проигрываем аудио-файл
    return hello_listen()          # Прослушиваем агента


def main_listen():
    with nv.listen(5000) as r:
        if not r:
            global recommend_null_count
            recommend_null_count = nn.counter('recommend_null', '+')
            return main_logic('recommend_null')

        else:
            result = nlu.extract(r, entities=['recommendation_score', 'recommendation', 'wrong_time', 'repeat', 'question'])

            if not result.has_entities():
                global recommend_default_count
                recommend_default_count = nn.counter('recommend_default', '+')
                return main_logic('recommend_default')

            elif 0 <= result.entity('recommendation_score') <= 8:
                return hangup_logic('hangup_negative', 'низкая оценка')

            elif 9 <= result.entity('recommendation_score') <= 10:
                return hangup_logic('hangup_positive', 'высокая оценка')

            elif result.entity('recommendation') == 'negative':
                return main_logic('recommend_score_negative')

            elif result.entity('recommendation') == 'neutral':
                return main_logic('recommend_score_neutral')

            elif result.entity('recommendation') == 'positive':
                return main_logic('recommend_score_positive')

            elif result.entity('wrong_time'):
                return hangup_logic('hangup_wrong_time', 'нет времени для разговора')

            elif result.entity('repeat'):
                return main_logic('recommend_repeat')

            elif result.entity('recommendation') == 'dont_know':
                return main_logic('recommend_repeat_2')

            elif result.entity('question'):
                return forward_logic('перевод на оператора')


def main_logic(file: str):
    if file == 'recommend_null' and recommend_null_count == 2 or \
       file == 'recommend_default' and recommend_default_count == 2:
        return hangup_logic('hangup_null', 'проблемы с распознаванием')

    nv.say(file)
    return main_listen()


def hangup_logic(file: str, data: str):
    nv.say(file)
    nn.dialog.result = nn.RESULT_DONE           # Завершаем диалог
    counter()                                   # Обнуляем внутренние счетчики
    nn.log('tag', data)                         # Передаем данные в статистику

    if file == 'hangup_wrong_time' or file == 'hangup_null':
        number_agent = nn.dialog.msisdn                             # Получение номера абонента
        nn.call(number_agent)                                       # Добавление звонка в очередь на обзвон

    return hangup_action()


def hangup_action():
    pass


# forward_logic

def forward_logic(data: str):
    nv.say('forward')
    nn.log('tag', data)
    nv.background('forward')      # Проигрываем запись на фоне

    return bridge_action()


def bridge_action():
    nv.background(None)           # Останавливаем запись на фоне


# Запуск диалога
if __name__ == '__main__':
    nn.dialog.result = nn.RESULT_START      # Переводим статус в начало диалога
    counter()                               # Создаем внутренние счетчики
    hello_logic('hello')


