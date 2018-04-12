class inspection:
  def create_inspection(post_values, backroom_id):
    est_finish_date = post_values['est_finish_date']
    next_inspection = post_values['next_inspection']
    work_done = post_values['work_done']
    extra_values = ""
    if(est_finish_date != ""):
      est_finish_date = ",\""+est_finish_date+"\""
      extra_values += ",est_finish_date" 
    if(next_inspection != ""):
      next_inspection = ",\""+next_inspection+"\""
      extra_values += ",next_inspection"
    if(work_done != ""):
      work_done = ",\""+work_done+"\""
      extra_values += ",work_done"

    # query
    query_string = "insert into inspection(backroom_id"+extra_values+") values("+str(backroom_id)+est_finish_date+next_inspection+work_done+");"
    query_string = query_string.replace(",)", ")")
    print(query_string)
    return query_string

  def update_inspection(post_values, backroom_id):
    est_finish_date = post_values['est_finish_date']
    next_inspection = post_values['next_inspection']
    work_done = post_values['work_done']
    if(est_finish_date != ""):
      est_finish_date = ",est_finish_date=\""+est_finish_date+"\""
    if(next_inspection != ""):
      next_inspection = ",next_inspection=\""+next_inspection+"\""
    if(work_done != ""):
      work_done = ",work_done=\""+work_done+"\""

    # query
    query_string = "update inspection set backroom_id="+str(backroom_id)+est_finish_date+next_inspection+work_done+" where backroom_id="+str(backroom_id)+";"
    print(query_string)
    return query_string

