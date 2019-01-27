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
        skillDict = {0:"FrontEnd Dev",1:"BackEnd Dev",2:"Mobile Dev",3:"Web Dev"}
        self.skill = skillDict[skill]

    def add_match(self,user):
        self.matches.append(user)
    def remove_matches(self,DB):
        for i in [x.id for x in self.matches]:
            DB[x].matches=[y for y in DB[x].matches if y != self]
        self.matches.clear()
