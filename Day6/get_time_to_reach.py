import requests
import sys

API_KEY = "" #removed from secirty 

def main():
    if len(sys.argv) != 3:
        print("Usage: python get_time_to_reach.py 'Source' 'Destination'")
        return

    source = sys.argv[1]
    destination = sys.argv[2]
    url = "https://routes.googleapis.com/directions/v2:computeRoutes"
    payload = {
        "origin": {"address": source},
        "destination": {"address": destination},
        "travelMode": "DRIVE"
    }
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "routes.duration"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        if response.status_code == 200 and "routes" in data:

            duration_seconds = data["routes"][0]["duration"]
            seconds = int(duration_seconds.replace("s", ""))
            
            minutes = round(seconds / 60)
            print(f"{minutes} Minutes")
        else:
            print(f"Error: {data.get('error', {}).get('message', 'Unknown Error')}")
            print(f"Status Code: {response.status_code}")

    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    main()