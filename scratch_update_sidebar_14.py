import os
import glob

base_dir = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp'
link_to_add = '\n            <li><a href="14-extension-methods.html">14. Extension Methods</a></li>'

html_files = glob.glob(os.path.join(base_dir, '*.html'))

for fpath in html_files:
    if '14-extension-methods.html' in fpath:
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '14-extension-methods.html' in content:
        continue
    
    # We want to insert the new link right after the 13th topic.
    target_active = '<li><a href="13-lambda-expressions.html" class="active">13. Lambda Expressions</a></li>'
    target_inactive = '<li><a href="13-lambda-expressions.html">13. Lambda Expressions</a></li>'
    
    if target_active in content:
        content = content.replace(target_active, target_active + link_to_add)
    elif target_inactive in content:
        content = content.replace(target_inactive, target_inactive + link_to_add)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
