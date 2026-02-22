# BlogAgentic

An intelligent AI-powered blog generation system built with **LangGraph** and **LLMs** to automatically create, generate, and translate blog content across multiple languages.

## 🌟 Features

- **Intelligent Blog Generation**: Automatically create SEO-friendly blog titles and detailed content
- **Multi-Language Support**: Translate generated blogs into Hindi and Bengali while maintaining tone and style
- **Agentic Workflow**: Uses LangGraph for intelligent routing and conditional execution
- **REST API**: FastAPI-based endpoint for easy integration
- **Structured Output**: Leverages LLM structured outputs for consistent blog data
- **Professional Content**: Uses expert prompts for blog writers and translators

## 📋 Project Structure

```
BlogAgentic/
├── src/
│   ├── graphs/
│   │   └── graph_builder.py        # LangGraph workflow builder
│   ├── llms/
│   │   └── groqllm.py              # Groq LLM integration
│   ├── nodes/
│   │   └── blog_node.py            # Blog generation nodes
│   └── states/
│       └── blogstate.py            # State definitions
├── app.py                          # FastAPI application
├── main.py                         # CLI entry point
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project configuration
└── README.md                       # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Groq API Key
- LangChain API Key (optional, for LangSmith)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/LSD20-crypto/blogagentic.git
cd BlogAgentic
```

2. **Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key  # Optional
```

## 📖 Usage

### API Endpoint

Start the FastAPI server:
```bash
python app.py
```

The server runs at `http://localhost:8000`

#### Generate Blog with Topic Only
```bash
POST /blogs
Content-Type: application/json

{
    "topic": "Agentic AI"
}
```

#### Generate and Translate Blog
```bash
POST /blogs
Content-Type: application/json

{
    "topic": "Agentic AI",
    "language": "hindi"
}
```

**Supported Languages:**
- `hindi` - Translate to Hindi
- `bengali` - Translate to Bengali

### Response Format
```json
{
    "data": {
        "topic": "Agentic AI",
        "blog": {
            "title": "Generated blog title...",
            "content": "Detailed blog content with markdown formatting...",
            "language": "hindi"
        },
        "current_language": "hindi"
    }
}
```

## 🏗️ Architecture

### LangGraph Workflow

The application uses two main workflows:

#### 1. Topic Graph
Generates blog content based on topic only:
```
START → title_creation → content_generation → END
```

#### 2. Language Graph
Generates blog and translates to specified language:
```
START → title_creation → content_generation → route → {hindi_translation, bengali_translation} → END
```

### Components

**BlogNode** - Handles all blog-related operations:
- `title_creation()` - Creates SEO-friendly titles
- `content_generation()` - Generates detailed blog content
- `translation()` - Translates content to target language
- `route()` - Routes based on language selection
- `route_decision()` - Conditional routing logic

**GraphBuilder** - Constructs LangGraph workflows with nodes and edges

**GroqLLM** - LLM integration for content generation

## 🔧 Configuration

### State Management
The application uses `BlogState` to manage workflow state:
```python
{
    "topic": str,              # Blog topic
    "blog": {
        "title": str,          # Generated title
        "content": str,        # Generated content
        "language": str        # Translation language
    },
    "current_language": str    # Target language
}
```

## 📝 Example Requests

### Using curl
```bash
# Topic only
curl -X POST http://localhost:8000/blogs \
  -H "Content-Type: application/json" \
  -d '{"topic": "Machine Learning"}'

# With translation
curl -X POST http://localhost:8000/blogs \
  -H "Content-Type: application/json" \
  -d '{"topic": "Agentic AI", "language": "hindi"}'
```

### Using Python
```python
import requests

url = "http://localhost:8000/blogs"
payload = {
    "topic": "Agentic AI",
    "language": "bengali"
}

response = requests.post(url, json=payload)
print(response.json())
```

## 🛠️ Development

### Project Dependencies
- `langchain-core` - LLM framework
- `langgraph` - Graph-based workflow orchestration
- `langchain-groq` - Groq LLM integration
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `python-dotenv` - Environment variable management

### Running Tests
```bash
pytest
```

## 🚦 Roadmap

- [ ] Add more language support (Spanish, French, German)
- [ ] Implement blog outline generation before content
- [ ] Add custom style/tone configurations
- [ ] Implement caching for repeated topics
- [ ] Add database persistence for generated blogs
- [ ] Create web UI dashboard
- [ ] Add image generation integration
- [ ] Implement blog SEO scoring

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For support, email [your-email] or open an issue on GitHub.

## 🙏 Acknowledgments

- Built with [LangChain](https://langchain.com/)
- Powered by [LangGraph](https://langchain-ai.github.io/langgraph/)
- LLM by [Groq](https://groq.com/)
- API framework [FastAPI](https://fastapi.tiangolo.com/)
