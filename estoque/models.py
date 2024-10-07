from django.db import models

class Categorias(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nome_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_categoria

class Grupos(models.Model):
    id_grupo = models.IntegerField(primary_key=True)
    nome_grupo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_grupo

class Tipos(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nome_tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_tipo


class Almoxarifados(models.Model):
    id_almoxarifado = models.AutoField(primary_key=True)
    nome_almoxarifado = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_almoxarifado

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14, default='00000000000000')


    def __str__(self):
        return self.razao_social

class Materiais(models.Model):
    id_material = models.AutoField(primary_key=True)
    nome_material = models.CharField(max_length=50)
    unidade_compra = models.CharField(max_length=2)
    unidade_requisicao = models.CharField(max_length=2)
    id_tipo = models.ForeignKey(Tipos, on_delete=models.CASCADE)
    id_grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    qtde_estoque = models.IntegerField()
    inativo = models.BooleanField()
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_almoxarifado = models.ForeignKey(Almoxarifados, on_delete=models.CASCADE)

#
# class Requisicoes(models.Model):
#     id_requisicao = models.AutoField(primary_key=True)
#     nome_requisicao = models.CharField(max_length=50)
#     id_responsavel = models.IntegerField()
#     id_material = models.ForeignKey(Materiais, on_delete=models.CASCADE)
#     quantidade = models.IntegerField()
#     data_hora = models.DateTimeField()
#
#
# class NotasFiscaisEntrada(models.Model):
#     id_nota_fiscal = models.AutoField(primary_key=True)
#     nome_nota_fiscal = models.CharField(max_length=50)
#     data_hora = models.DateTimeField()
#     id_material = models.ForeignKey(Materiais, on_delete=models.CASCADE)

class Log(models.Model):
    type = models.CharField(max_length=10)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30)  # Para identificar o tipo de log (ex: "estoque", "requisicao", etc.)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)  # Para registrar o usuário, se aplicável

    def __str__(self):
        return f"{self.category}: {self.message} at {self.created_at}"
