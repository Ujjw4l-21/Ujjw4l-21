@echo off
title Akshaya Portal Server
echo Starting Database and Portal...
cd /d "%~dp0"
:: Starts the server for the whole network
start /b npx json-server --watch db.json --host 0.0.0.0 --port 3000
:: Opens the portal locally
start "" "index.html"
exit