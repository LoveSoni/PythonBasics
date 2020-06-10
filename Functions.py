def defaultFunction():
    print("in the user defined function");
defaultFunction();


#function with arguments
def functionWithArguments(name):
    print("Welcome ",name);
functionWithArguments("love");


#functional/default parameters
def functionWithOptional(name="default name"):
    print("Name : ",name);
functionWithOptional(); # it will print default name
functionWithOptional("love");

#WAP to find factorial of the given number
def getFactorial(num):
    counter = 1;
    while(num>0):
        counter = counter * num;
        num = num-1;
    return counter;

print("Factorial is : ",getFactorial(6));



#pass list to function
def functionPrintingList(list):
    for i in list:
        print(i);
functionPrintingList(["java","python","javascript"]);


#Function with return statement
def sum(a,b):
    return a+b;
print("Sum is : ",sum(10,20));


#Call method using keys
def loginMethod(username,passoword):
    print("usename and passwords are : ",username,passoword);
loginMethod("love","unknown");
loginMethod(username="no",passoword="no");
loginMethod(passoword="pass",username="user");

# *arg as argument in method
# in this we can pass multiple values
def methodWithArg(*arg):
    for i in arg:
        print(i);

methodWithArg(1,2,3,4,5);

# **arg as argument which means we can pass key value pair to function
def methodWithKeyAndValue(**arg):
    for key,value in arg.items():
        print("%s=%s"%(key,value));
methodWithKeyAndValue(name="love",age="23");


#lamda function in python
res = lambda num : num* num;
print(res(4));