#basically just gotta copy the classes in car/car.py
class customer:
    def search_customer(post_values):
        license_no = post_values['license_no']
        if (license_no != ""):
            license_noo = " and license_no="+license_no
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
            
        query_string = "select * from customer  where"+license_no+phone_no+fname+lname+address+email
        if("where and" in query_string):
            query_string = query_string.replace("where and", "where")
        print(query_string)
        return query_string
    
