import matplotlib.pyplot as plt


def draw_diagram(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=50, color='skyblue', edgecolor='black')
    plt.title("Histogram of Data")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig("diagrams/histogram.png")  # Save as PNG
    plt.close()

    # Save the line plot as an image
    plt.figure(figsize=(10, 6))
    plt.plot(data, color='blue')
    plt.title("Line Plot of Data")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.savefig("diagrams/line_plot.png")  # Save as PNG
    plt.close()

