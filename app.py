import os
from flask import Flask, request, redirect, render_template
from lib.user_repository import UserRepository
from lib.user import User
from lib.database_connection import get_flask_database_connection
# Create a new Flask app
app = Flask(__name__)

