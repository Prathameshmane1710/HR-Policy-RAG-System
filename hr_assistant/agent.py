from langchain.agents import create_agent
from hr_assistant import config

def create_hr_agent(llm, tools):
    """Create an HR agent with the given LLM and tools"""
    return create_agent(
        model=llm,
        tools=tools,
        system_prompt=config.SYSTEM_PROMPT,
    )