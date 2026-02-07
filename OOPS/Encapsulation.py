#Encapsulation
#Problem Statement
#Create a program for an Instagram Account System using Encapsulation.
#Requirements
#Create a class named InstagramAccount
#Public Variable
#account_name
#Protected Variable
#_private_reels (list of strings)
#Private Variable
#__archived_reels (list of strings)
#Methods to Implement
#1. add_private_reel(reel_name)
#Adds a reel into _private_reels
#2. display_private_reels(is_follower)
#If is_follower is True → display all private reels
#Else → print "Access Denied! Only followers can view private reels"
#3. add_archived_reel(reel_name)
#Adds a reel into __archived_reels
#4. display_archived_reels(password)
#If password is correct → display all archived reels
#Else → print "Access Denied! Only account holder can view archived reels"
#5. getter method for archived reels
#Create a getter method to return archived reels only if password is correct
#6. setter method to update password
#Create a setter method to update password


class InstagramAccount:
    def __init__(self, account_name, password):
        
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print("Private reel  added.")

    
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:")
            for reel in self._private_reels:
                print("-", reel)
        else:
            print("Access Denied! Only followers can view private reels")

    
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print("Archived reel added.")

    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"

    
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Incorrect old password!")

acc = InstagramAccount("alice", "1234")
acc.add_private_reel("Dance Reel")
acc.display_private_reels(True)
acc.add_archived_reel("Old Memory Reel")

acc.display_archived_reels("1234")
acc.set_password("1234", "abcd")
