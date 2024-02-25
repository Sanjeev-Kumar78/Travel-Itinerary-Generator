# [Travel Itinerary Generator](https://sanjeev02.pythonanywhere.com)
***

[![GitHub license](https://img.shields.io/github/license/Sanjeev-Kumar78/Travel-Itinerary-Generator)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Sanjeev-Kumar78/Travel-Itinerary-Generator)]()
[![GitHub contributors](https://img.shields.io/github/contributors/Sanjeev-Kumar78/Travel-Itinerary-Generator)]()
[![GitHub last-commit](https://img.shields.io/github/last-commit/Sanjeev-Kumar78/Travel-Itinerary-Generator)]()


<img title="Travel-Itinerary-Generator" align='right' src="/static/logo.svg" alt="Travel Itinerary Generator Logo" width="150"/>

Plan your dream trip effortlessly with the Travel Itinerary Generator! This powerful trip planner is your ultimate companion for crafting seamless travel experiences. Whether you're embarking on a road trip, city excursion, or overseas adventure, our tool simplifies the entire planning process.

## Sample:
https://github.com/Sanjeev-Kumar78/Travel-Itinerary-Generator/assets/62820550/d55374a9-41bd-4454-8c2b-4f037b1f010b




<p align="center">
Make your travel dreams a reality. Start planning your next adventure with the Travel Itinerary Generator today!
</p>
<p align="center">
<i>Explore, discover, and make every trip unforgettable.*</i>
</p>

## Table of Contents

- [Travel Itinerary Generator](#travel-itinerary-generator)
  - [Sample:](#sample)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Limitations \& Future Work](#limitations--future-work)
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
- The Travel Itinerary Generator works only based on the user's source and destination and time of travel.

***Future Work***
- The Travel Itinerary Generator is not able to generate itineraries for multiple destinations.
- The Travel Itinerary Generator is not able to suggest hotels and flights.
- **Real-time Collaboration:** In an increasingly interconnected world, we plan to introduce real-time collaboration features. Users will be able to share their itineraries with travel companions or collaborators, making group travel planning an effortless and collaborative experience.

## Features

- **Weather Forecast:** The Travel Itinerary Generator provides a weather forecast of the destination for the whole travel time.
- **Travel Itinerary:** The Travel Itinerary Generator provides a travel itinerary for the whole travel time in an optimum budget.
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

Write API keys: In a `.env` file.
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
![image](https://github.com/Sanjeev-Kumar78/Travel-Itinerary-Generator/assets/62820550/a5e0f1c9-b0c4-4c1b-ba50-1a0b6c2a56bf)


**Register Page / Sign Up**
![image-1](https://github.com/Sanjeev-Kumar78/Travel-Itinerary-Generator/assets/62820550/2c2f90ff-c81d-48e6-a64f-ed71a1485cc8)


**Login Page**
![image-2](https://github.com/Sanjeev-Kumar78/Travel-Itinerary-Generator/assets/62820550/7f50219b-546a-43d0-83bd-ca5d2262c261)


**For Testing, I have taken Source Point as Varanasi & Destination as Mumbai, Starting Date of Journey: 06/11/2023, Return Date: 10/11/2023**
![image-3](https://github.com/Sanjeev-Kumar78/Travel-Itinerary-Generator/assets/62820550/9b429e5a-722c-4d0c-ae39-b4e64440a34a)


**Itinerary Page**
![image-4](https://github.com/Sanjeev-Kumar78/Travel-Itinerary-Generator/assets/62820550/9f91a253-7ab8-4211-9b58-0a843cc66f0e)


## License

This project is licensed under the [Apache License 2.0](LICENSE) - see the [LICENSE](LICENSE) file for details.

