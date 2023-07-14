"""Use standard control structures to compute the sum of 
all numbers in an (n x n) data set, represented as a list of lists."""

def sumOfListOfLists(dataSet): 
    totalSum = 0
    for listOfNums in dataSet:
        totalSum += sum(listOfNums)
    return totalSum

someData = [[1, 2, 3], [2, 3, 4], [1, 1, 1]]
print(sumOfListOfLists(someData))
