import math


def calculateSoftmax(homeTeamValues, awayTeamValues):
    
    hLow, hHigh = homeTeamValues["Goal0"]
    aLow, aHigh = awayTeamValues["Goal0"]
    # print(hLow, hHigh,aLow, aHigh)
    result = [hHigh, aHigh]
    # Subtracting the maximum value for numerical stability
    max_val = max(result)
    exp_values = [math.exp(i - max_val) for i in result]
    exp_sum = sum(exp_values)
    softmaxValue = [exp_val / exp_sum for exp_val in exp_values]

    return softmaxValue
    