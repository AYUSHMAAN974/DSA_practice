prices=[100,101,99,98,90,100,97]

def maxPrices(list1):
    arr=[]
    for i in range(len(list1)):
        found=False
        for j in range(i+1,len(list1)):
            if list1[j]>list1[i]:
                arr.append(j-i)
                found=True
                break
        if found==False:
            arr.append(0)
        
    return arr

print(maxPrices(prices))
