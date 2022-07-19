
from flask import (
    g, Blueprint, render_template, request, session, url_for, current_app
)
from scheduler.db import get_db
from scheduler.models import *
from scheduler import render_layout

bp = Blueprint("schedule", __name__, url_prefix="/schedule")

@bp.route('/view', methods=['POST'])
def view():

    teams = list(map(lambda team: Team(team.strip()), request.form['teams'].split(',')))
    schedule = list(map(lambda date: date.strip(), request.form['dates'].split(',')))
    places = list(map(lambda loc: Place(loc.strip(), schedule), request.form['places'].split(',')))

    scheduler = Scheduler(teams, places)
    schedule = scheduler.schedule_games()
    return render_layout(page="view", schedule=schedule, title="View schedule")

@bp.route('/create')
def create():
    return render_layout()