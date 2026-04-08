import os
import yfinance as yf
from newsapi import NewsApiClient
from openai import OpenAI
import hashlib
import time

# ==========================================
# CONFIGURATION
# ==========================================
# Use environment variables for secure API key management
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
MODEL = "qwen/qwen3.6-plus-preview:free"  # Free model on OpenRouter

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

# ==========================================
# UTILITY FUNCTIONS
# ==========================================

def format_currency(value: float | int) -> str:
    """Formats a numerical value as a currency string with dollar sign, thousand separators, and two decimal places.

    Args:
        value (float | int): The numeric value to format.

    Returns:
        str: The formatted currency string (e.g., "$1,234.56" or "- $1,234.56").

    Raises:
        TypeError: If the input value is not a numeric type.
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a numeric type (int or float).")

    is_negative = value < 0
    abs_value = abs(value)

    # Format the absolute value with commas and two decimal places
    formatted_abs_value = f"{abs_value:,.2f}"

    if is_negative:
        return f"- ${formatted_abs_value}"
    else:
        return f"${formatted_abs_value}"

# ==========================================
# STOCK DATA FUNCTIONS
# ==========================================

def get_stock_news(ticker: str) -> list[dict]:
    """Fetches recent news articles for the given stock ticker using NewsAPI with retry logic and duplicate filtering."""
    max_retries = 3
    retry_delay = 1
    for attempt in range(max_retries):
        try:
            news_api = NewsApiClient(api_key=NEWS_API_KEY)
            articles = news_api.get_top_headlines(q=ticker, language='en')
            
            if not articles.get('articles'):
                return []
            
            # Filter duplicates by title and content hash
            seen_hashes = set()
            unique_articles = []
            for article in articles['articles']:
                title = article.get('title', '').lower()
                description = article.get('description', '').lower()
                content_hash = hashlib.md5((title + description).encode()).hexdigest()
                
                if content_hash not in seen_hashes:
                    seen_hashes.add(content_hash)
                    unique_articles.append(article)
            return unique_articles
        except Exception:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            return []
    return []

def get_stock_price(ticker: str):
    pass
