class FamiliaDatabase:
    def __init__(self, database):
        self.db = database

    # Quem da família é Empresario?
    def get_empresarios(self):
        query = "MATCH (p:Pessoa:Empresario) RETURN p.nome AS nome_empresario"
        results = self.db.execute_query(query)
        return [result["nome_empresario"] for result in results]

    # Quem é pai de Gabriel Guimaraes?
    def get_pai_de_gabriel(self):
        query = "MATCH (p1:Pessoa)-[:MÃE_DE]->(p2:Pessoa {nome: 'Gabriel Guimaraes'}) RETURN p1.nome AS nome_pai"
        results = self.db.execute_query(query)
        return [result["nome_pai"] for result in results]

    # Com quem Lise é casada?
    def get_casados_com_lise(self):
        query = "MATCH (p1:Pessoa {nome:'Geraldo'})-[:CASADO_COM]->(p2:Pessoa) RETURN p2.nome AS nome_parceiro"
        results = self.db.execute_query(query)
        return [result["nome_parceiro"] for result in results]
