# Talk2DB

Enterprises struggle with complex, location bound database access and multilingual barriers. So an automated AI-driven platform is required for real-time, natural language interaction with databases accessible anytime, anywhere, by anyone. In database management, beginners and nontechnical users, often struggle with writing SQL queries. This challenge motivated me create Talk2DB to ease writing queries. **Talk2DB** is an AI-powered Database handling platform that allows users to interact with real-time databases using NLP through text and voice input, from any location on the globe with multilingual support.

<img width="571" height="548" alt="logo" src="https://github.com/user-attachments/assets/6a734545-3621-460b-b717-70dd0f7fc035" />

---

## 🚀 Features

- **Natural Language to SQL**: Convert plain English (or other supported languages) into accurate SQL queries using AI.
- **Voice Input Support**: Speak your queries—ideal for accessibility and hands-free environments.
- **Live SQL Execution**: Run generated queries directly on your **MySQL** database and view results instantly.
- **Schema Preview**: Visualize database tables and column structures for better context.
- **User Authentication**: Secure login system to manage user access.
- **Multi-Language Support**: Interact in various languages, breaking down language barriers in data querying.
- **Explanation Box**: View simplified explanations of the generated SQL queries to understand their function.
- **History Audits**: Track and view past queries, responses, and user activity for transparency and learning.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) – Interactive UI for seamless user experience.
- **Backend**:
  - **AI Model**: Google Gemini AI for natural language processing.
  - **Database**: **MySQL** for managing and executing SQL queries.
  - **Voice Recognition**: [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library for converting speech to text.
  - **Language Translation**: [Deep Translator](https://pypi.org/project/deep-translator/) for multi-language support.

---

## 📂 Project Structure

```
Talk2DB/
├── __pycache__/              # Compiled bytecode files
├── ai_generator.py           # Handles AI-based SQL generation
├── auth_utils.py             # Contains authentication helper functions
├── db_config.py              # Database configuration settings
├── db_handler.py             # Functions for database connections and query execution
├── logo.png                  # Application logo
├── main.py                   # Main application script
├── mysql_schema.json         # Sample MySQL schema for reference
├── prompt.py                 # Prompt templates for AI model
├── query_parser.py           # Parses and validates generated SQL queries
├── requirements.txt          # Python dependencies
├── schema_handler.py         # Manages database schema retrieval and display
└── README.md                 # Project documentation
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/khushi-0-1/Talk2DB.git
   cd Talk2DB
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   venv\Scripts\activate   #On MAC : source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   streamlit run main.py
   ```

---

## 🔐 Configuration

- **Database Settings**: Update `db_config.py` with your MySQL credentials and connection details.
- **AI Model API Key**: Ensure you have access to the Google Gemini AI API and set the necessary keys in `ai_generator.py`.
- **Language Support**: Modify `deep_translator` settings in `main.py` to add or change supported languages.

---

## 🧪 Usage

1. **Login**: Start the application and log in with your credentials.
2. **Select Database**: Choose the MySQL database you want to interact with.
3. **Input Query**:
   - **Text**: Type your query in natural language.
   - **Voice**: Click on the microphone icon and speak your query.
4. **Generate SQL**: The AI model will convert your input into an SQL query.
5. **Explanation Box**: Review the simplified explanation of what your SQL query does.
6. **Execute Query**: Run the generated SQL and view the results directly in the app.
7. **History Audits**: Navigate the history section to revisit previous queries and executions.

---

## 🛠️ Future Enhancements

- Support for cloud databases (e.g., PostgreSQL, MongoDB, AWS RDS)
- OAuth 2.0 authentication for enterprise-level security
- Query version control and rollback
- Enhanced data visualization and BI dashboard integrations
- Exportable query logs for enterprise audit compliance

---

## 🚀 UI
<img width="1919" height="881" alt="Talk2DB UI" src="https://github.com/user-attachments/assets/280b0a3e-a58e-4c61-940d-c974e34cd2b8" />

