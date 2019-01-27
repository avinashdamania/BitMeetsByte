from User import User
class DB:
    def __init__(self):
        self.database = {}
        self.id = 0
    def gen_database(self):
        bio=open("bios.txt", "r")#do bio.readline()
        for i in range(22)
            
    # Add a user to the database
    def add_user(self, first_name,last_name,age,bio,misc):
        user = User(first_name,last_name,age,bio,misc,self.id)
        self.database[self.id] = user
        self.id += 1

    # Get a user from the database
    def get_user(self, id):
        return self.database[id]
    
    # Delete the user from the database 
    def del_user(self, id):
        del self.database[id]
        
    def add_match(self,current_id,matched_user):
        self.database[current_id].add_match(matched_user)

    def bindaddy(self):
        print("YESSS BINDDADDY")
    
    def size(self):
        return len(self.database)