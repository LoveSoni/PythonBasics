#while loop
counter = 1;
while(counter<=10):
    print(counter);
    counter= counter+1;
else:
    print("out from while loop");

#iteratate over list using for loop
list = [1,2,4,5];
for counter in list:
    print(counter);

#iterate list using index
list = ["love","soni"]
for i in range(len(list)):
    print(list[i]);

#nested for loop
for i in range(1,5):
    for j in range(i):
        print(j,end="")
    print()