import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot conversation pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am an AI Chatbot created using Python."]
    ],
    [
        r"how are you?",
        ["I am doing well. Thank you!"]
    ],
    [
        r"what can you do?",
        ["I can chat with you and answer simple questions."]
    ],
    [
        r"bye",
        ["Goodbye!", "See you later!"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

print("AI Chatbot Started! Type 'bye' to exit.")

# Start conversation
chatbot.converse()
