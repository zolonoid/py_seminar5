

from pathlib import Path
import re

print("Программа, удаляющая из текста все слова, содержащие 'абв'.")
try:
    inText=Path("file1in.txt").read_text('utf-8')
    print("Получили текст из файла file1in.txt")
    words=inText.split()
    outText=' '.join([w for w in words if not ('а' in w or 'б' in w or 'в' in w)])
    Path("file1out.txt").write_text(outText,'utf-8')
    print("Удалили из текста все слова, содержащие 'абв' и записали в файл file1out.txt")
except Exception as exc:
    print(f"Что-то пошло не так...\n{exc}")