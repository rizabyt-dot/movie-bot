import requests

API_KEY = "2563f49e"
def get_movie(movie_name):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        print("\n🎬 Movie Found!")
        print("Title:", data["Title"])
        print("Year:", data["Year"])
        print("IMDb Rating:", data["imdbRating"])
        print("Director:", data["Director"])
        print("Actors:", data["Actors"])
        print("Plot:", data["Plot"])
    else:
        print("❌ Movie not found")

movie = input("Enter movie name: ")
get_movie(movie)
