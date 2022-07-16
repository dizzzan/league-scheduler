from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

_LAYOUT = "_layout.html"

@app.route('/')
def index():
    return render_template(_LAYOUT, title="Home", page="index")

@app.route('/view', methods=['POST'])
def view():

    teams = list(map(lambda team: Team(team.strip()), request.form['teams'].split(',')))
    schedule = list(map(lambda date: date.strip(), request.form['dates'].split(',')))
    locations = list(map(lambda loc: Location(loc.strip(), schedule), request.form['locations'].split(',')))

    scheduler = Scheduler(teams, locations)
    schedule = scheduler.schedule_games()
    return render_template(_LAYOUT, page="view", title="View Schedule", schedule=schedule)

@app.route('/create')
def create():
    return render_template(_LAYOUT, title="Create Schedule", page="create")
  
