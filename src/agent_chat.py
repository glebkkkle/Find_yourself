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
            temperature=0.1,
            # other params...
        )
        self.store={}

        self.agent=create_react_agent(model=self.llm, tools=[])
        
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

    # @tool
    # def search_engine(query:str) ->str:
    #     """Search engine for searching important information in world wide web. Use only when necessary
    #     """

    #     s = GoogleSearchAPIWrapper()
    #     res=s.run(query)
    #     return f'results from Google Search:{res}' 
    
    @tool
    def _find_similar():
        'does nothing for now'
        return 
    
    def __call__(self, session_id, query,):
        if session_id not in self.store:
            self.store={session_id:{'human_msgs':[], 'ai_msgs':[]}}
    
        self.store[session_id]['human_msgs'].append(query)

        ai_reply=self._ivoke_bot(query)

        self.store[session_id]['ai_msgs'].append(ai_reply)

        rep={'ai_msg':ai_reply, 'human_msg':query, 'session_id':session_id}

        return rep
    def _ivoke_bot(self, query):
        res=self.agent.invoke({'messages':[{'role':'user', 'content':f'{query}'}]})
        
        ai_msgs=[]
        for msg in res['messages']:
            if isinstance(msg, AIMessage):
                ai_msgs.append(msg.content)
        
        return ai_msgs[-1]  
instance=ChatModel()


