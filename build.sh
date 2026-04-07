#!/usr/bin/env bash
# Sair se houver erro
set -o errexit

# Instalar dependências
pip install -r requirements.txt

# Rodar Migrações (Cria as tabelas no Supabase)
python manage.py migrate
