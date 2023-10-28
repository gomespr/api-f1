from django.db import models


class Constructor(models.Model):
    id = models.AutoField(primary_key=True, db_column='constructorId')
    constructorRef = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    
    class Meta:
        # Especifique o nome da tabela existente no banco de dados
        db_table = 'constructors'
        # Indique ao Django para não gerenciar esta tabela
        managed = False

    def __str__(self):
        return self.name
