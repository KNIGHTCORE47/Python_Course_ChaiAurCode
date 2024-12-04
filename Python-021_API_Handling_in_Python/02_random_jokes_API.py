import requests

def fetch_random_joke_from_freeAPI():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    raw_data = response.json()

    if raw_data["statusCode"] != 200:
        print("Unable to fetch data from API")
        return None
    
    if raw_data["success"] and "data" in raw_data:
        joke_data = raw_data["data"]

        content = joke_data["content"]

        print(raw_data["message"])

        return content
    
    else:
        raise Exception("Unable to fetch data from API")


def main():
    try:
        joke = fetch_random_joke_from_freeAPI()
        print(f"Joke: {joke}")
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()