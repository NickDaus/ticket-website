from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/ticket')
def ticket_form():
    return render_template('ticket.html')

@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']
        tickets = request.form['tickets']
        return render_template('confirmation.html', name=name, email=email, event=event, tickets=tickets)
    else:
        return "<h1>Error: This page cannot be accessed directly.</h1>", 405


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

