class User:
    def __init__(self,first_name,last_name,age,bio,misc):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
        self.bio = bio
        self.misc = misc
        self.matches = []
    def add_match(self,user):
        self.matches.append(user)