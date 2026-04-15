"""A dataset was loaded and cleaned by eliminating the addition of extra spaces in column names. The student records were clustered to create one profile and all the features were normalized to the same range so as to compare them fairly. Students were compared and an interface was
designed to provide recommendations and adaptive dashboard which is dependent on the level of performance."""
# importing libraries
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# loading dataset from file location
df = pd.read_csv("C:/Work/adaptive_english_learning_dataset_2024.csv")

# removing extra spaces from column names
df.columns = df.columns.str.strip()

# selecting important student performance features
numeric_features = [
    "reading_speed_wpm",
    "pronunciation_accuracy",
    "listening_score",
    "reading_score",
    "speaking_score",
    "adaptive_score",
    "performance_improvement_rate",
    "engagement_level"  # will be encoded
]

# converting engagement level text into numeric values
eng_map = {"Low": 1, "Medium": 2, "High": 3}
df["engagement_level"] = df["engagement_level"].map(eng_map)

# grouping multiple records into single student profile
student_df = df.groupby("student_id")[numeric_features].mean().reset_index()

# scaling all values into same range for fair comparison
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(student_df[numeric_features])

# calculating similarity between student profiles
cosine_sim = cosine_similarity(data_scaled)

# defining function to find similar students
def recommend_similar_students(student_id):

    # checking whether student exists
    if student_id not in student_df["student_id"].values:
        return []

    # finding index of selected student
    idx = student_df[student_df["student_id"] == student_id].index[0]

    # computing similarity scores with all students
    sim_scores = list(enumerate(cosine_sim[idx]))

    # sorting students based on similarity score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    # selecting top 3 similar students excluding self
    for i in sim_scores[1:4]:

        # getting student id from index
        rec_id = student_df.iloc[i[0]]["student_id"]

        recommendations.append(rec_id)

    return recommendations

# displaying recommended students in message box
def show_recommendation():

    # getting input student id
    student_id = entry.get()

    # getting similar students list
    recs = recommend_similar_students(student_id)

    # showing error if no results found
    if not recs:
        messagebox.showerror("Error", "Student ID not found!")
        return

    # showing recommended students
    messagebox.showinfo(
        "Adaptive Recommendations",
        "\n".join(recs)
    )

# opening adaptive dashboard based on performance
def open_dashboard():

    # getting input student id
    student_id = entry.get()

    # checking valid student id
    if student_id not in student_df["student_id"].values:
        messagebox.showerror("Error", "Invalid Student ID")
        return

    # extracting student data
    user = student_df[student_df["student_id"] == student_id].iloc[0]

    # getting adaptive score
    score = user["adaptive_score"]

    # creating new dashboard window
    dashboard = tk.Toplevel(root)
    dashboard.title("Adaptive UI Dashboard")
    dashboard.geometry("500x300")

    # displaying student id
    tk.Label(dashboard, text=f"Student: {student_id}", font=("Arial", 14, "bold")).pack(pady=10)

    # setting UI mode based on score
    if score < 60:
        mode = "Beginner UI (High Guidance)"
        color = "blue"
    elif score < 80:
        mode = "Intermediate UI (Hints Enabled)"
        color = "green"
    else:
        mode = "Advanced UI (Minimal UI)"
        color = "red"

    # showing adaptive mode
    tk.Label(dashboard, text=mode, fg=color, font=("Arial", 12)).pack(pady=10)

    # creating task button
    tk.Button(
        dashboard,
        text="Start Task",
        command=lambda: messagebox.showinfo("Task", "Task Completed!")
    ).pack(pady=20)

# creating main application window
root = tk.Tk()
root.title("AI Adaptive UI System")
root.geometry("450x250")

# adding label for input
tk.Label(root, text="Enter Student ID:").pack(pady=10)

# creating input field
entry = tk.Entry(root)
entry.pack(pady=5)

# creating button for recommendations
tk.Button(root, text="Get Recommendations", command=show_recommendation).pack(pady=10)

# creating button for dashboard
tk.Button(root, text="Open Dashboard", command=open_dashboard).pack(pady=10)

# running application loop
root.mainloop()