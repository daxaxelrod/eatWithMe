from wtforms import Form, BooleanField, TextField
from wtforms import PasswordField, EmailField, validators, RadioField

class AreYouHungry(Form):
    yesOrNo = BooleanField("Feeling Hungry?", [validators.Required()])

class User(Form):
