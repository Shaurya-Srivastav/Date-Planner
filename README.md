# Date Planner for Couples - Technical Documentation

This Python application, "Date Planner for Couples," is designed to help couples plan a romantic food date in their chosen city. It utilizes various libraries and APIs to provide restaurant suggestions based on city and cuisine preferences. This document provides a detailed technical overview of the application.

## Features

### 1. Location-Based Date Planning

- **City Selection**: Users can input the name of their preferred city where they want to plan their date.

### 2. Cuisine Selection

- **Cuisine Dropdown**: Users can choose from a variety of cuisines, including Italian, Mexican, Indian, Chinese, Japanese, Thai, Greek, American, French, or even opt for a "Random" cuisine.

### 3. Randomized Date Plans

- **Randomization**: The application uses a random seed generated from the current time to ensure each date plan is unique and spontaneous.

- **Restaurant Suggestions**: Based on the selected city and cuisine, the application fetches restaurant data from Yelp and suggests five random food spots for the date.

### 4. Detailed Restaurant Information

- **Restaurant Details**: For each restaurant suggestion, the application provides the following information:
    - Restaurant Name
    - Rating (out of 5.0)
    - Number of Reviews
    - Popular Dish Photos (up to 3 photos)

### 5. Error Handling

- **Error Handling**: The application includes robust error handling to gracefully handle exceptions, providing users with informative error messages if any issues occur during execution.

## How the Application Works

1. **Import Statements**: The application begins with importing the necessary libraries and modules. These include Streamlit, random, time, geopy, yelpapi, Pillow (PIL), and requests.

2. **Yelp API Key**: You must provide your Yelp API key for accessing restaurant data. Replace the `YELP_API_KEY` variable in the code with your own key.

3. **Location Retrieval (get_coordinates)**: This function uses the Geopy library to obtain latitude and longitude coordinates for a given city. It performs a geocoding lookup and returns the coordinates if found.

4. **Restaurant Search (get_food_spots)**: This function utilizes the YelpAPI library to query Yelp for food spots in the specified city and cuisine. It returns a list of relevant restaurant data.

5. **Random Spot Selection (choose_random_food_spots)**: Given a list of food spots, this function randomly selects 5 spots for the date plan.

6. **Photo Retrieval (get_photos)**: This function fetches restaurant photos using the Yelp API based on a business ID.

7. **Main Function (main)**: The `main` function serves as the entry point for the Streamlit application. It defines the Streamlit interface, where users can input their city and cuisine preferences and initiate the date planning process.

8. **User Input and Button (st.text_input, st.selectbox, st.button)**: The application takes user input for the city and cuisine and provides a "Plan Date!" button to initiate the date planning.

9. **Date Planning Logic**: When the user clicks the "Plan Date!" button, the application generates a date plan. It fetches food spots based on the chosen city and cuisine, selects 5 random spots, and displays relevant information, including ratings, reviews, and photos.

## Running the Application

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will launch the Streamlit app in your default web browser. You can then interact with the app to plan your romantic food date.

## Customization

You can customize the application by modifying the available cuisines, changing the number of selected random food spots, or enhancing the user interface to include additional features. The code is modular and well-structured, making it easy to extend and customize as per your requirements.

## Note

This application is intended for educational and recreational purposes. Be sure to comply with Yelp's terms of service and usage guidelines when using their API.
