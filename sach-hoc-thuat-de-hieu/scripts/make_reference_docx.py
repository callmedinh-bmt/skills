#!/usr/bin/env python3
"""Tạo reference.docx (file mẫu style cho pandoc) với:
- Tiêu đề Arial màu xanh đậm, Heading 1 có gạch chân xanh
- Thân bài Cambria, giãn dòng dễ đọc, căn đều
- Bảng có viền, dòng đầu tô nền xanh nhạt
- 4 cặp style hộp màu: BoxKid / BoxAI / BoxWarn / BoxEx (+ ...Title)
- PartTitle (trang "Phần"), SourceCode (code nền xám, font Consolas)

Cách dùng: python3 make_reference_docx.py <đường_dẫn_ra.docx>
"""
import os, re, subprocess, sys, tempfile, zipfile, shutil

out = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "ref.docx")
tmp = tempfile.mkdtemp()
base = os.path.join(tmp, "base.docx")
with open(base, "wb") as f:
    f.write(subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                           capture_output=True, check=True).stdout)
x = os.path.join(tmp, "x")
zipfile.ZipFile(base).extractall(x)
p = os.path.join(x, "word", "styles.xml")
s = open(p, encoding="utf8").read()

HEAD_FONT = "Arial"      # Arial/Cambria/Consolas đều có đủ dấu tiếng Việt trên Word
BODY_FONT = "Cambria"
CODE_FONT = "Consolas"

s = re.sub(r'<w:rFonts[^/]*/>',
           f'<w:rFonts w:ascii="{BODY_FONT}" w:hAnsi="{BODY_FONT}" w:eastAsia="{BODY_FONT}" w:cs="{BODY_FONT}"/>',
           s, count=1)

def setstyle(sid, xml):
    global s
    s = re.sub(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % sid, xml, s, flags=re.S)

def heading(sid, name, size, color, before, lvl, border=False):
    bd = '<w:pBdr><w:bottom w:val="single" w:sz="12" w:space="4" w:color="4A90D9"/></w:pBdr>' if border else ""
    return (f'<w:style w:type="paragraph" w:styleId="{sid}"><w:name w:val="{name}"/><w:basedOn w:val="Normal"/>'
            f'<w:next w:val="BodyText"/><w:uiPriority w:val="9"/><w:qFormat/><w:pPr><w:keepNext/><w:keepLines/>{bd}'
            f'<w:spacing w:before="{before}" w:after="120"/><w:outlineLvl w:val="{lvl}"/></w:pPr>'
            f'<w:rPr><w:rFonts w:ascii="{HEAD_FONT}" w:hAnsi="{HEAD_FONT}" w:cs="{HEAD_FONT}"/><w:b/>'
            f'<w:color w:val="{color}"/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr></w:style>')

setstyle("Heading1", heading("Heading1", "heading 1", 40, "1F3A5F", 240, 0, border=True))
setstyle("Heading2", heading("Heading2", "heading 2", 30, "1F3A5F", 320, 1))
setstyle("Heading3", heading("Heading3", "heading 3", 25, "2E6DB4", 240, 2))
setstyle("Heading4", heading("Heading4", "heading 4", 22, "333333", 200, 3))

setstyle("BodyText", '<w:style w:type="paragraph" w:styleId="BodyText"><w:name w:val="Body Text"/><w:basedOn w:val="Normal"/>'
         '<w:link w:val="BodyTextChar"/><w:qFormat/><w:pPr><w:spacing w:before="80" w:after="100" w:line="288" w:lineRule="auto"/>'
         '<w:jc w:val="both"/></w:pPr><w:rPr><w:sz w:val="23"/></w:rPr></w:style>')

setstyle("Table", '<w:style w:type="table" w:default="1" w:styleId="Table"><w:name w:val="Table"/><w:basedOn w:val="TableNormal"/>'
         '<w:tblPr><w:tblStyleRowBandSize w:val="1"/><w:tblBorders>'
         '<w:top w:val="single" w:sz="6" w:color="4A90D9"/><w:bottom w:val="single" w:sz="6" w:color="4A90D9"/>'
         '<w:insideH w:val="single" w:sz="4" w:color="CCCCCC"/><w:insideV w:val="single" w:sz="4" w:color="DDDDDD"/>'
         '<w:left w:val="single" w:sz="4" w:color="DDDDDD"/><w:right w:val="single" w:sz="4" w:color="DDDDDD"/></w:tblBorders>'
         '<w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="100" w:type="dxa"/><w:bottom w:w="40" w:type="dxa"/>'
         '<w:right w:w="100" w:type="dxa"/></w:tblCellMar></w:tblPr><w:rPr><w:sz w:val="20"/></w:rPr>'
         '<w:tblStylePr w:type="firstRow"><w:rPr><w:b/><w:color w:val="1F3A5F"/></w:rPr>'
         '<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="E8F1FB"/></w:tcPr></w:tblStylePr></w:style>')

