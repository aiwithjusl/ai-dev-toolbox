# 🧰 AI DevToolBox

**Modular Python toolkit for AI development, debugging, data cleaning, and vector search.**  
Designed to accelerate ML workflows and showcase production-ready engineering.

---

## 🚀 Features

| Module | Purpose |
|--------|---------|
| **AITextToolkit** | NLP processing: tokenization, lemmatization, language detection |
| **AIDebugger** | Smart debugging with trace metadata and exception logging |
| **DatasetCleaner** | Clean missing values, fix columns, remove duplicates |
| **VectorDBConnector** | Add/search vectors using FAISS + metadata |
| **TaskRunner** | Register and trigger custom functions dynamically |

---

## 📦 Installation

```bash
git clone https://github.com/aiwithjusl/ai-dev-toolbox.git
cd ai-dev-toolbox
pip install -r requirements.txt

🧪 Run Tests

python3 -m unittest discover -s tests

🧠 Notebook Demos

Run the full interactive walkthrough here:
📓 notebooks/AI_DevToolBox_Demo.ipynb

💡 Example Use Case: AI Prototyping

- Clean incoming datasets
- Debug pipeline issues on the fly
- Test search accuracy with custom vector embeddings
- Run NLP pipelines from a single interface
- Register + trigger workflow functions

🧑‍💻 Built With

- Python 3.10
- NLTK, TextBlob, langdetect
- Pandas, NumPy
- FAISS (vector search)

📁 Project Structure

ai-dev-toolbox/
├── devtoolbox/
│   ├── ai/
│   ├── core/
│   ├── data/
│   ├── tasking/
│   ├── utils/
│   └── vector_db_connector.py
├── notebooks/
├── tests/
├── LICENSE
├── README.md
└── requirements.txt

👤 Author  
Justin Lane  
→ GitHub: [aiwithjusl](https://github.com/aiwithjusl)  
→ LinkedIn: [Justin Lane](https://www.linkedin.com/in/justin-lane-69b960219)

🪄 License

MIT License – free for personal + commercial use
