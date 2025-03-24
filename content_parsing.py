from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# call the LLM 

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="granite3.2:2b")

# parse our code to the LLM
def parse_with_Ollama(dom_chunks, parse_description):
    """_summary_
    This function passes our scraped content and parse description to the Ollama model. 

    Args:
        dom_chunks: chunk of text content from our scraping process. 
        parse_description: description of what we want to extract from the text. 

    Returns:
        str: The extracted information from the text content. 
    """
    prompt = ChatPromptTemplate.from_template(template) # create a prompt template from the given template
    chain = prompt | model # create a chain that takes the prompt and passes it to the model

    parsed_result = []
    for i, chunk in enumerate(dom_chunks, start=1): 
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description}) # pass the cleaned content and user prompt to the Ollama model
        print(f"Parsed {i} of {len(dom_chunks)}") # know the amount of chunks parsed
        parsed_result.append(response) # append the parsed result to the LLM

    return '\n'.join(parsed_result) # join all the parsed results into a single string and return it

    




    


