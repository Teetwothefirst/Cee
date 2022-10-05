import psycopg2 as pg
 
# conn = pg.connect


#this is for the dictionary type database

# #Starting another project even after I haven't finished the other ones
# #Ok we want to make an access control lock system using python
# #Let's make it inside a function and start using classes later on
# def Accesscontrollocksystem():
#     #This should house all my code;
#     def database():
#         #This would hold the users data;
#         #Create a dictionary and maybe use psycopg2 to connect to psql for postgresql maybe;
#         database = {
#             'name' : 'passkey',
#             'dexterdavid835@gmail.com' : '1234567890',
#             'dexterdavid001@gmail.com'  : '0987654321',
#             'Teetwothefirst@gmail.com' : '1029384756'
#         }
#         return database
        
#     database()
#     def auth():
#         #This is the authentication method for the application;
#         database_auth = database()
#         print(database_auth)
#         username = input("Enter your username: ")
#         passkey = input("Enter your passkey: ")
#         print(f"Your Username is {username}")
#         print(f"Your passkey is {passkey}")
        
#         # for i in database_auth:
#         #     if i ==username:
                
#         #         print(f"Success!!! Welcome{username}")
#         #         break
#         if name == username:
#             for name in database_auth:
#                 print("")
#     auth()
#     def login():
#         #This would mimic the users login by accessing the data;
#         pass
# Accesscontrollocksystem()




#This is for the array/List type database, another approach make it work then optimize
#function main
def Lock():
    def data():
        
        database = [ "dexterdavid835@gmail.com", 1234567890,"dexterdavid001@gmail.com" , 987654321,"Teetwothefirst@gmail.com", 1029384756]
        return database
    data()
    def auth():

        auth_data = data()

        print(auth_data)
        # dataUser = input("Enter any valid Username: ")
        # datakey = input("Enter a valid passkey: ")

        # #Test with if statement
        # if dataUser == auth_data[0] :
        #     if datakey == auth_data[1]:
        #         print("Record 1 Key Correct! Success")
        #     print("Record 1 Found! Success")
        # elif dataUser == auth_data[2]:
        #     if datakey == auth_data[3]:
        #         print("Record 2 Key Correct! Success")
        #     print("Record 2 Found! Success")

        # elif dataUser == auth_data[4]:
        #     if datakey == auth_data[5]:
        #         print("Record 3 Key Correct! Success")
        #     print("Record 3 Found! Success")
        # else:
        #     print("Record not found!!!")
        
       

    auth()    
    
    def login():
        def signup():
            NewUserName = input("Enter your Username: ")
            NewUserKey = input("Enter a valid Numeric key: ")
            hostconnect = data() 
            print(hostconnect)
            hostconnect.append(NewUserName)
            hostconnect.append(NewUserKey)
            print(hostconnect)
           
        signup()
        def signin():
            usersign = input()
    login()
Lock()