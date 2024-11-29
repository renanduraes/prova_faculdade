import sqlite3

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('contatos.db')
    return conn

# Dados de exemplo com uma instituição para cada estado
dados = [
    ('AC', 'Corpo de Bombeiros do Acre', '192', 'Emergências Urbanas e Florestais', 'O Corpo de Bombeiros do Acre atua no combate a incêndios e resgates.'),
    ('AL', 'Polícia Militar de Alagoas', '190', 'Segurança Pública', 'A Polícia Militar de Alagoas mantém a ordem e segurança no estado.'),
    ('AP', 'Corpo de Bombeiros do Amapá', '193', 'Emergências Urbanas', 'Responsável por resgates e combate a incêndios no Amapá.'),
    ('AM', 'SAMU Amazonas', '192', 'Serviço de Atendimento Móvel de Urgência', 'Presta atendimento pré-hospitalar em situações de emergência.'),
    ('BA', 'Polícia Militar da Bahia', '190', 'Segurança Pública', 'A Polícia Militar da Bahia garante a ordem pública e segurança.'),
    ('CE', 'SAMU Ceará', '192', 'Serviço de Atendimento Móvel de Urgência', 'O SAMU no Ceará oferece atendimento emergencial 24h.'),
    ('DF', 'Corpo de Bombeiros do Distrito Federal', '193', 'Emergências e Resgates', 'Atua em emergências e situações de risco no DF.'),
    ('ES', 'Polícia Militar do Espírito Santo', '190', 'Segurança Pública', 'Responsável pela manutenção da ordem no estado.'),
    ('GO', 'SAMU Goiás', '192', 'Serviço de Atendimento Móvel de Urgência', 'Atende emergências médicas em Goiás.'),
    ('MA', 'Polícia Militar do Maranhão', '190', 'Segurança Pública', 'Garante a segurança e ordem pública no Maranhão.'),
    ('MT', 'Corpo de Bombeiros de Mato Grosso', '193', 'Emergências e Resgates', 'Realiza resgates e combate a incêndios em Mato Grosso.'),
    ('MS', 'SAMU Mato Grosso do Sul', '192', 'Serviço de Atendimento Móvel de Urgência', 'Atendimento emergencial em Mato Grosso do Sul.'),
    ('MG', 'Polícia Militar de Minas Gerais', '190', 'Segurança Pública', 'A PM de Minas Gerais atua na prevenção e combate ao crime.'),
    ('PA', 'Corpo de Bombeiros do Pará', '193', 'Resgates e Incêndios', 'Atende emergências em áreas urbanas e florestais no Pará.'),
    ('PB', 'SAMU Paraíba', '192', 'Serviço de Atendimento Móvel de Urgência', 'O SAMU Paraíba oferece suporte em emergências médicas.'),
    ('PR', 'Polícia Militar do Paraná', '190', 'Segurança Pública', 'Manutenção da ordem e segurança no estado do Paraná.'),
    ('PE', 'Corpo de Bombeiros de Pernambuco', '193', 'Emergências Urbanas', 'O Corpo de Bombeiros de Pernambuco realiza resgates e combate a incêndios.'),
    ('PI', 'SAMU Piauí', '192', 'Serviço de Atendimento Móvel de Urgência', 'Serviço de atendimento emergencial pré-hospitalar.'),
    ('RJ', 'Polícia Militar do Rio de Janeiro', '190', 'Segurança Pública', 'Atua na manutenção da segurança pública no estado do Rio de Janeiro.'),
    ('RN', 'Corpo de Bombeiros do Rio Grande do Norte', '193', 'Emergências e Resgates', 'O Corpo de Bombeiros do RN realiza atendimentos emergenciais e resgates.'),
    ('RS', 'SAMU Rio Grande do Sul', '192', 'Serviço de Atendimento Móvel de Urgência', 'Presta atendimento emergencial em situações de saúde no Rio Grande do Sul.'),
    ('RO', 'Polícia Militar de Rondônia', '190', 'Segurança Pública', 'Garante a segurança pública no estado de Rondônia.'),
    ('RR', 'SAMU Roraima', '192', 'Serviço de Atendimento Móvel de Urgência', 'Presta atendimento em emergências médicas em Roraima.'),
    ('SC', 'Corpo de Bombeiros de Santa Catarina', '193', 'Emergências e Incêndios', 'O Corpo de Bombeiros de SC atua em resgates e emergências.'),
    ('SP', 'Polícia Militar de São Paulo', '190', 'Segurança Pública', 'Responsável pela manutenção da segurança no estado de São Paulo.'),
    ('SE', 'SAMU Sergipe', '192', 'Serviço de Atendimento Móvel de Urgência', 'Serviço emergencial de saúde no estado de Sergipe.'),
    ('TO', 'Corpo de Bombeiros de Tocantins', '193', 'Emergências e Resgates', 'Realiza resgates e combate a incêndios no Tocantins.')
]

# Função para popular o banco de dados
def popular_banco():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO contatos (estado, instituicao, telefone, area, historia) 
        VALUES (?, ?, ?, ?, ?)
    ''', dados)

    conn.commit()
    conn.close()
    print("Banco de dados populado com sucesso!")

# Executa a função para popular o banco
if __name__ == '__main__':
    popular_banco()
