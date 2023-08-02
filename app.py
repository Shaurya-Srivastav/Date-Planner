import streamlit as st
import random
import time
from geopy.geocoders import Nominatim
from yelpapi import YelpAPI
from PIL import Image
import requests
from io import BytesIO

YELP_API_KEY = "tMKtgU5qUHGDubCTAg-x03kX10IsgoP4mraQfmu3kG0Mx4N6r6fqWvIpcqtXPOR1jPtgUJQ8T-7XPxFlAzPqBRd3-O5qBvougUjHpzrY2C4XM4MtZgW3cnOqj7_JZHYx"

def get_coordinates(city):
    geolocator = Nominatim(user_agent="date-planner-app/1.0")
    location = geolocator.geocode(city, addressdetails=True)
    if location:
        return location.latitude, location.longitude
    return None

def get_food_spots(city, cuisine, random_seed):
    city_latitude, city_longitude = get_coordinates(city)
    if not city_latitude or not city_longitude:
        st.warning("No coordinates found for the city.")
        return []

    yelp_api = YelpAPI(YELP_API_KEY)
    params = {
        "term": cuisine,
        "latitude": city_latitude,
        "longitude": city_longitude,
        "limit": 30,  # Fetch 30 food spots
        "sort_by": "best_match",
        "random_seed": random_seed  # Use random seed in API query
    }
    response = yelp_api.search_query(**params)
    food_spots = [(spot["name"], spot["url"], spot["review_count"], spot["rating"], spot["id"]) for spot in response.get("businesses", [])]
    return food_spots

def choose_random_food_spots(food_spots):
    # Randomly choose 5 food spots from the list of 30
    random_food_spots = random.sample(food_spots, 5)
    return random_food_spots

def get_photos(business_id):
    yelp_url = f"https://api.yelp.com/v3/businesses/{business_id}/photos"
    headers = {
        "Authorization": f"Bearer {YELP_API_KEY}"
    }
    response = requests.get(yelp_url, headers=headers)
    photos = response.json().get("photos", [])
    return photos

def main():
    st.title("Date Planner for Couples")
    st.write("Select a city and cuisine, and the app will plan a food date for you!")

    city = st.text_input("Enter the city:", "San Francisco")

    cuisines = [
        "Italian",
        "Mexican",
        "Indian",
        "Chinese",
        "Japanese",
        "Thai",
        "Greek",
        "American",
        "French",
        "Random"
    ]
    cuisine = st.selectbox("Select cuisine:", cuisines)

    if st.button("Plan Date!"):
        if not city:
            st.warning("Please enter a valid city.")
            return

        if cuisine == "Random":
            cuisine = random.choice(cuisines[:-1])

        st.write("Generating date plan...")
        try:
            # Get the current time and use it as the random seed
            random_seed = int(time.time())
            random.seed(random_seed)

            food_spots = get_food_spots(city, cuisine, random_seed)
            if not food_spots:
                st.warning(f"No {cuisine} food spots found in {city}. Try another cuisine or location.")
                return

            random_food_spots = choose_random_food_spots(food_spots)
            st.subheader("Food Spots:")
            for i, (spot, url, review_count, rating, business_id) in enumerate(random_food_spots, 1):
                st.markdown(f"## **[{spot}]({url})**")
                st.write(f"Rating: {rating:.1f} / 5.0")
                st.write(f"Reviews: {review_count}")

                photos = get_photos(business_id)
                if photos:
                    for photo_url in photos[:3]:  # Show up to 3 photos in the collage
                        response = requests.get(photo_url)
                        img = Image.open(BytesIO(response.content))
                        st.image(img, caption=f"{spot} Popular Dish", use_column_width=True)

                st.write("")

        except Exception as e:
            st.error("Error occurred: {}".format(str(e)))

if __name__ == "__main__":
    main()
