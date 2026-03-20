#  Stock Market Risk Auditor

##  Problem:
There are many beginner investors who do not understand stock volatility and risk. 
They often make decisions without analyzing price movements.

##  Solution:
This project analyzes historical stock data and identifies high-risk days 
based on percentage price movement.

##  How It Works:
- Reads stock data from CSV file
- Extracts High and Low prices
- Calculates percentage movement:
  
  (High - Low) / Low * 100

- If movement > 2%, it is classified as "High Risk"

##  Features:
- Handles missing or invalid data
- Uses percentage-based risk calculation
- Provides summary of risky days

##  How to Run:
1. Install Python
2. Place your CSV file in the same folder
3. Run:
   python risk_analysis.py

##  Limitations:
- Uses a fixed threshold (2%)
- Does not consider long-term trends
- No visualization yet

##  Future Improvements:
- Add graphs and visualization
- Use moving averages
- Apply machine learning models

##  Author
Shaurya Bhatt
