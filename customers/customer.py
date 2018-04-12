#basically just gotta copy the classes in car/car.py
class customer:
    def search_customer(post_values):
        license_no = post_values['license_no']
        if (license_no != ""):
            license_no = " and license_no="+license_no
        phone_no = post_values['phone_no']
        if (phone_no != ""):
            phone_no = " and phone_no=\""+phone_no+"\""
        fname = post_values['fname']
        if (fname != ""):
            fname = " and fname=\""+fname+"\""
        lname = post_values['lname']
        if (lname != ""):
            lname = " and lname=\""+lname+"\""
        address = post_values['address']
        if (address != ""):
            address = " and address=\""+address+"\""
        email = post_values['email']
        if (email != ""):
            email = " and email=\""+email+"\""        
            
        query_body = license_no+phone_no+fname+lname+address+email
        if(query_body == ""):
          query_string = "select * from customer"
        else:
          query_string = "select * from customer  where"+license_no+phone_no+fname+lname+address+email
        if("where and" in query_string):
            query_string = query_string.replace("where and", "where")
        print(query_string)
        return query_string

    # Function for creating a customer
    def create_customer(post_values):
        license_no = "\"" + post_values['license_no'] + "\","
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
            
        address = post_values['address']
        if (address != ""):
            address = "\""+address+"\","
            extra_values += ", address"

        email = post_values['email']
        if (email != ""):
            email = "\""+email+"\","
            extra_values += ", email"

        query_string = "insert into customer (license_no"+extra_values+") values("+license_no+phone_no+fname+lname+address+email+");" 

        query_string = query_string.replace(",)",")")
        print(query_string)
        return query_string
    
