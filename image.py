import tkinter as t
from tkinter import filedialog
import easyocr
from PIL import Image
import numpy as np
import cv2
import re
def run():
    p=filedialog.askopenfilename(
        title='select image',
        filetypes=[('image file','*.jpg *.jpeg *.png *.bmp')]
    )
    if not p:return
    try:
        img_pil = Image.open(p).convert("RGB")
        img_cv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        r=easyocr.Reader(['ko','en'],gpu=False)
        ra=r.readtext(img_cv)
        lines = []
        for _, text, _ in ra:
            clean_text = re.sub(r'\s+', ' ', text.strip())  # 공백 정리
            if clean_text:
                lines.append(clean_text)
        final_text = '\n'.join(lines)  # 줄 바꿈으로 붙이기
        print("=== 인식된 텍스트 ===")
        print(final_text)
    except Exception as e:print(e)
w=t.Tk()
w.geometry('300x300')
b=t.Button(w,text='go',command=run,cursor='hand2')
b.pack()
w.mainloop()