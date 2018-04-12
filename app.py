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
from writeoff.writeoff import writeoff
from user.user import user

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
@app.route("/cars/available")
@require_login
def car_available():
  #user_info = "[username]"
  handler = car_handler()
  # query_string should select ONLY available cars
  query_string = "select * from car" 
  rows = handler.select_query_values(query_string)
  view = render_template("cars/available.html", row_data=rows)
  return view

# Submission form for renting a car
@app.route("/cars/rental_form")
@require_login
def car_rental_form():
  view = render_template("cars/rental_form.html")
  return view

# Submission form for buying a car
@app.route("/cars/buy_form")
@require_login
def car_buy_form():
  view = render_template("cars/buy_form.html")
  return view

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

# Edit car
@app.route("/cars/<int:car_id>/edit")
@require_login
def car_edit(car_id):
  handler = car_handler()
  rows = handler.select_query_values("select * from car where vin_no="+str(car_id))
  new_data = []
  for val in rows[0]:
    if val==None:
      new_data.append("")
    else:
      new_data.append(val)
  info = car_id
  view = render_template("cars/edit.html", car_id=info, row_data=[new_data])
  return view

# Update car
@app.route("/cars/<int:car_id>/update", methods=['POST'])
@require_login
def car_update(car_id):
  handler = car_handler()
  query_string = car.update_car(request.form)
  handler.insert_values(query_string)
  #view = render_template("cars/index.html", data=info)
  view = redirect(url_for('car_view', car_id=request.form['vin'])) 
  return view

# Delete car
@app.route("/cars/<int:car_id>/delete", methods=['POST'])
@require_login
def car_delete(car_id):
  handler = car_handler()
  rows = handler.insert_values("delete from car where vin_no="+str(car_id))
  view = redirect(url_for('cars')) 
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
  print("Creating pos")
  available_query = available.create_available(request.form, pos_id, "")
  available_id = handler.insert_values(available_query)
  info = car_id
  view = redirect(url_for('event_new', car_id=info)) 
  return view

@app.route("/events/pos/available/<int:event_id>/update", methods=['POST'])
@require_login
def event_available_pos_update(event_id):
  handler = car_handler()
  event_query = event.update_event(request.form, event_id)
  handler.insert_values(event_query)
  pos_query = pos.update_pos(request.form["assigned"], event_id)
  handler.insert_values(pos_query)
  # get pos_id
  row = handler.select_query_values("select pos_id from pos where event_id="+str(event_id))
  pos_id = row[0][0]
  available_query = available.update_available(request.form, pos_id, "")
  available_id = handler.insert_values(available_query)
  view = redirect(url_for('event_view',event_id=event_id)) 
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

@app.route("/events/pos/rental/<int:event_id>/update", methods=['POST'])
@require_login
def event_rental_update(event_id):
  handler = car_handler()
  event_query = event.update_event(request.form, event_id)
  handler.insert_values(event_query)
  pos_query = pos.update_pos(request.form["assigned"], event_id)
  handler.insert_values(pos_query)
  # get pos_id
  row = handler.select_query_values("select pos_id from pos where event_id="+str(event_id))
  pos_id = row[0][0]
  rental_query = rental.update_rental(request.form, pos_id)
  rental_id = handler.insert_values(rental_query)
  view = redirect(url_for('event_view',event_id=event_id)) 
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

@app.route("/events/pos/sale/<int:event_id>/update", methods=['POST'])
@require_login
def event_sale_update(event_id):
  handler = car_handler()
  event_query = event.update_event(request.form, event_id)
  handler.insert_values(event_query)
  pos_query = pos.update_pos(request.form["assigned"], event_id)
  handler.insert_values(pos_query)
  # get pos_id
  row = handler.select_query_values("select pos_id from pos where event_id="+str(event_id))
  pos_id = row[0][0]
  sale_query = sale.update_sale(request.form, pos_id)
  sale_id = handler.insert_values(sale_query)
  view = redirect(url_for('event_view',event_id=event_id)) 
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

@app.route("/events/backroom/repair/<int:event_id>/update", methods=['POST'])
@require_login
def event_repair_update(event_id):
  handler = car_handler()
  event_query = event.update_event(request.form, event_id)
  handler.insert_values(event_query)
  backroom_query = backroom.update_backroom(request.form["assigned"], event_id)
  handler.insert_values(backroom_query)
  # get pos_id
  row = handler.select_query_values("select backroom_id from backroom where event_id="+str(event_id))
  backroom_id = row[0][0]
  repair_query = repair.update_repair(request.form, backroom_id)
  repair_id = handler.insert_values(repair_query)
  view = redirect(url_for('event_view',event_id=event_id)) 
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
  inspection_id = handler.insert_values(inspection_query)
  info = car_id
  view = redirect(url_for('event_new', car_id=info)) 
  return view

@app.route("/events/backroom/inspection/<int:event_id>/update", methods=['POST'])
@require_login
def event_inspection_update(event_id):
  handler = car_handler()
  event_query = event.update_event(request.form, event_id)
  handler.insert_values(event_query)
  backroom_query = backroom.update_backroom(request.form["assigned"], event_id)
  handler.insert_values(backroom_query)
  # get pos_id
  row = handler.select_query_values("select backroom_id from backroom where event_id="+str(event_id))
  backroom_id = row[0][0]
  inspection_query = inspection.update_inspection(request.form, backroom_id)
  inspection_id = handler.insert_values(inspection_query)
  view = redirect(url_for('event_view',event_id=event_id)) 
  return view



