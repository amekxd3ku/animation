#!/usr/bin/env python3
# converter.py - запускаешь на СВОЕМ ПК

import subprocess
import os

# 1. Скачиваем гифку
gif_url = "https://i.pinimg.com/originals/09/0e/53/090e5393fa9cfef49a1f2bfde97c94ac.gif"
subprocess.run(['curl', '-s', '-o', 'input.gif', gif_url])

# 2. Разбиваем на кадры
subprocess.run(['mkdir', '-p', 'frames'])
subprocess.run(['convert', 'input.gif', '-coalesce', '-resize', '60x', 'frames/frame_%03d.png'])

# 3. Конвертируем в ASCII через chafa
ascii_frames = []
for frame in sorted(os.listdir('frames')):
    if frame.endswith('.png'):
        result = subprocess.run(
            ['chafa', '--size=60', f'frames/{frame}'],
            capture_output=True,
            text=True
        )
        ascii_frames.append(result.stdout)

# 4. Создаем финальный скрипт
script = '''#!/bin/bash
clear
echo "ASCII Animation - Ready to play!"
sleep 1

frames=(
'''

for frame in ascii_frames:
    # Экранируем для bash
    escaped = frame.replace('\\', '\\\\').replace('"', '\\"').replace('$', '\\$')
    escaped = escaped.replace('\n', '\\n')
    script += f'  "{escaped}"\n'

script += ''')
while true; do
  for frame in "${frames[@]}"; do
    printf "\\033[2J\\033[1;1H"
    echo -e "$frame"
    sleep 0.05
  done
done
'''

with open('animation.sh', 'w') as f:
    f.write(script)

print("✅ Created: animation.sh")
print("📦 Size:", len(script), "bytes")
print("🎬 Frames:", len(ascii_frames))
