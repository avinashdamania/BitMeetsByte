from PIL import Image
class User:
    def __init__(self,first_name,last_name,age,bio,count,img,skill):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
        self.bio = bio
        self.matches = []
        self.id = count
        self.img = img
        self.skill = skill

    def add_match(self,user):
        self.matches.append(user)

    def bindaddy(self):
        print("YASSSSS")z