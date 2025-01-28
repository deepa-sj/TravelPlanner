# AI Travel Planner

This is an interactive travel itinerary generator built using OpenAI and Streamlit. The application allows users to input their travel preferences and generates a personalized itinerary, including activities, accommodations, and dining suggestions. The app takes into account factors such as budget, dietary preferences, mobility concerns, and accommodation types.

## Features:
- Generate a personalized travel itinerary based on user preferences.
- Provide suggestions for meals, accommodations, and activities.
- Flexible design for different travel needs and interests, including budget, dietary, and mobility preferences.
- Easy to deploy and use with Streamlit Cloud or locally.

## Installation

Follow the steps below to run the application locally or deploy it on your own machine.

### Prerequisites:
- Python 3.6 or higher installed on your machine.
- An OpenAI API key (You’ll need this to access the GPT model).

### Step 1: Clone the Repository
Start by cloning the repository to your local machine using Git or by downloading the ZIP file from GitHub.

If you have Git installed, open your terminal and run the following command:

```bash
git clone https://github.com/deepa-sj/TravelPlanner.git
```

Alternatively, you can download the repository as a ZIP file by clicking the "Code" button on the GitHub repository page and selecting "Download ZIP."

### Step 2: Navigate to the Project Folder
After cloning or downloading the repository, navigate to the project folder:

```bash
cd TravelPlanner
```

### Step 3: Install the Required Dependencies
The application uses `Streamlit` for the user interface and `OpenAI` for generating itineraries. Install the necessary Python dependencies using `pip`.

Create a **virtual environment** (optional but recommended) and install the dependencies listed in the `requirements.txt` file.

1. **Create a virtual environment**:
   - On **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

The `requirements.txt` file includes the necessary libraries such as:
- `streamlit`
- `openai`

### Step 4: Set Up Your OpenAI API Key
To use OpenAI’s GPT model, you’ll need to set up your API key.

1. Go to [OpenAI’s API](https://beta.openai.com/signup/) and sign up for an API key.
2. After you have the API key, create a `.env` file in the root of the project directory.
3. Add the following line to the `.env` file, replacing `your_openai_api_key` with your actual API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

**Note**: This step is crucial for the app to work, as it needs the API key to interact with OpenAI’s models.

### Step 5: Run the Streamlit Application

Once the dependencies are installed and the API key is set up, you can run the app with Streamlit.

1. In your terminal, run the following command to launch the Streamlit app:

```bash
streamlit run app.py
```

2. The Streamlit app should now launch, and you can interact with the app through the browser (usually at `http://localhost:8501`).

### Step 6: Use the Application
Once the app is running, you'll be prompted to input your travel preferences:
- **Destination**
- **Trip Duration**
- **Budget** (Low, Moderate, High)
- **Interests** (e.g., art, history, local cuisine)
- **Dietary Preferences** (e.g., vegetarian, vegan)
- **Mobility Concerns** (e.g., none, limited walking)
- **Accommodation Preferences** (e.g., budget, central location)

After submitting your preferences, the app will generate a personalized travel itinerary, including day-by-day activities, meal recommendations, and accommodation suggestions.

---

## Troubleshooting

- **Missing Dependencies**: If you encounter any issues related to missing dependencies, ensure that `requirements.txt` contains all the necessary libraries.
- **API Key Not Set**: Make sure your `.env` file is correctly set up with the OpenAI API key. If the app can’t find the API key, it will not be able to generate itineraries.
- **App Not Loading**: If the app is not loading, try restarting Streamlit by stopping the app (`Ctrl+C` in the terminal) and running it again using the `streamlit run app.py` command.

---

## Contributing

Feel free to fork the repository, submit issues, or create pull requests if you'd like to contribute to this project.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

This updated `README.md` provides clear instructions for setting up the project locally and troubleshooting common issues. Let me know if you need any further additions or modifications!
