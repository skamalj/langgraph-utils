from langchain_core.tools import tool, StructuredTool

@tool
def multiply(a: int, b: int) -> int:
   """Multiply two numbers."""
   return a * b

tools = [multiply]
# create function to create josn for tools list for every attribute  
# @! example formt of tool -- name='multiply' description='Multiply two numbers.' args_schema=<class 'langchain_core.utils.pydantic.multiply'> func=<function multiply at 0x7f6853c4fd90>

def create_tools_json(tools):
    tools_json = []
    for tool in tools:
        tool_info = {
            'name': tool.name,
            'description': tool.description,
            'args_schema': tool.args_schema.model_json_schema()
        }
        tools_json.append(tool_info)
    return tools_json

# Example usage
json_tools = create_tools_json(tools)

# @! create function to convert json_output to structuredtool or list of structuredtool basis input type provider=anthropic

def json_to_structured_tools(json_tools):
    if not isinstance(json_tools, list):
        json_tools = [json_tools]
    
    structured_tools = []
    for tool_json in json_tools:
            
        structured_tool = StructuredTool(
            name=tool_json['name'],
            description=tool_json['description'],
            func=None,
            args_schema=tool_json['args_schema']
        )
        structured_tools.append(structured_tool)
    
    return structured_tools if len(structured_tools) > 1 else structured_tools[0]

tools_from_json = json_to_structured_tools(json_tools)
print(json_tools)
print(tools_from_json)