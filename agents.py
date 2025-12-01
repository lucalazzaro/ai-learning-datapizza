# agents.py
from datapizza.agents import Agent
from config import get_client
from tools import web_search

client = get_client()

profile_agent = Agent(
    name="ProfileRoadmapArchitect",
    client=client,
)

resources_agent = Agent(
    name="ResourceCurator",
    client=client,
    tools=[web_search],
)

planner_agent = Agent(
    name="StudyPlanDesigner",
    client=client,
)
