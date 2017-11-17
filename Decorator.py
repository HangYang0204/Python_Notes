"""Functions are first class citizens and you can assign them to variables!"""

def greet0(name):
    return"hello " + name

greet_someone = greet0

##print(greet_someone("John")) #same as set greet_someone alias greet().

#variable of function type.

##print(type(greet_someone))
#in this case, the variable greet_someone works as a funciton

#another amazing thing about python is that you can define function inside
#function

def greet(name):
    def get_message():
        return "hello "
    result = get_message() + name
    return result
##print(greet("John"))

#function can also be passed as parameter to other functions
def greet1(name):
    return "hello " + name

def call_func(func):
    other_name = "john"
    return func(other_name)
##print(call_func(greet1))

#the scope of inner function and closure

def hello(name):
    def get_message():
        return "hello " + name
    return get_message()
#what if I return get_message??

a = hello("hang")
##print(a)

#an ultimate example for the above concept
################################################################
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func): #get_text is passed to parameter func
   def func_wrapper(name): #result of func(name) is passed to parameter name
       return "<p>{0}</p>".format(func(name))
   return func_wrapper
#assing a function to variable my_get_text
my_get_text = p_decorate(get_text)

##print(my_get_text("John"))

#see below example

def p_dec(name):
    return "<p>{0}</p>".format(name)

def abp_dec(func):
    def b_dec(name):
        return "<b>{0}</b>".format(func(name))
    return b_dec

a = abp_dec(p_dec)
##print(type(a))
##print(a("Hang"))
#this functionality is call decorator.
#The decorator example

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

@p_decorate
@div_decorate
@strong_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("hang"))
