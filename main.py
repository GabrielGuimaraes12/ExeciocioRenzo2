from neo4j import GraphDatabase
from database import Database
from FamiliaDatabase import FamiliaDatabase
# Configuração da conexão com o Neo4j
db=Database("bolt://18.206.64.77:7687" , "neo4j", "checkouts-reference-dynamometers")


familia=FamiliaDatabase(db)

# Consulta: Quem da família é Empresario?
empresarios = familia.get_empresarios()
print("Empresários da família:")
print(empresarios)

# Consulta: Quem é pai de Gabriel Guimaraes?
pais_de_gabriel = familia.get_pai_de_gabriel()
print("Pais de Gabriel Guimaraes:")
print(pais_de_gabriel)

# Consulta: Com quem Lise é casada?
parceiros_de_lise = familia.get_casados_com_lise()
print("Parceiros de Lise:")
print(parceiros_de_lise)

db.close()