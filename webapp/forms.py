from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import IntegerField, SubmitField, SelectField


class ChoiceFormEvent(FlaskForm):
    event = SelectField('event', choices=[])
    coefficient = SelectField('coefficient', choices=[])

    bet = IntegerField(
                      'Ваша ставка',
                      validators=[DataRequired(),
                                  NumberRange(min=1000, max=100000)],
                      render_kw={"class": "form-control"}
                      )
    submit = SubmitField('Отправить',
                         render_kw={"class": "btn btn-primary"}
                         )
