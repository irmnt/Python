import requests

API_KEY = "0a8f6398a706dc750d70328c97246cc7"
city = input("Where are you located?: ")

lat = -11.8092
lon = 51.509865

url = f"https://api.openweathermap.org/data/3.0/onecall/overview?lat={lat}&lon={lon}&appid={API_KEY}"

response = requests.get(url)

print(response.status_code)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    
    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s")
else:
    print("Error: Could not retrieve weather data.")