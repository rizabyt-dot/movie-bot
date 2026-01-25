import requests

API_KEY = "thewdb"   # demo key, safe for GitHub

def get_movie(movie_name):
    url = "https://www.omdbapi.com/"
    params = {
        "t": movie_name,
        "apikey": API_KEY
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if data.get("Response") == "True":
        print("\n🎬 Movie Found!")
        print("Title       :", data.get("Title"))
        print("Year        :", data.get("Year"))
        print("IMDb Rating :", data.get("imdbRating"))
        print("Director    :", data.get("Director"))
        print("Actors      :", data.get("Actors"))
        print("Plot        :", data.get("Plot"))
    else:
        print("❌ Movie not found.")
        print("Reason:", data.get("Error"))

def main():
    print("🎥 OMDb Movie Search Bot")
    print("-" * 30)
    movie = input("Enter movie name: ").strip()
    if movie:
        get_movie(movie)
    else:
        print("❌ Movie name cannot be empty")

if __name__ == "__main__":
    main()
