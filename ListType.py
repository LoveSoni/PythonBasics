#Following is the way to define list in the java
#List list = new ArrayList<>(){
#{
# add(1);add(2);
#}
#}

#define list in python
id = [10,20,30,"dummy"]
print(id);

#get item using index in list
print("item at the position",id.__getitem__(3));
print("item at position using []",id[2]);
print("item with in range",id[0:3]);

#print the length of list
print(len(id));

#append value in the list
list = [1,2];
list.append(100);
print("append list",list);

#concate list: in java we used to have a add method to add another list collection
list1 =[1,2,3];
list2 = [4];
print(list1 + list2);

#replace value on existing index
newList = [1,2,3];
newList[1]=-7;
print(newList);


