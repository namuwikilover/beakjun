def getMedian(li) :
    li_len = len(li)
    li_center = int(li_len / 2)
    return li[li_center]

li = [1, 2, 3, 5, 4]

#result =getMedian(li)#중간값.
#print(max(li))#최댓값.
print(max(li)-min(li))#범위