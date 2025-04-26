#define two arrays(lists)
array1=[1,2,3,4,5,10]
array2=[1,2,6,7,8,9,10]
#convert arrays to sets and find intersection
common_values=set(array1).intersection(set(array2))
#convert the result back to a list(optional)
common_values=list(common_values)
#print the common values
print("common values between the two arrays;",common_values)

                                       
