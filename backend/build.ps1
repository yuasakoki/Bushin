# build.ps1

$rootPath = Resolve-Path "$PSScriptRoot\.."

# 1. frontend に移動しビルド
Set-Location -Path "$rootPath/frontend"
npm install
npm run build

# 4. backendディレクトリへ移動し、Flask起動
Set-Location -Path "$rootPath/backend"
python -m app.app
