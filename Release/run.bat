@echo off
cd "LED Programmer"
java -Djava.library.path=native/ -jar LEDProgrammer.jar ../glasses.li ../glasses.lp
pause