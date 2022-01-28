# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL


# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #============================================
    # 1. Get all Users from database
    #============================================
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        print(results)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user_data in results:
            users.append( cls(user_data) )
        return users

    #============================================
    # 2. Creat one user in database
    #============================================

    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, created_at) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW());
        """ 
        results = connectToMySQL('users_schema').query_db(query, data)
        print(results)
        return results

    # #============================================
    # # 3. Get one user from database
    # #============================================

    @classmethod
    def one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        results = connectToMySQL('users_schema').query_db(query, data)
        # print(results)
        return cls(results[0])

    # #============================================
    # # 4. Edit one user from database
    # #============================================

    @classmethod
    def update(cls, data):
        query = """
        UPDATE users 
        SET 
            first_name = %(first_name)s, 
            last_name = %(last_name)s, 
            email = %(email)s,
            updated_at = NOW()
        WHERE id = %(edit_user)s;
        """
        # results = connectToMySQL('users_schema').query_db(query, data)
        # print(results)
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(user_id)s;"
        return connectToMySQL('users_schema').query_db(query, data)