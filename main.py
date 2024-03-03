from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import app

app = Flask(__name__)
app.secret_key = '12345678a' 

DATABASE = 'database.db'

# Create a function to establish connection to SQLite database
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

# Initialize the database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Define QuizResponse model
class QuizResponse:
    def __init__(self, question_id, answer):
        self.question_id = question_id
        self.answer = answer

# Sample quiz questions
questions = {
    1: " Your Name?",
    2: "What's your favorite color?",
    3: "Which is your favorite movie genre?",
    4: "What's your favorite food?",
    5: "Where is your dream travel destination?",
    6: "What's your favorite season?",
    7: "What's your favorite animal?",
    8: "What's your favorite sport?",
    9: "What's your favorite hobby?",
    10: "What's your favorite music genre?",
    11: "What's your favorite book genre?",
    12: "What's your biggest fear?",
    13: "What's your dream?",
    14: "What do you like about yourself?",
    15: "What do you like about me?",
    16: "On a scale of 1 to 10, how much do you like me?",
    17: "Will you be my girlfriend?❤😊"
}

def get_responses():
  try:
      responses = app.added_responses()
      return responses
  except Exception as e:
      print("Error:", e)
      return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        try:
            # Store quiz responses in session
            session['quiz_responses'] = {}
            for qnum in questions:
                user_answer = request.form.get(f'q{qnum}')
                if not user_answer:
                    raise ValueError(f"Answer for question {qnum} is missing.")
                session['quiz_responses'][qnum] = user_answer
            return redirect(url_for('feedback'))  # Redirect to feedback page after submitting quiz
        except Exception as e:
            return render_template('error.html', error=str(e))
    return render_template('quiz.html', questions=questions)

@app.route('/result')
def result():
    # Retrieve quiz responses from session
    quiz_responses = session.get('quiz_responses', {})
    # Check if the current quiz session is completed
    if quiz_responses:
        # Check if the user said "yes" or "no" in the current quiz session
        if 'yes' in quiz_responses.values():
            result_message = "Congratulations! You completed the quiz. you are now my girlfriend💖😍"
        elif 'no' in quiz_responses.values():
            result_message = "Sorry, you didn't complete the quiz. You are not my girlfriend😢, If you want to try again, please go back and click the 'Quiz' button."
        else:
            result_message = "No responses found!"
    else:
        result_message = "No responses found!"
    return render_template('result.html', result=result_message)

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')



@app.route('/responses')
def view_responses():
    responses = get_responses()
    if responses:
        return render_template('database.html', responses=responses,questions = questions)
    else:
        return render_template('error.html', error= "Error fetching responses from the database.")


if __name__ == '__main__':
    app.run(debug=True)
