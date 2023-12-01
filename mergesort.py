def merge_sort(A):
    if len(A)>1:
        #splitting input array
        print('splitting',A)
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        print(left,right)
        #recursive calls to mergesort for left and right sub arrays
        merge_sort(left)
        merge_sort(right)
        #initialize the pointers for left(i) for right (j) and output array (k)
        i=j=k=0
        #traverse and merges the sorted array
        while i < len(left) and j<len(right):
            if left[i]<right[j]:
                A[k] = left[i]
                i+=1
            else:
                A[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            A[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            A[k] = right[j]
            j+=1
            k+=1
    print('merging ',A)
    return(A)

print(merge_sort([356,97,846,215]))
    
    
        