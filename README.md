# Date Planner for Couples - Technical Documentation

This Python application, "Date Planner for Couples," is designed to help couples plan a romantic food date in their chosen city. It utilizes various libraries and APIs to provide restaurant suggestions based on city and cuisine preferences. This document provides a detailed technical overview of the application.

## Prerequisites

Before running the application, ensure that you have the required Python libraries installed. You can install these dependencies using pip:

```bash
pip install streamlit geopy yelpapi pillow requests
```

### Additional Requirements

You'll also need a Yelp API key to access restaurant data. Replace the `YELP_API_KEY` in the code with your own API key.

## Application Structure

The application is built using the Streamlit framework and comprises several functions and modules:

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

You can customize the application by modifying the available cuisines or changing the number of selected random food spots. Additionally, you can enhance the user interface or add more features as per your requirements.

## Error Handling

The application includes error handling to capture and display any exceptions that may occur during execution, ensuring a smooth user experience.

## Note

This application is intended for educational and recreational purposes. Be sure to comply with Yelp's terms of service and usage guidelines when using their API.
