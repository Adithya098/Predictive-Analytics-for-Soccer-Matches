import math


def calculate_softmax(parsed_values):
    # goals = ["Goal0", "Goal1", "Goal2", "Goal3", "Goal4"]
    
    
    # probability_ranges = []
    # for goal in goals:
    #     range_ = parsed_values[goal]
    #     probability_ranges.append(range_)
    
    # average_probabilities = np.mean(probability_ranges, axis=1)
    # softmax_value = np.exp(average_probabilities) / np.sum(np.exp(average_probabilities), axis=0)
    
    
    high, low = parsed_values["Goal1"]
    softmax_value = math.exp((high + low) / 2) / (math.exp(high) + math.exp(low))
    
    
    
    return softmax_value
    