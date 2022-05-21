
import json

# DATA_PATH = 'cand.json'

def load_candidates_from_json():
    """ Функция загружает данные о кандидатах"""
    with open('cand.json', "r", encoding='utf-8') as f:
        file = f.read()
        data_file = json.loads(file)
    return data_file


def get_all_candidates():
    """ Функция получает список всех кандидатов"""
    list_of_candidates = load_candidates_from_json()
    return list_of_candidates

# print(load_candidates_from_json())

def get_id_cand(id):
    """ Функция возвращает кандидата по id"""
    list_of_candidates = load_candidates_from_json()
    for candidate in list_of_candidates:
        if candidate["id"] == id:
            return candidate

def get_candidate_by_name(name):
    """ Функция возвращает кандидата/список кандидатов
        по совпадению имени
    """
    list_of_candidates = get_all_candidates()
    # name = candidate_name.lower()
    names_list = []
    for candidate in list_of_candidates:
        names = candidate["name"].lower().strip().split()
        if name.lower() in names:
            names_list.append(candidate)
    return names_list

# print(get_candidate_by_name('Day'))


def get_candidates_by_skill(skill_name):
    """ Функция возвращает кандидатов по навыку"""
    skilled_candidates = []
    skill_name = skill_name.lower()

    list_of_candidates = load_candidates_from_json()
    for candidate in list_of_candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name in skills:
            skilled_candidates.append(candidate)
            continue

    return skilled_candidates

