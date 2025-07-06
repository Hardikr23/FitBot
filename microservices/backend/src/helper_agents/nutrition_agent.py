import src.config as config
from google.adk.agents import LlmAgent
from src.prompts.nutrition_agent import nutrition_agent_desc
from src.tools.nutrition_tool import get_nutrition_advice_tool

# Define individual agents
nutrition_doc = LlmAgent(
    name="nutrition_agent",
    model=config.LLM_MODEL,  # Can be a string for Gemini or a LiteLlm object
    description=nutrition_agent_desc,
    tools=[get_nutrition_advice_tool],  # Pass the function directly
)

print(f"Agent '{nutrition_doc.name}' created using model '{config.LLM_MODEL}'.")
