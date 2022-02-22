lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
new_nums = list(filter(lambda x: x<0, lst1))
myneglist = [-x for x in new_nums]
print(myneglist)