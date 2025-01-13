import numpy
from calculate_mean import calculate_mean


def calculate_variance(data_list):
    mean_value = calculate_mean(data_list)
    squared_differences = [(x - mean_value) ** 2 for x in data_list]
    return sum(squared_differences) / len(data_list)


if __name__ == "__main__":
    sample_data = [1, 2, 3, 4, 5, 6]
    variance_value = calculate_variance(sample_data)
    print(f"Variance (custom code): {variance_value}")
    print(f"Variance (numpy): {numpy.var(sample_data)}")
