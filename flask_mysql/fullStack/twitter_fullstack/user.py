from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.handle = data['handle']
        self.birthday = data['birthday']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    @classmethod
    def all_users(cls):
        query = "SELECT * FROM users;"                              #declare query
        results = connectToMySQL('twitter').query_db(query)         #run function that calls on query
        print(results)                                              #parce through the query
        users = []
        #loop through results                                       #always check for spelling errors or that variable is call on
        for user_data in results: 
            #call on (cls)
                #User(user_data)
            # user = cls(user_data) #or users.append(cls(user_data))
            # users.append(user)
            users.append(cls(user_data))
        
        return users

    @classmethod
    def one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        results = connectToMySQL('twitter').query_db(query, data)
        print(results)
        return cls(results[0])