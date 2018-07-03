# BUBBLE SORT

#input no. of elemetns and the values into empty array a 
a = []
element = int(input("insert the no. of elements in array:"))
for i in range(0,element):              
    a.append(int(input("Enter element:")))

    
#starting bubble sort
array_length = len(a)

#no. of iterations = length of array  
for iteration in range(0,array_length):   
    maximum = a[0]
    max_index = 0
    
    #in each iteration the last element is replaced by the max 
    for element_no in range(0,array_length-iteration):  
        if(a[element_no] > maximum):
            maximum = a[element_no]
            max_index = element_no

    #swapping maximum element with the last element of that iteration   
    c = a[max_index]                   
    a[max_index] = a[array_length - iteration -1]
    a[array_length - iteration-1] = c

print("\n sorted array \n")
print(a)
