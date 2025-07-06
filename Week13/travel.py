import streamlit as st
import openai

# Put your OpenAI API key here
openai.api_key = "MY_API_KEY"

st.title("NZ Travel Itinerary Generator")

# User inputs
destinations = st.multiselect("Destinations", ["Auckland", "Christchurch", "Queenstown"])
num_days = st.number_input("Number of days", min_value=1, value=7)
num_people = st.number_input("Number of people", min_value=1, value=2)
budget = st.selectbox("Budget", ["Low", "Mid-range", "Luxury"])
preferences = st.multiselect("Preferences", ["food", "nature", "adventure", "culture"])

if st.button("Generate Itinerary"):
    prompt = (
        f"Instructions: Make a detailed, day-by-day trip plan for a client who is going to New Zealand. "
        f"The client's tastes, budget, and travel plans should be taken into account when making the itinerary. "
        f"Include suggestions for each day's attractions, events, restaurants, and places to stay. "
        f"Make sure the ideas are reasonable and workable for the places and preferences that were given.\n\n"
        f"Context: You work for a travel firm in New Zealand as an AI travel assistant. "
        f"Your job is to make it easy for travel agents to quickly make custom itineraries for their clients "
        f"that take into account different budgets, hobbies, and places to visit in New Zealand, "
        f"such as those interested in adventure, culture, food, or nature.\n\n"
        f"Data to enter:\n"
        f"-Destinations: {', '.join(destinations)}\n"
        f"-Number of people: {num_people}\n"
        f"-Number of days: {num_days}\n"
        f"-Costs: {budget}\n"
        f"-Preferences: {', '.join(preferences)}\n\n"
        f"Output Indicator:\n"
        f"A structured, day-by-day travel itinerary that includes:\n"
        f"-Daily activities and attractions\n"
        f"-Recommended places to eat\n"
        f"-Suggested accommodations\n"
        f"-Estimated daily costs (optional)\n"
        f"-Local tips or highlights for each day"
    )
    with st.spinner("Generating itinerary..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
            temperature=0.7,
        )
        itinerary = response.choices[0].message.content
        st.markdown(itinerary)
