# 🚀 Sales ETL & Visualization Project
This project uses PySpark to perform ETL (Extract, Transform, Load) operations on sales data and Matplotlib/Seaborn to visualize insights.
# 📋 Project Overview
The project is designed to process sales data from a CSV file, load it into a MySQL database, and generate visual insights.
Main functionalities:
ETL Process:
Extract data from CSV
Transform and clean data (e.g., correct types, add calculated columns)
Load data into MySQL
Data Visualization:
Total sales per product line
Total sales per country
Sales distribution per deal size
# 🗂️ Project Structure
data/
sales_data.csv
screenshots/
Figure_2.png
Figure_3.png
Figure_4.png
src/
extract.py
transform.py
load.py
visualize.py
.env
requirements.txt
README.md
# 🛠️ Technologies Used
Python 3.14
PySpark
MySQL
Pandas, Matplotlib, Seaborn
# ⚙️ Setup Instructions
Clone the repository and navigate to the folder.
Create a virtual environment and activate it.
Install dependencies using pip install -r requirements.txt.
Configure the .env file with your MySQL credentials:
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_DB=salesdb
# ▶️ How to Run
Run the ETL script to load data into MySQL: python src/load.py
Run the visualization script: python src/visualize.py
# 🖼️ Screenshots
## Sales per Product Line
![Screenshot 1](screenshots/figure_1.png)
## Sales per Country
![Screenshot 2](screenshots/figure_2.png)
## Sales per Deal Size
![Screenshot 3](screenshots/figure_3.png)

# ⚠️ Notes
The .env file should not be pushed to GitHub. It is included in .gitignore.
Make sure the MySQL connector JAR is correctly referenced in your PySpark scripts.




