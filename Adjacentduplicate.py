def remove_adjacent_duplicates_stack(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
# Example usage:
input_string = input()
output_string = remove_adjacent_duplicates_stack(input_string)
print(output_string)  # Output: "abcdef"

