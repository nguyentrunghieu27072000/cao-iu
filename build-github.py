#!/usr/bin/env python3
"""Tạo bản đầy đủ để đưa lên GitHub Pages: docs/index.html + ảnh + nhạc."""
import os, re, shutil
root = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
title = re.search(r'<title>(.*?)</title>', src).group(1)
body = src.replace(f'<title>{title}</title>\n', '', 1)
body = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n', '', body, count=1)
page = f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#160819">
<title>{title}</title>
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
{body}
</body>
</html>
'''
out = os.path.join(root, 'docs'); os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page)
open(os.path.join(out, '.nojekyll'), 'w').close()
shutil.copy(os.path.join(root, 'chochut.mp3'), out)
imgs = os.path.join(out, 'images'); os.makedirs(imgs, exist_ok=True)
used = set(re.findall(r'images/([\w\-]+\.(?:jpg|png))', src))
for f in used:
    p = os.path.join(root, 'images', f)
    if os.path.exists(p): shutil.copy(p, imgs)
    else: print('THIẾU ảnh:', f)
print('docs/ sẵn sàng:', len(used), 'ảnh,', os.path.getsize(os.path.join(out,'index.html'))//1024, 'KB html')
