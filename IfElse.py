a = int(input('Enter number'));

print("Got ",a," from user");

#write a program to find the highest number
a,b,c=200,100,100;
print("Numbers are : ",a,b,c);
if(a>b and a>c):
    print(a," is the highest number");
elif(b>c):
    print(b," is the highest number");
else:
    print(c," is the highest number");

#write a program to find the highest number from the 4 different numbers
a,b,c,d=3400,450,200,46;
print("Numbers are ",a,b,c,d);
if(a>b and a>c and a>c):
    print(a," is the highest number")
elif(b>c and b>d):
    print(b," is the highest number")
elif(c>d):
    print(c," is the highest number");
else:
    print(d," is the highest number");