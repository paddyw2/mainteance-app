class repair:
  def create_repair(post_values, backroom_id):
    est_finish_date = post_values['est_finish_date']
    description = post_values['description']
    parts_list = post_values['parts_list']
    extra_values = ""
    if(est_finish_date != ""):
      est_finish_date = ",\""+est_finish_date+"\""
      extra_values += ",est_finish_date" 
    if(description != ""):
      description = ",\""+description+"\""
      extra_values += ",description"
    if(parts_list != ""):
      parts_list = ",\""+parts_list+"\""
      extra_values += ",parts_list"

    # query
    query_string = "insert into repair(backroom_id"+extra_values+") values("+str(backroom_id)+est_finish_date+description+parts_list+");"
    query_string = query_string.replace(",)", ")")
    print(query_string)
    return query_string

