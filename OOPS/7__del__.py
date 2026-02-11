# Task 7: __del__ (Destructor Task)
# Problem Statement:
# Create a class Session.
# Requirements:
# Implement:
# __del__() → print "Session Ended"
# Task:
# Create an object and delete it manually using:
# del obj


class Session:
    def __del__(self):
        print("Session Ended")

obj=Session()
del obj