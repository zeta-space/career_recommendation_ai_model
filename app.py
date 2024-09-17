import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import altair as alt

# Expanded skill data for various occupations
data = {
    "Occupation": ["Agriculture", "Tourism", "Business", "Healthcare", "Technology", "Engineering", 
                   "Education", "Arts and Design", "Media", "Construction", "Finance", "Law", 
                   "Logistics", "Marketing", "Renewable Energy", "Software Development", 
                   "AI & Data Science", "Cybersecurity", "E-commerce", "Fashion Design", "Game Development"],
    "Demand_Level": [5, 3, 4, 2, 4, 3, 5, 4, 4, 3, 5, 4, 3, 5, 4, 5, 5, 4, 3, 5, 4],
    "Skills_Required": ["Basic farming, Agro-knowledge", 
                        "Languages, Customer Service, Cultural Sensitivity", 
                        "Financial Analysis, Negotiation, Project Management", 
                        "Medical Knowledge, Patient Care, First Aid", 
                        "Programming, Cybersecurity, Cloud Computing", 
                        "Mechanical Skills, Problem-Solving, Blueprint Reading", 
                        "Lesson Planning, Public Speaking, Mentorship", 
                        "Graphic Design, Creative Thinking, Artistic Expression", 
                        "Social Media Management, Content Creation, SEO", 
                        "Construction Management, Engineering", 
                        "Financial Analysis, Accounting", 
                        "Legal Research, Critical Thinking, Client Management", 
                        "Supply Chain Management, Organization", 
                        "Social Media, SEO, Marketing Strategy", 
                        "Sustainable Energy, Environmental Science, Technical Installation", 
                        "Software Engineering, Algorithms", 
                        "Data Analysis, Machine Learning", 
                        "Network Security, IT Management", 
                        "E-commerce Platforms, Online Marketing", 
                        "Pattern Making, Trend Analysis, Sewing", 
                        "Game Design, Coding"]
}

df = pd.DataFrame(data)

# Collect user details
user_name = st.text_input("Your Name:")
user_age = st.number_input("Your Age:", min_value=5, max_value=100, value=10)

# Define skill levels with more clarity
st.write("""
### Skill Level Definitions:
- **1:** I have no knowledge or experience in this area.
- **2:** I have very limited knowledge and experience.
- **3:** I have some knowledge and experience, but I’m still learning.
- **4:** I have solid knowledge and can work independently in this area.
- **5:** I’m an expert and very confident in this area.
""")

# Dynamic questions for younger children (<15)
if user_age < 15:
    st.write("### Career Guidance for Young Learners")
    interest = st.selectbox("What do you enjoy the most?", 
                            ["Drawing", "Music", "Dance", "Mechanics", "Architecture", "Sports", "Teaching", "Helping Animals", "Solving Problems"])
    creativity = st.selectbox("Which activity do you do most often?", 
                              ["Playing music", "Dancing", "Building objects", "Drawing", "Constructing from materials", "Taking care of animals", "Helping others", "Solving puzzles"])

    if interest == "Drawing":
        st.write("You may enjoy careers in visual arts like illustration, graphic design, or architecture.")
    elif interest == "Music":
        st.write("Music may be a great path for you! You can explore playing instruments, singing, or composing music.")
    elif interest == "Dance":
        st.write("You might be interested in becoming a dancer or choreographer!")
    elif interest == "Mechanics":
        st.write("You may have a future in engineering or mechanical design.")
    elif interest == "Architecture":
        st.write("You could become an architect and design amazing buildings!")
    elif interest == "Sports":
        st.write("Athletics could be a path for you! You might become a coach or a professional athlete.")
    elif interest == "Teaching":
        st.write("You could be a future teacher, helping others learn and grow.")
    elif interest == "Helping Animals":
        st.write("Veterinary science or wildlife conservation could be perfect for you!")
    elif interest == "Solving Problems":
        st.write("You might enjoy a career in technology, science, or engineering, where problem-solving is key.")

