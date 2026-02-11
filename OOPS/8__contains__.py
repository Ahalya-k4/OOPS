# Task 8: __contains__ (Membership Operator Task)
# Problem Statement:
# Create a class Library.
# Requirements:
# Store list of book names.
# Implement:
# __contains__(item) → return True if book exists
# Task:
# Check using:
# "Python" in library


class Library:
    def __init__(self,books):
        self.books=books

    def __contains__(self,item):
        return item in self.books
    
Library=Library(["python","Data science","AI Basics"])
print("python" in Library)