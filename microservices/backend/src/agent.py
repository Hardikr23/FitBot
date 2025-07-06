import src.config as config
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from src.helper_agents.injury_agent import injury_doc
from src.helper_agents.nutrition_agent import nutrition_doc
from src.prompts.big_doc import big_doc_desc, big_doc_inst

# List of sub-agents to be used as tools
sub_agents = [nutrition_doc, injury_doc]

# Create a parent agent and assign children via sub_agents
root_agent = LlmAgent(
    name="big_doc",
    model=config.LLM_MODEL,
    description=big_doc_desc,
    instruction=big_doc_inst,
    tools=[AgentTool(agent=sub_agent) for sub_agent in sub_agents],
    sub_agents=[nutrition_doc, injury_doc],
)
