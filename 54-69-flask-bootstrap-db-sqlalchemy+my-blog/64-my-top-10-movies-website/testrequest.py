import requests

API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYzllYTNlYzdmYzc2YWVjOTEwM2NhYmE0NTU2MTkxNCIsInN1YiI6IjYyMTRiYTBmOWY1ZGZiMDAxYjMxY2E4ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tce2nN80Z-uNrcLHHcpS6RslVPd3WGH0U0m4EruluDQ"
API_ENDPOINT = "https://api.themoviedb.org/3/search/movie"

params = {
            "query": "Phone Booth",
            "include_adult": False,
            "language": "en-US"
        }
headers = {
    "accept": "application.json",
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url=API_ENDPOINT, params=params, headers=headers).json()

print(response)
