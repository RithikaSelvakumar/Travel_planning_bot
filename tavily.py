# Import relevant functionality
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.llms import Ollama  # Importing Ollama
import os

os.environ["TAVILY_API_KEY"] = "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"
# Create memory and Ollama model
memory = MemorySaver()
model = Ollama(model="llama3.2")  # Specify the Ollama model

# Initialize Tavily search with max 2 results
search = TavilySearchResults(max_results=2)


# Function to interact dynamically with the agent
def dynamic_agent_interaction():
    while True:
        # Get dynamic input from the user
        user_input = input("Enter your question or type 'exit' to quit: ")

        # Exit the loop if the user wants to quit
        if user_input.lower() == 'exit':
            print("Exiting...")
            break

        # Generate a response using Ollama, passing the input as a list
        model_response = model.generate([user_input])  # user_input passed as a list
        print("Model Response:", model_response)

        # Perform a search using Tavily search tool
        search_response = search.run(user_input)
        print("Search Results:", search_response)

        print("----")


# Start dynamic interaction with the agent
dynamic_agent_interaction()