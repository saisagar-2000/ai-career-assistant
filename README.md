

# AI Career Assistant Backend

This is a Django REST Framework based backend application that integrates AI capabilities for resume analysis and career guidance.

The system provides secure authentication, resume upload and processing, AI-powered resume feedback, and an AI career chatbot. It demonstrates modern backend architecture with external AI integration.



## Project Overview

This project includes:

* JWT-based authentication
* Resume upload (PDF)
* Resume text extraction using pdfplumber
* AI-based resume analysis using Groq (Llama 3.1)
* AI career chatbot
* Chat history persistence
* Modular Django architecture with service layer separation


## Architecture

The application follows a layered backend architecture:

Request → API View → Service Layer → AI Engine → External AI Model → Response

Project structure:

ai_career_assistant/

* config/ – Django settings and main URLs
* users/ – Authentication and user management
* resumes/ – Resume upload and processing
* chat/ – Chatbot APIs and chat storage
* ai_engine/ – AI integration logic (Groq client and prompt handling)
* core/ – Shared utilities
* manage.py

The AI logic is separated into a dedicated module (`ai_engine`) to maintain clean separation of concerns.



## Features

### 1. User Authentication

* Register new users
* Login using JWT
* Protected APIs using Bearer token authentication

### 2. Resume Analyzer

* Upload resume in PDF format
* Extract text from PDF
* Send extracted text to Groq Llama model
* Return structured feedback including strengths, weaknesses, and suggestions

### 3. AI Career Chatbot

* Accept career-related questions
* Generate AI-powered responses
* Store chat history in database



## Technology Stack

* Python
* Django
* Django REST Framework
* SimpleJWT (JWT Authentication)
* Groq API (Llama 3.1 model)
* pdfplumber
* SQLite (development database)



## Setup Instructions

### 1. Clone the repository

git clone [https://github.com/saisagar-2000/ai-career-assistant.git](https://github.com/saisagar-2000/ai-career-assistant.git)
cd ai-career-assistant



### 2. Create virtual environment

python -m venv venv
source venv/bin/activate



### 3. Install dependencies

pip install -r requirements.txt



### 4. Create environment file

Create a file named `.env` in the project root and add:

GROQ_API_KEY=your_api_key_here



### 5. Apply migrations

python manage.py migrate



### 6. Run the server

python manage.py runserver

The application will run at:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)



## API Endpoints

### Authentication

POST /api/users/register/
POST /api/login/

### Resume

POST /api/resumes/upload/

Headers:
Authorization: Bearer ACCESS_TOKEN

Body:
form-data with key "file" (PDF file)



### Chat

POST /api/chat/

Headers:
Authorization: Bearer ACCESS_TOKEN

Body (JSON):
{
"message": "How can I become a backend developer?"
}



## Key Design Decisions

* Business logic is separated into a service layer.
* AI integration is isolated in a dedicated module.
* Sensitive keys are stored in environment variables.
* JWT authentication is used for stateless API security.
* External AI model is abstracted behind a reusable function.



## Author

Sagar
Backend Developer focused on Python, Django, and AI integration.




