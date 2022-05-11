import json


def load_data(path):
    """ Получает список кандидатов """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_candidate_by_id(candidate_id):
    """ Возвращает данные кандидата по его id """
    data = load_data("candidates.json")
    for candidate in data:
        if candidate['id'] == candidate_id:
            return candidate
            # return next(filter(lambda _: _["id"] == candidate_id, data)


def get_candidate_by_name(candidate_name):
    """ возвращает кандидатов по имени """
    data = load_data("candidates.json")
    result = []
    for candidate in data:
        if candidate_name.lower() in candidate["name"].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    """ Возвращает список скиллов кандидата """
    data = load_data("candidates.json")
    result = []
    for candidate in data:
        if skill_name.lower() in candidate["skills"].lower().split(', '):
            result.append(candidate)
    return result

# print(load_data('candidates.json'))
# print(get_candidate_by_id(1))
# print(get_candidate_by_name('bu'))
# print(get_candidates_by_skill('go'))
