import openai
import streamlit as st
from openai import OpenAI

# Initialize OpenAI client with your API key
api_key="YOUR_API_KEY"
if not api_key:
    st.error("API key not found. Set the environment variable OPENAI_API_KEY.")
    st.stop()

client = OpenAI(api_key=api_key)


def get_itinerary(destination, trip_duration, budget, interests, dietary, mobility, accommodation):
    system_prompt = (
        "You are TravelGPT, an AI travel assistant. "
        "Your goal is to help the user plan a personalized itinerary based on their preferences. "
        "Ask clarifying questions if needed. "
        "Refine inputs like 'moderate budget' into actionable details. Provide detailed day-by-day plans."
    )

    refinement_prompt = (
        f"Destination: {destination}\n"
        f"Trip Duration: {trip_duration} days\n"
        f"Budget: {budget}\n"
        f"Interests: {interests}\n"
        f"Dietary Preferences: {dietary}\n"
        f"Mobility Concerns: {mobility}\n"
        f"Accommodation Preferences: {accommodation}\n"
        "If any input is vague, clarify it by asking relevant questions."
    )

    user_prompt = f"""
    Based on the provided details, create a detailed day-by-day travel itinerary. 
    Include:
    - Morning, afternoon, and evening activities.
    - Recommendations for meals and accommodations.
    - Suggestions aligned with interests and mobility concerns.
    - Balance between famous attractions and hidden gems.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": refinement_prompt},
            {"role": "assistant", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response["choices"][0]["message"]["content"]

# Streamlit app
st.title("AI-Powered Travel Planner")

# User input fields
destination = st.text_input("Destination", placeholder="e.g., Paris")
trip_duration = st.number_input("Number of Days", min_value=1, max_value=30, value=5)
budget = st.selectbox("Budget", ["Low", "Moderate", "High"])
interests = st.text_input("Interests", placeholder="e.g., art, history, local cuisine")
dietary = st.text_input("Dietary Preferences or Restrictions", placeholder="e.g., vegetarian, vegan")
mobility = st.text_input("Mobility Concerns", placeholder="e.g., none, limited walking")
accommodation = st.text_input("Preferred Accommodation Type", placeholder="e.g., budget, central location")

# Button to generate itinerary
if st.button("Generate Itinerary"):
    if destination and interests:
        st.info("Generating your personalized itinerary. Please wait...")
        itinerary = get_itinerary(destination, trip_duration, budget, interests, dietary, mobility, accommodation)
        st.subheader("Your Personalized Itinerary:")
        st.write(itinerary)
    else:
        st.error("Please provide at least the destination and your interests to proceed.")


