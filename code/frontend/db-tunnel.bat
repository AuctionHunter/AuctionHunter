@echo off

REM pass username as an argument to this file to connect

ssh -L 27017:localhost:27017 %1@theorange.institute