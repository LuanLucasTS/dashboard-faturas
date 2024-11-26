#pip install flask
#pip install flask_mail
#pip install bcrypt
#pip install mysql-connector-python
from flask_mail import Mail, Message
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
from datetime import datetime, timedelta
import bcrypt
import os
import secrets
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asklasd89asd8n23zx'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=180) #tempo de expiração da seção

conexao = mysql.connector.connect(
    host="IP_SRV_BD",
    user="USUARIO_BD",
    password="PASSWORD_BD",
    database="NOME_DB",
    pool_reset_session="False"  # Evita o reset da sessão
)

cursor = conexao.cursor()

@app.route('/')
def home():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login.')
        return redirect(url_for('login'))

    return render_template('home.html')
@app.route('/faturas/<string:mes>')
def faturas(mes):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login.')
        return redirect(url_for('login'))

    cursor.execute(f"SELECT id_fatura, emitido from faturas_{mes}")
    emitido_rows = cursor.fetchall()
    for row in emitido_rows:
        emitido_date = datetime.combine(row[1], datetime.min.time())  # Cria um objeto datetime a partir da data
        diff_days = (datetime.now() - emitido_date).days
        cursor.execute(f"UPDATE faturas_{mes} SET dias_emitido = '{diff_days}' WHERE id_fatura = {row[0]}")
        conexao.commit()

    cursor.execute(f"SELECT id_fatura, vencimento from faturas_{mes}")
    vencimento_rows = cursor.fetchall()
    for row in vencimento_rows:
        emitido_date = datetime.combine(row[1], datetime.min.time())  # Cria um objeto datetime a partir da data
        diff_days = (emitido_date - datetime.now()).days
        cursor.execute(f"update faturas_{mes} set dias_vencimento = '{diff_days}' where id_fatura = {row[0]}")
        conexao.commit()

    #fatura = conn.execute(f"SELECT * FROM faturas_{mes} order by emitido").fetchall()
    cursor.execute(f"select f.* , fo.razao_social, fo.descricao from faturas_{mes} as f join fornecedor as fo on f.fornecedor = fo.id_fornecedor order by emitido")
    fatura = cursor.fetchall()
    return render_template('faturas.html', fatura=fatura, mes=mes)

@app.route('/editar_faturas2/<mes>/<id_fatura>', methods=['POST','GET'])
def editar_faturas2(mes, id_fatura):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    if request.method=='GET':
        #fatura = conn.execute(f"SELECT * FROM faturas_{mes} WHERE id_fatura={id_fatura}").fetchall()
        cursor.execute(f"select f.* , fo.razao_social, fo.descricao from faturas_{mes} as f join fornecedor as fo on f.fornecedor = fo.id_fornecedor where id_fatura={id_fatura}")
        fatura = cursor.fetchall()
        cursor.execute((f"select * from fornecedor order by razao_social"))
        fornecedor = cursor.fetchall()
        return render_template('edita_faturas2.html', fatura=fatura, mes=mes, fornecedor=fornecedor)
    else:
        recebida = request.form['recebida']
        gestaotop = request.form['gestaotop']
        rateio = request.form['rateio']
        fornecedor = request.form['fornecedor']
        emitido = request.form['emitido']
        vencimento = request.form['vencimento']
        valor = request.form['valor']
        nf = request.form['nf']
        cursor.execute(f"update faturas_{mes} set recebida='{recebida}', gestaotop='{gestaotop}', rateio='{rateio}', fornecedor='{fornecedor}', emitido='{emitido}', vencimento='{vencimento}', valor='{valor}', nf='{nf}' where id_fatura='{id_fatura}'")
        conexao.commit()
        return redirect(url_for('faturas', mes=mes))


@app.route('/nova_fatura/<mes>', methods=['POST','GET'])
def nova_fatura(mes):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    if request.method=='GET':
        cursor.execute((f"select * from fornecedor order by razao_social"))
        fornecedor = cursor.fetchall()
        return render_template('nova_fatura.html', mes=mes, fornecedor=fornecedor)
    else:
        recebida = request.form['recebida']
        gestaotop = request.form['gestaotop']
        rateio = request.form['rateio']
        fornecedor = request.form['fornecedor']
        emitido = request.form['emitido']
        vencimento = request.form['vencimento']
        valor = request.form['valor']
        nf = request.form['nf']
        cursor.execute(f"insert into faturas_{mes} (recebida, gestaotop, rateio, fornecedor, emitido, vencimento, valor, nf) values ('{recebida}', '{gestaotop}', '{rateio}', '{fornecedor}', '{emitido}', '{vencimento}', '{valor}', '{nf}')")
        conexao.commit()
        return redirect(url_for('nova_fatura', mes=mes))

