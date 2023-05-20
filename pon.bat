@echo off
powershell -c "(New-Object System.Media.SoundPlayer 'pon3.wav').PlaySync();"
chcp 65001
title PON.exe
color a
echo #####################################################
echo  ██████╗░░█████╗░███╗░░██╗░░░███████╗██╗░░██╗███████╗
echo  ██╔══██╗██╔══██╗████╗░██║░░░██╔════╝╚██╗██╔╝██╔════╝
echo  ██████╔╝██║░░██║██╔██╗██║░░░█████╗░░░╚███╔╝░█████╗░░
echo  ██╔═══╝░██║░░██║██║╚████║░░░██╔══╝░░░██╔██╗░██╔══╝░░
echo  ██║░░░░░╚█████╔╝██║░╚███║██╗███████╗██╔╝╚██╗███████╗
echo  ╚═╝░░░░░░╚════╝░╚═╝░░╚══╝╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
echo ######################################################
echo PON.exe - v1.1 BETA
pip install PyHotKey
pip install subprocess.run
pip install pygame
pip install opencv-python
pip install pywin32
python pon.py
explorer.exe
exit