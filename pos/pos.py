class pos:
  def create_pos(event_id, assigned_id):
    # query
    if(assigned_id == ""):
      optional_values = ""
      license_no = ""
    else:
      optional_values = ", license_no"
      license_no = ", \"" + str(assigned_id) +"\""
    query_string = "insert into pos(event_id" + optional_values + ") values("+str(event_id) + license_no+");"
    print(query_string)
    return query_string

  def update_pos(assigned_id, event_id):
    # query
    if(assigned_id == "" or assigned_id == "None"):
      optional_values = ""
      license_no = ""
    else:
      license_no = ", license_no=\"" + str(assigned_id) + "\""
    query_string = "update pos set event_id="+str(event_id) + license_no + " where event_id="+str(event_id)+";"
    print(query_string)
    return query_string