@app.route('/excluir_fatura/<int:id_fatura>/<mes>')
def excluir_fatura(id_fatura, mes):
    cursor.execute(f"delete from faturas_{mes} where id_fatura = {id_fatura}")
    conexao.commit()
    return redirect(url_for('faturas', mes=mes))

@app.route('/pesquisar_fatura/<mes>', methods=['POST'])
def pesquisar_fatura(mes):
    pesquisa = request.form['pesquisar']
    #fatura = conn.execute(f"SELECT * FROM faturas_{mes} where fornecedor like '%{pesquisa}%' or descricao_produto like '%{pesquisa}%' ")
    cursor.execute(f"select f.* , fo.razao_social, fo.descricao from faturas_{mes} as f join fornecedor as fo on f.fornecedor = fo.id_fornecedor where fo.razao_social COLLATE utf8_general_ci like '%{pesquisa}%' or fo.descricao like '%{pesquisa}%' order by emitido")
    fatura = cursor.fetchall()
    return render_template('faturas.html', fatura=fatura, mes=mes)

@app.route('/changelog')
def changelog():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    return render_template('changelog.html')

@app.route('/logs')
def logs():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    cursor.execute("SELECT * FROM log_login")
    logs_login = cursor.fetchall()
    return render_template('logs.html', logs_login=logs_login)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        data = datetime.now().strftime('%d-%m-%Y %H:%M')
        usuario = request.form['usuario']
        senha = request.form['senha']

        cursor.execute(f"SELECT senha from usuarios where usuario='{usuario}'")
        resultado = cursor.fetchone()


        if resultado is None:
            flash('Falha na autenticação.')
            cursor.execute(f"insert into log_login (usuario, data_login, tipo) values ('{usuario}', '{data}', 'Falha')")
            conexao.commit()
            return redirect(url_for('login'))
        elif bcrypt.checkpw(senha.encode('utf-8'), resultado[0].encode('utf-8')):
            session['usuario_logado'] = request.form['usuario']
            cursor.execute(f"insert into log_login (usuario, data_login, tipo) values ('{usuario}', '{data}', 'Sucesso')")
            conexao.commit()
            return redirect(url_for('home'))
        else:
            flash('Falha na autenticação.')
            cursor.execute(f"insert into log_login (usuario, data_login, tipo) values ('{usuario}', '{data}', 'Falha')")
            conexao.commit()
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Você foi desconectado.')
    return redirect(url_for('login'))

@app.route('/usuarios', methods=['POST','GET'])
def usuarios():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    if request.method=='GET':
        cursor.execute("select * from usuarios where usuario != 'super.user' ")
        usuarios = cursor.fetchall()
        return render_template('usuarios.html', usuarios=usuarios)
    else:
        id_usuario = request.form['id_usuario']
        nome = request.form['nome']
        usuario = request.form['usuario']
        senha = request.form['senha']
        email = request.form['email']
        if senha == '':
            cursor.execute(f"update usuarios set nome='{nome}', usuario='{usuario}', email='{email}' where id_usuario={id_usuario}")
            conexao.commit()
            return redirect(url_for('usuarios'))
        else:
            senha = bcrypt.hashpw(request.form['senha'].encode(), bcrypt.gensalt(12))
            senha = senha.decode()
            cursor.execute(f"update usuarios set nome='{nome}', usuario='{usuario}', senha='{senha}', email='{email}' where id_usuario={id_usuario}")
            conexao.commit()
            return redirect(url_for('usuarios'))

@app.route('/novo_usuario', methods=['POST','GET'])
def novo_usuario():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('novo_usuario.html')
    else:
        nome = request.form['nome']
        usuario = request.form['usuario']
        email = request.form['email']
        senha = bcrypt.hashpw(request.form['senha'].encode(), bcrypt.gensalt(12))
        senha = senha.decode()
        cursor.execute(f"insert into usuarios (nome, usuario, senha, email) values ('{nome}', '{usuario}', '{senha}', '{email}')")
        conexao.commit()
        return redirect(url_for('novo_usuario'))

