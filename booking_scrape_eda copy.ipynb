#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 13:07:18 2025

@author: chrisl
"""
#pip install matplotlib
#pip install tensorflow

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Set Seaborn theme
sns.set_theme()

# Connect to SQLite database
conn = sqlite3.connect(r"/Users/chrisl/Documents/Project Work 2025/Xccelerate_Scraping_Project /hotels.db")

# Load data into DataFrame
df = pd.read_sql("SELECT * FROM hotel_data", conn)

# Close connection (good practice)
conn.close()

# Display first 5 rows
print("Display the First 5 Rows of Dataset")
print("-" * 200)
display(df.head())
print("-" * 200)

# Show data types
print("Data Types in the Dataset:")
print(df.info())
print("-" * 200)

# Show shape and dimension
print("Data Shape and Dimension")
print("Number of Columns:", df.shape[1], "And Number of Rows:", df.shape[0])
print("-" * 200)

# --- CLEANING SECTION ---

# Clean Prices column: Remove non-numeric characters and convert safely to integer
if 'Prices' in df.columns:
    df['Prices'] = df['Prices'].astype(str).str.replace(r'[^\d.]+', '', regex=True)  # Remove all non-digit chars
    df['Prices'] = pd.to_numeric(df['Prices'], errors='coerce')                     # Convert to float
    df['Prices'] = df['Prices'].fillna(0).astype(int)                               # Fill blanks and convert to int

# Clean 'Distances' column - keep only numbers and decimals
if 'Distances' in df.columns:
    df['Distances'] = df['Distances'].astype(str).str.replace(r'[^\d.]+', '', regex=True)
    df['Distances'] = pd.to_numeric(df['Distances'], errors='coerce')
    df['Distances'] = df['Distances'].fillna(0.0)

# Display cleaned data
print("Cleaned Data:")
display(df.head())

# --- EXPLORATORY DATA ANALYSIS (EDA) ---

# Histogram of hotel prices
plt.figure(figsize=(10, 6))
sns.histplot(df['Prices'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Hotel Prices')
plt.xlabel('Price (USD)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Scatter plot of price vs distance (only if Distances column exists)
if 'Distances' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Distances', y='Prices')
    plt.title('Hotel Price vs Distance to City Center')
    plt.xlabel('Distance (km)')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.show()

# Summary statistics
print("Summary Statistics:")
print(df.describe(include='all'))

# Save Cleaned Data to New SQLite DB and CSV File

# Define new file paths
sqlite_clean_db = r"/Users/chrisl/Documents/Project Work 2025/Xccelerate_Scraping_Project /hotels_cleaned.db"
csv_file = r"/Users/chrisl/Documents/Project Work 2025/Xccelerate_Scraping_Project /hotel_prices_cleaned.csv"

# Save to SQLite
conn = sqlite3.connect(sqlite_clean_db)
df.to_sql("cleaned_hotel_data", conn, if_exists='replace', index=False)
conn.close()
print(f"Cleaned data saved to SQLite: {sqlite_clean_db} (Table: cleaned_hotel_data)")

# Save to CSV
df.to_csv(csv_file, index=False)
print(f"Cleaned data saved to CSV: {csv_file}")

# Optional: Show final cleaned data
print("\n First 5 Rows of Cleaned Data:")
display(df.head())