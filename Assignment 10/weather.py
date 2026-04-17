import requests

API_KEY = "YOUR_API_KEY"  

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Error: City not found or API issue.")
        return

    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    description = data["weather"][0]["description"]

    print("Weather:", description)
    print(f"Temperature: {temp_celsius:.2f} °C")


if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)