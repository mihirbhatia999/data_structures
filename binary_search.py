#Binary search

#start the binary sort function 
def bsearch(a,e,index):
    
    mid = len(a)//2
    if(e<a[mid]):
        b=a[0:mid]
        index = index[0:mid]
        bsearch(b,e,index)
        
    elif(e>a[mid]):
        b=a[mid+1:len(a)]
        index = index[mid+1:len(a)]
        bsearch(b,e,index)
        
    else:
        print(index[mid])
        return
    

#input no. of elemetns and the values into empty array a 
a = []
element = int(input("insert the no. of elements in array:"))
for i in range(0,element):              
    a.append(int(input("Enter element:")))
    
#element that we are looking for in the sorted array a 
e = int(input("insert the element that you are looking for:"))
index = list(range(len(a)))
print("element has index")
x=bsearch(a,e,index)


        
   
        
        
    
