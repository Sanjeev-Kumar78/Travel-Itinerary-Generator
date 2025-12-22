from google import genai
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Initialize client lazily
_client = None

def get_client():
    global _client
    if _client is None:
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set. Please create a .env file with your API key.")
        _client = genai.Client(api_key=api_key)
    return _client

# Google Search grounding tool
grounding_tool = genai.types.Tool(
    google_search=genai.types.GoogleSearch()
)


# Generate some text.
def generate_itinerary(source, destination, start_date, end_date, no_of_days):
    # prompt = f"Generate a personalized trip itinerary for a {no_of_day}-day trip from {source} to {destination} on {start_date} to {end_date}, with an optimum budget (Currency:INR)."
    system_prompt = (
        "You are an expert travel planner specializing in Indian and international trips. "
        "Always give detailed, practical, and budget-friendly itineraries. "
        "Ensure the tone is friendly, informative, and concise. "
        "Use INR for all costs, and include real, popular attractions and dining options."
    )
    user_prompt = (
        f"Generate a personalized {no_of_days}-day trip itinerary "
        f"from {source} to {destination} between {start_date} and {end_date}. "
        f"Include sightseeing, food recommendations, transport suggestions, "
        f"and an optimum budget per day in INR."
    )

    # Get the client and generate content
    client = get_client()
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents=user_prompt,
        config=genai.types.GenerateContentConfig(
            tools=[grounding_tool], 
            system_instruction=[system_prompt]
        )
    )

    return response.text