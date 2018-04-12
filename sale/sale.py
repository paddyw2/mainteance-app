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

