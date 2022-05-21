from flask import Flask, render_template
import utils
app = Flask(__name__)

# Главная страница
@app.route('/')
def page_candidates():  # put application's code here
    items = utils.get_all_candidates()
    return render_template('list.html', items=items)


@app.route('/candidate/<int:pk>')
def page_name_id(pk):
    """ Функция выводит кандидата по id"""
    candidate = utils.get_id_cand(pk)
    name_ = candidate["name"]
    position = candidate["position"]
    picture = candidate["picture"]
    skills = candidate["skills"]
    return render_template('single.html', name=name_, position=position, picture=picture, skills=skills)

@app.route('/search/<candidate_name>')
def page_search(candidate_name):
    """ Функция выводит кандидата/кандидатов по совпадению имен"""
    items = utils.get_candidate_by_name(candidate_name)
    len_item = len(items)
    return render_template('search.html', len_item=len_item, items=items)


@app.route('/skills/<skill_name>')
def page_skills(skill_name):
    """ Функция выводит кандидата/кандидатов по совпадению навыков"""
    items = utils.get_candidates_by_skill(skill_name)
    len_item = len(items)
    return render_template('search.html', len_item=len_item, items=items)



# if __name__ == '__main__':
#     app.run(debug=True)
app.run(debug=True)