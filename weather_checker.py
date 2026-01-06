# Import the module.
import python_weather

import asyncio
import os


def fahrenheit_to_celsius(fahrenheit: float) -> float:
  """Convert Fahrenheit to Celsius."""
  return (fahrenheit - 32) * 5/9


async def main() -> None:
  
  # Declare the client. The measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    

    print('Enter the city name to get the weather forecast:')
    city = input()
    
    # Fetch a weather forecast from a city.
    weather = await client.get(city)
    
    # Error handling for invalid city names.
    if weather is False:
      print(f'City "{city}" not found. Please check the city name and try again.')
      return
    
    hour = []
    hourly_weather = []
    description = []
    
    # Fetch the temperature for today.
    print('Today:', f'{weather.temperature}F', ' | ', f'{fahrenheit_to_celsius(weather.temperature):.1f}C')
    print('\n')
    
    # Fetch weather forecast for upcoming days.
    for daily in weather:
      print(daily.date, end=' :\n ')
    
      # Each daily forecast has their own hourly forecasts.
      for hourly in daily:
        # collect data of hour, temperature and sky description
        hour.append(hourly.time.strftime('%I%p'))
        hourly_weather.append(hourly.temperature)
        if len(description) == 0 or description[-1] != hourly.description:
          description.append(hourly.description) 
        
      for i in range(len(description)): 
        desc = description[i] 
        print(f'{desc}', end=' ')
        print('-->', end=' ') if i != len(description)-1 else print(end=' ')
           
      # Calculate column width based on max of hour, F, and C values
      col_width = 3
      for k in range(len(hourly_weather)):
        celsius = fahrenheit_to_celsius(hourly_weather[k])
        f_str = f'{hourly_weather[k]}F'
        c_str = f'{celsius:.1f}C'
        col_width = max(col_width, len(hour[k]), len(f_str), len(c_str)) + 1
      
      #print hour 
      print(end='\n') 
      print('Hour'.rjust(12), end='|')
      for j in range(len(hour)):
        output = f'{hour[j]}'
        output_centerd  = output.center(col_width)
        print(f'{output_centerd}'.rjust(col_width), end='|')
      
      #print temperature in Fahrenheit
      print(end='\n')
      print('Fahrenheit'.rjust(12), end='|')
      for k in range(len(hourly_weather)):
        output = f'{hourly_weather[k]}F'
        output_centered = output.center(col_width)
        print(f'{output_centered}'.rjust(col_width), end='|')
      
      #print temperature in Celsius
      print(end='\n')
      print('Celsius'.rjust(12), end='|')
      for k in range(len(hourly_weather)):
        celsius = fahrenheit_to_celsius(hourly_weather[k])
        output = f'{celsius:.1f}C'
        output_centered = output.center(col_width)
        print(f'{output_centered}'.rjust(col_width), end='|')
        
      print(end='\n')
      hour.clear()
      hourly_weather.clear()
      description.clear()
      print('\n')


if __name__ == '__main__':
  
  # See https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details.
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
  asyncio.run(main())