@app.route('/excluir_usuario/<int:id_usuario>')
def excluir_usuario(id_usuario):
    cursor.execute(f'delete from usuarios where id_usuario={id_usuario}')
    conexao.commit()
    return redirect(url_for('usuarios'))

@app.route('/manutencao')
def manutencao():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    return render_template('manutencao.html')

@app.route('/teste', methods=['POST','GET'])
def teste():
    return render_template('index.html')

@app.route('/fornecedores')
def fornecedores():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    cursor.execute(f"select * from fornecedor order by razao_social")
    fornecedor = cursor.fetchall()
    return render_template('fornecedores.html', fornecedor=fornecedor)


@app.route('/novo_fornecedor', methods=['POST','GET'])
def novo_fornecedor():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('novo_fornecedor.html')
    else:
        def remover_caracteres_nao_numericos(cep):
            numeros = [caractere for caractere in cep if caractere.isdigit()]
            return ''.join(numeros)

        rateio = request.form['rateio']
        razao_social = request.form['razao_social']
        nome_fantasia = request.form['nome_fantasia']
        descricao = request.form['descricao']
        telefone = request.form['telefone']
        email = request.form['email']
        contato = request.form['contato']
        cep =  remover_caracteres_nao_numericos(request.form['cep'])
        rua = request.form['rua']
        numero = request.form['numero']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        uf = request.form['uf']
        informacao_adicional = request.form['informacao_adicional']
        cursor.execute(f"insert into fornecedor (razao_social, nome_fantasia, descricao, telefone, email, contato, cep, rua, numero, complemento, bairro, cidade, uf, informacao_adicional, rateio) values ('{razao_social}', '{nome_fantasia}', '{descricao}', '{telefone}', '{email}', '{contato}', '{cep}', '{rua}', '{numero}', '{complemento}', '{bairro}', '{cidade}', '{uf}', '{informacao_adicional}', '{rateio}')")
        conexao.commit()
        return redirect(url_for('novo_fornecedor'))

@app.route('/edita_fornecedor/<id_fornecedor>', methods=['POST','GET'])
def edita_fornecedor(id_fornecedor):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    if request.method == 'GET':
        cursor.execute(f"select * from fornecedor where id_fornecedor={id_fornecedor}")
        fornecedor = cursor.fetchall()
        return render_template('edita_fornecedor.html', fornecedor=fornecedor)
    else:
        def remover_caracteres_nao_numericos(cep):
            numeros = [caractere for caractere in cep if caractere.isdigit()]
            return ''.join(numeros)

        rateio = request.form['rateio']
        razao_social = request.form['razao_social']
        nome_fantasia = request.form['nome_fantasia']
        descricao = request.form['descricao']
        telefone = request.form['telefone']
        email = request.form['email']
        contato = request.form['contato']
        cep =  remover_caracteres_nao_numericos(request.form['cep'])
        rua = request.form['rua']
        numero = request.form['numero']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        uf = request.form['uf']
        informacao_adicional = request.form['informacao_adicional']
        cursor.execute(f"update fornecedor set razao_social='{razao_social}', nome_fantasia='{nome_fantasia}', descricao='{descricao}', telefone='{telefone}', email='{email}', contato='{contato}', cep='{cep}', rua='{rua}', numero='{numero}', complemento='{complemento}', bairro='{bairro}', cidade='{cidade}', uf='{uf}', informacao_adicional='{informacao_adicional}', rateio='{rateio}' where id_fornecedor='{id_fornecedor}'")
        conexao.commit()
        return redirect(url_for('fornecedores'))

@app.route('/pesquisar_fornecedor/', methods=['POST'])
def pesquisar_fornecedor():
    pesquisa = request.form['pesquisar']
    cursor.execute(f"SELECT * FROM fornecedor where razao_social COLLATE utf8_general_ci like '%{pesquisa}%' or nome_fantasia like '%{pesquisa}%' or informacao_adicional like '%{pesquisa}%'")
    fornecedor = cursor.fetchall()
    return render_template('fornecedores.html', fornecedor=fornecedor)