# Write Off
@app.route("/cars/<int:car_id>/events/backroom/writeoff/new")
@require_login
def event_writeoff(car_id):
  info = car_id
  view = render_template("events/backroom/writeoff/new.html", car_id=info)
  return view

@app.route("/cars/<int:car_id>/events/backroom/writeoff/create", methods=['POST'])
@require_login
def event_writeoff_create(car_id):
  handler = car_handler()
  event_query = event.create_event(request.form, car_id, session.get("employee_no"))
  event_id = handler.insert_values(event_query)
  backroom_query = backroom.create_backroom(event_id, request.form["assigned"])
  backroom_id = handler.insert_values(backroom_query)
  writeoff_query = writeoff.create_writeoff(request.form, backroom_id)
  writeoff_id = handler.insert_values(writeoff_query)
  info = car_id
  view = redirect(url_for('event_new', car_id=info)) 
  return view

@app.route("/events/backroom/writeoff/<int:event_id>/update", methods=['POST'])
@require_login
def event_writeoff_update(event_id):
  handler = car_handler()
  event_query = event.update_event(request.form, event_id)
  handler.insert_values(event_query)
  backroom_query = backroom.update_backroom(request.form["assigned"], event_id)
  handler.insert_values(backroom_query)
  # get pos_id
  row = handler.select_query_values("select backroom_id from backroom where event_id="+str(event_id))
  backroom_id = row[0][0]
  writeoff_query = writeoff.update_writeoff(request.form, backroom_id)
  writeoff_id = handler.insert_values(writeoff_query)
  view = redirect(url_for('event_view',event_id=event_id)) 
  return view


# Available
@app.route("/cars/<int:car_id>/events/backroom/available/new")
@require_login
def event_available_backroom(car_id):
  info = car_id
  view = render_template("events/backroom/available/new.html", car_id=info)
  return view

@app.route("/cars/<int:car_id>/events/backroom/available/create", methods=['POST'])
@require_login
def event_available_backroom_create(car_id):
  handler = car_handler()
  event_query = event.create_event(request.form, car_id, session.get("employee_no"))
  event_id = handler.insert_values(event_query)
  backroom_query = backroom.create_backroom(event_id, request.form["assigned"])
  backroom_id = handler.insert_values(backroom_query)
  print("Creating backroom")
  available_query = available.create_available(request.form, "", backroom_id)
  available_id = handler.insert_values(available_query)
  info = car_id
  view = redirect(url_for('event_new', car_id=info)) 
  return view

@app.route("/events/backroom/available/<int:event_id>/update", methods=['POST'])
@require_login
def event_available_backroom_update(event_id):
  handler = car_handler()
  event_query = event.update_event(request.form, event_id)
  handler.insert_values(event_query)
  backroom_query = backroom.update_backroom(request.form["assigned"], event_id)
  handler.insert_values(backroom_query)
  # get pos_id
  row = handler.select_query_values("select backroom_id from backroom where event_id="+str(event_id))
  backroom_id = row[0][0]
  available_query = available.update_available(request.form, "", backroom_id)
  available_id = handler.insert_values(available_query)
  view = redirect(url_for('event_view',event_id=event_id)) 
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

@app.route("/events/<int:event_id>/edit")
@require_login
def event_edit(event_id):
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
  new_data = []
  for val in row[0]:
    if val==None:
      new_data.append("")
    else:
      new_data.append(val)
  view = render_template('events/'+event_type[0]+'/'+event_type[1]+'/edit.html', row_data=[new_data], event_id=event_id)
  return view

@app.route("/events/<int:event_id>/delete", methods=["POST"])
@require_login
def event_delete(event_id):
  handler = car_handler()
  rows = handler.insert_values("delete from event where event_id="+str(event_id))
  view = redirect(url_for('homepage')) 
  return view


# Other routes

@app.route("/events")
@require_login
def events():
  handler = car_handler()
  rows = handler.select_query_values("select * from event;")
  view = render_template("events/results.html", row_data=rows)
  return view

@app.route("/events/search")
@require_login
def event_search():
  view = render_template("events/search.html")
  return view


# Displays list of events based on search parameters
@app.route("/events/results", methods=['POST'])
@require_login
def event_results():
  handler = car_handler()
  query_string = event.search_event(request.form)
  rows = handler.select_query_values(query_string)
  view = render_template("events/results.html", row_data=rows)
  return view

@app.route("/customers")
@require_login
def customers():
  user_info = "[username]"
  view = render_template("customers/index.html", data=user_info)
  return view

@app.route("/users")
@require_login
def users():
  user_info = "[username]"
  view = render_template("users/index.html", data=user_info)
  return view

@app.route("/users/results", methods=['POST'])
@require_login
def users_search():
  handler = car_handler()
  query_string = user.search_user(request.form)
  rows = handler.select_query_values(query_string)
  view = render_template("users/results.html", row_data=rows)
  return view

