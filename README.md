# Chain Store Sales Analysis

## Project Overview

This project analyzes sales and profit data from a chain store using Python, Pandas, and Matplotlib. The goal is to identify top-performing products, compare city performance, examine monthly sales trends, and generate insights that can support business decision-making.

## Dataset

The dataset contains 30 records and includes the following fields:

- `Date`: Transaction date
- `Product`: Product name
- `City`: Sales city
- `Employee`: Employee responsible for the sale
- `Quantity`: Quantity sold
- `Price`: Selling price per unit
- `Cost`: Cost per unit
- `Sales`: Total sales amount

The `Profit` column is calculated in Python.

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- Microsoft Excel

## Data Analysis

The project includes the following analyses:

- Total sales and profit by product
- Total sales and profit by city
- Profit by product and employee using a pivot table
- Profit by city for a selected product
- Monthly sales analysis

## Key Findings

- **Laptop** generated the highest sales and profit among the products.
- **Keyboard** had the lowest total sales and profit.
- **Rasht** generated the highest total profit among the cities.
- **Tehran** had the highest total sales amount.
- **June** recorded the highest total sales and profit in the dataset.
- Sales and profit comparisons between employees should be interpreted carefully because employees did not sell every product type.

## Visualizations

The project includes four charts:

1. `profit_by_product.png` — Profit by Product
2. `sales_by_product.png` — Sales by Product
3. `profit_by_city.png` — Profit by City
4. `sales_by_month.png` — Sales by Month

## How to Run the Project

1. Download or clone this repository.
2. Make sure Python is installed.
3. Install the required libraries:

   ```bash
   pip install pandas matplotlib openpyxl
   ```

4. Keep `chain_store.py` and `chain_store.xlsx` in the same directory.
5. Run the Python script:

   ```bash
   python chain_store.py
   ```

The script performs the analysis and generates the charts.

## Business Recommendations

- Maintain or strengthen marketing efforts for high-performing products such as laptops.
- Investigate why keyboard sales were zero in March and June.
- Examine differences in sales and profitability across cities.
- Review employee performance alongside product allocation and sales opportunities.
- Collect additional operational data to support more detailed analysis.

## Limitations

- The dataset contains only 30 records, so findings should be interpreted within the scope of this sample.
- Unit costs are assumed to be fixed for each product.
- The dataset does not contain records for every month; therefore, missing months should not be interpreted as months with zero sales.
- Employees did not have equal opportunities to sell all product types, which limits direct performance comparisons.

## Project Purpose

This project demonstrates practical skills in data cleaning, data transformation, exploratory data analysis, aggregation, pivot tables, visualization, and business reporting using Python.
