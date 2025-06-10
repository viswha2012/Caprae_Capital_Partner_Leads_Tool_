import streamlit as st
import requests
import json

st.set_page_config(page_title="Intelligent Querying", layout="wide")

st.title("Intelligent Querying for Investment Leads")
st.write("Enter your query below. The AI will return structured parameters for lead enrichment.")

user_query = st.text_area("Enter your query", placeholder="e.g. Find SaaS companies in London with Series A funding and more than 10 employees.")

if st.button("Run Query") and user_query.strip():
    prompt = f"""You are a lead enrichment AI for private equity investors. 
Given a user's query about investment opportunities, extract structured search parameters to be used in an API.

Respond ONLY in a valid Python dictionary with the following fields populated based on the query.
Do not add any text or explanation outside the dictionary.

Here is the schema:
params = {{
    "q_organization_name": "",          
    "q_organization_website": "",       
    "q_organization_domain": "",        
    "q_organization_funding_stage": "", 
    "q_organization_funding_total": "", 
    "q_organization_funding_rounds": "",
    "q_organization_location_city": "", 
    "q_organization_location_state": "",
    "q_organization_location_country": "United Kingdom",
    "q_organization_industry": "",      
    "q_organization_employee_count": "",
    "q_organization_revenue": "",       
    "q_organization_technologies": "",  
    "q_organization_linkedin_url": "",  
    "q_organization_facebook_url": "",  
    "q_organization_twitter_url": "",   
    "per_page": 10
}}

Below is the user query. Extract and format the parameters accordingly.

USER QUERY:
{user_query}
"""
    url = "http://localhost:11434/api/generate"
    response = requests.post(url, json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        result = response.json()
        st.success("Parsed Parameters:")
        st.code(result['response'])
    else:
        st.error("Model API call failed.")
        st.code(response.text)
