# Caprae Capital Partners Lead Search Tool

A **Streamlit-based application** that enables investors and M&A professionals to **discover**, **enrich**, and **contact** high-potential companies using **LLMs**, **Apollo API**, and **real-time web crawling**.

#### Youtube Link: https://youtu.be/r3W6yBv2phA?si=XMiJiGIHLiOMkYvF
---

## Features

- **Natural Language Querying** for company search (e.g., *"Healthtech startups in the UK with Series A funding"*)
- **LLM-Powered Parsing** to convert free-form queries into structured API parameters
- **Apollo API Integration** to enrich company profiles with live data
- **AI-Generated Outreach Emails** tailored to each company
- **PDF & Markdown Reports** for insights and analysis
- **Local LLM (Ollama)** for secure, offline inference

---

## Technologies Used

- [Streamlit](https://streamlit.io/)
- [Ollama + Mistral 7B](https://ollama.com/)
- [Apollo.io API](https://apollo.io/)
- [crawl4ai](https://pypi.org/project/crawl4ai/) 
- Python 3.10+

---

## ⚙️ Setup & Installation

### 1. **Clone the repository**
   ```bash
   git clone https://github.com/viswha2012/Caprae_Capital_Partner_Leads_Tool_.git
   cd Caprae_Capital_Partner_Leads_Tool_
   ```

### 2. Create a .env or config.py file with your API keys
```bash
# config.py
APOLLO_KEY = "your_apollo_api_key"
SERPAPI_KEY = "your_serpapi_key"
```

### 3. Run Ollama with Mistral locally
```bash
ollama run mistral
```

### 4. Start the Streamlit app
```bash
streamlit run Leads.py
```

## 🗂 Project Structure
```bash
Caprae_Capital_Partner_Leads_Tool_/
│
├── lead_app.py                # Main Streamlit app
├── pages/
│   ├── 1_Enrichment.py        
│   ├── 2_Intelligent_Querying.py 
│
├── utils/
│   ├── email_generator.py    
│   ├── query_to_params.py     
│
├── crawl4ai/                  
├── config.py                  
├── requirements.txt
└── README.md
```

## 📊 Models & Justification

We used the **Mistral 7B** model via **Ollama** for:

- Lightweight yet powerful language understanding  
- On-device privacy and secure inference  
- Rapid local inference with reduced latency  
- Better control over model behavior compared to hosted LLMs  

For tasks like **email generation** and **intelligent lead queries**, Mistral 7B performed best in terms of:

- Adherence to structured prompts  
- Professional tone for outreach content  
- Minimal hallucination in factual data extraction  

## Project Demo

### 1. Lead Search with Filters
<img width="1470" alt="SaaSquatch Leads" src="https://github.com/user-attachments/assets/f826d60a-024e-4d1c-8a34-9f660079a72f" />
￼
### 2. Post Enrichment with Email Generation
<img width="1470" alt="Enriched Company Information" src="https://github.com/user-attachments/assets/02b4b372-2b09-401d-8749-8fc98e21ceb2" />

### 3. Intelligent Querying : Parameter Generation (No API Access)
<img width="1470" alt="Intelligent Querying for Investment Leads" src="https://github.com/user-attachments/assets/5741e4d5-cb7d-48bd-a59d-5690ae7cbcbb" />

￼
