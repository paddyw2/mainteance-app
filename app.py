from flask import Flask, render_template, redirect, url_for, request, session, g
from functools import wraps
from handlers.car_handler import car_handler
import os
from rental.rental import rental
from car.car import car
from event.event import event
from pos.pos import pos
from sale.sale import sale
from available.available import available
from backroom.backroom import backroom
from repair.repair import repair
from inspection.inspection import inspection

app = Flask(__name__)
app.secret_key = os.urandom(32)

# sets the global object g
# to have the session status
# before each request (used
# in require_login)
@app.before_request
def load_login_status():
  try:
    g.login_status = session.get("logged_in")
  except:
    g.login_status = False

# returns the decorated function
# only if the login status is
# true
def require_login(function):
  @wraps(function)
  def decorator(*args, **kwargs):
    if(g.login_status == True):
      return function(*args, **kwargs)
    else:
      return redirect(url_for("login"))
  return decorator

# gets the users posted login information
# and verifies the ID is in the db
# if successul, sets the session values
# as the current users
@app.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == "GET":
    view = render_template("auth/login.html", data="")
  else:
    handler = car_handler()
    if handler.check_valid_user(request.form['eid']):
      session["logged_in"] = True
      user_values = handler.select_query_values("select * from user where employee_no="+request.form['eid'])
      session["employee_no"] = user_values[0][0]
      session["phone"] = user_values[0][1]
      session["fname"] = user_values[0][2]
      session["lname"] = user_values[0][3]
      session["is_admin"] = user_values[0][4]
      session["address"] = user_values[0][5]
      view = redirect(url_for("homepage"))
    else:
      message = "Not a valid employee ID"
      view = render_template("auth/login.html", data=message)
  return view

@app.route("/logout")
def logout():
  session["logged_in"] = False
  view = redirect(url_for("login"))
  return view

@app.route("/")
@require_login
def homepage():
  user_info = session
  view = render_template("index.html", data=user_info)
  return view

@app.route("/cars")
@require_login
def cars():
  view = render_template("cars/index.html")
  return view

@app.route("/cars/search")
@require_login
def cars_search():
  user_info = "[username]"
  view = render_template("cars/search.html", data=user_info)
  return view

@app.route("/cars/new")
@require_login
def cars_new():
  user_info = "[username]"
  view = render_template("cars/new.html", data=user_info)
  return view


#This section is for a customer renting a car, not for a user searching cars
############################################################################

# Displays list of available cars that a user can choose to rent (or possibly buy) from
@app.route("/cars/rental")
@require_login
def car_rental():
  return true

# Submission form for renting a car
@app.route("/cars/rental_form")
@require_login
def car_rental_form():
  return true

# Submission form for buying a car
@app.route("/cars/buy_form")
@require_login
def car_buy_form():
  return true

############################################################################

# Displays list of cars based on search parameters
@app.route("/cars/results", methods=['POST'])
@require_login
def car_results():
  handler = car_handler()
  query_string = car.search_car(request.form)
  rows = handler.select_query_values(query_string)
  view = render_template("cars/results.html", row_data=rows)
  return view

# Create Car

@app.route("/cars/new", methods=['POST'])
@require_login
def car_new_post():
  handler = car_handler()
  query_string = car.create_car(request.form)
  handler.insert_values(query_string)
  #view = render_template("cars/index.html", data=info)
  view = redirect(url_for('car_view', car_id=request.form['vin'])) 
  return view

# View Car

@app.route("/cars/<int:car_id>")
@require_login
def car_view(car_id):
  handler = car_handler()
  rows = handler.select_query_values("select * from car where vin_no="+str(car_id))
  info = car_id
  view = render_template("cars/show.html", data=info, row_data=rows)
  return view

# Create Event - Functionality for creation visible per each car

@app.route("/cars/<int:car_id>/events/new")
@require_login
def event_new(car_id):
  handler = car_handler()
  info = handler.insert_query("input")
  info = car_id
  view = render_template("events/new.html", data=info)
  return view

#-------------------------#
# Create POS Event
#-------------------------#

@app.route("/cars/<int:car_id>/events/pos/new")
@require_login
def event_pos_new(car_id):
  info = car_id
  view = render_template("events/pos/new.html", data=info)
  return view

# Available
@app.route("/cars/<int:car_id>/events/pos/available/new")
@require_login
def event_available_pos_new(car_id):
  info = car_id
  view = render_template('events/pos/available/new.html', car_id=info)
  return view

@app.route("/cars/<int:car_id>/events/pos/available/create", methods=['POST'])
@require_login
def event_available_pos_create(car_id):
  handler = car_handler()
  event_query = event.create_event(request.form, car_id, session.get("employee_no"))
  event_id = handler.insert_values(event_query)
  pos_query = pos.create_pos(event_id, request.form["assigned"])
  pos_id = handler.insert_values(pos_query)
  available_query = available.create_available(request.form, pos_id)
  available_id = handler.insert_values(available_query)
  info = car_id
  view = redirect(url_for('event_new', car_id=info)) 
  return view

