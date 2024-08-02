from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Initialize variables
target_number = random.randint(1, 10)
correct_guesses = 0
total_guesses = 0

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def guess_number():
    global target_number, correct_guesses, total_guesses

    if request.method == 'POST':
        guess = int(request.form['guess'])
        total_guesses += 1
        if guess == target_number:
            correct_guesses += 1
            message = "Congratulations! You guessed the number. Now you can try a new one."
            target_number = random.randint(1, 10)
        elif guess < target_number:
            message = "Try guessing higher."
        else:
            message = "Try guessing lower."
    else:
        message = "From 1 to 10, Go for it!"

    # Calculate accuracy
    accuracy = "{:.1f}".format((correct_guesses / total_guesses) * 100) if total_guesses > 0 else 0

    return render_template('index.html', message=message, accuracy=accuracy, correct_guesses=correct_guesses, total_guesses=total_guesses)

if __name__ == '__main__':
    app.run(debug=True)
