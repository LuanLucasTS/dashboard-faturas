
# Gerenciador de Faturas 💼

Um sistema web para **gerenciamento de faturas**, desenvolvido em **Python (Flask)**.  
Permite cadastrar, listar, editar e excluir faturas de forma simples e intuitiva.

---

## 🚀 Funcionalidades

- Cadastro de faturas com campos como:
  - Cliente
  - Valor
  - Data de emissão
  - Data de vencimento
  - Status (Pendente, Pago, Atrasado)
- Edição e exclusão de faturas
- Filtros por status e data
- Painel com resumo financeiro
- Exportação de relatórios em PDF/CSV

---

## 🧩 Tecnologias Utilizadas

- **Backend:** Python, Flask  
- **Banco de Dados:** SQLite (padrão) ou MySQL  
- **Frontend:** HTML, CSS, Bootstrap  
- **Outros:** Jinja2, SQLAlchemy

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/gerenciador-faturas.git
cd gerenciador-faturas
```

### 2️⃣ Criar e ativar um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o projeto
```bash
flask run
```

O sistema estará disponível em: [http://localhost:5000](http://localhost:5000)

---
<!--
## 🧠 Estrutura do Projeto

```
gerenciador-faturas/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   └── static/
│
├── instance/
│   └── faturas.db
│
├── requirements.txt
└── run.py
```

---

## 📊 Futuras Implementações

- Autenticação de usuários
- Gráficos e dashboards
- Integração com APIs financeiras
- Envio automático de lembretes de pagamento

---
-->
## 🧑‍💻 Autor

Desenvolvido por **Luan Lucas**  

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.  
Consulte o arquivo [LICENSE](LICENSE) para mais informações.
