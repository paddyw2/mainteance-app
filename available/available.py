class available:
  def create_available(post_values, pos_id):
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
    query_string = "insert into available(pos_id"+extra_values+") values("+str(pos_id)+sale_price+car_condition+next_repair+");"
    query_string = query_string.replace(",)", ")")
    print(query_string)
    return query_string

