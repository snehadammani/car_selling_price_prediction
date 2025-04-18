import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn theme for better visuals
sns.set_theme(style="whitegrid", palette="muted")

# Page setup
st.set_page_config(page_title="Car Price Visualizations", layout="wide")

# ------------------ HEADER ------------------
st.markdown("<h1 style='text-align: center;'>🚗 Car Price Data Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Explore price trends and insights for used cars</p>", unsafe_allow_html=True)

# ------------------ LOAD DATA ------------------
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\RAHUL\Desktop\Project\car_selling_price_prediction\Car details.csv")
    return df

df = load_data()

# Optional: Show data
with st.expander("🔍 Click to view raw data"):
    st.dataframe(df, use_container_width=True, height=250)

# ------------------ SELECT VISUAL ------------------
chart_options = [
    "Year vs Selling Price (Line Chart)",
    "Fuel vs Selling Price (Bar Chart)",
    "Seller Type vs Selling Price",
    "Transmission vs Selling Price",
    "Owner vs Selling Price",
    "Seats vs Selling Price (Box Plot)",
    "KM Driven vs Selling Price",
    "Engine CC vs Selling Price",
    "Max Power vs Selling Price",
    "Mileage vs Selling Price",
    "Torque RPM vs Selling Price",
    "Fuel Type Distribution (Pie)",
    "Seller Type Distribution (Pie)",
    "Transmission Distribution (Pie)",
    "Owner Count (Bar Chart)"
]

selected_chart = st.selectbox("📊 Choose a visualization", chart_options)

# ------------------ TITLE DISPLAY ------------------
st.markdown(
    f"<div style='background-color:#f0f2f6;padding:10px;border-radius:10px;margin-top:20px;'>"
    f"<h3 style='text-align:center;color:#2c3e50;'>{selected_chart}</h3></div>",
    unsafe_allow_html=True
)

# ------------------ LAYOUT ------------------
left_col, right_col = st.columns([0.2, 0.8])
with right_col:
    fig, ax = plt.subplots(figsize=(8, 5))  # Medium-sized plot

    # ------------------ PLOT LOGIC ------------------
    if selected_chart == "Year vs Selling Price (Line Chart)":
        chart_data = df.groupby("year")["selling_price"].mean().reset_index()
        sns.lineplot(data=chart_data, x="year", y="selling_price", marker="o", ax=ax)

    elif selected_chart == "Fuel vs Selling Price (Bar Chart)":
        sns.barplot(data=df, x="fuel", y="selling_price", estimator="mean", ax=ax)

    elif selected_chart == "Seller Type vs Selling Price":
        sns.barplot(data=df, x="seller_type", y="selling_price", estimator="mean", ax=ax)

    elif selected_chart == "Transmission vs Selling Price":
        sns.barplot(data=df, x="transmission", y="selling_price", estimator="mean", ax=ax)

    elif selected_chart == "Owner vs Selling Price":
        sns.barplot(data=df, x="owner", y="selling_price", estimator="mean", ax=ax)

    elif selected_chart == "Seats vs Selling Price (Box Plot)":
        sns.boxplot(data=df, x="seats", y="selling_price", ax=ax)

    elif selected_chart == "KM Driven vs Selling Price":
        sns.scatterplot(data=df, x="km_driven", y="selling_price", alpha=0.5, ax=ax)

    elif selected_chart == "Engine CC vs Selling Price":
        sns.scatterplot(data=df, x="engine_cc", y="selling_price", alpha=0.5, ax=ax)

    elif selected_chart == "Max Power vs Selling Price":
        sns.scatterplot(data=df, x="max_power_new", y="selling_price", alpha=0.5, ax=ax)

    elif selected_chart == "Mileage vs Selling Price":
        if "mil_kmpl" in df.columns:  # Ensure column exists
            sns.scatterplot(data=df, x="mil_kmpl", y="selling_price", alpha=0.5, ax=ax)
        else:
            st.error("Column 'mil_kmpl' not found in the dataset.")

    elif selected_chart == "Torque RPM vs Selling Price":
        sns.scatterplot(data=df, x="torque_rpm", y="selling_price", alpha=0.5, ax=ax)

    elif selected_chart == "Fuel Type Distribution (Pie)":
        fuel_counts = df["fuel"].value_counts()
        ax.pie(fuel_counts, labels=fuel_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")

    elif selected_chart == "Seller Type Distribution (Pie)":
        seller_counts = df["seller_type"].value_counts()
        ax.pie(seller_counts, labels=seller_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")

    elif selected_chart == "Transmission Distribution (Pie)":
        trans_counts = df["transmission"].value_counts()
        ax.pie(trans_counts, labels=trans_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")

    elif selected_chart == "Owner Count (Bar Chart)":
        sns.countplot(data=df, x="owner", ax=ax)

    # Clean up layout
    plt.xticks(rotation=15)
    plt.tight_layout()

    # Show plot
    st.pyplot(fig)