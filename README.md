🚗 Used Car Price Dashboard Report
📘 Introduction
This report provides an insightful analysis of used car pricing trends using interactive data visualization techniques. Built with Streamlit, this dashboard empowers users to explore how key vehicle features influence the resale value of cars.

The primary goals of this project are to:
- Analyze car features impacting price
- Enable dynamic visual exploration
- Build a user-friendly dashboard for insights
📊 Dataset Overview
The dataset used contains detailed attributes of second-hand cars listed for resale.
🔑 Key Features:
Attribute	Description
year	Year of manufacture
selling_price	Resale value in INR
fuel	Type of fuel used (Petrol, Diesel, etc.)
seller_type	Individual or dealer
transmission	Manual or automatic
owner	Number of previous owners
km_driven	Kilometers driven
engine_cc	Engine capacity
max_power	Maximum horsepower
mil_kmpl	Mileage in km/l
torque_rpm	Torque RPM value
🧹 Data Preprocessing
- Missing values were identified and handled
- Columns like max_power, torque, and mileage were cleaned and converted to numeric
- New derived columns were created:
  - mil_kmpl (Mileage as float)
  - max_power_new
  - torque_rpm
📈 Exploratory Data Analysis (EDA)
The Streamlit dashboard allows users to select from multiple chart types for interactive exploration.
✨ Visuals Included:
1. Trend Over Time (Line Chart)
2. Categorical Comparisons (Bar Charts, Box Plot, Count Plot)
3. Relationship Insights (Scatter Plots)
4. Distributions (Pie Charts)
🧠 Feature Engineering
The following transformations were made for enhanced analysis:
New Feature	Description
mil_kmpl	Cleaned mileage value as float
max_power_new	Numerical conversion of power data
torque_rpm	Extracted numeric RPM values from textual torque entries
📊 Key Insights
- Diesel cars show higher resale value than petrol cars on average.
- Automatic cars generally fetch higher prices than manual ones.
- Engine CC and Max Power have a strong positive correlation with price.
- Higher KM Driven tends to reduce the resale price.
- More recent models retain more value.
🖥️ Application Deployment
This project features a fully functional dashboard:
Tech	Description
Streamlit	Web app framework for interactive data apps
Seaborn / Matplotlib	Plotting libraries
Pandas	Data manipulation and analysis
Launch with:

streamlit run car_app.py

 
✅ Conclusion
This dashboard successfully showcases how data visualization can reveal valuable insights into the used car market. From understanding fuel efficiency trends to examining seller behaviors, this tool helps users make data-informed decisions.

🔮 Future Enhancements:
- Integrate machine learning for price prediction
- Add filtering by brand or city
- Upload user datasets for custom exploration

This project lays the foundation for a complete car price intelligence platform.
