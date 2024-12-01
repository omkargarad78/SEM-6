import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"Hi|Hello|Hey there|Hola",
        ["Hello, I'm your real estate assistant.\n"]
    ],
    [
        r"What's your expertise in real estate?",
        ["I specialize in real estate assistance worldwide. Where are you currently located or interested in exploring real estate?\n",]
    ],
    [
        r"What specific services do you offer in real estate?",
        [" I specialize in a range of real estate services, including property search, market analysis, and advice on buying, selling, or renting. Where are you currently located or interested in exploring real estate?\n",]
    ],
    [
        r"How is the real estate market",
        ['The real estate market in is dynamic. Are you looking to buy, sell, or rent a property in this area?\n',]
    ],
    [
        r"Any real estate suggestions around my workplace?",
        ["Property areas can vary. Are you looking for a specific size or type of property that suits your preferences?\n",]
    ],
    [
        r"What's the typical property area around here?",
        ["Great! In which area would you like to explore real estate options? I can help you find properties near your workplace.\n",]
    ],
    [
        r"I'm looking for properties in my area.",
        ["The property area can vary. Are you looking for a specific size or type of property? Let me know your preferences.\n",]
    ],
    [
        r"Can you recommend a real estate expert in my location?",
        ["While I'm here to assist, consulting a local real estate expert for specific advice is recommended. I can provide general information and insights.\n",]
    ],
    [
        r"Thank you for your help.",
        ["You're welcome! If you have more questions or need further assistance with real estate, feel free to ask.\n",]
    ],
    [
        r"quit|bye",
        ["Thank you for considering me as your real estate assistant. If you have more questions, feel free to ask!\n"]
    ],
]


print("---------------------------------------------")
print("Hello! I am RealtyBot, your real estate assistant at your service.\n")
print("You can start by saying 'hi' or 'hello'.")
print("To exit, simply say 'bye' or 'quit'.\n")
chat = Chat(pairs)
chat.converse()