@app.route('/dashboard/<string:mes>')
def dashboard(mes):
    cursor.execute(f"SELECT id_fatura, emitido from faturas_{mes}")
    emitido_rows = cursor.fetchall()
    for row in emitido_rows:
        emitido_date = datetime.combine(row[1], datetime.min.time())  # Cria um objeto datetime a partir da data
        diff_days = (datetime.now() - emitido_date).days
        cursor.execute(f"UPDATE faturas_{mes} SET dias_emitido = '{diff_days}' WHERE id_fatura = {row[0]}")
        conexao.commit()

    cursor.execute(f"SELECT id_fatura, vencimento from faturas_{mes}")
    vencimento_rows = cursor.fetchall()
    for row in vencimento_rows:
        emitido_date = datetime.combine(row[1], datetime.min.time())  # Cria um objeto datetime a partir da data
        diff_days = (emitido_date - datetime.now()).days
        cursor.execute(f"update faturas_{mes} set dias_vencimento = '{diff_days}' where id_fatura = {row[0]}")
        conexao.commit()

    #fatura = conn.execute(f"SELECT * FROM faturas_{mes} order by emitido").fetchall()
    cursor.execute(f"select f.* , fo.razao_social, fo.descricao from faturas_{mes} as f join fornecedor as fo on f.fornecedor = fo.id_fornecedor order by emitido")
    fatura = cursor.fetchall()
    return render_template('dashboard.html', fatura=fatura, mes=mes)


@app.route('/atualiza_versao')
def atualiza_versao():
    cursor.execute("select token_github from sistema")
    chave = cursor.fetchone()
    print(chave[0])
    if chave is not None:
        pasta_projeto = 'cd /sistemas/dashboard-faturas || exit'
        atualiza = f'git pull "https://github.com/LuanLucasTS/dashboard-faturas.git"'
        os.system(pasta_projeto)
        os.system(atualiza)
        return redirect(url_for('manutencao'))


@app.route('/altera_token_github', methods=['POST','GET']) #Essa opção só é usada quando o repositório for privado
def altera_token_github():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login.')
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('altera_token_github.html')
    else:
        chave = request.form['chave']
        validade = request.form['validade']
        cursor.execute(f"update sistema set token_github='{chave}', validade_token='{validade}' where id_sistema=1")
        conexao.commit()
        return redirect(url_for('altera_token_github'))

def learquivos(arquivo):
    ref_arquivo = open(arquivo, "r")
    ref_arquivo = ref_arquivo.read()
    return ref_arquivo

def envia_email(email, arquivo, assunto):
    app.config['MAIL_SERVER'] = 'URL_EMAIL'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'EMAIL'
    app.config['MAIL_PASSWORD'] = 'SENHA'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    mail = Mail(app)

    msg = Message(f'{assunto}', sender='DESTINO', recipients=[email, 'DESTINO_CÓPIA'])
    msg.body = learquivos(arquivo)
    mail.send(msg)

@app.route('/recuperasenha', methods=['POST', 'GET'])
def recuperasenha():
    if request.method == 'GET':
        return render_template('recupera_senha.html')
    else:
        email = request.form['email']
        cursor.execute(f"select * from usuarios where email='{email}'")
        usuario = cursor.fetchone()
    if usuario is None:
        flash(f'Email enviado para {email}.')
        return redirect(url_for('login'))
    else:
        #Gera o token para redefinir a senha
        token = secrets.token_urlsafe()
        #Cria a validade do token
        data_inicio = datetime.now()
        hora = datetime.now().strftime('%H:%M:%S')
        if hora > '22:00:00':
            expira = '23:59:59'
            cursor.execute(f"update usuarios set token='{token}', expira='{expira}' where email='{email}'")
            conexao.commit()
        else:
            validade = '2:00:00'  # Tempo de validade do token
            horas, minutos, segundos = map(int, validade.split(':'))
            # transforma a string em timedelta
            validade = timedelta(hours=horas, minutes=minutos, seconds=segundos)
            # soma a hora atual ao tempo de validade do token
            termino = data_inicio + validade
            # formata o resultado
            expira = termino.strftime('%H:%M:%S')
            cursor.execute(f"update usuarios set token='{token}', expira='{expira}' where email='{email}'")
            conexao.commit()
        # Monta o email de reset de senha e envia
        usuario = usuario[2]
        linkint = f'http://192.168.1.110:5000/reset/{token}'
        emailtxt = render_template('email.txt', linkint=linkint, usuario=usuario)
        with open('reset.txt', 'w') as f:
            print(emailtxt, file=f)
        envia_email(email, 'reset.txt', 'Recuperação de senha')
        flash(f'Se existir uma conta para {email}, um e-mail será enviado com mais instruções.')
        return redirect(url_for('login'))

