![An elegant and minimalistic image showing a tin of caviar and a champagne glass on a dark background](header.webp)

# Caviar Recommendation and Analysis

## Table of Contents

1. [CrewAI Integration](#crewai-integration)
2. [Installation](#installation)
3. [API Configuration](#api-configuration)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Contributing](#contributing)
7. [License](#license)

## CrewAI Integration

This project leverages CrewAI, an advanced AI framework designed to orchestrate multiple specialized agents that collaborate to achieve complex goals. CrewAI enables the seamless integration of domain-specific expertise into the project, enhancing the overall user experience.

### What is CrewAI?

CrewAI is a platform that allows the deployment of multiple AI agents with specific roles and goals, working together to solve problems, provide recommendations, or generate content. Each agent is equipped with a distinct personality, backstory, and expertise, which makes the interactions more realistic and effective.

### Advantages of Using CrewAI

- **Domain Expertise:** Each agent in CrewAI is tailored to possess deep knowledge in a specific area, ensuring high-quality outputs.
- **Collaboration:** Multiple agents can work together, combining their expertise to provide comprehensive solutions.
- **Customization:** Agents can be customized with unique roles, goals, and backstories, making them versatile for various applications.
- **Scalability:** CrewAI allows for the easy scaling of operations by adding or modifying agents as needed.

### Agents Used in This Project

The following agents are used in this project to provide a sophisticated and well-rounded caviar dining experience:

1. **Caviar Expert**

   - **Role:** Imperial Caviar Connoisseur
   - **Goal:** Provide expert recommendations on caviar selection based on individual preferences and dietary restrictions.
   - **Backstory:** You are a world-renowned caviar expert with decades of experience in the luxury dining industry. Your palate is refined, and you have an encyclopedic knowledge of caviar varieties, their origins, and optimal pairings. You take pride in elevating each client's dining experience to new heights of sophistication.

2. **Sommelier**

   - **Role:** Royal Champagne Sommelier
   - **Goal:** Recommend the perfect champagne pairing for each caviar selection.
   - **Backstory:** You are a master sommelier with a particular expertise in champagne. Your knowledge of vintage years, terroir, and flavor profiles is unparalleled. You have a passion for creating harmonious pairings that enhance both the caviar and champagne experience.

3. **Content Curator**
   - **Role:** Luxury Dining Content Curator
   - **Goal:** Curate exclusive content related to caviar, including expert insights and the latest industry trends.
   - **Backstory:** You are a seasoned content curator with a keen eye for luxury dining trends. You work closely with industry experts to bring the most valuable and exclusive content to discerning caviar enthusiasts.

## Installation

To run this project, you'll need to have Python installed along with the following packages:

- `gradio`
- `google-generativeai`
- `textwrap`
- `langchain`
- `langchain_openai`
- `crewai`

You can install the necessary packages using pip:

```sh
pip install pandas jupyter os gradio dotenv google-generativeai re requests json textwrap langchain langchain_openai crewai
```

## API Configuration

This project requires several API keys to function correctly. These should be stored in a `.env` file in the root directory of the project.

The following API keys are required:

- `GOOGLE_PALM_API_KEY` for Google PaLM API
- `SERPER_API_KEY` for SerpAPI
- `OPENAI_API_KEY` for OpenAI API
- `YELP_API_KEY` for Yelp API
- `WEATHER_API_KEY` for weather-related data

Example `.env` file:

```env
GOOGLE_PALM_API_KEY=your_google_palm_api_key_here
SERPER_API_KEY=your_serper_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
YELP_API_KEY=your_yelp_api_key_here
WEATHER_API_KEY=your_weather_api_key_here
```

These keys will be loaded using the `dotenv` package:

## Usage

To use this notebook, follow these steps:

1. Clone the repository or download the notebook file.
2. Navigate to the directory containing the notebook.
3. Ensure your `.env` file is properly configured with the necessary API keys.
4. Open the notebook using Jupyter:

```sh
jupyter notebook caviar_trivia_added_to_vlad_file.ipynb
```

5. Run the cells in the notebook to generate the visualizations and analysis.

## Project Structure

- `caviar_trivia_added_to_vlad_file.ipynb`: The main notebook containing all the code and analysis.
- `README.md`: Instructions and guidelines for using the project.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.