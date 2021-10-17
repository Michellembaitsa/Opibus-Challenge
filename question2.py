def  availableBike(n):
      newArr =[]
      for items in n:
            for i in range(items[0],items[1]+1): #convert items in the array to ranges, +1 enables us to loop to the next index.
                  newArr.append(i)
      newSet =set(newArr)
      if len(newSet)==len(newArr): #comparing if the length of new set == to length of new array
            return True
      else:
            return False

print(availableBike([[1,4], [2,5], [7,9]]))
print(availableBike([[6,7], [2,4], [8,12]]))
print(availableBike([[4,5], [2,3], [3,6]]))