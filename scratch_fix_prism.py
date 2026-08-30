import os

filepath = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\09-file-operations.html'

prism_scripts = """    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-csharp.min.js"></script>
"""

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = '<script src="../../js/ui-enhancements.js"></script>'

if "prism.min.js" not in content:
    content = content.replace(target, prism_scripts + '    ' + target)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
