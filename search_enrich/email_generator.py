import requests
from crawl4ai import AsyncWebCrawler

async def generate_email(website_url: str, model: str = "mistral"):
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=website_url)

            prompt = f"""
            You are an expert investment analyst and relationship manager working in private equity. Using the following company information:

            {result.markdown}

            Draft a highly professional outreach email to the company's founder or leadership team. The goal of the email is to express genuine interest in their business and request a meeting to explore potential collaboration around mergers and acquisitions or private equity investment opportunities.

            The email should:
            - Mention what we found impressive about their company (based on the provided information).
            - Communicate that we're conducting strategic outreach to select, high-potential companies.
            - Suggest a meeting or call at their convenience to explore synergies.
            - Be warm, concise, and businesslike.

            Do not include any disclaimers or AI explanations. Generate only the email content in markdown format (with subject line and body).
            """

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False
                }
            )

            if response.status_code == 200:
                return response.json()['response']
            else:
                return f"Error generating email: {response.text}"

    except Exception as e:
        return f"Error processing website: {str(e)}"
