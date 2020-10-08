from packages import *

class signupForm(FlaskForm):
    Email = StringField('E-Mail',
                         validators=[DataRequired(), Email()])
    Nickname = StringField('Nickname',
                         validators=[DataRequired(), Length(min = 2, max=20)])
    Password = PasswordField('Password',
                         validators=[DataRequired(), Length(min = 2, max=20)])
    rep_password = PasswordField('Repeat Password',
                         validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('SignUp')

class loginForm(FlaskForm):
    Email = StringField('E-Mail',
                         validators=[DataRequired(), Email()])
    Password = PasswordField('Password',
                         validators=[DataRequired(), Length(min = 2, max=20)])
    submit = SubmitField('Login')