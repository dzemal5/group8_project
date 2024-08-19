import os
import gradio as gr
from dotenv import load_dotenv
import google.generativeai as palm

# Load environment variables
load_dotenv()

# Configure the API
palm.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_text(prompt):
    completion = palm.generate_text(
        model="models/text-bison-001",
        prompt=prompt,
        temperature=0.7,
        max_output_tokens=800,
    )
    return completion.result

def caviar_coach(taste_profile, texture_preference, budget):
    prompt = f"""
    As a luxury caviar expert, provide a personalized recommendation based on the following preferences:
    Taste Profile: {taste_profile}
    Texture Preference: {texture_preference}
    Budget: ${budget}

    Please provide:
    1. A specific caviar recommendation
    2. A champagne pairing suggestion
    3. Some exclusive insights or tips for enjoying this caviar experience

    Format your response as follows:
    Caviar Selection: [Your recommendation]
    Champagne Pairing: [Your pairing suggestion]
    Exclusive Insights: [Your insights or tips]
    """

    try:
        response = generate_text(prompt)
        formatted_response = f"""
        Your Imperial Highness,

        Based on your exquisite preferences, I am honored to present our recommendation:

        {response}

        May this experience elevate your senses and leave an indelible mark on your palate.

        Bon appétit, Your Highness.
        """
        return formatted_response
    except Exception as e:
        return f"An error occurred: {str(e)}\nPlease check if the API key is set correctly."

iface = gr.Interface(
    fn=caviar_coach,
    inputs=[
        gr.Dropdown(["Mild & Delicate", "Rich & Buttery", "Bold & Intense"], label="Preferred Taste Profile"),
        gr.Dropdown(["Soft & Creamy", "Firm & Distinct"], label="Preferred Texture"),
        gr.Slider(minimum=50, maximum=1000, step=50, label="Budget (USD)")
    ],
    outputs=gr.Textbox(label="Your Royal Recommendation"),
    title="🍾 Imperial Caviar Connoisseur 🥂",
    description="Your Imperial Highness, please share your preferences for an exquisite caviar experience.",
)

if __name__ == "__main__":
    iface.launch()
