#basically just gotta copy the classes in car/car.py
class user:
    def search_user(post_values):
        employee_no = post_values['employee_no']
        if (employee_no != ""):
            employee_no = " and employee_no="+employee_no
        phone_no = post_values['phone_no']
        if (phone_no != ""):
            phone_no = " and phone_no=\""+phone_no+"\""
        fname = post_values['fname']
        if (fname != ""):
            fname = " and fname=\""+fname+"\""
        lname = post_values['lname']
        if (lname != ""):
            lname = " and lname=\""+lname+"\""
        is_admin = post_values['is_admin']
        if (is_admin != ""):
            is_admin = " is_admin="+is_admin
        address = post_values['address']
        if (address != ""):
            address = " and address=\""+address+"\""
            
        query_string = "select * from user where"+employee_no+phone_no+fname+lname+address
        if("where and" in query_string):
            query_string = query_string.replace("where and", "where")
        print(query_string)
        return query_string
    
