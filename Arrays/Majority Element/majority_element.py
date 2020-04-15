def find_majority_element(a, n):
        count_map = {}
        max_count = 0
        majority_element = a[0]
        for i in range(n):
            if a[i] in count_map:
                count_map[a[i]] += 1
            else:
                count_map[a[i]] = 1
            if count_map[a[i]] > max_count:
                max_count = count_map[a[i]]
                majority_element = a[i]
        
        return majority_element if max_count > n // 2 else None


if __name__ == '__main__':
    A = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    N = len(A)
    majority_element = find_majority_element(A, N)
    if majority_element:
        print(f'Majority element: {majority_element}')
    else:
        print('There is no majority element.')