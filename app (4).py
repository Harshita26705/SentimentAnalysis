import gradio as gr
import random
import re
import pickle

# 🔁 Load saved model components
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("stopwords.pkl", "rb") as f:
    stop_words = pickle.load(f)

with open("stemmer.pkl", "rb") as f:
    stemmer = pickle.load(f)

# ✂️ Text Preprocessing
def preprocess(text):
    text = re.sub(r'[^a-zA-Z ]', '', text)
    words = text.lower().split()
    words = [stemmer.stem(w) for w in words if w not in stop_words]
    return " ".join(words)

# 🎈 Emoji Animation HTML Generator
def generate_emoji_explosion(emojis):
    html = "<style>"
    html += """
    @keyframes fly {
        0% { transform: translateY(0) scale(1); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(-120vh) scale(1.5); opacity: 0; }
    }
    .emoji-burst {
        position: fixed;
        font-size: 2.5rem;
        animation: fly 4s ease-out forwards;
        z-index: 9999;
        pointer-events: none;
    }
    """
    html += "</style>"

    for _ in range(75):
        emoji = random.choice(emojis)
        left = random.randint(0, 100)
        bottom = random.randint(0, 20)
        delay = round(random.uniform(0, 3), 2)
        html += f"<span class='emoji-burst' style='left:{left}%; bottom:{bottom}%; animation-delay:{delay}s'>{emoji}</span>\n"

    return html

# 🔍 Prediction + Emoji Burst
def predict_sentiment_burst(review_text):
    clean = preprocess(review_text)
    vec = vectorizer.transform([clean])
    pred = model.predict(vec)[0]

    emoji_dict = {
        "positive": ['🎉', '✨', '😍', '💖', '🥳', '💕', '😘', '❤️', '😎'],
        "neutral":  ['😐', '🤔', '🫤', '😊', '🤓', '👍'],
        "negative": ['💩', '😡', '💔', '🤮', '😭', '😒', '🤦‍♀️', '🤡', '💢', '😤']
    }

    flying_emojis = generate_emoji_explosion(emoji_dict.get(pred, ['❓']))
    return flying_emojis + f"<h2 style='text-align:center;'>Sentiment: {pred}</h2>"

# 🌐 Gradio Interface
iface = gr.Interface(
    fn=predict_sentiment_burst,
    inputs=gr.Textbox(lines=3, placeholder="Type your product review here..."),
    outputs=gr.HTML(),
    title="🧠 Product Review Sentiment Analysis",
    description="Enter a product review to see its predicted sentiment and matching emoji animation!"
)

iface.launch()
