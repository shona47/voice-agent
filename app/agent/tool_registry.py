from app.tools.email import send_email
from app.tools.search import web_search
from app.tools.history import show_history
from app.tools.reminder import set_reminder
from app.tools.memory_rag import memory_tool
from app.tools.chat import chat_tool

TOOLS = {

    "email": send_email,

    "search": web_search,

    "history": show_history,

    "reminder": set_reminder,

    "memory": memory_tool,

    "chat": chat_tool

}