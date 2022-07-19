from flask import (
    g, Blueprint, render_template, request, session, url_for, current_app
)
from scheduler.db import get_db
from scheduler.models import *
from scheduler import render_layout

bp = Blueprint("league", __name__, url_prefix="/league")
  
@bp.route('/')
def index():
    return render_layout()
