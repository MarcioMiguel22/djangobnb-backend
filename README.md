# Djangobnb Backend

Backend API para o clone do Airbnb construído com Django REST Framework.

## Tecnologias

- Django 5.0.2
- Django REST Framework
- PostgreSQL
- Django Channels (WebSockets)
- JWT Authentication
- Django Allauth

## Estrutura

```
backend/
├── djangobnb_backend/  # Configurações principais
├── chat/              # App de chat com WebSockets
├── property/          # App de propriedades
├── useraccount/       # App de autenticação
├── media/            # Upload de arquivos
├── requirements.txt
└── manage.py
```

## Instalação

### Com Docker (Recomendado)

```bash
# Criar e iniciar containers
docker-compose up -d

# Executar migrações
docker-compose exec web python manage.py migrate

# Criar superuser
docker-compose exec web python manage.py createsuperuser

# Parar containers
docker-compose down
```

### Sem Docker

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com suas configurações

# Executar migrações
python manage.py migrate

# Criar superuser
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DEBUG=1
SECRET_KEY=sua-secret-key-aqui
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=djangobnb
SQL_USER=postgresuser
SQL_PASSWORD=postgrespassword
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

## Apps Django

### useraccount
- Autenticação de usuários com email
- JWT tokens
- Perfis de usuário

### property
- CRUD de propriedades
- Upload de imagens
- Sistema de reservas
- Filtros e busca

### chat
- Chat em tempo real com WebSockets
- Conversas entre usuários
- Histórico de mensagens

## Endpoints API

### Autenticação
- `POST /api/auth/registration/` - Registro
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout
- `GET /api/auth/user/` - Usuário atual
- `POST /api/auth/token/refresh/` - Refresh token

### Propriedades
- `GET /api/properties/` - Listar propriedades
- `GET /api/properties/:id/` - Detalhes da propriedade
- `POST /api/properties/create/` - Criar propriedade
- `GET /api/properties/:id/reservations/` - Reservas da propriedade

### Chat
- `GET /api/chat/` - Listar conversas
- `GET /api/chat/:id/` - Mensagens da conversa
- WebSocket: `/ws/chat/:conversation_id/` - Chat em tempo real

## Desenvolvimento

```bash
# Executar servidor de desenvolvimento
python manage.py runserver

# Criar novas migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Acessar shell Django
python manage.py shell

# Executar testes
python manage.py test
```

## Admin

Acesse o Django Admin em: http://localhost:8000/admin

## CORS

O backend está configurado para aceitar requisições de:
- http://localhost:5173 (Vite)
- http://localhost:3000 (Next.js)
- http://127.0.0.1:8000

## WebSockets

Para usar o chat em tempo real, conecte-se ao WebSocket:

```javascript
const ws = new WebSocket('ws://localhost:8000/ws/chat/conversation_id/');
```

## Deploy

Para produção, configure:
1. `DEBUG=False`
2. Configure `ALLOWED_HOSTS`
3. Use PostgreSQL
4. Configure variáveis de ambiente seguras
5. Colete arquivos estáticos: `python manage.py collectstatic`
