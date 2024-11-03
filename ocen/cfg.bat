@echo off

if "%1"=="_chk_" shift

rem --- Konfiguracja ocen.bat ---
rem W przypadku opracowania wlasnego zestawu testow nalezy zmienic
rem zawartosc zmiennej TESTS a testy zabpiowac do kataloguw IN\, OUT\
rem nazwy testow powinny analogiczne do przykladowych

if "%1"=="bit" goto bit
if "%1"=="BIT" goto bit
if "%1"=="spr" goto spr
if "%1"=="SPR" goto spr
if "%1"=="usu" goto usu
if "%1"=="USU" goto usu
if "%1"=="wal" goto wal
if "%1"=="WAL" goto wal
if "%1"=="zam" goto zam
if "%1"=="ZAM" goto zam


set T=%1
goto end

:bit
set I=bit
set T=0 1 2 3 4
set C=bin\cmp.exe
goto end
:spr
set I=spr
set T=0 1 2 3
set C=bin\cmp.exe
goto end
:usu
set I=usu
set T=0 1 2 3 4
set C=bin\cmp.exe
goto end
:wal
set I=wal
set T=0a 0b 1 2 3 4
set C=bin\cmp.exe
goto end
:zam
set I=zam
set T=0 1 2 3
set C=bin\cmp.exe
goto end


rem --- Koniec konfiguracji

:end

if "%C%"=="" goto def_chk
goto new_chk
:def_chk
set C=bin\cmp.exe
:new_chk

:real_end
