def distribute_candies(ratings, n):
    candies = [1]*n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    
    sum = candies[-1]
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
        sum += candies[i]
    
    return sum


if __name__ == '__main__':
    Ratings = [1, 5, 2, 1]
    N = len(Ratings)
    total_candies = distribute_candies(Ratings, N)
    print(f'Total candies distributed: {total_candies}')