from langchain_core.tools import tool
from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
import requests

# === API Credentials ===
EXCHANGE_API_KEY = "exchange_rate_api_key"
BASE_URL = "http://api.exchangeratesapi.io/v1/latest"

# === Tool 1: Get Conversion Rate from EUR to any supported currency ===
@tool
def get_eur_to_currency(currency: str) -> float:
    """
    Get the conversion rate from EUR to the given currency.
    """
    url = f"{BASE_URL}?access_key={EXCHANGE_API_KEY}&symbols={currency}"
    response = requests.get(url)
    data = response.json()

    if "rates" not in data or currency not in data["rates"]:
        raise ValueError(f"Could not get conversion rate for {currency}. Response: {data}")
    
    return data["rates"][currency]

# === Tool 2: Convert Currency ===
@tool
def convert(value: float, rate: float) -> float:
    """
    Convert value using conversion rate.
    Example: Convert 1000 BDT to USD using BDT->USD rate.
    """
    return value * rate

# === Gemini LLM Setup ===
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key="gemini_api_key",
    temperature=0
)

# === Agent Setup ===
agent_executor = initialize_agent(
    tools=[get_eur_to_currency, convert],
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

# === Custom Prompt (Optional but helpful) ===
instruction = """
Always convert currencies using EUR as the base currency.
To convert from BDT to USD, first get:
- EUR to BDT rate
- EUR to USD rate
Then calculate BDT to USD rate as (EUR_to_USD / EUR_to_BDT).
Finally, use that rate to convert the amount.
"""

# === Question ===
question = "What is 1000 BDT in USD?"
agent_executor.invoke({"input": instruction + question})
