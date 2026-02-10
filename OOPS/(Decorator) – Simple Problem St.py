# Task 3 (Decorator) – Simple Problem Statement
# Problem: Permission Checker
# You want a function dashboard() but only admin should access it.
# What to do
# Create a decorator called admin_only
# Decorator behavior
# if username == "admin" → allow function execution
# else → print "Access Denied"
# Apply decorator
# Use it on:
# dashboard()
# Test
# Call dashboard using:
# admin → works
# other user → blocked
# Main point
# Decorator means:
#  ✅ adding extra security/checks to a function
#  ✅ without changing the function code


def admin_only(func):
    def wrapper(username):
        if username == "admin":
            func(username)  
        else:
            print("Access Denied")  
    return wrapper

@admin_only
def dashboard(username):
    print(f"Welcome to the dashboard, {username}!")

print("Trying with admin:")
dashboard("admin")   

print("\nTrying with normal user:")
dashboard("rahul")   
