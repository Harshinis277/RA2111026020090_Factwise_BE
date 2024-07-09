def maxScore(cardPoints, k):
    n = len(cardPoints)
    window_sum = sum(cardPoints[:k])
    max_score = window_sum
    for i in range(1, k+1):
        window_sum += cardPoints[-i] - cardPoints[k-i]
        max_score = max(max_score, window_sum)
    return max_score
print(maxScore([1,2,3,4,5,6,1], 3))  
print(maxScore([2,2,2], 2))          
print(maxScore([9,7,7,9,7,7,9], 7))  
