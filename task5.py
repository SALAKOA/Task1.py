# a list that contains at list on string,one int and one float
detail_of_a_boy=["faiz",22,1.2]
print(detail_of_a_boy)

#grab 2 from nested list
figure=[1,1,[1,2]]
print(figure[2][1])

#result of lst.pop()
lst=[0,1,2]
print(lst.pop())

# List can have multiple data types 
#yes

#result of lst[1:]
lst=["a","b","c"]
print(lst[1:])

"""list is used to hold or store sequence data type .and dict is a key to value pair"""

#dict with three key-value pair
items_prices={"rice":2000,"ball":200,"beans":2500}
print(items_prices)

#dict where all key are strings and all values are integers
ages_of_boys_in_class={"faiz":23,"kabir":24,"femi":30,"wale":25}
print(ages_of_boys_in_class)

#output of d["k1"][1]
d={"k1":[1,2,3]}
print(d["k1"][1])

# dict are immutable? N0,They are mutable

#grab hello
d={"simple_key":"hello"}
print(d["simple_key"])

#grab hello
my_dict={"k1":{"k2":"hello"}}
print(my_dict["k1"]["k2"])

#grab hello
my_dict={"k1":[{"nest_key":["this is deep",["hello"]]}]}
print(my_dict["k1"][0]["nest_key"][1][0])

#grab hello
my_dict={"k1":[1,2,{"k2":["this is tricky",{"tough":[1,2,["hello"]]}]}]}
print(my_dict["k1"][2]["k2"][1]["tough"][2])