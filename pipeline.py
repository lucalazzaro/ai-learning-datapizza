# pipeline.py
from agents import profile_agent, resources_agent, planner_agent

def generate_roadmap(user_profile: str, target_role: str) -> str:
    prompt = f"""
You are an AI career mentor.

Task:
1. Analyze this user profile: {user_profile}
2. Role target: {target_role}
3. Produce a clear, numbered 4-6 phase roadmap to become an AI/ML Engineer.

Each phase must include:
- title
- goals
- key topics
- prerequisites
    """
    result = profile_agent.run(task_input=prompt)
    return result.text  # 👈 IMPORTANT


def gather_resources(roadmap: str) -> str:
    prompt = f"""
You are a Resource Curator.

Based on this roadmap:
{roadmap}

Provide 2-3 courses, 1-2 books/articles, 1-2 GitHub repos per phase.
Use the web search tool if needed to find updated resources.
    """
    result = resources_agent.run(task_input=prompt)
    return result.text  # 👈 IMPORTANT


def create_study_plan(roadmap: str, resources: str) -> str:
    prompt = f"""
You are a Study Plan Designer.

Build a weekly study plan based on:
Roadmap:
{roadmap}

Resources:
{resources}

Organize the plan into 4-week blocks.
Each block must include:
- focus
- weekly goals
- activities
- one mini-project
    """
    result = planner_agent.run(task_input=prompt)
    return result.text  # 👈 IMPORTANT


def run_pipeline(user_profile: str, target_role: str):
    roadmap = generate_roadmap(user_profile, target_role)
    resources = gather_resources(roadmap)
    plan = create_study_plan(roadmap, resources)

    return {
        "roadmap": roadmap,
        "resources": resources,
        "study_plan": plan,
    }


