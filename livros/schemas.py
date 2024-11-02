from ninja import ModelSchema, Schema
from .models import Livros

#Sempre que for cadastrar um livro, eu preciso receber essas três informações

class LivrosSchema(ModelSchema):
    class Meta:
        model = Livros
        fields = ['nome', 'streaming', 'categorias']


class AvaliacaoSchema(ModelSchema):
    class Meta:
        model = Livros
        fields = ['nota', 'comentarios']

class FiltrosSchema(Schema):
    nota_minima: int = None
    categorias: int = None
    reler: bool = False