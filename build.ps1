# npmでビルド
npm run build

# dist/assets を src/python/static にコピー（フォルダごと上書き）
Copy-Item -Path "dist/assets/*" -Destination "src/python/static/" -Recurse -Force

# dist/index.html を src/python/templates にコピー
Copy-Item -Path "dist/index.html" -Destination "src/python/templates/" -Force

# src/python/static/index.html を src/python/templates/index.html にコピー（必要なら）
Copy-Item -Path "src/python/static/index.html" -Destination "src/python/templates/index.html" -Force

# Python アプリ起動
python -m src.python.app