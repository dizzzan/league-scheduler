import os
from flask import Flask, render_template, current_app

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"],
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        LAYOUT = "_layout.html"
    )

    from . import db
    db.init_app(app)

    from . import league, place, schedule
    app.register_blueprint(league.bp)
    app.register_blueprint(place.bp)
    app.register_blueprint(schedule.bp)

    @app.route('/')
    def index():
        return render_template(app.config['LAYOUT'])

    return app


def render_layout(**kwargs):
    return render_template(current_app.config['LAYOUT'], **kwargs)