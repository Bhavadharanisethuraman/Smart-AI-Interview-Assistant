# Smart AI Interview Assitant

An advanced AI-powered platform designed to simulate realistic job interviews, analyze candidate resumes, generate tailored questions, and provide insightful feedback to help candidates excel.

---

## 🔗 Detailed Documentation

For a complete overview of the project design, implementation details, and features,  
please check the [Full Project Documentation](./Smart AI interview Assistant.pdf).

___

## ✨ Key Features

- **Smart Resume Parsing**  
  Upload your PDF resume and instantly extract key skills, experiences, and highlights.

- **Tailored Interview Questions**  
  AI crafts personalized questions based on your resume details and target job description.

- **Seamless Voice Interaction**  
  Answer questions naturally via voice; responses are transcribed and evaluated in real-time.

- **Interactive Chat Interface**  
  Clean, conversational UI displaying AI questions and your answers for easy tracking.

- **Comprehensive Scoring & Feedback**  
  Receive detailed evaluations for each answer, including scores and improvement tips.

- **Complete Interview Summary**  
  Review a full transcript of the interview along with an overall performance score.

---

## 🚀 How It Works

1. **Get Started**  
   Upload your resume and paste the job description. Optionally set max questions and select AI voice.

2. **Begin Interview**  
   The AI interviewer welcomes you and asks the first question using text-to-speech.

3. **Respond via Voice**  
   Speak your answers; the system records, transcribes, and analyzes your responses instantly.

4. **Adaptive Questioning**  
   Follow-up questions adjust dynamically based on your previous answers for a realistic flow.

5. **Review Results**  
   Complete the interview and receive a detailed performance report with scores and personalized advice.

---

## 🎯 Why Choose This System?

- **Adaptive & Contextual**  
  Questions evolve naturally based on your unique profile and interview progression.

- **Human-Like Interaction**  
  Experience a smooth, conversational flow that mimics real interviews.

- **Insightful & Actionable Feedback**  
  Go beyond scores with meaningful recommendations to improve your interview skills.

- **User-Friendly Interface**  
  Intuitive chat layout with audio recording tools for a frictionless experience.

---

## 📋 Prerequisites

- PDF format resume  
- Job description text  
- API keys for LLM & speech-to-text services (see `.env` setup below)

---

## 🚀 How to run in local environment


# Step 1: Clone the repository
git clone https://github.com/manthan89-py/AI-Interview-System.git
cd AI-Interview-System

# Step 2: Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Setup environment variables
cp .env.example .env

# Step 5: Edit the .env file and add your API keys
Open .env in a text editor and replace the placeholders with your actual keys:
GOOGLE_API_KEY=your_google_api_key
LLM_MODEL="gemini"  # or any supported model
SPEECHMATICS_API_KEY=your_speechmatics_api_key

# For API keys, visit:
Google API Key: https://console.cloud.google.com/apis/credentials
LiteLLM Models: https://docs.litellm.ai/docs/providers
Speechmatics API Key: https://www.speechmatics.com/

# Step 6: Run the application
streamlit run app.py











