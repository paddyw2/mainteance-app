class available:
  def create_available(post_values, pos_id, backroom_id):
    sale_price = post_values['sale_price']
    car_condition = post_values['car_condition']
    next_repair = post_values['next_repair']
    extra_values = ""
    if(sale_price != ""):
      sale_price = ",\""+sale_price+"\""
      extra_values += ",sale_price" 
    if(car_condition != ""):
      car_condition = ",\""+car_condition+"\""
      extra_values += ",car_condition" 
    if(next_repair != ""):
      next_repair = ",\""+next_repair+"\""
      extra_values += ",next_repair" 
    # query
    if(pos_id != ""):
      query_string = "insert into available(pos_id"+extra_values+") values("+str(pos_id)+sale_price+car_condition+next_repair+");"
    else:
      query_string = "insert into available(backroom_id"+extra_values+") values("+str(backroom_id)+sale_price+car_condition+next_repair+");"
    query_string = query_string.replace(",)", ")")
    print(query_string)
    return query_string

  def update_available(post_values, pos_id, backroom_id):
    sale_price = post_values['sale_price']
    car_condition = post_values['car_condition']
    next_repair = post_values['next_repair']
    if(sale_price != ""):
      sale_price = ",sale_price=\""+sale_price+"\""
    if(car_condition != ""):
      car_condition = ",car_condition=\""+car_condition+"\""
    if(next_repair != ""):
      next_repair = ",next_repair=\""+next_repair+"\""
    # query
    if(pos_id != ""):
      query_string = "update available set pos_id="+str(pos_id)+sale_price+car_condition+next_repair+" where pos_id="+str(pos_id)+";"
    else:
      query_string = "update available set backroom_id="+str(backroom_id)+sale_price+car_condition+next_repair+" where backroom_id="+str(backroom_id)+";"
    query_string = query_string.replace(", where", " where")
    print(query_string)
    return query_string

