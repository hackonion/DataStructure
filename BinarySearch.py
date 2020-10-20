def findValue(numbers, number_to_find, low, high):
	if high >= low:
		middle = low + (high - low) // 2

		if numbers[middle] == number_to_find:
			return middle
		elif numbers[middle] < number_to_find:
			return findValue(numbers, number_to_find, middle + 1, high)
		else:
			return findValue(numbers, number_to_find, low, middle - 1)
	
	else:
		return -1


data = [1,45,46,42,56]
max_len = len(data) - 1
print(findValue(data,56,0,max_len))

