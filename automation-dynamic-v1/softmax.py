import math


def calculateSoftmax(homeTeamValues, awayTeamValues):
    
    hHigh, hLow = homeTeamValues["Goal0"]
    aHigh, aLow = awayTeamValues["Goal0"]

    result = [hHigh, aHigh]
    # Subtracting the maximum value for numerical stability
    max_val = max(result)
    exp_values = [math.exp(i - max_val) for i in result]
    exp_sum = sum(exp_values)
    softmaxValue = [exp_val / exp_sum for exp_val in exp_values]

    return softmaxValue
    