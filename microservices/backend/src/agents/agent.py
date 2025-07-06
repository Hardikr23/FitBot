from google.adk.agents import LlmAgent
# from microservices.backend.src.agents.injury_agent import injury_agent
# from microservices.backend.src.agents.nutrition_agent import nutrition_agent
from prompts.big_doc import big_doc_desc, big_doc_inst

# Create a parent agent and assign children via sub_agents
root_agent = LlmAgent(
    name="big_doc",
    model="gemini-2.0-flash",
    description=big_doc_desc,
    instruction=big_doc_inst,
    # sub_agents=[
    #     nutrition_agent,
    #     injury_agent
    # ]
)
