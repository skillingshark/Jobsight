import streamlit as st
import requests
from api import fetch_job_postings , adzuna_api_key , openai_api_key
import openai



# Streamlit UI elements
st.title('Job Market Analyzer Dashboard')
query = st.text_input('Enter job title or keyword', 'Python Developer')
submit_button = st.button('Fetch Job Postings')

if submit_button:
    job_postings = fetch_job_postings(query)
    st.write(job_postings)  # Display the fetched job postings

    # Add more Streamlit components to display and analyze the data
    # Perform LLM analysis on job descriptions, visualize trends, etc.

# api_key = 'YOUR_OPENAI_API_KEY'
openai.api_key = openai_api_key

# Job posting text to be analyzed by LLM
job_description = "Software Engineer with experience in Python, Java, and web development."

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=job_description,
  max_tokens=150
)

llm_analysis = response.choices[0].text.strip()
# Use llm_analysis for further insights or analysis

###################################################333
# 5. Predictive Analysis


import pandas as pd
from sklearn.linear_model import LinearRegression

# Hypothetical historical job market data
# Your actual data might include more features and a larger dataset
data = {
    'Year': [2015, 2016, 2017, 2018, 2019],
    'JobOpenings': [2000, 2500, 3000, 3200, 3500]
}

df = pd.DataFrame(data)

# Train a simple linear regression model
X = df[['Year']]
y = df['JobOpenings']

model = LinearRegression()
model.fit(X, y)

# Predict job openings for future years
future_years = [2020, 2021, 2022]
predicted_job_openings = model.predict(pd.DataFrame(future_years, columns=['Year']))
