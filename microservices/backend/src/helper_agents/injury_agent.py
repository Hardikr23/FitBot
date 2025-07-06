from google.adk.agents import LlmAgent
from src.prompts.injury_agent import injury_agent_desc
from src.tools.injury_tool import get_injury_advice_tool
import src.config as config


# Define individual agent
injury_doc = LlmAgent(
    name="injury_agent",
    model=config.LLM_MODEL,  # Can be a string for Gemini or a LiteLlm object
    description=injury_agent_desc,
    tools=[get_injury_advice_tool],  # Pass the function directly
)

print(f"Agent '{injury_doc.name}' created using model '{config.LLM_MODEL}'.")
