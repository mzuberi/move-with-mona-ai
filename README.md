# Move With Mona AI ✧

A gentle, empowering AI assistant built by Mona SK — combining mindful movement, self-awareness, and modern technology.

This chatbot speaks in Mona’s nurturing, real voice. It meets you exactly where you are and offers:
- ✨ Personalized movement guidance
- ✨ Encouraging words + mindset resets
- ✨ Direct access to Mona’s own blog posts
- ✨ A tone that’s soft, grounded, and lovingly honest

---

## 💡 Why I Built This

I wanted to create an experience that blends everything I am:  
☁️ Cloud tech,  
🌿 Wellness,  
🤍 Healing,  
🧘‍♀️ Movement,  
🗝 And purpose.

**Move With Mona AI** is here to be a calm, strong companion —  
like your best friend, Pilates guide, and inner coach in one.

---

## 🛠 Built With
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-4](https://openai.com/)
- [ChromaDB](https://www.trychroma.com/)
- [Markdown Blog Embedding](https://monaskhana.com/)

---

## 🧠 What It Does
1. Loads Mona’s actual blog content
2. Embeds it into a vector memory
3. Responds to your mood or question with calm, confident advice
4. Pulls real insights from blog posts using RAG (Retrieval-Augmented Generation)

---

## 🚀 To Run Locally

```bash
git clone https://github.com/mzuberi/move-with-mona-ai.git
cd move-with-mona-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app/main.py
