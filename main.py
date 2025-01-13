import numpy

from data_loading import load_data
from calculate_mean import calculate_mean
from calculate_variance import calculate_variance
from draw_diagram import draw_diagram
from calculate_pda import pda


def show_desired_statistics(data_list, x=0):
    print("Duo to the size of date it might takes some time, pls wait...\n")
    print(f"Mean (custom code): {calculate_mean(data_list)}")
    print(f"Mean (numpy): {numpy.mean(data_list)}")
    print(f"Variance (custom code): {calculate_variance(data_list)}")
    print(f"Variance (numpy): {numpy.var(data_list)}")
    print(f"PDA : {pda(data_list, x)}\n\n")
    print("The diagrams will be saved in diagrams folder")
    draw_diagram(data_list)
    print("Diagram drawn successfully.")


if __name__ == "__main__":
    # Sample data for testing
    main_data = load_data("data/data.xlsx")
    data_list_sample1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

    # give func bellow a second arg as the value for which you want to calculate the PDF
    show_desired_statistics(main_data)







