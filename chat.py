from flask import Flask, rendertemplate, request, session #used session

app = Flask(name)
app.config['SECRETKEY'] = 'my key'
@app.route('/', methods=["GET","POST"]) #GET method also included
def index():
    if request.method == 'POST':
        if request.form['submitaction'] == 'add':
            currnotes = session['notes']
            note = request.form['note']
            if bool(note) & (note not in curr_notes):
                curr_notes.append(note)
        else:
            del_notes = request.form.getlist('del_notes')
            curr_notes = session['notes']
            for note in del_notes:
                if note in del_notes:
                    curr_notes.remove(note)
        session['notes'] = curr_notes
    else:
        if 'notes' not in session:
            session['notes'] = []
    return render_template('home.html', notes = session['notes'])

if __name == '__main':
    app.run(debug=True)
