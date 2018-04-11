class rental:
  def create_rental(post_values, pos_id):
    problems = post_values['problems']
    extra_values = ""
    if(problems != ""):
      problems = ",\""+problems+"\""
      extra_values += ",problems" 
    est_return = post_values['est_return']
    if(est_return != ""):
      est_return = ",\""+est_return+"\""
      extra_values += ",est_return"
    # query
    query_string = "insert into rental(pos_id"+extra_values+") values("+str(pos_id)+problems+est_return+");"
    query_string = query_string.replace(",)", ")")
    print(query_string)
    return query_string

