#!/bin/bash
clear; tput civis

# Путь, откуда брать кадры (папка frames/ уже есть в Pages)
BASE_URL="https://amekxd3ku.github.io/animation/frames"
DELAY=0.1

# Бесконечный цикл по кадрам
while true; do
  for i in $(seq -w 000 199); do
    clear
    # тихо скачиваем кадр и выводим в консоль
    curl -s "${BASE_URL}/frame_${i}.txt"
    sleep "$DELAY"
  done
done

tput cnorm
