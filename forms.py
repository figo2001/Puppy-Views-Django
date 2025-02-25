from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField


class AddForm(FlaskForm):

    name=StringField('Name of Puppy: ')
    submit=SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id=IntegerField('Id Number of Puppy to Remove: ')
    submit=SubmitField('Remove Puppy')

class AddOwnerForm(FlaskForm):
    name=StringField('Name of Owner: ')
    pup_id=IntegerField('Id of Puppy: ')
    submit=SubmitField('Add Owner')