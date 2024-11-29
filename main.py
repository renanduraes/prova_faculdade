from flask import Flask, redirect, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estado TEXT NOT NULL,
            instituicao TEXT NOT NULL,
            telefone TEXT NOT NULL,
            area TEXT NOT NULL,
            historia TEXT NOT NULL,
            UNIQUE(estado, instituicao)  -- Adiciona uma restrição de unicidade para (estado, instituicao)
        )
    ''')
    conn.commit()
    conn.close()

# Inicializar o banco de dados na primeira execução
init_db()

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('contatos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para renderizar a página de contatos
@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/api/contatos/<estado>', methods=['GET'])
def get_contatos(estado):
    conn = get_db_connection()
    contatos = conn.execute('SELECT * FROM contatos WHERE estado = ?', (estado,)).fetchall()
    conn.close()

    if not contatos:
        return jsonify({'error': 'Nenhum contato encontrado para este estado.'}), 404
    else:
        return jsonify([{
            'id': contato['id'],  # Inclua o ID aqui para o frontend usar
            'instituicao': contato['instituicao'],
            'telefone': contato['telefone'],
            'area': contato['area'],
            'historia': contato['historia']
        } for contato in contatos])


# Rota para adicionar um novo contato
@app.route('/add', methods=['POST'])
def add_contato():
    data = request.get_json()

    estado = data.get('estado')
    instituicao = data.get('instituicao')
    telefone = data.get('telefone')
    area = data.get('area')
    historia = data.get('historia')

    if not (estado and instituicao and telefone and area and historia):
        return jsonify({'error': 'Todos os campos são obrigatórios.'}), 400

    conn = get_db_connection()

    # Verificar se a instituição já existe para o estado
    existing_contact = conn.execute(
        'SELECT * FROM contatos WHERE estado = ? AND instituicao = ?',
        (estado, instituicao)
    ).fetchone()

    if existing_contact:
        conn.close()
        return jsonify({'error': 'Essa instituição já existe no estado selecionado.'}), 400

    # Adicionar o novo contato
    conn.execute(
        'INSERT INTO contatos (estado, instituicao, telefone, area, historia) VALUES (?, ?, ?, ?, ?)',
        (estado, instituicao, telefone, area, historia)
    )
    conn.commit()
    conn.close()

    return jsonify({'message': 'Contato adicionado com sucesso!'}), 201, {'Content-Type': 'application/json'}

@app.route('/apagar', methods=['POST'])
def apagar():
    try:
        data = request.get_json()  # Pega o corpo da requisição em JSON
        id_contato = data.get('id_contato')  # Pega o id do contato a ser apagado
        
        if not id_contato:
            return jsonify({'error': 'ID do contato não fornecido.'}), 400
        
        conn = get_db_connection()
        # Deletar o contato pelo ID
        conn.execute('DELETE FROM contatos WHERE id = ?', (id_contato,))
       
        conn.commit()
        conn.close()

        return jsonify({'message': 'Contato apagado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro ao apagar o contato: {str(e)}'}), 500


# Rota para editar um contato
@app.route('/editar', methods=['POST'])
def editar_contato():
    data = request.get_json()
    id_contato = data.get('id_contato')
    estado = data.get('estado')
    instituicao = data.get('instituicao')
    telefone = data.get('telefone')
    area = data.get('area')
    historia = data.get('historia')

    if not (id_contato and estado and instituicao and telefone and area and historia):
        return jsonify({'error': 'Todos os campos são obrigatórios.'}), 400

    conn = get_db_connection()

   # Atualizar o contato no banco de dados
    conn.execute('''
        UPDATE contatos
        SET estado = ?, instituicao = ?, telefone = ?, area = ?, historia = ?
        WHERE id = ?
    ''', (estado, instituicao, telefone, area, historia, id_contato))
   
    conn.commit()
    conn.close()

    return jsonify({'message': 'Contato atualizado com sucesso!'}), 200




if __name__ == '__main__':
    app.run(debug=True)
