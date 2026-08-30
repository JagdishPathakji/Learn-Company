import os
import re

# 1. Fix the sidebar in 15-linq.html
topic_14 = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\14-extension-methods.html'
topic_15 = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\15-linq.html'

with open(topic_14, 'r', encoding='utf-8') as f:
    content_14 = f.read()

# Extract the full sidebar <ul> from 14
sidebar_match = re.search(r'(<aside class="sidebar">.*?</aside>)', content_14, re.DOTALL)
if sidebar_match:
    full_sidebar = sidebar_match.group(1)
    # The active class in 14 is on 14. We need to move it to 15.
    full_sidebar = full_sidebar.replace('class="active">14.', '>14.')
    full_sidebar = full_sidebar.replace('>15. LINQ', ' class="active">15. LINQ')
    
    with open(topic_15, 'r', encoding='utf-8') as f:
        content_15 = f.read()
    
    # Replace the short sidebar in 15 with the full one
    content_15 = re.sub(r'<aside class="sidebar">.*?</aside>', full_sidebar, content_15, flags=re.DOTALL)
    
    with open(topic_15, 'w', encoding='utf-8') as f:
        f.write(content_15)

# 2. Fix the CSS animation bug (pages vanishing)
css_path = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\css\global.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Make the fade-in much faster and don't start at completely invisible (opacity 0)
old_anim = """.topic-tab-content { display: none; animation: fadeIn 0.4s ease; }
.topic-tab-content.active { display: block; }

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}"""

new_anim = """.topic-tab-content { display: none; }
.topic-tab-content.active { display: block; animation: fadeIn 0.15s ease-out; }

@keyframes fadeIn {
  from { opacity: 0.5; transform: translateY(5px); }
  to { opacity: 1; transform: translateY(0); }
}"""

if old_anim in css_content:
    css_content = css_content.replace(old_anim, new_anim)
else:
    # Fallback if slightly different
    css_content = re.sub(r'@keyframes fadeIn\s*\{[^}]+\}', '@keyframes fadeIn { from { opacity: 0.5; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }', css_content)
    css_content = css_content.replace('animation: fadeIn 0.4s ease;', 'animation: fadeIn 0.15s ease-out;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Done fixing sidebar and CSS!")
