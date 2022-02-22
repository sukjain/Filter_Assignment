import functools

class num:

    list=[2,3,4,5,6,1]

    print(list)

    val=functools.reduce(lambda a,b:a*b, list)

    print(val) 