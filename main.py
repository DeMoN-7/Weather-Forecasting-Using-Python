from tkinter import Tk, Label, Button, Entry, Frame
import requests

# API details
base_url = "http://api.weatherapi.com/v1/forecast.json?"
api_key = "08d22e6bb56e468b9e292129230407"  # Replace with your own API key

# Function to fetch weather data from API
def get_weather():
    city = city_entry.get()  # Get city name from user input
    url = f"{base_url}key={api_key}&q={city}&days=1&aqi=yes&alerts=yes"
    
    try:
        response = requests.get(url)
        weather_data = response.json()
        
        # Extract and format weather information
        temperature = f"{weather_data['current']['temp_c']}°C"
        feels_like = f"{weather_data['current']['feelslike_c']}°C"
        day = weather_data['current']['condition']['text']
        wind_speed = f"{weather_data['current']['wind_kph']} km/h"
        wind_direction = weather_data['current']['wind_dir']
        humidity = f"{weather_data['current']['humidity']}%"
        pressure = f"{weather_data['current']['pressure_mb']} hPa"
        visibility = f"{weather_data['current']['vis_km']} km"
        uv_index = weather_data['current']['uv']
        
        # Update labels with the real weather data
        temperature_label.config(text=temperature)
        feels_like_label.config(text=feels_like)
        day_label.config(text=day)
        wind_speed_label.config(text=wind_speed)
        wind_direction_label.config(text=wind_direction)
        humidity_label.config(text=humidity)
        pressure_label.config(text=pressure)
        visibility_label.config(text=visibility)
        uv_index_label.config(text=uv_index)
        
    except Exception as e:
        # Display an error if the API request fails
        temperature_label.config(text="--")
        feels_like_label.config(text="--")
        day_label.config(text="--")
        wind_speed_label.config(text="--")
        wind_direction_label.config(text="--")
        humidity_label.config(text="--")
        pressure_label.config(text="--")
        visibility_label.config(text="--")
        uv_index_label.config(text="--")
        print("Error fetching weather data:", e)

# Create the main window
root = Tk()
root.title("Weather Forecast")
root.geometry("600x600")
root.configure(bg="#57adff")
root.resizable(False, False)

# Title label
title_label = Label(root, text="Weather Forecast App", font=("Arial", 18, "bold"), bg="#57adff", fg="white")
title_label.pack(pady=20)

# Input frame for City
input_frame = Frame(root, bg="#57adff")
input_frame.pack(pady=10)

city_label = Label(input_frame, text="Enter City:", font=("Arial", 12), bg="#57adff", fg="white")
city_label.grid(row=0, column=0, padx=5)

city_entry = Entry(input_frame, font=("Arial", 12), width=20)
city_entry.grid(row=0, column=1, padx=5)

get_weather_button = Button(input_frame, text="Get Weather", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=get_weather)
get_weather_button.grid(row=0, column=2, padx=5)

# Weather info frame
weather_frame = Frame(root, bg="white", bd=5, relief="groove")
weather_frame.pack(pady=20, padx=20, fill="both", expand=True)

Label(weather_frame, text="Temperature", font=("Arial", 12), bg="white", fg="#333").grid(row=0, column=0, padx=20, pady=10)
temperature_label = Label(weather_frame, text="--", font=("Arial", 14, "bold"), bg="white", fg="#ff7f50")
temperature_label.grid(row=1, column=0, padx=20, pady=5)

Label(weather_frame, text="Feels Like", font=("Arial", 12), bg="white", fg="#333").grid(row=0, column=1, padx=20, pady=10)
feels_like_label = Label(weather_frame, text="--", font=("Arial", 14, "bold"), bg="white", fg="#ff7f50")
feels_like_label.grid(row=1, column=1, padx=20, pady=5)

Label(weather_frame, text="Day Condition", font=("Arial", 12), bg="white", fg="#333").grid(row=2, column=0, padx=20, pady=10)
day_label = Label(weather_frame, text="--", font=("Arial", 14, "bold"), bg="white", fg="#ff7f50")
day_label.grid(row=3, column=0, padx=20, pady=5)

Label(weather_frame, text="Wind Speed", font=("Arial", 12), bg="white", fg="#333").grid(row=2, column=1, padx=20, pady=10)
wind_speed_label = Label(weather_frame, text="--", font=("Arial", 14, "bold"), bg="white", fg="#ff7f50")
wind_speed_label.grid(row=3, column=1, padx=20, pady=5)

Label(weather_frame, text="Wind Direction", font=("Arial", 12), bg="white", fg="#333").grid(row=4, column=0, padx=20, pady=10)
wind_direction_label = Label(weather_frame, text="--", font=("Arial", 14, "bold"), bg="white", fg="#ff7f50")
wind_direction_label.grid(row=5, column=0, padx=20, pady=5)

Label(weather_frame, text="Humidity", font=("Arial", 12), bg="white", fg="#333").grid(row=4, column=1, padx=20, pady=10)
humidity_label = Label(weather_frame, text="--", font=("Arial", 14, "bold"), bg="white", fg="#ff7f50")
humidity_label.grid(row=5, column=1, padx=20, pady=5)

Label(weather_frame, text="Pressure", font=("Arial", 12), bg="white", fg="#333").grid(row=6, column=0, padx=20, pady=10)
pressure_label = Label(weather_frame, text="--", font=("Arial", 14, "bold"), bg="white", fg="#ff7f50")
pressure_label.grid(row=7, column=0, padx=20, pady=5)

Label(weather_frame, text="Visibility", font=("Arial", 12), bg="white", fg="#333").grid(row=6, column=1, padx=20, pady=10)
visibility_label = Label(weather_frame, text="--", font=("Arial", 14, "bold"), bg="white", fg="#ff7f50")
visibility_label.grid(row=7, column=1, padx=20, pady=5)

Label(weather_frame, text="UV Index", font=("Arial", 12), bg="white", fg="#333").grid(row=8, column=0, padx=20, pady=10)
uv_index_label = Label(weather_frame, text="--", font=("Arial", 14, "bold"), bg="white", fg="#ff7f50")
uv_index_label.grid(row=9, column=0, padx=20, pady=5)

# Start the Tkinter main loop
root.mainloop()
