def count_substring(string, sub_string):
    count = 0
    start = 0
    while start < len(string):
        start = string.find(sub_string, start)
        if start == -1:  # No more occurrences found
            break
        count += 1
        start += 1  # Move past this match
    return count

# Example usage
result = count_substring("ABCDCDC", "CDC")
print(result)
