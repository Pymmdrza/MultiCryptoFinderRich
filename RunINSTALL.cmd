@Echo off
title MultiCrypto.py Mmdrza.Com
Pushd "%~dp0"
pip install hdwallet
pip install lxml
pip install requests
:loop
python MultiCrypto.py
goto loop
