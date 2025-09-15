# Import the module.
import python_weather

import asyncio
import os


async def main() -> None:
  
  # Declare the client. The measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    
    # Fetch a weather forecast from a city.
    weather = await client.get('Toronto')
    hour = []
    hourly_weather = []
    description = []
    
    # Fetch the temperature for today.
    print(weather.temperature)
    
    # Fetch weather forecast for upcoming days.
    for daily in weather:
      print(daily.date, end=' : ')
    
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
           
      #print hour 
      print(end='\n') 
      for j in range(len(hour)):
        print(f' {hour[j]} |', end=' ')
      
      #print temperature  
      print(end='\n')
      for k in range(len(hourly_weather)):
        print(f' {hourly_weather[k]}F  |', end=' ')
        
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
