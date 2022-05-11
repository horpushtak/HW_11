from utils import load_data, get_candidate_by_id, get_candidates_by_skill, get_candidate_by_name
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def list_candidates():
    """Главная страница"""
    candidates = load_data('candidates.json')
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>')
def candidate_page(candidate_id):
    """Страница кандидата по id"""
    candidate = get_candidate_by_id(candidate_id)
    return render_template('card.html', candidate=candidate)


@app.route('/skill/<string:skill_name>')
def get_candidate_by_skill(skill_name):
    """Поиск кандидата по навыку"""
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, candidates_count=len(candidates))


@app.route('/search/<string:candidate_name>')
def get_candidate_by_name(candidate_name):
    """Поиск кандидата по имени"""
    candidates = get_candidate_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, candidates_count=len(candidates))


if __name__ == '__main__':
    app.run()
