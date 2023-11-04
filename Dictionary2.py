temp_dict = {
    "sam": 92,
    "Annie": 88,
     "Harry" : 82
}
#print (temp_dict["Annie"])
#print (temp_dict.get("Harry"))
#print (temp_dict.get("XYZ",0))

# key = input ("Enter students name whose marks you want to get : ")
#print (temp_dict.get(key,0))


keys = temp_dict.keys()
for key in keys :
    #print("Student " + key)
    pass
#print (temp_dict.values())
#print (temp_dict.items())
for key in temp_dict: 
    print ("marks of" + key + " is = " + str(temp_dict[key]))