#break: break is used to break the flow in between

for i in range(1,11):
    if(i>=5):
        print("Number is greater than 5");
        break;
    print(i);

string = "lovesoni"
for i in string:
    if(i=='s'):
        continue;
    print(i);