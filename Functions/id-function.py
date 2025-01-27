# id():-
# id is a built in function of python.
# -> Every python value/object has its own unique identity number. It is called as id.

# id is assign while execution of a program, it is used to identify the objects/values.
# Many people think that id() returns the memory address, but it is not 100% true, it depends on the type of the python that we are using. when we install python from the offical site of python the type of pyhton we get is 'Cpython' in which the id retuns the memory address

# for Standard python: id<=>memory address
# for python program that is running on a web brower: id is not the memory address

x=100
my_name="jay"
print(id(x))
print(id(my_name))