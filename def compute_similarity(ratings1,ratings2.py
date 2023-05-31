from math import sqrt

def compute_similarity(ratings1,ratings2):


    sum1 = sum(ratings1)
    sum2 = sum(ratings2)
    sum1_sq = sum(rating ** 2 for rating in ratings1)
    sum2_sq = sum(rating ** 2 for rating in ratings2)
    p_sum = sum(ratings1[i] * ratings2[i] for i in range(len(ratings1)))

    n = len(ratings1)
    num = p_sum - (sum1 * sum2 / n)
    den = sqrt((sum1_sq - (sum1 ** 2) / n) * (sum2_sq - (sum2 ** 2) / n))

    if den == 0:
        return 0.0  # Division par zéro, similarité de 0

    return num / den

ratings1 = [3.0,5.0,5.0,2.0,3.0]
ratings2 = [3.0,5.0,5.0,2.0,2.0]
print(compute_similarity(ratings1,ratings2))