# Rental
@app.route("/cars/<int:car_id>/events/pos/rental/new")
@require_login
def event_rental_new(car_id):
  info = car_id
  view = render_template('events/pos/rental/new.html', car_id=info)
  return view

@app.route("/cars/<int:car_id>/events/pos/rental/create", methods=['POST'])
@require_login
def event_rental_create(car_id):
  handler = car_handler()
  event_query = event.create_event(request.form, car_id, session.get("employee_no"))
  event_id = handler.insert_values(event_query)
  pos_query = pos.create_pos(event_id, request.form["assigned"])
  pos_id = handler.insert_values(pos_query)
  rental_query = rental.create_rental(request.form, pos_id)
  rental_id = handler.insert_values(rental_query)
  info = car_id
  view = redirect(url_for('event_new', car_id=info)) 
  return view

# Sale
@app.route("/cars/<int:car_id>/events/pos/sale/new")
@require_login
def event_sale_new(car_id):
  info = car_id
  view = render_template('events/pos/sale/new.html', car_id=info)
  return view

@app.route("/cars/<int:car_id>/events/pos/sale/create", methods=['POST'])
@require_login
def event_sale_create(car_id):
  handler = car_handler()
  event_query = event.create_event(request.form, car_id, session.get("employee_no"))
  event_id = handler.insert_values(event_query)
  pos_query = pos.create_pos(event_id, request.form["assigned"])
  pos_id = handler.insert_values(pos_query)
  sale_query = sale.create_sale(request.form, pos_id)
  sale_id = handler.insert_values(sale_query)
  info = car_id
  view = redirect(url_for('event_new', car_id=info)) 
  return view

#-------------------------#
# Create Backroom Event
#-------------------------#

@app.route("/cars/<int:car_id>/events/backroom/new")
@require_login
def event_backroom_new(car_id):
  info = car_id
  view = render_template("events/backroom/new.html", data=info)
  return view

# Repair
@app.route("/cars/<int:car_id>/events/backroom/repair/new")
@require_login
def event_repair(car_id):
  info = car_id
  view = render_template("events/backroom/repair/new.html", car_id=info)
  return view

@app.route("/cars/<int:car_id>/events/backroom/repair/create", methods=['POST'])
@require_login
def event_repair_create(car_id):
  handler = car_handler()
  event_query = event.create_event(request.form, car_id, session.get("employee_no"))
  event_id = handler.insert_values(event_query)
  backroom_query = backroom.create_backroom(event_id, request.form["assigned"])
  backroom_id = handler.insert_values(backroom_query)
  repair_query = repair.create_repair(request.form, backroom_id)
  repair_id = handler.insert_values(repair_query)
  info = car_id
  view = redirect(url_for('event_new', car_id=info)) 
  return view

# Inspection
@app.route("/cars/<int:car_id>/events/backroom/inspection/new")
@require_login
def event_inspection(car_id):
  info = car_id
  view = render_template("events/backroom/inspection/new.html", car_id=info)
  return view

@app.route("/cars/<int:car_id>/events/backroom/inspection/create", methods=['POST'])
@require_login
def event_inspection_create(car_id):
  handler = car_handler()
  event_query = event.create_event(request.form, car_id, session.get("employee_no"))
  event_id = handler.insert_values(event_query)
  backroom_query = backroom.create_backroom(event_id, request.form["assigned"])
  backroom_id = handler.insert_values(backroom_query)
  inspection_query = inspection.create_inspection(request.form, backroom_id)
  inspectino_id = handler.insert_values(inspection_query)
  info = car_id
  view = redirect(url_for('event_new', car_id=info)) 
  return view


#----------------
# Event
#----------------

@app.route("/events/<int:event_id>")
@require_login
def event_view(event_id):
  handler = car_handler()
  queries = event.view_events_all(event_id)
  index = 0
  for query in queries:
    row = handler.select_query_values(query)
    if(len(row) != 0):
      break
    else:
      index += 1
  event_type = event.get_type_event(index)
  view = render_template('events/'+event_type[0]+'/'+event_type[1]+'/view.html', row_data=row)
  return view


# Other routes

@app.route("/events")
@require_login
def events():
  view = render_template("events/index.html")
  return view

# Displays list of events based on search parameters
@app.route("/events/results", methods=['POST'])
@require_login
def events_results():
  handler = car_handler()
  query_string = event.create_event(request.form, request.form["vin"], session.get("employee_no"))
  rows = handler.select_query_values(query_string)
  view = render_template("events/results.html", row_data=rows)
  return view

# Redirects to specific page dedicated to a single event for a car
"""
@app.route("/events/<int:event_id>")
@require_login
def event_view(event_id):
  handler = car_handler()
  rows = handler.select_query_values("select * from event where event_id ="+str(event_id))
  info = event_id
  view = render_template("events/show.html", data=info, row_data=rows)
  return view
  """


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
