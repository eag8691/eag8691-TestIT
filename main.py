import json, requests

base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "e14d849bcdb2f061967f170f841733bd"

def main():
  city = input("\nPlease enter a city or zipcode: ")

  url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
  print(url)
  print ()

  response = requests.get(url)
  unformatted_data = response.json()

  unformatted_data = response.json()

  def get_temp():
    try:
      temp = unformatted_data["main"]["temp"]
      print(f"The current temp is: {temp}")

      temp_max = unformatted_data["main"]["temp_max"]
      print(f"The max temp is: {temp_max}")

    except Exception:
      print(f"{city} is not a valid city or zipcode. Please try again.")


  get_temp()

main()

active = True
while active:
  message = input("Would you like to run again? y/n: ")

  if message == 'n':
    active = False
    print("\nThank you for using openweather.org")
  else: 
    main()

