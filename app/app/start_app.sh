npm i
npm run build
flask db upgrade
gunicorn --worker-class gevent --reload --workers 1 --bind 0.0.0.0:8008 wsgi:app --max-requests 1000 --timeout 30 --keep-alive 30 --log-level info