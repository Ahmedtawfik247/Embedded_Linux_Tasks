import requests
import webbrowser

def get_random_activity():
  """Gets a random activity from the Bored API."""
  response = requests.get("https://www.boredapi.com/api/activity")
  data = response.json()
  return data

def main():
  """Suggests a random activity."""
  activity = get_random_activity()
  print(f"Here is a random activity for you: {activity['activity']}")
  print(f"Do you want to try it? (y/N)")
  choice = input()
  if choice == "y":
    print(f"Opening {activity['link']} in your browser...")
    webbrowser.open(activity['link'])

if __name__ == "__main__":
  main()