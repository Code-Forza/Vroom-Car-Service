from vroom import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
  return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
  return render_template('home.html')

@app.route('/book-service')
def book_service():
  return render_template('book_service.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/service-details')
def service_details():
  return render_template('service_details.html')

