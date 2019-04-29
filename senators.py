from flask import Flask, render_template, redirect, url_for, request
from modules import convert_to_dict

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import Required

app = Flask(__name__)

# web host requires this
application = app

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = ''

# Flask-Bootstrap requires this line
Bootstrap(app)

# create a list of dicts
senate_list = convert_to_dict("senatorList.csv") #dict 1
bill_list = convert_to_dict("senatebill.csv") #dict 2

# with Flask-WTF, each web form is represented by a class
# "SearchForm" can change; "(FlaskForm)" cannot
class SearchForm(FlaskForm):
    # the choices are (option, string)
    sen_choice = SelectField('Select from this list')
    submit = SubmitField('Search')


@app.route('/', methods=['GET', 'POST'] )
def index():
    lastname = []
    fullname = []
    pairs_list = []
    #Fill one with the last name from bill List
    #Fill the next with full name from senate List
    for senator in senate_list:
        lastname.append(senator['LAST_NAME'])
        fullname.append(senator['SENATOR_FULLNAME'])
    pairs_list = zip(lastname, fullname)

    # this is from the class above; form will go to the template
    form = SearchForm()
    # this is how we auto-populate a select menu in a form
    form.sen_choice.choices = [ (p[0], p[1]) for p in pairs_list ]

    # if page opened by form submission, redirect to detail page
    if request.method == "POST":
        # get the input from the form
        sen_choice = request.form.get("sen_choice")
        return redirect( url_for('detail', name=sen_choice ) )

    # no else - just do this by default
    return render_template('index.html', form=form)


# second route
@app.route('/senator/<name>')
def detail(name):
    for senator in senate_list:
        if senator['LAST_NAME'] == name:
            sen_dict = senator
            break
    sen_bills_list = []
    for bill in bill_list:
        if bill['FILED_BY'] == name:
            sen_bills_list.append(bill)
    return render_template('senator.html', sen=sen_dict, name=name, sen_bills_list=sen_bills_list)



# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
