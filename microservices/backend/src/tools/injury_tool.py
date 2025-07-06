import src.config as config
from src.utils.datastore_helper import vertex_search_app


def get_injury_advice_tool(user_query: str):
    """
    Queries a sports injury datastore to provide evidence-based advice.

    It takes a user's question about sports injury and finds relevant
    information from a specialized datastore. It constructs a search request
    and retrieves results, which can include summaries and source citations.

    Args:
        user_query (str): The user's question or topic related to sports injury.

    Returns:
        A `discoveryengine.services.search_service.pagers.SearchPager` object
        containing the search results on success.
        A dictionary with 'status' and 'error_message' keys on failure.
    """
    print(
        # Log tool execution
        f"--- Tool: get_injury_advice_tool called for query: {user_query} ---"
    )
    try:
        tool_result = vertex_search_app(
            engine_id=config.INJURY_ENGINE_ID, search_query=user_query,
        )
        return tool_result
    except Exception as e:
        print(f"Error in get_injury_advice_tool. Details: {e}")
        return {
            "status": "error",
            "error_message": f"Sorry, I am unable to access my datasource to fetch injury advice.",
        }
