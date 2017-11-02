#write a function to take a list of numbers and returns the cumulative sum.
#step 1
#write a function to sum the nested list
def _nestsum_(l):
    res = []
    for e in l:
        res.append(sum(e))
    return res

##print(_nestsum_([[1],[1,2],[1,2,3]]))

#step2
#write to create nexted list from standard list
def _cretenested_(l):
    index = 0
    res = []
    while index < len(l):
        tem = []
        j = 0
        while j <= index:
            tem.append(l[j])
            j = j + 1
        index = index + 1
        res.append(tem)
    return res

##print(_cretenested_([1,2,3]))

#step 3
#combine them together to get answer
def _cumlativesum_(l):
    res = []
    iml = []
    iml = _cretenested_(l)
    res = _nestsum_(iml)
    return res

print(_cumlativesum_([1,2,3]))

#another apporach, whithout using sum() function
#user accumlater instead
def _cumlativesumv2_(l):
    res = []
    index = 0
    while index < len(l):
        total = 0
        j = 0
        while j <= index:
            total = total + l[j]
            j = j + 1
        index = index + 1
        res.append(total)
    return res

print(_cumlativesumv2_([1,2,3]))





