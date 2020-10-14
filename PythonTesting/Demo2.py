values = [1, 2, "Lakshmi",3]

print(values[0])   #1

#List is a data type which accepts multiple values with different data types.

print(values[1:3]);  #[2, 'Lakshmi']

values.insert(3, "Shetty") #[1, 2, 'Lakshmi', 'Shetty', 3]

print(values);

values.append("End");
print(values);   #[1, 2, 'Lakshmi', 'Shetty', 3, 'End']

values[2] = "Rathna"
del values[0]

print(values)  #[2, 'Rathna', 'Shetty', 3, 'End']


val = ( 1, 2, 3, "test");
print(val);

#Tuple is same as list data type,but data is immutable.

#val[1] = "qwe";
print(val)

dic = {"a" : 3, 4: "Hello World", "a" :2}
print(dic["a"])
print(dic[4])


dict = {}

dict["FirstName"] = "Rahul"
dict["LastName"]  = "Shetty"
print(dict)                           #{'FirstName': 'Rahul', 'LastName': 'Shetty'}

print(dict["LastName"]);              #Shetty

a=2
print("The value is "+a)