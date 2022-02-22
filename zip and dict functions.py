list1 = ["Netflix", "Hulu", "Sling", "Hbo"]
list2 = [198, 166, 237, 125]

print("Original key list is : " + str(list1))
print("Original value list is : " + str(list2))

res = dict(zip(list1, list2))

print("Resultant dictionary is : " + str(res))
