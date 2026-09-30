def parse_output(response):
    """
    Convert LangChain response to plain text.
    """

    if hasattr(response, "content"):
        return response.content

    return str(response)