# Detailed skill-based questions for teens (15-18)
elif 15 <= user_age < 18:
    st.write("### Career Guidance for Teens")
    
    st.write("Please answer the following questions:")
    enjoys_creativity = st.radio("Do you enjoy creative tasks (e.g., drawing, writing, creating content)?", ("Yes", "No"))
    good_with_people = st.radio("Are you good at communicating and working with others?", ("Yes", "No"))
    likes_technology = st.radio("Do you enjoy working with technology?", ("Yes", "No"))
    
    st.write("Tell us about your skills:")
    skill_level_business = st.slider("Business Skills", 1, 5, 3)
    skill_level_technology = st.slider("Technology Skills", 1, 5, 3)
    skill_level_creative = st.slider("Creative Skills (Arts & Design)", 1, 5, 3)
    skill_level_languages = st.slider("Language Skills", 1, 5, 3)
    skill_level_communication = st.slider("Communication Skills", 1, 5, 3)
    skill_level_problem_solving = st.slider("Problem-Solving Skills", 1, 5, 3)

# Professional skills for adults (18+)
else:
    st.write("### Career Guidance for Adults")
    st.write("Tell us about your professional skills:")
    skill_level_business = st.slider("Business Skills", 1, 5, 3)
    skill_level_technology = st.slider("Technology Skills", 1, 5, 3)
    skill_level_creative = st.slider("Creative Skills (Arts & Design)", 1, 5, 3)
    skill_level_languages = st.slider("Language Skills", 1, 5, 3)
    skill_level_communication = st.slider("Communication Skills", 1, 5, 3)
    skill_level_problem_solving = st.slider("Problem-Solving Skills", 1, 5, 3)

# Prepare job demand data (5 features per job)
demand_data = np.array([
    [5, 3, 4, 3, 2],  # Agriculture
    [2, 5, 3, 4, 3],  # Tourism
    [4, 4, 5, 3, 4],  # Business
    [2, 3, 2, 5, 2],  # Healthcare
    [4, 4, 5, 4, 5],  # Technology
    [3, 3, 3, 3, 3],  # Engineering
    [5, 5, 5, 4, 5],  # Education
    [4, 4, 4, 5, 4],  # Arts and Design
    [4, 4, 3, 5, 4],  # Media
    [3, 3, 3, 3, 3],  # Construction
    [5, 4, 5, 4, 4],  # Finance
    [4, 4, 3, 3, 4],  # Law
    [3, 3, 3, 3, 3],  # Logistics
    [5, 5, 5, 4, 5],  # Marketing
    [4, 4, 4, 5, 4],  # Renewable Energy
    [5, 5, 5, 4, 5],  # Software Development
    [5, 5, 5, 5, 5],  # AI & Data Science
    [4, 4, 4, 4, 4],  # Cybersecurity
    [3, 3, 4, 4, 3],  # E-commerce
    [5, 4, 4, 5, 4],  # Fashion Design
    [5, 4, 5, 4, 4]   # Game Development
])

# Input new user data
if user_age >= 15:
    new_data = np.array([[skill_level_business, skill_level_technology, skill_level_creative, skill_level_communication, skill_level_problem_solving]])

    # Train model for recommendations
    model = NearestNeighbors(n_neighbors=3)
    model.fit(demand_data)

    # Generate career recommendations
    distances, indices = model.kneighbors(new_data)
    recommended_jobs = df.iloc[indices[0]]["Occupation"].values
    st.write(f"Recommended careers: {', '.join(recommended_jobs)}")

# Tailored conclusions based on age group and skill levels
if user_age < 15:
    conclusion = f"It seems you enjoy {interest} and prefer {creativity}. Keep exploring your creativity to discover new possibilities!"
elif 15 <= user_age < 18:
    if skill_level_technology < 3:
        conclusion = f"You're still learning about technology, but there's great potential if you continue to develop your skills. You could explore areas like {', '.join(recommended_jobs)}."
    else:
        conclusion = f"Based on your skills, you have great potential in fields such as {', '.join(recommended_jobs)}. Keep developing these skills!"
else:
    if skill_level_technology < 3:
        conclusion = f"Your technology skills are still growing. Consider additional training to enhance your career opportunities in areas like {', '.join(recommended_jobs)}."
    else:
        conclusion = f"Your skills in technology and problem-solving align well with careers such as {', '.join(recommended_jobs)}. Continue refining these skills for career success."

st.write(conclusion)

# Display job demand data in a chart
chart = alt.Chart(df).mark_bar().encode(
    x='Occupation',
    y='Demand_Level',
    color='Occupation'
)
st.altair_chart(chart, use_container_width=True)

# Final conclusion for the user
if user_age < 15:
    st.write("**Conclusion**: The chart shows high demand for technology and business-related careers, but for now, focus on exploring your creativity and interests.")
else:
    st.write("**Conclusion**: Careers in technology and business are highly sought after. Continue to grow in these areas to access more opportunities.")
