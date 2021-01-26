def adjacentElementsProduct(inputArray):
    new_list = []
    for i in range(len(inputArray) - 1):
        new_list.append(inputArray[i] * inputArray[i + 1])
        answer = max(new_list)

    return answer