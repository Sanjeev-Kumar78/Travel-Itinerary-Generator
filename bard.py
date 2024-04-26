import google.generativeai as palm
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
palm_api_key = os.environ.get("PALM_API_KEY")


# Create a config.
palm.configure(api_key=palm_api_key)
model = palm.GenerativeModel(model_name="gemini-pro")
# print(list(palm.list_models()))


# Generate some text.
def generate_itinerary(source, destination, start_date, end_date, no_of_day):
    prompt = f"Generate a personalized trip itinerary for a {no_of_day}-day trip {source} to {destination} from {start_date} to {end_date}, with an optimum budget (Currency:INR)."
    response = model.generate_content(prompt)
    return(response.text)