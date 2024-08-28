from openapi_key import api_key
import os
os.environ['OPENAI_API_KEY'] = api_key
from langchain.chains import SequentialChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI  # Note the capitalization of "OpenAI"
import os

# Set your OpenAI API key
from openapi_key import api_key
os.environ['OPENAI_API_KEY'] = api_key

# Initialize the LLM with desired settings
llm = OpenAI(temperature=0.6)

def generate_restaurant_name_and_items(cuisine):
    # Define the prompt for generating the restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Define the prompt for generating the menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma-separated list."
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Combine the chains in sequence
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    # Run the chain and return the response
    response = chain({'cuisine': cuisine})
    return response

