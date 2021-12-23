from flask import Flask

app = Flask(__name__)

from extentions import *
from models import *
from controllers import *

