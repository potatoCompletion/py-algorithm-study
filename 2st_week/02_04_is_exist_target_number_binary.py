finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    array.sort()
    first_target = 0
    end_target = len(array) - 1

    while first_target <= end_target:
        target_index = (first_target + end_target) // 2

        if finding_numbers[target_index] == finding_target:
            return True
        elif finding_numbers[target_index] < finding_target:
            first_target = target_index + 1
        elif finding_numbers[target_index] > finding_target:
            end_target = target_index - 1

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)