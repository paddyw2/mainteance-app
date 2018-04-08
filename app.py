from flask import Flask, render_template, redirect, url_for, request
from handlers.car_handler import car_handler
app = Flask(__name__)


@app.route("/")
def homepage():
  user_info = "[username]"
  view = render_template("index.html", data=user_info)
  return view

@app.route("/cars")
def cars():
  view = render_template("cars/index.html")
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
  # TODO: parse post parameters and include in query
  vin = request.form['vin']
  if(vin != ""):
    vin = " vin_no="+vin
  make = request.form['make']
  if(make != ""):
    make = " and make=\""+make+"\""
  model = request.form['model']
  if(model != ""):
    model = " and model=\""+model+"\""
  lno = request.form['lno']
  if(lno != ""):
    lno = " and license_plate=\""+lno+"\""
  status = request.form['status']
  if(status != ""):
    status = " and status=\""+status+"\""
  description = request.form['description']
  if(description != ""):
    description = " and description=\""+description+"\""
  # query
  query_string = "select * from car where"+vin+make+model+lno+status+description
  if("where and" in query_string):
    query_string = query_string.replace("where and", "where")
  print(query_string)
  rows = handler.select_query_values(query_string)
  view = render_template("cars/results.html", row_data=rows)
  return view

# Create Car

@app.route("/cars/new", methods=['POST'])
def car_new_post():
  handler = car_handler()
  vin = request.form['vin'] + ","
  make = request.form['make']
  extra_values = ""
  if(make != ""):
    make = "\""+make+"\"" ","
    extra_values += ", make"
  model = request.form['model']
  if(model != ""):
    model = "\""+model+"\"" + ","
    extra_values += ", model"
  lno = request.form['lno']
  lno = "\""+lno+"\"" + ","
  status = request.form['status']
  if(status != ""):
    status = "\""+status+"\"" + ","
    extra_values += ", status"
  description = request.form['description']
  if(description != ""):
    description = "\""+description+"\"" + ","
    extra_values += ", description"

  # query
  query_string = "insert into car(vin_no, license_plate"+extra_values+") values("+vin+make+model+lno+status+description+");"
  query_string = query_string.replace(",)", ")")
  print(query_string)
  handler.insert_values(query_string)
  #view = render_template("cars/index.html", data=info)
  view = redirect(url_for('car_view', car_id=request.form['vin'])) 
  return view

# View Car

@app.route("/cars/<int:car_id>")
def car_view(car_id):
  handler = car_handler()
  rows = handler.select_query_values("select * from car where vin_no="+str(car_id))
  info = car_id
  view = render_template("cars/show.html", data=info, row_data=rows)
  return view

# Create Event

@app.route("/cars/<int:car_id>/events/new")
def event_new(car_id):
  handler = car_handler()
  info = handler.insert_query("input")
  info = car_id
  view = render_template("events/new.html", data=info)
  return view

# Create POS Event

@app.route("/cars/<int:car_id>/events/pos/new")
def event_pos_new(car_id):
  handler = car_handler()
  info = handler.insert_query("input")
  info = car_id
  view = render_template("events/pos/new.html", data=info)
  return view

@app.route("/cars/<int:car_id>/events/pos/create", methods=['POST'])
def event_pos_create(car_id):
  handler = car_handler()
  info = handler.insert_query("input")
  info = car_id

  view = redirect(url_for('event_new', car_id=info)) 
  return view

# Create Backroom Event

@app.route("/cars/<int:car_id>/events/backroom/new")
def event_backroom_new(car_id):
  handler = car_handler()
  info = handler.insert_query("input")
  info = car_id
  view = render_template("events/backroom/new.html", data=info)
  return view

@app.route("/cars/<int:car_id>/events/backroom/create", methods=['POST'])
def event_backroom_create(car_id):
  handler = car_handler()
  info = handler.insert_query("input")
  info = car_id

  view = redirect(url_for('event_new', car_id=info)) 
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
