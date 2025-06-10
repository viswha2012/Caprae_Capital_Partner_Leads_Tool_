from serpapi import GoogleSearch
from config import SERPAPI_KEY

def fetch_leads(industry_input, location_input):
    serpapi_query = f"{industry_input} companies in {location_input}"
    params = {
        'engine': 'google_maps',
        'type': 'search',
        'q': serpapi_query,
        'hl': 'en',
        'api_key': SERPAPI_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    leads = []
    for place in results.get("local_results", []):
        leads.append({
            "Name": place.get("title"),
            "Phone": place.get("phone"),
            "Website": place.get("website"),
            "Address": place.get("address"),
            "Rating": place.get("rating"),
            "Reviews": place.get("reviews"),
            "Category": place.get("type")
        })
    return leads