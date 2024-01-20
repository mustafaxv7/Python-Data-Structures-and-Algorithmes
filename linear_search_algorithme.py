# Linear Search Algorithme
def linear_search(arr,var):
    isInside = False
    for i in range(len(arr)):
        if (arr[i] == var):
           isInside = True
           break
    if isInside:    
        return f'Index:{i}'
    else:
        return f'{var} Not Found'
    
var = int(input("\n\nEnter The variable that You Searching for>>: "))
our_list = list(map(int,input().split()))
print(linear_search(our_list,var))
    