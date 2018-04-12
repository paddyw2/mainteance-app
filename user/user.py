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
            if (is_admin.upper() == "YES"):
                is_admin = "and is_admin=1"
            elif(is_admin.upper() == "NO"):
                is_admin = "and is_admin=0"
            else:
                is_admin = ""
        address = post_values['address']
        if (address != ""):
            address = " and address=\""+address+"\""
            
        query_string = "select * from user where"+employee_no+phone_no+fname+lname+is_admin+address
        if("where and" in query_string):
            query_string = query_string.replace("where and", "where")
        print(query_string)
        return query_string
    

    def create_user(post_values):
        employee_no = post_values['employee_no'] + ","
        extra_values = ""
        phone_no = post_values['phone_no']
        if (phone_no != ""):
            phone_no = "\""+phone_no+"\","
            extra_values += ", phone_no"

        fname = post_values['fname']
        if (fname != ""):
            fname = "\""+fname+"\","
            extra_values += ", fname"

        lname = post_values['lname']
        if (lname != ""):
            lname = "\""+lname+"\","
            extra_values += ", lname"
        is_admin = post_values['is_admin']
        print("is_admin value : " + is_admin)
        if (is_admin != ""):
            if (is_admin.upper() == "YES"):
                is_admin = "1,"
                extra_values += ", is_admin"
            elif(is_admin.upper() == "NO"):
                is_admin = "0,"
                extra_values += ", is_admin"
            else:
                is_admin = ""
        address = post_values['address']
        if (address != ""):
            address = "\""+address+"\","
            extra_values += ", address"

        query_string = "insert into user (employee_no"+extra_values+") values("+employee_no+phone_no+fname+lname+is_admin+address+");" 

        query_string = query_string.replace(",)",")")
        print(query_string)
        return query_string
