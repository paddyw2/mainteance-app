class event:
  pos_tables = ["rental","available", "sale"]
  backroom_tables = ["repair", "inspection", "writeoff", "available"]

  def create_event(post_values, car_id, user_id):
    vin = str(car_id)
    created_by = ","+str(user_id)
    extra_values = ""
    title = post_values['title']
    if(title != ""):
      title = ",\""+title+"\""
      extra_values += ",title"
    start_date = post_values['start_date']
    if(start_date != ""):
      start_date = ",\""+start_date+"\""
      extra_values += ",start_date"
    end_date = post_values['end_date']
    if(end_date != ""):
      end_date = ",\""+end_date+"\""
      extra_values += ",end_date"
    status = post_values['status']
    if(status != ""):
      status = ",\""+status+"\""
      extra_values += ",status"
    description = post_values['description']
    if(description != ""):
      description = ",\""+description+"\""
      extra_values += ",description"
    # query
    query_string = "insert into event(car_vin, created_by"+extra_values+") values("+vin+created_by+title+start_date+end_date+status+description+");"
    query_string = query_string.replace(",)", ")")
    print(query_string)
    return query_string

  def update_event(post_values, event_id):
    title = post_values['title']
    if(title != ""):
      title = "title=\""+title+"\","
    start_date = post_values['start_date']
    if(start_date != ""):
      start_date = "start_date=\""+start_date+"\","
    end_date = post_values['end_date']
    if(end_date != ""):
      end_date = "end_date=\""+end_date+"\","
    status = post_values['status']
    if(status != ""):
      status = "status=\""+status+"\","
    description = post_values['description']
    if(description != ""):
      description = "description=\""+description+"\","
    # query
    query_string = "update event set "+title+start_date+end_date+status+description+" where event_id="+str(event_id)+";"
    query_string = query_string.replace(", where", " where")
    print(query_string)
    return query_string


  def view_events_all(event_id):
    list_of_queries = []
    for event_type in event.pos_tables:
      query_string = """select * from 
      event as e, pos as p, """+ event_type + """ as t 
      where e.event_id="""+str(event_id)+""" and p.event_id=e.event_id
      and t.pos_id=p.pos_id;"""
      list_of_queries.append(query_string)

    for event_type in event.backroom_tables:
      query_string = """select * from 
      event as e, backroom as b, """+ event_type + """ as t 
      where e.event_id="""+str(event_id)+""" and b.event_id=e.event_id
      and t.backroom_id=b.backroom_id;"""
      list_of_queries.append(query_string)

    return list_of_queries

  def view_event(event_id, type_event, table):
    if(type_event == "pos"):
      table_id = "pos_id"
    else:
      table_id = "backroom_id"

    query_string = """select * from 
    event as e, """ + type_event +""" as p, """ + table + """ as t 
    where e.event_id="""+str(event_id)+""" and p.event_id=e.event_id
    and t.""" + table_id + """=p."""+ table_id+""";"""
    return query_string

  def get_type_event(index):
    # figures out if this event is pos/backroom
    # and what subtype
    # defined by constants in class
    # pos_tables = ["rental","available", "sale"]
    # backroom_tables = ["repair", "inspection", "writeoff", "available"]
    event_type = ["",""]
    if(index in [0,1,2]):
      event_type[0] = "pos"
      event_type[1] = event.pos_tables[index]
    else:
      event_type[0] = "backroom"
      event_type[1] = event.backroom_tables[index-3]

    return event_type

  def search_event(post_values):
    vin = post_values['vin']
    if(vin != ""):
      vin = " e.car_vin="+vin
    createdBY = post_values['created_by']
    if(createdBY != ""):
      createdBY = " and e.created_by=\""+createdBY+"\""
    title = post_values['title']
    if(title != ""):
      title = " and e.title=\""+title+"\""
    startDate = post_values['start_date']
    if(startDate != ""):
      startDate = " and e.start_date=\""+start_date+"\""
    endDate = post_values['end_date']
    if(endDate != ""):
      endData = " and e.end_date=\""+end_date+"\""
    status = post_values['status']
    if(status != ""):
      status = " and e.status=\""+status+"\""
    description = post_values['description']
    if(description != ""):
      description = " and e.description=\""+description+"\""

    if(post_values["event_type"] == "All Event Types"):
        query_end = ""
    elif(post_values["event_type"] == "Sale"):
      event_type = "sale"
      query_end = " and exists(select * from pos as p, "+event_type+" as s where p.event_id=e.event_id and s.pos_id=p.pos_id)"
    elif(post_values["event_type"] == "Rental"):
      event_type = "rental"
      query_end = " and exists(select * from pos as p, "+event_type+" as s where p.event_id=e.event_id and s.pos_id=p.pos_id)"
    elif(post_values["event_type"] == "Available"):
      event_type = "available"
      part_one = " and exists(select * from pos as p, "+event_type+" as s where p.event_id=e.event_id and s.pos_id=p.pos_id) or"
      part_two = " exists(select * from backroom as b, "+event_type+" as s where b.event_id=e.event_id and s.backroom_id=b.backroom_id)"
      query_end = part_one + part_two
    elif(post_values["event_type"] == "Repair"):
      event_type = "repair"
      query_end = " and exists(select * from backroom as b, "+event_type+" as s where b.event_id=e.event_id and s.backroom_id=b.backroom_id)"
    elif(post_values["event_type"] == "Inspection"):
      event_type = "inspection"
      query_end = " and exists(select * from backroom as b, "+event_type+" as s where b.event_id=e.event_id and s.backroom_id=b.backroom_id)"
    elif(post_values["event_type"] == "Write Off"):
      event_type = "writeoff"
      query_end = " and exists(select * from backroom as b, "+event_type+" as s where b.event_id=e.event_id and s.backroom_id=b.backroom_id)"
    else:
      query_end = ""

        # query
    query_string = "select * from event as e where"+vin+createdBY+title+startDate+endDate+status+description + query_end
    if("where and" in query_string):
      query_string = query_string.replace("where and", "where")
    print(query_string)
    return query_string

