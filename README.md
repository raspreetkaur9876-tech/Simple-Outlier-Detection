# Simple Outlier Detection

## Project Overview
This project identifies unusual values (outliers) in a dataset using the Interquartile Range (IQR) method with Python.

## Objective
To detect unusually high or low values in student marks and understand how outliers affect data analysis.

## Technologies Used
- Python
- Pandas
- Matplotlib

## Methodology
1. Load the dataset using Pandas.
2. Calculate Q1 (First Quartile).
3. Calculate Q3 (Third Quartile).
4. Calculate the Interquartile Range (IQR).
5. Calculate lower and upper limits.
6. Identify outliers.
7. Visualize the results using a box plot.

## IQR Formula

IQR = Q3 - Q1

Lower Limit = Q1 - 1.5 × IQR

Upper Limit = Q3 + 1.5 × IQR

## Dataset
The project uses a sample student marks dataset containing 15 records.

## Expected Results
- Student M (95 marks): Outlier
- Student N (5 marks): Outlier

## Project Files
- `data.csv` – Dataset
- `outlier_detection.py` – Main Python code
- `requirements.txt` – Required libraries
- `README.md` – Project documentation

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python outlier_detection.py
```

## Conclusion
This project demonstrates how the IQR method can identify unusual values in a dataset and how box plots help visualize outliers.