# 🧠 Sentiment Analysis of Amazon Product Reviews with Emoji Effects

This web app analyzes product reviews and predicts whether the sentiment is **positive**, **neutral**, or **negative**. Based on the prediction, it triggers a dynamic emoji animation to visually reflect the mood of the review.

---

## 🔗 Live App  
🎯 Try it out here: [Sentiment Analysis Web App](https://huggingface.co/spaces/HarshitaSuri/SentimentAnalysis)

## 🧪 Training Notebook  
📓 See the model training process on Colab: [Google Colab Link](https://colab.research.google.com/drive/1HmNJ3EeoVdi8Ax0-EGD3sxFeOV4t76F5?usp=sharing)

---

## 📌 Features
- ✅ Built using a **Naive Bayes classifier**
- ✅ Trained on the [Amazon Product Reviews dataset](https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews)
- ✅ NLP preprocessing: tokenization, stopword removal, stemming, TF-IDF
- ✅ Balanced dataset with equal samples of positive, neutral, and negative reviews
- ✅ Animated emoji bursts that match the sentiment
- ✅ Clean, interactive interface powered by **Gradio**

---

## 📊 Example Review Inputs

| Review | Prediction | Emoji Animation |
|--------|------------|-----------------|
| `"Absolutely loved it!"` | Positive | 🎉✨😍 |
| `"It's okay, nothing special."` | Neutral | 😐🤔🫤 |
| `"Worst purchase ever!"` | Negative | 😡💩😭 |

---

## 🛠 Tech Stack
- Python
- Scikit-learn (Naive Bayes)
- NLTK (text preprocessing)
- Gradio (web UI)
- HTML & CSS (emoji animation)

---

## 📁 Dataset Used
- **Name**: Amazon Product Reviews  
- **Source**: [Kaggle - arhamrumi/amazon-product-reviews](https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews)  
- **Size**: ~275,000 reviews  
- **Preprocessing**: Cleaned, balanced, and labeled reviews as `positive`, `neutral`, or `negative`.

---

## 🚀 How to Use
Enter any product review in the textbox, and get an instant sentiment prediction along with animated emojis reflecting the mood.

---

