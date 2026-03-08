# FitBuddy AI 🏋️‍♂️

FitBuddy AI is a generative AI-powered web application that creates personalized 7-day workout routines and nutrition tips based on user profiles.

Users enter their fitness details such as age, weight, goal, and workout intensity, and the system generates a structured workout plan along with targeted nutrition advice.

The application also stores user profiles and generated plans in a database so they can be viewed later.

---

# 🚀 Features

• Personalized 7-day workout plans  
• AI-generated nutrition tips  
• Dynamic user input form  
• SQLite database storage  
• Simple admin page to view all users  
• Ready for Google Gemini AI integration  

## 🛠️ Tech Stack

* **Backend:** (Python)
* **Database:** SQLite
* **AI Integration:** Google GenAI SDK
* **Frontend:** HTML5, CSS3, Jinja2 Templates, Python-Markdown

## 📂 Project Structure

```text
FitBuddy
│
├── main.py # Main Flask application
├── database.py # Database helper functions
├── gemini_flash_generator.py # AI generation logic
├── fitbuddy.db # SQLite database
│
├── templates/
│ ├── index.html # User input form
│ ├── result.html # Generated workout plan
```


# ⚙️ Installation
Clone the repository:
git clone https://github.com/abhinav2327cse1223/FitBuddy
Navigate to the project folder:
cd FitBuddy
Install dependencies:
pip install flask
Run the application:
python main.py


Open in browser:


http://127.0.0.1:5000
