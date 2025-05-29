# WeatherApp ☀️🌧️🌪️

A sleek weather application built with **PyQt5** that fetches and displays real-time weather data using the **OpenWeatherMap API**.

## Features

- Enter any city and get:
  - Temperature in Celsius 
  - Weather condition description
  - Weather emoji based on condition
- Handles various error scenarios gracefully (invalid city, connection issues, etc.)
- Responsive and colorful UI using custom styling

## How It Works

The app uses the [OpenWeatherMap API](https://openweathermap.org/api) to retrieve live weather data based on user input.
The weather condition ID is then used to generate a matching emoji and display the temperature.

## Setup & Usage

1. Clone the repository:

   ```
   git clone https://github.com/shivendraghb/Projects.git
   cd Projects/WeatherApp

2. Install the dependencies:

   pip install -r requirements.txt

3. Run the app:

   python main.py

## Notes
  
=> Make sure your internet connection is active to fetch weather data.
  
=> You can replace the default API key in the code with your own from OpenWeatherMap.
  
=> Consider using environment variables (.env) to store your API key securely for production use.

## Example Emojis

| Condition    | Emoji |
| ------------ | ----- |
| Clear        | ☀️    |
| Cloudy       | ☁️    |
| Rain         | 🌧️   |
| Thunderstorm | ⛈️    |
| Snow         | ❄️    |
| Mist/Fog     | 🌫️   |
| Tornado      | 🌪️   |


