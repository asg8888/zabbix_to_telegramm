#!/bin/bash
TOKEN='354207743:AAEP63AGoeTk4a_Kg5Slkm2wFUFfrRg0Bpo' 
if [ $# -ne 3 ] ; then echo 'Error! You must to define three params' && exit 1 ; fi 
CHAT_ID="$1" 
SUBJECT="$2" 
MESSAGE="$3" 
curl --header 'Content-Type: application/json' --request 'POST' --data "{\"chat_id\":\"${CHAT_ID}\",\"text\":\"${SUBJECT}\n${MESSAGE}\"}" "https://api.telegram.org/bot${TOKEN}/sendMessage" | grep -q '"ok":false,'
#curl --header 'Content-Type: application/json' --request 'POST' --data '{"chat_id":"_ID_","text":"_MESSAGE_"}' "https://api.telegram.org/bot_TOKEN_/sendMessage"
#if [ $? -eq 0 ] ; then exit 1 ; fi
