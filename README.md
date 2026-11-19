# 🎥 AI Video Assistant

An AI-powered Video Assistant that transforms YouTube videos and local audio/video files into meaningful insights. It automatically generates transcripts, summaries, key decisions, action items, and open questions — with an interactive **RAG-based chatbot** that lets you ask questions about video content.

Built using **Python, Whisper, LangChain, Mistral AI, and ChromaDB**.

---

## 🖥️ Application Preview


### 1. Home Page

<img width="1917" height="1020" alt="Screenshot 2026-11-19 231128" src="https://github.com/user-attachments/assets/2a966c88-5973-4ada-8c15-c528ebc35f66" />


### 2. Terminal and UI design

<img width="1917" height="1020" alt="Screenshot 2026-11-19 230853" src="https://github.com/user-attachments/assets/9b2c496c-29b9-4639-a766-3b8c14c3b627" />


### 3. Meeting Insights

<img width="1915" height="1020" alt="Screenshot 2026-11-19 231025" src="https://github.com/user-attachments/assets/57f6b354-19f3-4f77-9b31-7243c561261c" />


### 4. AI Chat Assistant

<img width="1912" height="1020" alt="Screenshot 2026-11-19 231044" src="https://github.com/user-attachments/assets/eb2c8897-4243-4294-a44d-ec909595ffd0" />


---

## ✨ Features

- **YouTube Video Processing:** Extract audio directly from YouTube URLs.
- **Local File Support:** Process locally stored audio and video files.
- **Automatic Transcription:** Convert speech into text using OpenAI Whisper.
- **AI-Generated Titles:** Generate meaningful titles from video content.
- **Smart Summarization:** Create concise summaries of long transcripts.
- **Action Item Extraction:** Identify tasks, owners, and deadlines.
- **Key Decision Detection:** Extract important decisions from conversations.
- **Open Question Identification:** Find unresolved topics and follow-up questions.
- **RAG-Based Chatbot:** Ask questions about the processed video and receive context-aware answers.
- **Vector Search:** Store and retrieve transcript chunks using ChromaDB.
- **Interactive UI:** Simple and user-friendly Streamlit interface.

---

## 🏗️ Project Architecture

```text
              YouTube URL / Local File
                        |
                        ▼
                Audio Processing
                 (yt-dlp / FFmpeg)
                        |
                        ▼
                  Audio Chunking
                        |
                        ▼
                Whisper Transcription
                        |
                        ▼
                  Text Transcript
                        |
             ┌──────────┼──────────┐
             ▼          ▼          ▼
          Title &    Summary    Insight
          Generation             Extraction
             |          |          |
             └──────────┼──────────┘
                        |
                        ▼
                 Text Embeddings
                 (HuggingFace)
                        |
                        ▼
                   ChromaDB
                 Vector Database
                        |
                        ▼
                 RAG Retrieval
                        |
                        ▼
                  Mistral AI
                        |
                        ▼
               Interactive AI Chat
```

---

## 🛠️ Tech Stack

| Technology     | Purpose                            |
| -------------- | ---------------------------------- |
| Python         | Core programming language          |
| Streamlit      | Web application interface          |
| OpenAI Whisper | Speech-to-text transcription       |
| yt-dlp         | YouTube audio extraction           |
| FFmpeg         | Audio/video processing             |
| Pydub          | Audio conversion and chunking      |
| LangChain      | LLM orchestration and RAG pipeline |
| Mistral AI     | Summarization, analysis, and chat  |
| HuggingFace    | Text embeddings                    |
| ChromaDB       | Vector database                    |
| Python-dotenv  | Environment variable management    |

---

## 📂 Project Structure

```text
AI-Video-Assistant/
│
├── app.py
│
├── core/
│   ├── audio_processor.py
│   ├── transcription.py
│   ├── summarizer.py
│   ├── extractor.py
│   ├── vector_store.py
│   └── rag_engine.py
│
├── downloads/
│
├── vector_db/
│
├── .streamlit/
│   └── secrets.toml
│
├── requirements.txt
├── .gitignore
└── README.md
```

*The structure above is a reference. Adjust filenames and folders to match your actual repository.*

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Video-Assistant.git
```

### 2. Navigate to the Project

```bash
cd AI-Video-Assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a `.streamlit/secrets.toml` file:

```toml
MISTRAL_API_KEY = "your_mistral_api_key"
```

Get your API key from the [Mistral AI Platform](https://console.mistral.ai/).

**Important:** Never upload your actual API key or `secrets.toml` file to GitHub.

### 6. Install FFmpeg

Install FFmpeg and make sure it is accessible through your system PATH.

---

## 🚀 Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

---

## 💬 How It Works

1. Enter a YouTube URL or upload a local audio/video file.
2. The application extracts and processes the audio.
3. Whisper converts the audio into a text transcript.
4. The LLM generates a title and summary.
5. The system extracts action items, key decisions, and open questions.
6. Transcript chunks are converted into embeddings and stored in ChromaDB.
7. The RAG pipeline retrieves relevant transcript chunks for user questions.
8. Mistral AI generates answers based on the retrieved context.

---

## 🔐 Environment Variables

| Variable          | Description                           |
| ----------------- | ------------------------------------- |
| `MISTRAL_API_KEY` | API key required to access Mistral AI |

For local development, you can also use a `.env` file if your application loads environment variables through `python-dotenv`.

---

## 🌐 Deployment

This project can be deployed using **Streamlit Community Cloud**.

1. Push your project to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository.
4. Select `app.py` as the main application file.
5. Add `MISTRAL_API_KEY` in the application's Secrets settings.
6. Deploy your application.

---

## 🔮 Future Improvements

- Support for multiple languages.
- Speaker identification and diarization.
- Export transcripts and summaries as PDF.
- Timestamp-based transcript navigation.
- Support for multiple video sessions and searchable history.
- More advanced semantic search and retrieval.
- Improved response handling and API usage optimization.

---

## 👨‍💻 Developer

**Swopnil Biswas**
Python Developer | AI/ML Engineer

- GitHub: [@swopnil676](https://github.com/swopnil676)
- LinkedIn: [Swopnil Biswas](https://www.linkedin.com/in/swopnilbiswas/)

---

## ⭐ Support

If you find this project useful, consider giving it a **star ⭐** on GitHub!

**Built with Python, AI, and a passion for building intelligent applications.**
