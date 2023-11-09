# [Travel Itinerary Generator](https://www.sanjeev02.pythonanywhere.com)
***

<img align='right' src="/static/logo.svg" alt="Travel Itinerary Generator Logo" width="150"/>


A web-based Travel Itinerary Generator that simplifies travel planning with personalized itineraries.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [API Keys](#api-keys)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)

## About

Travel Itinerary Generator is a computer program that empowers travelers to effortlessly create personalized travel itineraries. By considering users' interests, budgets, and travel dates, this application generates comprehensive lists of activities, attractions, and accommodations. Whether you're an experienced traveler or a novice, the Travel Itinerary Generator is your key to saving time and ensuring an enriching and well-rounded travel experience.

## Limitations & Future Work
- The Travel Itinerary Generator is works only on the basis of user's source and destination and time of travel.

***Future Work***
- The Travel Itinerary Generator is not able to generate itineraries for multiple destinations.
- The Travel Itinerary Generator is not able to suggest hotels and flights.
- **Real-time Collaboration:** In an increasingly interconnected world, we plan to introduce real-time collaboration features. Users will be able to share their itineraries with travel companions or collaborators, making group travel planning an effortless and collaborative experience.

## Features

- **Weather Forecast:** The Travel Itinerary Generator provides a weather forecast of the destination for the whole travel time.
- **Travel Itinerary:** The Travel Itinerary Generator provides a travel itinerary for the whole travel time in a optimum budget.
## Requirements

- Python 3.11
- Flask
- Flask-SQLAlchemy
- google-generativeai==0.2.2

## Setup and Installation

1. Clone the repository:

   ```shell
   https://github.com/Sanjeev-Kumar78/Travel-Itinerary-Generator.git
   cd Travel-Itinerary-Generator
2. Install required packages:

   ```shell
   pip install -r requirements.txt
   ```

## API Keys
- Visual Crossing Weather API Key: [Sign up](https://www.visualcrossing.com/weather-api) for a free account and get your API key.
- Google Palm API: [Sign up](https://makersuite.google.com) for a free account and get your API key.

## Usage
- Please follow the instructions below to run the application locally.

Apply APIs keys create a `.env` file.
```shell
WEATHER_API_KEY='Your Visual Crossing Weather API Key'
PALM_API_KEY='Your Google Palm API Key'
```
and save it in the root directory of the project.

Run the following command to start the application:
```shell
python wsgi.py
```

## Screenshots

**Home Page of Travel Itinerary Generator without Login.**


**Register Page / Sign Up**


**Login Page**


**For Testing, I have taken Source Point as Varanasi & Destination as Mumbai, Starting Date of Journey: 06/11/2023, Return Date: 10/11/2023**


**Itinerary Page**


## License

This project is licensed under the [Apache License 2.0](LICENSE) - see the [LICENSE](LICENSE) file for details.

