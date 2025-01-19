import streamlit as st
import pandas as pd

# Sample data for the leaderboard
data = {
    "SR": range(1, 21),  # 20 rows
    "Topics": [
        "Python Basics", "Data Science", "AI in Healthcare", "Machine Learning",
        "Deep Learning", "Natural Language Processing", "Web Development", 
        "Cloud Computing", "Blockchain", "Cybersecurity", "IoT",
        "Quantum Computing", "Big Data", "AI Ethics", "Robotics",
        "Autonomous Vehicles", "Virtual Reality", "Augmented Reality", "Game Development", "App Development"
    ],
    "Total Views": [1234, 5400, 2345, 6789, 4567, 2100, 876, 2345, 6789, 3456, 7890, 456, 1234, 5678, 8901, 3456, 5678, 1234, 4567, 890],
    "Total Likes": [230, 560, 120, 430, 380, 150, 200, 250, 600, 350, 500, 100, 230, 670, 560, 890, 100, 120, 180, 230],
    "Total Comments": [45, 67, 23, 98, 56, 12, 34, 89, 112, 65, 54, 23, 76, 32, 44, 21, 65, 34, 89, 56],
    "Total Shares": [120, 230, 78, 190, 160, 45, 100, 90, 230, 150, 230, 32, 65, 89, 112, 90, 120, 180, 45, 60]
}

# Manually verify that all columns have the same length (20 items)
assert len(data["SR"]) == 20
assert len(data["Topics"]) == 20
assert len(data["Total Views"]) == 20
assert len(data["Total Likes"]) == 20
assert len(data["Total Comments"]) == 20
assert len(data["Total Shares"]) == 20

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Set the Streamlit page title
st.title("Leaderboard")

# Display the leaderboard table
st.table(df)
