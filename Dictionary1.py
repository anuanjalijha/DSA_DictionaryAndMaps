temp_dict = dict({
    "sam": 92,
    "Harry" : 82,
    "Annie": 88
})
print (temp_dict)
temp_dict2 = dict([
    ("sam", 92),
    ("Harry" , 82),
    ("Annie", 88)
])
print(temp_dict2)
temp_dict3 = {
    "sam": 90,
    "Harry" : 85,
    "Annie": 80
}
print(temp_dict3)
#print(type(temp_dict),type(temp_dict2),type(temp_dict3))
keys = ["sam","Harry","Anne"]
temp_dict4=dict.fromkeys(keys,0)
print(temp_dict4)
print(type (temp_dict4))
temp_dict5= temp_dict
temp_dict5["Harry"]=77
print(temp_dict)
print(temp_dict5)

print(len(temp_dict5))