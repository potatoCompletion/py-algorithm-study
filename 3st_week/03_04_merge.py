array_a = [1, 2, 3, 5]
array_b = [4, 5, 6, 7, 8]


def merge(array1, array2):
    result_array = []
    first_array_index = 0
    second_array_index = 0

    while first_array_index < len(array1) and second_array_index < len(array2):
        if array1[first_array_index] < array2[second_array_index]:
            result_array.append(array1[first_array_index])
            first_array_index += 1
        elif array1[first_array_index] > array2[second_array_index]:
            result_array.append(array2[second_array_index])
            second_array_index += 1
        else:
            result_array.append(array1[first_array_index])
            result_array.append(array2[second_array_index])
            first_array_index += 1
            second_array_index += 1

    if first_array_index < len(array1):
        for i in range(first_array_index, len(array1)):
            result_array.append(array1[i])
    else:
        for i in range(second_array_index, len(array2)):
            result_array.append(array2[i])

    return result_array


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))