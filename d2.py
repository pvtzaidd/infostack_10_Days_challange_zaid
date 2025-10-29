def find_max_min(arr, mode='both'):
    if not arr:
        return None, None

    max_value = min_value = arr[0]

    for num in arr[1:]:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    if mode == 'max':
        return max_value, None
    elif mode == 'min':
        return None, min_value
    else:
        return max_value, min_value

arr = list(map(int, input(f"Enter  integers separated by spaces: ").split()))

print("Choose option:")
print("1. Find only maximum")
print("2. Find only minimum")
print("3. Find both maximum and minimum")
choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    max_value, _ = find_max_min(arr, mode='max')
    print(f"Maximum: {max_value}")
elif choice == '2':
    _, min_value = find_max_min(arr, mode='min')
    print(f"Minimum: {min_value}")
elif choice == '3':
    max_value, min_value = find_max_min(arr)
    print(f"Maximum: {max_value} Minimum: {min_value}")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")