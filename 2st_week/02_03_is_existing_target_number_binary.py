finding_target = 10
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    first_target = 0
    end_target = len(finding_numbers) - 1

    while first_target != end_target:
        target_index = (first_target + end_target) // 2

        if array[target_index] == target:
            return True

        if array[target_index] > target:
            end_target = target_index - 1

        if array[target_index] < target:
            first_target = target_index + 1

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)