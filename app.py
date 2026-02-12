from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy student data
students = {
    "101": {"name": "Charan", "marks": 85},
    "102": {"name": "Ravi", "marks": 78},
    "103": {"name": "Sita", "marks": 92}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    roll_no = request.form['roll_no']
    student = students.get(roll_no)
    return render_template('result.html', student=student)

if __name__ == "__main__":
    app.run(debug=True)
