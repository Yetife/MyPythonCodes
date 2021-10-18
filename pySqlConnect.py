# import needed dependencies
import mysql.connector as mysql
import getpass
from mysql.connector import Error


#define the connector function
def connect_fetch():
    '''function to connect and fetch rows in database'''
    
    #create a variable for the connector object
    conn = None
    
    host = input("Enter host: ")
    database = input("Enter database: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
   
    try:
        conn = mysql.connect(host= host, database = database, 
                             user = username, password = password)
        print('Connecting to the database server')
        if conn.is_connected:
            print('Connected to the database')
            
            #select query
            sql_insert_query = "insert into BUYER value('Boluwatife', 'Purchasing', 'Buyer 5', 'Mary Smith')"
            sql_update_query = "update BUYER set Supervisor = 'Pete Hansen' where Position = 'Manager'"
            # sql_delete_query = "delete from BUYER where Position = 'Buyer 1'"
            sql_select_query = "select * from BUYER"
            cursor = conn.cursor()
            cursor.execute(sql_insert_query)
            cursor.execute(sql_update_query)
            # cursor.execute(sql_delete_query)
            cursor.execute(sql_select_query)
            # cursor.execute(sql_insert_query)
            records = cursor.fetchall()
            print('Total number of rows in buyer is: ', cursor.rowcount)
            
            #display data from the database
            print("\nPrinting each Buyer record")
            # records.insert(5,['Boluwatife', 'Purchasing', 'Buyer 5', 'Mary Smith'])
            # records.insert(6,['Henrieta', 'Purchasing', 'Buyer 6', 'Mary Smith'])
            for row in records:
                print("BuyerName : ", row[0])
                print("Department : ", row[1])
                print("Position : ", row[2])
                print("Supervisor : ", row[3], '\n')
    except Error as e:
        print('Not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database shutdown')
connect_fetch()