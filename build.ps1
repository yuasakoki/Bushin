# npm�Ńr���h
npm run build

# dist/assets �� src/python/static �ɃR�s�[�i�t�H���_���Ə㏑���j
Copy-Item -Path "dist/assets/*" -Destination "src/python/static/" -Recurse -Force

# dist/index.html �� src/python/templates �ɃR�s�[
Copy-Item -Path "dist/index.html" -Destination "src/python/templates/" -Force

# src/python/static/index.html �� src/python/templates/index.html �ɃR�s�[�i�K�v�Ȃ�j
Copy-Item -Path "src/python/static/index.html" -Destination "src/python/templates/index.html" -Force

# Python �A�v���N��
python -m src.python.app