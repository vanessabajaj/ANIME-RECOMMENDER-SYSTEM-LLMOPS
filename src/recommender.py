from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.retriever = retriever
        self.api_key = api_key
        self.model_name = model_name
        self.prompt = get_anime_prompt()
        self.model = ChatGroq(model=self.model_name, temperature=0, api_key=self.api_key)

    def get_recommendations(self, query: str):
        # retrieve relevant documents
        docs = self.retriever.invoke(query)
        context = "\n\n".join(doc.page_content for doc in docs)
        # self.prompt is a plain string template
        prompt_text = self.prompt.format(context=context, question=query)
        message = HumanMessage(content=prompt_text)
        response = self.model.invoke([message])
        return response.content
    