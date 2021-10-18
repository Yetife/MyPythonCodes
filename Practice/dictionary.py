biodata = {"Name": "julie", "Age": 21, "height": "180m", "profession": "Banker"}
print ("Julie is a ", biodata["profession"])
print ("Julie is %d years old" %(biodata["Age"]))
biodata["Age"] = 25
print ("Julie is %d years old" %(biodata["Age"]))

# biodata["Company"] = "Google"
biodata.update(Company = "Google")

print (biodata)
print(biodata.values())
print(biodata.keys())
# print (str(biodata))