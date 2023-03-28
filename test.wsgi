import sys
import os

# add the Flask app directory to the Python path
sys.path.append('/var/www/html/test')

# import the Flask app object
from app import app as application

