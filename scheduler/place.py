from flask import (
    g, Blueprint, render_template, request, session, url_for, current_app
)
from scheduler.db import get_db
from scheduler.models import *
from scheduler import render_layout

bp = Blueprint("place", __name__, url_prefix="/place")

@bp.route('/')
def index():
    return render_layout()

    