####################################### Reset da Senha #######################################
@app.route('/reset/<string:token>', methods=['POST','GET'])
def reset(token):
    cursor.execute(f"select token, expira from usuarios where token='{token}'")
    token1 = cursor.fetchone()
    if request.method == 'GET':
        #Procura o usuário pelo token
        if token1 is None:
            flash('Não foi possível prosseguir com a solicitação. Por favor, Tente novamente.')
            return redirect(url_for('login'))
        else:
            #Verifica a validade do token
            horabd = token1[1]
            horas, minutos, segundos = map(int, horabd.split(':'))
            horabd = timedelta(hours=horas, minutes=minutos, seconds=segundos)

            data_inicio = datetime.now().strftime('%H:%M:%S')
            data_inicio = str(data_inicio)
            horas, minutos, segundos = map(int, data_inicio.split(':'))
            data_inicio = timedelta(hours=horas, minutes=minutos, seconds=segundos)

            expira = horabd - data_inicio

            if expira < timedelta(hours=0, minutes=0, seconds=0):
                flash('A validade do email para a troca da senha expirou. Por favor tente novamente.')
                return redirect(url_for('login'))
            else:
                return render_template('reset_senha.html', token=token)
    else:
        senha = request.form['senha']
        confirmacao = request.form['confirmacao']
        if senha != confirmacao:
            flash('Senhas não conferem. Por favor, Tente novamente.')
            return redirect(url_for('reset', token=token))
        else:
            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt(12))
            senha_hash = senha_hash.decode()
            cursor.execute(f"update usuarios set senha='{senha_hash}', token='', expira='' where token='{token}'")
            conexao.commit()
            flash('Senha alterada com sucesso!')
            return redirect(url_for('login'))
####################################### Idéias #######################################
@app.route('/ideias')
def ideias():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    cursor.execute(f"select * from ideias")
    ideias = cursor.fetchall()
    return render_template('ideias.html', ideias=ideias)

@app.route('/nova_ideia', methods=['POST','GET'])
def nova_ideia():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    if request.method=='GET':
        return render_template('nova_ideia.html')
    else:
        ideia = request.form['ideia']
        prioridade = request.form['prioridade']
        categoria = request.form['categoria']
        atribuido = request.form['atribuido']
        status = request.form['status']
        usuario = session['usuario_logado']
        data = datetime.now().strftime('%d-%m-%Y %H:%M')
        cursor.execute(f"insert into ideias (ideia, prioridade, categoria, atribuido, status, usuario_criado, data_criado, usuario_alterado, data_alterado) values ('{ideia}', '{prioridade}', '{categoria}', '{atribuido}', '{status}', '{usuario}', '{data}', '{usuario}', '{data}')")
        conexao.commit()
        return redirect(url_for('nova_ideia'))


@app.route('/editar_ideia/<id_ideia>/', methods=['POST','GET'])
def editar_ideia(id_ideia):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Necessário fazer login')
        return redirect(url_for('login'))

    if request.method=='GET':
        cursor.execute(f"select * from ideias where id_ideias={id_ideia}")
        ideia = cursor.fetchall()
        return render_template('edita_ideia.html', ideia=ideia)
    else:
        ideia = request.form['ideia']
        prioridade = request.form['prioridade']
        categoria = request.form['categoria']
        atribuido = request.form['atribuido']
        status = request.form['status']
        usuario = session['usuario_logado']
        data = datetime.now().strftime('%d-%m-%Y %H:%M')
        cursor.execute(f"update ideias set ideia='{ideia}', prioridade='{prioridade}', categoria='{categoria}', atribuido='{atribuido}', status='{status}', usuario_alterado='{usuario}', data_alterado='{data}' where id_ideias={id_ideia}")
        conexao.commit()
        return redirect(url_for('editar_ideia', id_ideia=id_ideia))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')