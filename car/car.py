class car:
  def create_car(post_values):
    vin = post_values['vin'] + ","
    make = post_values['make']
    extra_values = ""
    if(make != ""):
      make = "\""+make+"\"" ","
      extra_values += ", make"
    model = post_values['model']
    if(model != ""):
      model = "\""+model+"\"" + ","
      extra_values += ", model"
    lno = post_values['lno']
    lno = "\""+lno+"\"" + ","
    status = post_values['status']
    if(status != ""):
      status = "\""+status+"\"" + ","
      extra_values += ", status"
    description = post_values['description']
    if(description != ""):
      description = "\""+description+"\"" + ","
      extra_values += ", description"

    # query
    query_string = "insert into car(vin_no, license_plate"+extra_values+") values("+vin+lno+make+model+status+description+");"
    query_string = query_string.replace(",)", ")")
    print(query_string)
    return query_string

  def update_car(post_values):
    vin = post_values['vin']
    make = post_values['make']
    extra_values = ""
    if(make != ""):
      make = "make=\""+make+"\"" ","
    model = post_values['model']
    if(model != ""):
      model = "model=\""+model+"\"" + ","
    lno = post_values['lno']
    if(lno != ""):
      lno = "license_plate=\""+lno+"\"" + ","
    status = post_values['status']
    if(status != ""):
      status = "status=\""+status+"\"" + ","
    description = post_values['description']
    if(description != ""):
      description = "description=\""+description+"\"" + ","

    # query
    query_string = "update car set "+make+model+lno+status+description+" where vin_no="+vin+";"
    query_string = query_string.replace(", where", " where")
    print(query_string)
    return query_string


  def search_car(post_values):
    vin = post_values['vin']
    if(vin != ""):
      vin = " vin_no="+vin
    make = post_values['make']
    if(make != ""):
      make = " and make=\""+make+"\""
    model = post_values['model']
    if(model != ""):
      model = " and model=\""+model+"\""
    lno = post_values['lno']
    if(lno != ""):
      lno = " and license_plate=\""+lno+"\""
    status = post_values['status']
    if(status != ""):
      status = " and status=\""+status+"\""
    description = post_values['description']
    if(description != ""):
      description = " and description=\""+description+"\""
    # query
    query_string = "select * from car where"+vin+make+model+lno+status+description
    if("where and" in query_string):
      query_string = query_string.replace("where and", "where")
    print(query_string)
    return query_string
