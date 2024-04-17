import pandas as pd
import matplotlib.pyplot as plt

file_path = './Json/flight_data_296160_3.json' 
df = pd.read_json(file_path)

df['Price'] = df['Price'].str.replace(',', '').astype(int)

df['Duration_minutes'] = df['Total timing (Duration)'].str.extract('(\d+)h (\d+)m').apply(lambda x: int(x[0]) * 60 + int(x[1]), axis=1)

avg_price_per_airline = df.groupby('Type of Flight')['Price'].mean()

flight_durations = df['Duration_minutes']

flights_per_airline = df['Type of Flight'].value_counts()

plt.figure(figsize=(10, 6))
plt.hist(flight_durations, bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Flight Durations')
plt.xlabel('Duration in Minutes')
plt.ylabel('Number of Flights')
plt.show()

avg_price_per_airline.plot(kind='bar', figsize=(10, 6), color='lightgreen')
plt.title('Average Price per Airline')
plt.xlabel('Airline')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.show()

flights_per_airline.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%')
plt.title('Proportion of Flights by Airline')
plt.ylabel('')
plt.show()
