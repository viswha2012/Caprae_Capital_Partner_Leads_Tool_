import streamlit as st
import requests
import pandas as pd
import asyncio
from search_enrich.email_generator import generate_email
from config import APOLLO_KEY

st.set_page_config(page_title="Enriched Data123", layout="wide")

st.title("Enriched Company Information")

if "enriched_websites" not in st.session_state or not st.session_state.enriched_websites:
    st.warning("No enriched websites found. Please go to the main page and generate them.")
    st.stop()

domains = st.session_state.enriched_websites

url = "https://api.apollo.io/api/v1/organizations/enrich"
headers = {
    "accept": "application/json",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "X-Api_Key": APOLLO_KEY
}

# Fetch enrichment data
data = []
with st.spinner("Fetching enrichment data from Apollo API..."):
    for domain in domains:
        params = {"domain": domain}
        try:
            response = requests.get(url, headers=headers, params=params)
            res_json = response.json()
            org = res_json.get("organization", {})

            data.append({
                "Name": org.get("name"),
                "Website": org.get("website_url"),
                "LinkedIn": org.get("linkedin_url"),
                "Primary Phone": org.get("primary_phone", {}).get("number"),
                "Phone": org.get("phone"),
                "Founded Year": org.get("founded_year"),
                "Industries": ", ".join(org.get("industries", [])),
                "Employees": org.get("estimated_num_employees"),
                "Address": org.get("raw_address"),
                "Owner Org ID": org.get("owned_by_organization_id"),
                "Funding": org.get("total_funding_printed"),
                "Latest Funding Date": org.get("latest_funding_round_date")
            })
        except Exception as e:
            data.append({"Name": domain, "Error": str(e)})

if not data:
    st.info("No data retrieved.")
    st.stop()

df = pd.DataFrame(data)

df['Action'] = "Generate Email"
st.dataframe(df, use_container_width=True, hide_index=True)

for index, row in df.iterrows():
    if 'Website' in row and pd.notna(row['Website']):
        if st.button(f"Generate Email for {row['Name']}", key=f"btn_{index}"):
            with st.spinner(f"Generating email for {row['Name']}..."):
                try:

                    import nest_asyncio
                    nest_asyncio.apply()
                    email_content = asyncio.run(generate_email(row['Website']))
                    
                    st.subheader(f"Generated Email for {row['Name']}")
                    st.text_area("Email Content", email_content, height=300)
                    st.download_button(
                        label="Download Email",
                        data=email_content,
                        file_name=f"email_to_{row['Name']}.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"Failed to generate email: {str(e)}")