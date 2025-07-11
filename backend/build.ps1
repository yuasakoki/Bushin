# build.ps1
$rootPath = Resolve-Path "$PSScriptRoot\.."
Set-Location -Path "$rootPath/frontend"
npm install
npm run build
(Get-Content "$rootPath/backend/app/static/index.html") `
    -replace 'src="./assets/', 'src="/static/assets/' `
    -replace 'href="./assets/', 'href="/static/assets/' |
    Set-Content "$rootPath/backend/app/templates/index.html"
Set-Location -Path "$rootPath/backend"
python -m app.app
