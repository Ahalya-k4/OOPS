#Decorators:
#addstra functionality to a method without changing its original code.

# def login(login_page):
#    def wrapper(user,password):
#        if user=="admin" and password=="1234":
#            print("login succesful")
#            login_page(user,password)
#        else:
#            print("login failed")
#   return wrapper

    
# @login
# def login_page(user,password):
#    print("welcome to the dashboard")

#login_page("admin","1234")

import time
def execution_time(first_n):
    def wrapper(n):
        start=time.time()
        first_n(n)
        end=time.time()
        print(end-start)
    return wrapper

@execution_time
def first_n(n):
    sum=0
    for i in range(1,n+1):
        sum+=1
    print("sum:",sum)

first_n(1000000)