from google.adk.agents import LlmAgent
from src.helper_agents.injury_agent import injury_agent
from src.helper_agents.nutrition_agent import nutrition_agent
from src.prompts.big_doc import big_doc_desc, big_doc_inst
import src.config as config

# Create a parent agent and assign children via sub_agents
root_agent = LlmAgent(
    name="big_doc",
    model=config.LLM_MODEL,
    description=big_doc_desc,
    instruction=big_doc_inst,
    sub_agents=[
        nutrition_agent,
        injury_agent
    ]
)
