from pathlib import Path
import re

def Compress(text: str) -> str:
    l=len(text)
    i=0
    syms=[]
    while i < l:
        sym = text[i]
        count = 1
        ii = i+1
        while ii < l:
            if sym!=text[ii]:
                i = ii-1
                break
            count += 1
            ii += 1
        syms.append((count, sym))
        if ii >= l: break
        i += 1
    return ''.join([f"{c}{s}" for c,s in syms])

def Decompress(text: str) -> str:
    syms=[(int(m.group(1)),m.group(2)) for m in re.finditer(r'(\d+)(\w)',text)]
    return ''.join([sym[1] for sym in syms for i in range(sym[0])])


print("Сжатие и восстановление данных по RLE алгоритму.")
text=Path("file4.txt").read_text('utf-8')
print("Прочитали исходный текст из файла file4.txt")
Path("file4RLE.txt").write_text(Compress(text),'utf-8')
print("Сжали текст и записали в файл file4RLE.txt")
text=Path("file4RLE.txt").read_text('utf-8')
print("Получили сжатый текст из файла file4RLE.txt")
Path("file4.txt").write_text(Decompress(text),'utf-8')
print("Восстановили сжатый текст и записали в файл file4.txt")