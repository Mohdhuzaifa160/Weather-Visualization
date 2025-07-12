import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your API key
API_KEY = 'your_api_key_here'
CITY = 'Delhi'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Extract required data
dates = []
temps = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temps.append(entry['main']['temp'])

# Visualization using seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps, marker='o')
plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
