import User
import db

for i in range(22)
class DB:
    def __init__(self):
        self.database = {}
        self.id = 0
    def gen_database(self):
        bio=open("bios.txt", "r")#do bio.readline()
        for i in range(22)
            
    # Add a user to the database
    def add_user(self, name):
        self.database[self.id] = name
        self.id += 1
    
    # Get a user from the database
    def get_user(self, id):
        return self.database[id]
    
    # Delete the user from the database 
    def del_user(self, id):
        del self.database[id]
        
    def bindaddy(self):
        print("YESSS BINDDADDY")
    
    def size(self):
        return len(self.database)