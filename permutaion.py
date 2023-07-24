class Permutations:
    def permute(self, nums):
        def backtrack(temp_list):
            # If the tempList has the same length as nums, it is a permutation
            if len(temp_list) == len(nums):
                result_list.append(temp_list[:])
                return

            for number in nums:
                # Skip if we already have the number in the tempList
                if number in temp_list:
                    continue

                # Add the new number to the tempList
                temp_list.append(number)

                # Go back to try other numbers
                backtrack(temp_list)

                # Remove the last added number to backtrack
                temp_list.pop()

        result_list = []
        backtrack([])
        return result_list


# Example usage:
nums = [1, 2, 3]
permutations = Permutations().permute(nums)
print(permutations)
