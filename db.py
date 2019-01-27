from User import User
import random
class DB:
    def __init__(self):
        self.database = {}
        self.id = 0
    def gen_database(self):
        bio=open("./UserInfo/bios.txt", "r")#do bio.readline()
        age_first_last=open("./UserInfo/first_last_age.txt","r")
        for i in range(21):
            self.add_user(*(age_first_last.readline().split()),bio.readline(),"./UserInfo/photos/"+str(i)+".png",random.randint(0,3))
    # Add a user to the database
    def add_user(self, first_name,last_name,age,bio,img,skill):
        self.database[self.id] = User(first_name,last_name,age,bio,self.id,img,skill)
        self.id += 1
    def find_match(self, id):
        return random.choice([y for y in self.database.values() if y.skill!=self.database[id].skill]).id
    # Get a user from the database
    def get_user(self, id):
        return self.database[id]
    # Clear a user's matches
    def remove_User_matches(self,id):
        for i in  self.database[id].matches:
            self.database[i].matches=[y for y in self.database[i].matches if y != id]
        self.database[id].remove_matches()
    # Delete the user from the database 
    def del_user(self, id):
        del self.database[id]
        
    def add_match(self,current_id,matched_user):
        self.database[current_id].add_match(matched_user)
        self.database[matched_user].add_match(current_id)
    
    def size(self):
        return len(self.database)