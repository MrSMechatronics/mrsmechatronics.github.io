from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_mysqldb import MySQL
import mysql.connector as msconn
import bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from form_validator import *
app = Flask(__name__)
app.permanent_session_lifetime = timedelta(weeks=2)

app.secret_key = "KBgjlZUhzw73AqrJ"
app.config['MYSQL_HOST'] = "localhost" #datab['mysql_host']
app.config['MYSQL_USER'] = "ZjlinhzUgw7et"
app.config['MYSQL_PASSWORD'] = "KBgjlZUhzw73AqrJ"
app.config['MYSQL_DB'] = "web"
app.config['SECRET_KEY'] = "047d23444570cfdfe1702a956e215e71b5ea4de7dffa68344d2ecbb10f5bdd18"
mysql = MySQL(app)