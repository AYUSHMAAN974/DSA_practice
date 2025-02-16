string=input("Enter the array:")
arr=list(map(int,string.split()))

def bubble_sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(0,i):
            if lst[j+1]<lst[j]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                swapped = True
        if not swapped:  
            break
    return lst

        
print(bubble_sort(arr))