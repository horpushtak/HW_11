###Поиграемся в md

В приложении так и не 
заработала вьюшка, показывающая
кандидатов _по имени_

Это **очень** утомило, но найти ошибку
я не смог

***
да и кусочек кода впихнуть нормально не вышло
***

'''
def get_candidate_by_name(candidate_name):
    """ возвращает кандидатов по имени """
    data = load_data("candidates.json")
    result = []
    for candidate in data:
        if candidate_name.lower() in candidate["name"].lower():
            result.append(candidate)
    return result
'''

> видать,судьба такая!