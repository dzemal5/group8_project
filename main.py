import gradio as gr
from crew import CaviarCrew

def caviar_coach(taste_profile, texture_preference, budget):
    preferences = {
        "taste_profile": taste_profile,
        "texture_preference": texture_preference,
        "budget": int(budget)
    }
    
    crew = CaviarCrew()
    result = crew.get_caviar_experience(preferences)
    
    response = f"""
    Your Imperial Highness,

    Based on your exquisite preferences, I am honored to present our recommendation:

    🥄 Caviar Selection: {result['caviar_recommendation']}

    🍾 Champagne Pairing: {result['champagne_pairing']}

    📜 Exclusive Insights:
    {result['exclusive_content']}

    May this experience elevate your senses and leave an indelible mark on your palate.

    Bon appétit, Your Highness.
    """
    
    return response

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