from collections import Counter
from langdetect import detect
from transformers import pipeline,AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("digit82/kobart-summarization")
model = AutoModelForSeq2SeqLM.from_pretrained("digit82/kobart-summarization")
s=pipeline('summarization',model=model,tokenizer=tokenizer)
def lang(t):
    try:return detect(t)
    except:return 'fail'
def sum(t):
    if len(t.split())<50:return 'too short'
    try:
        sa=s(t,**{
            'max_length':1000,
            'min_length':30,
            'do_sample':False
        })
        return sa[0]['summary_text']
    except Exception as e:return e
def anal(t):
    print('summary')
    print(sum(t))
if __name__=='__main__':
    print('input text')
    l=[]
    while True:
        la=input()
        if la=='':break
        l.append(la)
    f='\n'.join(l)
    anal(f)