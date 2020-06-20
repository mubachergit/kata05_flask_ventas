from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

def valida_coste(form, field):
    if field.data > form.precio_unitario.data:
        raise ValidationError('Ya te he dicho que el coste unitario ha de ser menor que el precio')

class ProductForm(FlaskForm):
    tipo_producto = StringField('Tipo de Producto', validators=[DataRequired(), Length(min=3, message="Debe tener al menos tres caracteres")])
    precio_unitario = FloatField ('Precio Unitario', validators= [DataRequired (message="Introduce algo")])
    coste_unitario = FloatField ('Coste Unitario', validators=[DataRequired(), valida_coste])

    submit = SubmitField('Aceptar')
    '''
    #Otra forma de validar el error
    def validate_coste_unitario(self, field):
        if field.data > self.precio_unitario.data:
            raise ValidationError('El coste unitario ha de ser menor o igual que el precio unitario')
    '''