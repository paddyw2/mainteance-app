import mysql.connector

class car_handler:

  def connect_db(self):
    """
    You can test db connection using this code
    Make sure the mysql server is running and replace
    test_env with a database you created.
    cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test_env')
    cnx.close()
    """
    return True

  def select_query(self, user_input):
    return ["these", "are", "the", "results"]

  def insert_query(self, values):
    return True

  def update_query(self, values):
    return True

  def delete_query(self, values):
    return True
