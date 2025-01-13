
# Statistical Data Analysis Project

This repository contains a project for statistical data analysis using Python. It includes functions to calculate basic statistical measures, draw diagrams, and analyze probability density. The project follows a modular structure with individual scripts for each task.

## 📂 Project Structure
```
statistical-data-analysis/
│
├── data/
├── diagrams/              # Contains generated diagram images
├── data_loading.py        # Script to load data from files
├── draw_diagram.py        # Script to draw diagrams (histograms, plots)
├── calculate_mean.py      # Function to calculate the mean of a dataset
├── calculate_variance.py  # Function to calculate the variance of a dataset
├── calculate_pda.py       # Probability density analysis function
└── main.py                # Main entry point to run the analysis
```

---

## ⚙️ Scripts Overview

### 1️⃣ `data_loading.py`
- **Purpose:** Loads input data from a file (e.g., `.csv`, `.txt`).
- **Usage:**
  ```bash
  python data_loading.py
  ```
- **Functionality:**  
  - Reads data from a file.
  - Prepares the dataset for analysis.

---

### 2️⃣ `calculate_mean.py`
- **Purpose:** Calculates the mean (average) of a dataset.
- **Usage:**
  ```bash
  python calculate_mean.py
  ```
- **Functionality:**  
  - Takes a list of numbers as input.
  - Outputs the mean value.

---

### 3️⃣ `calculate_variance.py`
- **Purpose:** Computes the variance of a dataset.
- **Usage:**
  ```bash
  python calculate_variance.py
  ```
- **Functionality:**  
  - Takes a list of numbers as input.
  - Outputs the variance.

---

### 4️⃣ `calculate_pda.py`
- **Purpose:** Analyzes the Probability Density Function (PDF) of the dataset.
- **Usage:**
  ```bash
  python calculate_pda.py
  ```

---

### 5️⃣ `draw_diagram.py`
- **Purpose:** Draws diagrams such as histograms and line plots.
- **Usage:**
  ```bash
  python draw_diagram.py
  ```
- **Functionality:**  
  - Takes the analyzed data and generates visual diagrams.
  - Saves the diagrams in the `diagrams/` folder.

---

### 6️⃣ `main.py`
- **Purpose:** Main entry point for running the entire analysis workflow.
- **Usage:**
  ```bash
  python main.py
  ```
- **Functionality:**  
  - Loads the data.
  - Calculates statistical measures.
  - Draws diagrams.
  - Saves results in the `diagrams/` folder.

---

## 📊 Project Requirements
Make sure you have the following libraries installed before running the project:

```bash
pip install numpy matplotlib
```

---

## 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/username/statistical-data-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd statistical-data-analysis
   ```
3. Run the main script:
   ```bash
   python main.py
   ```

---

## 📄 Reports
After running the analysis, the generated diagrams will be saved in the `diagrams/` folder. You can use these diagrams in your reports.

---

## 🧑‍💻 Contributors
- **Project Lead:** [Ali Mahdi]
- **Tools Used:** Python, Matplotlib, NumPy
