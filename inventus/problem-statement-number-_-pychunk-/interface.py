from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    
    data = {
        'Name': [name],
        'Email': [email],
        'Age': [age]
    }
    
    df = pd.DataFrame(data)
    df.to_excel('user_data.xlsx', index=False)
    
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
