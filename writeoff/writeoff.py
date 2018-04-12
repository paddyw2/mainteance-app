class writeoff:
  def create_writeoff(post_values, backroom_id):
    reason = post_values['reason']
    extra_values = ""
    if(reason != ""):
      reason = ",\""+reason+"\""
      extra_values += ",reason" 

    # query
    query_string = "insert into writeoff(backroom_id"+extra_values+") values("+str(backroom_id)+reason+");"
    query_string = query_string.replace(",)", ")")
    print(query_string)
    return query_string

