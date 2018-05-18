def mergesort(a):

    n = len(a)

    if(n>1):
        centre = n//2

        #making the left and right matrix 
        k=0
        left=a[0:centre]
        right=a[centre:n]
            
        #applying recursive function to left and right matrix   
        mergesort(left) 
        mergesort(right)

        n1 = len(left)
        n2 = len(right)
        i = 0
        j = 0
        k = 0
        while(i<n1 and j<n2):
            if(left[i]<right[j]):
                a[k] = left[i]
                i = i + 1
                k = k + 1
            else:
                a[k] = right[j]
                j = j +1
                k = k + 1
        while(i<n1):
            a[k] = left[i]
            i=i+1
            k = k+1

        while(j<n2):
            a[k] = right[j]
            j=j+1
            k = k+1

    

#input no. of elemetns and the values into empty array a 
a = []
element = int(input("insert the no. of elements in array:"))
for i in range(0,element):              
    a.append(int(input("Enter element:")))

mergesort(a)
print(a)

