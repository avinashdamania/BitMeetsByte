from User import User
import random
class DB:
    def __init__(self):
        self.database = {}
        self.id = 0
    def gen_database(self):
        bio=open("bios.txt", "r")#do bio.readline()
        age_first_last=open("age_first_last.txt","r")
        for i in range(22):
            self.add_user(*age_first_last.readline().split(),bio.readline(),"./UserInfo/photos/"+str(i)+".png",random.randInt(0,3))
    # Add a user to the database
    def add_user(self, first_name,last_name,age,bio,img,skill):
        user = User(first_name,last_name,age,bio,self.id,img,skill)
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
    
    def size(self):
        return len(self.database)