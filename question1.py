#Solved using the sliding window technique.



def findMaxSubAverage(arr):
    k=2 #the size subarray.
    maxSum=windowSum=sum(arr[:k]) #maxSum == to the windowSum ending at k.
    for i in range(k,len(arr)):
        windowSum+=arr[i]-arr[i-k] #moving to new window
        maxSum=max(maxSum,windowSum)
        return maxSum / k
print(findMaxSubAverage([2,3,4,1,5]))


