from google.adk.agents import LlmAgent
from src.prompts.nutrition_agent import nutrition_agent_desc, nutrition_agent_inst
from src.tools.nutrition_tool import get_nutrition_advice_tool
import src.config as config

# Define individual agents
nutrition_agent = LlmAgent(
    name="nutrition_agent",
    model=config.LLM_MODEL,  # Can be a string for Gemini or a LiteLlm object
    description=nutrition_agent_desc,
    tools=[get_nutrition_advice_tool],  # Pass the function directly
)

print(
    f"Agent '{nutrition_agent.name}' created using model '{config.LLM_MODEL}'.")
