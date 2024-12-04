import requests

def fetch_random_user_data_from_freeAPI():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    raw_data = response.json()

    if raw_data["statusCode"] != 200:
        print("Unable to fetch data from API")
        return None
    
    if raw_data["success"] and "data" in raw_data:
        user_data = raw_data["data"]

        username = user_data["login"]["username"]
        country = user_data["location"]["country"]

        print(raw_data["message"])

        return username, country
    else:
        raise Exception("Unable to fetch data from API")
    

def main():
    try:
        username, country = fetch_random_user_data_from_freeAPI()

        print(f"Username: {username}")

        print(f"Country: {country}")
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
        