from flask import render_template

from app import app
from models import *

@app.route('/')
def home():
    blogs = Blog.query.all() # select 
    return render_template('index.html', blogs=blogs)