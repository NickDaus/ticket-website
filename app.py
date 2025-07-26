from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/ticket')
def ticket_form():
    return render_template('ticket.html')

@app.route('/confirmation', methods=['POST'])
def confirmation():
    name = request.form['name']
    email = request.form['email']
    event = request.form['event']
    tickets = request.form['tickets']

    return render_template('confirmation.html', name=name, email=email, event=event, tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)
