import os
from dotenv import load_dotenv
from langchain_community.llms import GooglePalm  # Updated import
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from typing import Dict, Any

@CrewBase
class CaviarCrew():
    """Caviar crew for luxury dining experiences"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        load_dotenv()
        self.llm = GooglePalm(google_api_key=os.getenv("gemini_api_key"))

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
        result = self.crew().kickoff(inputs=inputs)
        return {
            "caviar_recommendation": result.get("recommend_caviar", "No recommendation available"),
            "champagne_pairing": result.get("pair_champagne", "No pairing available"),
            "exclusive_content": result.get("curate_content", "No content available")
        }