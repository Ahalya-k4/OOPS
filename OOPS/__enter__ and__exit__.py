# Task 4: __enter__ and __exit__ (Context Manager Task)
# Problem Statement:
# Create a class DatabaseConnection.
# Requirements:
# Implement:
# __enter__() → print "Database Connected"
# __exit__() → print "Database Closed"
# Task:
# Use the class with with statement.
# Example:
# with DatabaseConnection():
#     print("Performing Query...")
# Expected Output:
# Database Connected
# Performing Query...
# Database Closed


class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")
        return self   

    def __exit__(self,exc_type,exc_val,exc_tb):
        print("Database Closed")

with DatabaseConnection():
    print("Performing Query...")
