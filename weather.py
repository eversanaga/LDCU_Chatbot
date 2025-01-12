from requests import get

def fetchWeather(APIKey) -> str:
	output = get(f"http://api.openweathermap.org/data/2.5/weather?q=Cagayan%20De%20Oro&appid={APIKey}&units=metric")
	if output.status_code == 200:
		out = output.json()
		return f"The current weather in Cagayan De Oro City is {out['weather'][0]['description']} with a temperature of {out['main']['temp']}°C."

	else:
		return "I apologize, It seems that I am not able fetch the current weather data."