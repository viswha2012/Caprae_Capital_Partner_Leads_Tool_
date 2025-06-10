import streamlit as st
import pandas as pd
import re
from search_enrich.fetch_leads_maps import fetch_leads

st.set_page_config(page_title="SaaSquatch Leads", layout="wide")

st.markdown("""
    <style>
    .title {
        font-size: 3rem;
        font-weight: bold;
        color: #00ff88;
        text-align: center;
        margin-bottom: 30px;
        font-family: 'Courier New', monospace;
    }
    .section-title {
        font-size: 1.8rem;
        color: #00ff88;
        margin-top: 3rem;
        margin-bottom: 1rem;
        text-align: center;
        font-family: 'Courier New', monospace;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">SaaSquatch Leads</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 3, 1])
with col1:
    industry = st.text_input("", placeholder="Industry", label_visibility="collapsed")
with col2:
    location = st.text_input("", placeholder="Location", label_visibility="collapsed")
with col3:
    if st.button("→"):
        st.session_state.show_results = True
        st.session_state.enrich_mode = False
        st.session_state.enriched_websites = []

if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'enrich_mode' not in st.session_state:
    st.session_state.enrich_mode = False
if 'leads_data' not in st.session_state:
    st.session_state.leads_data = []
if 'enriched_websites' not in st.session_state:
    st.session_state.enriched_websites = []


if st.session_state.show_results and not st.session_state.enrich_mode:
    if not industry or not location:
        st.warning("Please enter both Industry and Location.")
    else:
        if not st.session_state.leads_data:
            with st.spinner("Fetching leads..."):
                st.session_state.leads_data = fetch_leads(industry, location)

        if st.session_state.leads_data:
            st.markdown('<div class="section-title">Leads</div>', unsafe_allow_html=True)

            df = pd.DataFrame(st.session_state.leads_data)
            df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
            df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")
            df["Select"] = False

            st.markdown("###Filters")

            col1, col2, col3 = st.columns(3)
            with col1:
                min_rating = st.slider("Minimum Rating", min_value=0.0, max_value=5.0, value=0.0, step=0.1)
            with col2:
                min_reviews = st.number_input("Minimum Reviews", min_value=0, value=0, step=1)
            with col3:
                categories = df["Category"].dropna().unique().tolist()
                category_filter = st.selectbox("Category", options=["All"] + categories)

            # Apply filters
            filtered_df = df[
                (df["Rating"].fillna(0) >= min_rating) &
                (df["Reviews"].fillna(0) >= min_reviews)
            ]
            if category_filter != "All":
                filtered_df = filtered_df[filtered_df["Category"] == category_filter]

                
            edited_df = st.data_editor(
                filtered_df,
                use_container_width=True,
                height=600,
                column_order=["Select", "Name", "Phone", "Website", "Address", "Rating", "Reviews", "Category"],
                hide_index=True,
                key="lead_editor"
            )

            if st.button("Enrich"):
                selected_rows = edited_df[edited_df["Select"] == True]
                if selected_rows.empty:
                    st.warning("Please select at least one row.")
                else:
                    cleaned_websites = []
                    for website in selected_rows["Website"]:
                        if pd.notna(website):
                            clean = re.sub(r"^(https?://)?(www\.|@)?", "", website).split("/")[0]
                            cleaned_websites.append(clean)

                    st.session_state.enriched_websites = cleaned_websites
                    st.success("Enrichment data prepared. Please go to the 'Enrichment' page from the sidebar.")