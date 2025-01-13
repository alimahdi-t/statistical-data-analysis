import numpy


def calculate_mean(data_list):
    return sum(data_list) / len(data_list)


if __name__ == "__main__":
    sample_data = [1, 2, 3, 4, 5, 6]
    mean_value = calculate_mean(sample_data)

    print(f"Mean (custom code): {mean_value}")
    print(f"Mean (numpy): {numpy.mean(mean_value)}")