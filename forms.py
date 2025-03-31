from flask_wtf import FlaskFormfrom wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TimeFieldfrom wtforms.validators import EqualTofrom wtforms.validators import DataRequired, Length# Форма для входа пользователяclass LoginForm(FlaskForm):    username = StringField('Имя пользователя', validators=[DataRequired()])    password = PasswordField('Пароль', validators=[DataRequired()])    remember_me = BooleanField('Запомнить меня')    submit = SubmitField('Войти')# Форма для регистрации учителяclass TeacherRegistrationForm(FlaskForm):    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=4, max=80)])    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6, max=120)])    confirm_password = PasswordField('Подтвердите пароль',                                     validators=[DataRequired(),                                                 EqualTo('password', message='Пароли должны совпадать')])    submit = SubmitField('Зарегистрироваться')class AddAvailabilityForm(FlaskForm):    date = SelectField('Дата', coerce=int, validators=[DataRequired()])    subject = SelectField('Предмет', coerce=int, validators=[DataRequired()])    teacher = SelectField('Учитель', coerce=int, validators=[DataRequired()])    start_time = TimeField('Время начала', validators=[DataRequired()])    end_time = TimeField('Время окончания', validators=[DataRequired()])    duration = StringField('Длительность (минут)', validators=[DataRequired()])    submit = SubmitField('Добавить доступность')# Форма для добавления учителяclass AddTeacherForm(FlaskForm):    teacher = StringField('Имя учителя', validators=[DataRequired()])    submit = SubmitField('Добавить')# Форма для добавления датыclass AddDateForm(FlaskForm):    date = StringField('Дата (YYYY-MM-DD)', validators=[DataRequired()])    submit = SubmitField('Добавить')# Форма для добавления предметаclass AddSubjectForm(FlaskForm):    subject = StringField('Название предмета', validators=[DataRequired()])    submit = SubmitField('Добавить')# Форма для удаления датыclass DeleteDateForm(FlaskForm):    date_id = SelectField('Дата', coerce=int, validators=[DataRequired()])    submit = SubmitField('Удалить')# Форма для удаления предметаclass DeleteSubjectForm(FlaskForm):    subject_id = SelectField('Предмет', coerce=int, validators=[DataRequired()])    submit = SubmitField('Удалить')# Форма для удаления учителяclass DeleteTeacherForm(FlaskForm):    teacher_id = SelectField('Учитель', coerce=int, validators=[DataRequired()])    submit = SubmitField('Удалить')