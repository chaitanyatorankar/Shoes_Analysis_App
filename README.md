# Shoes_Analysis_App

# Data Description 

The Shoes Sales Analysis & Region Estimator is a data-driven, interactive web application designed to help footwear companies and analysts gain meaningful insights into sales, returns, and inventory across different regions and subsidiaries. Built using Python, Pandas, Seaborn, Matplotlib, and Streamlit, the app transforms raw sales data into clear, actionable visualizations for informed business decision-making.

# Dataset Field

-Region : Description: The geographic region where the subsidiary operates.
Purpose in App: Used for filtering and region-based sales analysis. (E.g North America, Europe, Asia-Pacific.)

-Subsidiary: Description: Name of the company branch or store within the region.
Purpose in App: Shown on the bar chart X-axis to compare performance across subsidiaries in the selected region. (E.g Nike USA, Adidas UK, Puma India.)

-Sales: Description: Total sales revenue for the subsidiary in the given region.
Purpose in App: Plotted on the Y-axis of the bar chart to visualize performance. (e.g $120,000, $95,500 (converted to 120000, 95500).

-Returns: Description: Total monetary value of product returns for the subsidiary.
Purpose in App: Could be used for future enhancements like return rate analysis. (E.g $5,000, $3,200 (converted to 5000, 3200).

-Inventory: Description: Current inventory value or stock on hand for the subsidiary.
Purpose in App: Useful for tracking stock levels and balancing supply with demand. (E.g  $45,000, $50,300 (converted to 45000, 50300).

# Key Focus Area

📊 Region-Wise Sales Performance: Analyze and compare sales data across different regions to identify high-performing and low-performing areas.

🏢 Subsidiary Comparison: Evaluate individual subsidiaries within a selected region to detect top revenue generators and those needing attention.

🧹 Data Cleaning & Accuracy: Ensure numeric fields like Sales, Returns, and Inventory are properly cleaned and converted for precise calculations.

📈 Visual Data Insights: Use bar plots to provide clear, easy-to-understand visualizations for quick decision-making.

🌐 Interactive User Experience: Implement a Streamlit-based interface that allows users to explore data dynamically without technical barriers.

📦 Inventory & Returns Tracking (Future Enhancement): Incorporate returns and inventory data into advanced metrics such as return rates and stock turnover.
