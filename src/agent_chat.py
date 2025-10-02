from langchain_ollama import ChatOllama
from langchain_core.tools import tool

from typing import List, Union, Literal
from langchain_core.messages import AIMessage,  ToolMessage

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.messages import AIMessage
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.memory import ConversationBufferWindowMemory

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from langgraph.prebuilt import create_react_agent

class ChatModel:
    def __init__(self,model='mistral', temperature=0.9):
        self.llm = ChatOllama(
            model="mistral",
            temperature=0,
            # other params...
        ).bind_tools([self.search_engine])
        self.messages={}

        # self.agent=create_react_agent(model=self.llm, tools=[self.search_engine])
        
        # res=self.agent.invoke({'messages':[{'role':'user', 'content':'who can I work as with computer science major?'}]})

        # print(res)

    def get_session_history(self, session_id: str) -> InMemoryChatMessageHistory:
        if session_id not in self.messages:
            self.messages[session_id] = InMemoryChatMessageHistory()
            return self.messages[session_id]

        memory = ConversationBufferWindowMemory(
            chat_memory=self.messages[session_id],
            k=3,
            return_messages=True,
        )
        assert len(memory.memory_variables) == 1
        key = memory.memory_variables[0]
        messages = memory.load_memory_variables({})[key]
        self.messages[session_id] = InMemoryChatMessageHistory(messages=messages)
        return self.messages[session_id]



    @tool
    def search_engine(query:str) ->str:
        """Search engine for searching information about specific major in World Wide Web
        Can be used to find relevant information about a specific Major, or Documents or other questions that go beyond model's internal knowledge
        """

        s = GoogleSearchAPIWrapper()
        res=s.run(query)
        return f'results from Google Search:{res}' 
    

    def __call__(self, session_id, query,):
        self.chain=RunnableWithMessageHistory(self.llm, self.get_session_history)



        _=self.chain.invoke(query, config={'configurable':{'session_id':session_id}})
        
        print(_)


        curr_chat_history=self.messages[session_id].messages 
        human_msgs=[msg.content for msg in curr_chat_history if isinstance(msg, HumanMessage)] 
        ai_msgs=[m.content for m in curr_chat_history if isinstance(m, AIMessage)]
        
        return human_msgs[-1], ai_msgs[-1]
    
    def _ivoke_bot(self, query, session_id):
        llm_output=self.chain.invoke(input=query, config={'configurable': {'session':session_id}})
        
        return llm_output 
instance=ChatModel()

instance('1', 'who can i work as with cs major')