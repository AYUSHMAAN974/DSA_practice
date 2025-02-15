string=input("Enter the array:")
arr=list(map(int,string.split()))

def selection_sort(lst):
    for i in range(0,len(list)-1):
        mini=i
        for j in range(i+1,len(list)):
            if list[j]<list[mini]:
                mini=j
        list[mini],list[i]=list[i],list[mini]
    return lst

print(selection_sort(arr))
    
        