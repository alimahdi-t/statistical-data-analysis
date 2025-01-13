import math
from calculate_mean import calculate_mean

def pda(data_list, x):
    # Step 1: Check if the list is empty
    if len(data_list) == 0:
        raise ValueError("The data list is empty.")

    # Step 2: Calculate mean
    mu = calculate_mean(data_list)

    # Step 3: Calculate standard deviation
    sigma = math.sqrt(sum((val - mu) ** 2 for val in data_list) / len(data_list))

    # Step 4: Calculate PDF
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)

    return coefficient * math.exp(exponent)
