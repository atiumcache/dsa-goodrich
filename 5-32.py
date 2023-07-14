"""Write a python function that takes two 3-D numeric data sets and adds them component-wise."""
def addingTwo3DSets(A, B):
    totalSum = 0;
    for i in range(3):
        totalSum += (A[i] + B[i])
    return totalSum

"""Testing."""
setOne = [i for i in range(3)]
setTwo = [i for i in range(3, 6)]
print(addingTwo3DSets(setOne, setTwo))