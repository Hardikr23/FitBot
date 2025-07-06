from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

import src.config as config
from src.prompts.injury_agent import injury_agent_template
from src.prompts.nutrition_agent import nutrition_agent_template


def vertex_search_app(
    engine_id: str,
    search_query: str,
) -> discoveryengine.services.search_service.pagers.SearchPager:
    client_options = (
        ClientOptions(
            api_endpoint=f"{config.LOCATION}-discoveryengine.googleapis.com")
        if config.LOCATION != "global"
        else None
    )

    # Create a client
    client = discoveryengine.SearchServiceClient(client_options=client_options)

    # The full resource name of the search app serving config
    serving_config = f"projects/{config.PROJECT_ID}/locations/{config.LOCATION}/collections/default_collection/engines/{engine_id}/servingConfigs/default_config"

    # defining the prompt
    prompt_template = injury_agent_template if "injury" in engine_id else nutrition_agent_template
    agent_prompt = prompt_template.render(search_query=search_query)

    content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
        snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
            return_snippet=True
        ),
        summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
            summary_result_count=5,
            include_citations=True,
            ignore_adversarial_query=True,
            ignore_non_summary_seeking_query=False,
            model_prompt_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec(
                preamble=agent_prompt
            ),
            model_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec(
                version="stable",
            ),
        ),
    )

    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=search_query,
        page_size=5,
        content_search_spec=content_search_spec,
        query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
            condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
        ),
        spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
            mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
        ),
    )

    page_result = client.search(request)

    # TODO: Need to add function to clean the response and return only relevant data

    return page_result