setstyle("Title", f'<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/>'
         f'<w:next w:val="BodyText"/><w:qFormat/><w:pPr><w:spacing w:before="2400" w:after="240"/><w:jc w:val="center"/></w:pPr>'
         f'<w:rPr><w:rFonts w:ascii="{HEAD_FONT}" w:hAnsi="{HEAD_FONT}"/><w:b/><w:color w:val="1F3A5F"/><w:sz w:val="60"/></w:rPr></w:style>')
setstyle("Subtitle", '<w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Title"/>'
         '<w:next w:val="BodyText"/><w:qFormat/><w:pPr><w:spacing w:before="200" w:after="200"/></w:pPr>'
         '<w:rPr><w:b w:val="0"/><w:color w:val="4A90D9"/><w:sz w:val="32"/></w:rPr></w:style>')

BOXES = {"BoxKid": ("4A90D9", "EEF5FC"), "BoxAI": ("8E5BD6", "F5EFFC"),
         "BoxWarn": ("F08C00", "FFF5E8"), "BoxEx": ("3BA55C", "EDF8F0")}
extra = ""
for sid, (c, bg) in BOXES.items():
    bd = (f'<w:pBdr><w:top w:val="single" w:sz="4" w:space="4" w:color="{c}"/>'
          f'<w:left w:val="single" w:sz="24" w:space="8" w:color="{c}"/>'
          f'<w:bottom w:val="single" w:sz="4" w:space="4" w:color="{c}"/>'
          f'<w:right w:val="single" w:sz="4" w:space="4" w:color="{c}"/></w:pBdr>')
    extra += (f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="{sid}"><w:name w:val="{sid}"/>'
              f'<w:basedOn w:val="BodyText"/><w:qFormat/><w:pPr>{bd}<w:shd w:val="clear" w:color="auto" w:fill="{bg}"/>'
              f'<w:spacing w:before="0" w:after="60"/><w:ind w:left="200" w:right="200"/><w:jc w:val="left"/></w:pPr></w:style>')
    extra += (f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="{sid}Title"><w:name w:val="{sid}Title"/>'
              f'<w:basedOn w:val="BodyText"/><w:next w:val="{sid}"/><w:qFormat/><w:pPr><w:keepNext/>{bd}'
              f'<w:shd w:val="clear" w:color="auto" w:fill="{c}"/><w:spacing w:before="200" w:after="0"/>'
              f'<w:ind w:left="200" w:right="200"/></w:pPr><w:rPr><w:rFonts w:ascii="{HEAD_FONT}" w:hAnsi="{HEAD_FONT}"/>'
              f'<w:color w:val="FFFFFF"/><w:sz w:val="21"/></w:rPr></w:style>')
extra += (f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="PartTitle"><w:name w:val="PartTitle"/>'
          f'<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:before="4000" w:after="200"/><w:jc w:val="center"/>'
          f'<w:pBdr><w:top w:val="single" w:sz="12" w:space="12" w:color="4A90D9"/>'
          f'<w:bottom w:val="single" w:sz="12" w:space="12" w:color="4A90D9"/></w:pBdr></w:pPr>'
          f'<w:rPr><w:rFonts w:ascii="{HEAD_FONT}" w:hAnsi="{HEAD_FONT}"/><w:b/><w:color w:val="1F3A5F"/><w:sz w:val="52"/></w:rPr></w:style>')
extra += (f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="SourceCode"><w:name w:val="Source Code"/>'
          f'<w:basedOn w:val="Normal"/><w:link w:val="VerbatimChar"/><w:pPr><w:shd w:val="clear" w:color="auto" w:fill="F6F6F6"/>'
          f'<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="200" w:right="200"/></w:pPr>'
          f'<w:rPr><w:rFonts w:ascii="{CODE_FONT}" w:hAnsi="{CODE_FONT}"/><w:sz w:val="18"/></w:rPr></w:style>')
s = s.replace("</w:styles>", extra + "</w:styles>")
s = re.sub(r'(<w:style [^>]*w:styleId="VerbatimChar".*?<w:rPr>)',
           rf'\1<w:rFonts w:ascii="{CODE_FONT}" w:hAnsi="{CODE_FONT}"/>', s, count=1, flags=re.S)
open(p, "w", encoding="utf8").write(s)

if os.path.exists(out):
    os.remove(out)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(x):
        for fn in files:
            full = os.path.join(root, fn)
            z.write(full, os.path.relpath(full, x))
shutil.rmtree(tmp)
print("Đã tạo", out)
