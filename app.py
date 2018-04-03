from flask import Flask, render_template, redirect, url_for
from handlers.car_handler import car_handler
app = Flask(__name__)

@app.route("/")
def homepage():
  user_info = "[username]"
  view = render_template("index.html", data=user_info)
  return view

@app.route("/cars")
def cars():
  user_info = "[username]"
  view = render_template("cars/index.html", data=user_info)
  return view

@app.route("/cars/search")
def cars_search():
  user_info = "[username]"
  view = render_template("cars/search.html", data=user_info)
  return view

@app.route("/cars/new")
def cars_new():
  user_info = "[username]"
  view = render_template("cars/new.html", data=user_info)
  return view


@app.route("/cars/results", methods=['POST'])
def car_results():
  handler = car_handler()
  info = handler.select_query("input")
  user_info = "[username]"
  view = render_template("cars/results.html", data=info)
  return view

@app.route("/cars/new", methods=['POST'])
def car_new_post():
  handler = car_handler()
  info = handler.insert_query("input")
  user_info = "[username]"
  #view = render_template("cars/index.html", data=info)
  view = redirect(url_for('cars')) 
  return view



# Other routes

@app.route("/events")
def events():
  user_info = "[username]"
  view = render_template("events/index.html", data=user_info)
  return view

@app.route("/customers")
def customers():
  user_info = "[username]"
  view = render_template("customers/index.html", data=user_info)
  return view

@app.route("/users")
def users():
  user_info = "[username]"
  view = render_template("users/index.html", data=user_info)
  return view
