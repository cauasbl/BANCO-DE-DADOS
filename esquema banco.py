from mongoengine import connect, Document, StringField, FloatField, IntField, ObjectIdField, ListField, EmbeddedDocument, EmbeddedDocumentField

connect(host='mongodb+srv://cauasbl:uRjwOMQ44k7vnaUb@pymongo.ttb7i.mongodb.net/perfumaria')

class Usuario(Document):
    nome = StringField(required=True, description="O nome do usuário é obrigatório e deve ser uma string")
    email = StringField(required=True, description="O email do usuário é obrigatório e deve ser uma string")
    senha = StringField(required=True, description="A senha do usuário é obrigatória e deve ser uma string")
    tipo_usuario = StringField(choices=["cliente", "admin"], required=True, description="O tipo de usuário deve ser 'cliente' ou 'admin'")

    meta = {'collection': 'usuarios'}

class Produto(Document):
    nome = StringField(required=True, description="O nome do produto é obrigatório e deve ser uma string")
    descricao = StringField(required=True, description="A descrição do produto é obrigatória e deve ser uma string")
    preco = FloatField(required=True, description="O preço do produto é obrigatório e deve ser um número")
    tamanho = StringField(required=True, description="O tamanho do produto é obrigatório e deve ser uma string")
    marca = StringField(required=True, description="A marca do produto é obrigatória e deve ser uma string")

    meta = {'collection': 'produtos'}

class Estoque(Document):
    produto_id = ObjectIdField(required=True, description="O ID do produto é obrigatório e deve ser um ObjectId")
    quantidade = IntField(min_value=0, required=True, description="A quantidade em estoque é obrigatória e deve ser um inteiro não negativo")

    meta = {'collection': 'estoque'}

class ItemComprado(EmbeddedDocument):
    produto_id = ObjectIdField(required=True, description="O ID do produto é obrigatório e deve ser um ObjectId")
    quantidade = IntField(min_value=1, required=True, description="A quantidade é obrigatória e deve ser um inteiro positivo")
    preco_unitario = FloatField(required=True, description="O preço unitário é obrigatório e deve ser um número")

class Compra(Document):
    usuario_id = ObjectIdField(required=True, description="O ID do usuário é obrigatório e deve ser um ObjectId")
    total = FloatField(required=True, description="O total da compra é obrigatório e deve ser um número")
    itens_comprados = ListField(EmbeddedDocumentField(ItemComprado), required=True, description="A lista de itens comprados é obrigatória e deve ser um array")

    meta = {'collection': 'compras'}