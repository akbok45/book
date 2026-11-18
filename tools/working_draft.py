import os,re,sys,glob
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
root=sys.argv[1]; out=sys.argv[2]
chapters=[('ch01-the-temple',1,'The Temple'),('ch02-petit-goave',2,'Petit-Goâve'),('ch03-the-cay',3,'The Cay'),('ch04-the-half-moon',4,'The Half Moon'),('ch05-the-hidden-village',5,'The Hidden Village'),('ch06-the-road-under-the-lilies',6,'The Road Under the Lilies'),('ch07-the-patrol',7,'The Patrol')]
doc=Document()
st=doc.styles['Normal']; st.font.name='Times New Roman'; st.font.size=Pt(12)
st.paragraph_format.space_after=Pt(0); st.paragraph_format.line_spacing=1.5
for s in doc.sections:
    s.left_margin=s.right_margin=Inches(1); s.top_margin=s.bottom_margin=Inches(1)
def centered(text,size,bold=False,italic=False,before=0,after=0):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before=Pt(before); p.paragraph_format.space_after=Pt(after)
    r=p.add_run(text); r.font.size=Pt(size); r.bold=bold; r.italic=italic; return p
centered('THE CODEX TRILOGY',12,before=180,after=18)
centered('Book One',36,bold=True,after=18)
centered('Working draft',14,italic=True,after=200)
centered('Caribbean, 1670',12)
def pagebreak():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
def inline(p,text):
    parts=re.split(r'(\*[^*\n]+\*)',text)
    for part in parts:
        if part.startswith('*') and part.endswith('*') and len(part)>2:
            r=p.add_run(part[1:-1]); r.italic=True
        else: p.add_run(part)
total=0
for folder,num,title in chapters:
    files=sorted(glob.glob(os.path.join(root,'manuscript',folder,'*.md')))
    if not files: continue
    pagebreak()
    centered(f'Chapter {num}',14,before=72,after=6)
    centered(title,20,bold=True,after=36)
    if folder=='ch07-the-patrol':
        centered('Drafted ahead of the village arc rebuild. To be revised.',11,italic=True,after=24)
    for i,f in enumerate(files):
        t=open(f,encoding='utf-8').read()
        t=re.sub(r'^---\n.*?\n---\n','',t,flags=re.S)
        t=re.sub(r'<!--.*?-->','',t,flags=re.S).strip()
        total+=len(t.split())
        if i>0: centered('*',12,before=12,after=12)
        first=True
        for para in re.split(r'\n\s*\n',t):
            para=para.strip()
            if not para: continue
            if para in ('⸻','* * *','***','*'):
                centered('*',12,before=12,after=12); first=True; continue
            p=doc.add_paragraph()
            p.paragraph_format.first_line_indent=Inches(0 if first else 0.3)
            inline(p,para.replace('\n',' '))
            first=False
doc.save(out); print(total)

# Markdown copy in the same layout as Aydin's master file.
def write_md(md_out):
    out=["# The Codex Trilogy","","## Book One","","*Working draft · Caribbean, 1670*",""]
    names={1:'The Temple',2:'Petit-Goâve',3:'The Cay',4:'The Half Moon',5:'The Hidden Village',6:'The Road Under the Lilies',7:'The Patrol'}
    folders={1:'ch01-the-temple',2:'ch02-petit-goave',3:'ch03-the-cay',4:'ch04-the-half-moon',5:'ch05-the-hidden-village',6:'ch06-the-road-under-the-lilies',7:'ch07-the-patrol'}
    for n in sorted(names):
        out+=[f"## Chapter {n} · {names[n]}",""]
        files=sorted(glob.glob(os.path.join(root,'manuscript',folders[n],'*.md')))
        if not files:
            out+=["*Undrafted.*",""]; continue
        if n==7: out+=["*Drafted ahead of the village arc rebuild. To be revised.*",""]
        for i,f in enumerate(files):
            t=open(f,encoding='utf-8').read()
            t=re.sub(r'^---\n.*?\n---\n','',t,flags=re.S)
            t=re.sub(r'<!--.*?-->','',t,flags=re.S).strip()
            if i>0: out+=["---",""]
            for para in re.split(r'\n\s*\n',t):
                para=para.strip()
                if not para: continue
                out+=["---" if para in ('⸻','* * *','***','*') else para,""]
    open(md_out,'w',encoding='utf-8').write("\n".join(out).rstrip("\n")+"\n")
if len(sys.argv)>3: write_md(sys.argv[3])
