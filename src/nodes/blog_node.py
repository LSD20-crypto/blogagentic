from src.states.blogstate import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.states.blogstate import Blog
from langgraph.graph import END   

class BlogNode:
    """
    A class to represent he blog node
    """

    def __init__(self,llm):
        self.llm=llm

    
    def title_creation(self,state:BlogState):
        """
        create the precise title for the blog
        """

        if "topic" in state and state["topic"]:
            system_prompt="""You are an expert blog content writer. Use Markdown formatting. Generate
a blog title for the topic. This title should be precise, creative and SEO friendly"""
            
            messages = [
                SystemMessage(system_prompt),
                HumanMessage(f"Topic: {state['topic']}")
            ]
            print(messages)
            response=self.llm.invoke(messages)
            print(response)
            return {"blog":{"title":response.content}}
        
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use Markdown formatting.
Generate a detailed blog content with detailed breakdown for the topic"""
            
            messages = [
                SystemMessage(system_prompt),
                HumanMessage(f"Topic: {state['topic']}")
            ]
            response = self.llm.invoke(messages)
            return {"blog": {"title": state['blog']['title'], "content": response.content}}

    def translation(self,state:BlogState):
        """
        Translate the blog content to the specified language
        """
        system_prompt = """You are an expert translator. Maintain the original tone, style and formatting of the blog.
Adapt cultural references and idiomatic expressions to resonate with the target language speaking audience."""
        
        translation_request = f"""translate the following blog content into {state["current_language"]}:

ORIGINAL CONTENT:
{state['blog']['content']}"""

        messages =[
            SystemMessage(system_prompt),
            HumanMessage(translation_request)
        ]
        response = self.llm.with_structured_output(Blog).invoke(messages)
        return {"blog": {"title": state['blog']['title'], "content": response.content, "language": state["current_language"]}}

    def route(self,state:BlogState):
        return {"current_language":state["current_language"]}
    
    def route_decision(self,state:BlogState):
        """
        Route the content based on the language specified in the state
        """
        if state["current_language"]=="hindi":
            return "hindi_translation"
        elif state["current_language"]=="bengali":
            return "bengali_translation"
        else:
            return END
