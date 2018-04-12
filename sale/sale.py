class sale:
  def create_sale(post_values, pos_id):
    price = post_values['price']
    extra_values = ""
    if(price != ""):
      price = ",\""+price+"\""
      extra_values += ",price" 
    # query
    query_string = "insert into sale(pos_id"+extra_values+") values("+str(pos_id)+price+");"
    query_string = query_string.replace(",)", ")")
    print(query_string)
    return query_string

  def update_sale(post_values, pos_id):
    price = post_values['price']
    if(price != ""):
      price = ",price=\""+price+"\""
    # query
    query_string = "update sale set pos_id="+str(pos_id)+price+" where pos_id="+str(pos_id)+";"
    print(query_string)
    return query_string

