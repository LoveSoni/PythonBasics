name='love';
print('name is :'+name);
print(len(name));
print(name[3]);
print(name.upper());
print("hello \n"+"world"+"\t new");
print(name*3);
name = "love";
print(name[0:4]);
newString= "lo3lovelov5";
print(name in newString);
largeString="printtest";
smallString = "test1";

print(smallString not in largeString);

#format specifier
print("My name is %s and age is %d"%("love",23));

#handle literals
print("My name is \"love soni\"");
print('printing value in \'single quotes\'');

#string build in functions

#capatilize: convert first letter of the string to the upper case
myString = "love soni";
print(myString.capitalize());

#count : count the number of occurance of letter in string
myString = "this is again this is";
print(myString.count("this is"));

#find: works like indexOf() method of java which returns the index of the string
#if not found it will return -1
myString = "findIndex";
print(myString.find("find"));

#length: find the length of the string
myString = "findLength";
print(len(myString));

#lower: will lower the entire string
myString = "LOWERSTring";
print(myString.lower());

#upper: will capatilize the entire string
myString="upperText"
print(myString.upper());

#lstrip: will trim the string from the left side
#rstring: will trim the string from the right side
myString=" lstring   and    ";
print(myString.lstrip());
print(myString.rstrip());

#min: will get the min character from the string
#max: will get the max character from the string
myString="love";
print(min(myString));
print(max(myString));

#replace: used to replace the selected string
myString="a b c";
print(myString.replace(" ",""));

#split: used to split the string
myString="java c c++";
print(myString.split(" "));
print(myString.split(" ")[1])

#is : operator used to compare string
firstString = "love";
lastString = "love";
print(firstString is lastString);
