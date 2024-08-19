import os
import logging
from dotenv import load_dotenv
from langchain_community.llms import GooglePalm
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from typing import Dict, Any

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@CrewBase
class CaviarCrew():
    """Caviar crew for luxury dining experiences"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("gemini_api_key")
        if not api_key:
            raise ValueError("No API key found. Please set GOOGLE_API_KEY or gemini_api_key environment variable.")
        logger.debug(f"API key found: {api_key[:5]}...{api_key[-5:]}")
        try:
            self.llm = GooglePalm(google_api_key=api_key)
            logger.debug("GooglePalm LLM initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing GooglePalm: {str(e)}")
            raise

    @agent
    def caviar_expert(self) -> Agent:
        return Agent(config=self.agents_config['caviar_expert'], llm=self.llm, verbose=True)

    @agent
    def sommelier(self) -> Agent:
        return Agent(config=self.agents_config['sommelier'], llm=self.llm, verbose=True)

    @agent
    def content_curator(self) -> Agent:
        return Agent(config=self.agents_config['content_curator'], llm=self.llm, verbose=True)

    @task
    def recommend_caviar(self) -> Task:
        return Task(config=self.tasks_config['recommend_caviar'])

    @task
    def pair_champagne(self) -> Task:
        return Task(config=self.tasks_config['pair_champagne'])

    @task
    def curate_content(self) -> Task:
        return Task(config=self.tasks_config['curate_content'])

    @crew
    def crew(self) -> Crew:
        """Creates the Caviar crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

    def get_caviar_experience(self, preferences: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a personalized caviar experience based on user preferences.
        
        Args:
            preferences (Dict[str, Any]): User's preferences for caviar selection.
        
        Returns:
            Dict[str, Any]: Personalized caviar recommendation, champagne pairing, and exclusive content.
        """
        inputs = {"preferences": preferences}
        try:
            result = self.crew().kickoff(inputs=inputs)
            return {
                "caviar_recommendation": result.get("recommend_caviar", "No recommendation available"),
                "champagne_pairing": result.get("pair_champagne", "No pairing available"),
                "exclusive_content": result.get("curate_content", "No content available")
            }
        except Exception as e:
            logger.error(f"An error occurred in get_caviar_experience: {str(e)}", exc_info=True)
            return {
                "caviar_recommendation": "Error occurred",
                "champagne_pairing": "Error occurred",
                "exclusive_content": "Error occurred"
            }
