#Scripting style---> (small Scripts)---print("Hello,world")
#object oriented Style--->class,object-----> class demo,def sample();print(inside sample method)
#procedural Style--> methods----> def message();print("hello, world")#//

#Scaripting 
print('Hello world')

#procedural way of writing the code
def message():
    print('inside method message: Hello world')
    message()

    #object oriented way of wriring the code:
    class Demo:
        def instance_method():
            print('inside instance method, helloworld')

            d1= Demo()
            d1.instance_method
