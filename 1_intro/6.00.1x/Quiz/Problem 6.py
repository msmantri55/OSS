# Write a function to flatten a list. The list contains other lists, strings, 
# or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into 
# [1,'a','cat',2,3,'dog',4,5]

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flatlist = []
    for element in aList:
        if type(element) is list:
            flatlist.extend(flatten(element))
        else:
            flatlist.append(element)
    return flatlist