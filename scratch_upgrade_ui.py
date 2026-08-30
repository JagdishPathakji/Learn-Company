import os
import glob

base_dir = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website'
css_file = os.path.join(base_dir, 'css', 'global.css')
js_dir = os.path.join(base_dir, 'js')
js_file = os.path.join(js_dir, 'ui-enhancements.js')

# 1. Ensure JS directory exists
os.makedirs(js_dir, exist_ok=True)

# 2. Create the ui-enhancements.js file
ui_js = """
document.addEventListener("DOMContentLoaded", () => {
    // 1. Reading Progress Bar
    const progressBar = document.createElement("div");
    progressBar.id = "reading-progress";
    document.body.appendChild(progressBar);

    window.addEventListener("scroll", () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + "%";
    });

    // 2. Table of Contents (Mini-Map)
    const mainContent = document.querySelector(".main-content");
    if (mainContent) {
        const headings = mainContent.querySelectorAll("h2, h3");
        if (headings.length > 0) {
            const tocPanel = document.createElement("div");
            tocPanel.className = "toc-panel";
            tocPanel.innerHTML = "<strong>On this page</strong><ul></ul>";
            const ul = tocPanel.querySelector("ul");

            headings.forEach((heading, index) => {
                if (!heading.id) {
                    heading.id = "heading-" + index;
                }
                const li = document.createElement("li");
                li.className = "toc-" + heading.tagName.toLowerCase();
                const a = document.createElement("a");
                a.href = "#" + heading.id;
                a.textContent = heading.textContent;
                li.appendChild(a);
                ul.appendChild(li);
            });
            
            document.body.appendChild(tocPanel);
        }
    }

    // 3. Copy Code Buttons Logic
    const copyButtons = document.querySelectorAll(".copy-btn");
    copyButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const codeBlock = btn.parentElement.nextElementSibling.querySelector("code");
            if (codeBlock) {
                navigator.clipboard.writeText(codeBlock.textContent).then(() => {
                    const originalText = btn.textContent;
                    btn.textContent = "Copied! ✔";
                    btn.style.color = "#4ade80";
                    setTimeout(() => {
                        btn.textContent = originalText;
                        btn.style.color = "";
                    }, 2000);
                });
            }
        });
    });
});
"""
with open(js_file, 'w', encoding='utf-8') as f:
    f.write(ui_js)

# 3. Update global.css
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

new_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

#reading-progress {
    position: fixed;
    top: 0; left: 0;
    height: 4px;
    background: #38bdf8;
    z-index: 10000;
    width: 0%;
    transition: width 0.1s ease-out;
}

.toc-panel {
    position: fixed;
    right: 30px;
    top: 100px;
    width: 250px;
    background: #1e293b;
    color: #f1f5f9;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    padding: 20px;
    font-size: 0.9rem;
    max-height: calc(100vh - 200px);
    overflow-y: auto;
    border: 1px solid #334155;
    z-index: 900;
}

.toc-panel strong {
    display: block;
    margin-bottom: 15px;
    color: #38bdf8;
    text-transform: uppercase;
    font-size: 0.8rem;
    letter-spacing: 1px;
}

.toc-panel ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.toc-panel li {
    margin-bottom: 10px;
    line-height: 1.4;
}

.toc-panel li.toc-h3 {
    padding-left: 15px;
    font-size: 0.85rem;
    border-left: 2px solid #475569;
}

.toc-panel a {
    color: #94a3b8;
    text-decoration: none;
    transition: color 0.2s;
}

.toc-panel a:hover {
    color: #fff;
}

body.notes-open .toc-panel {
    display: none;
}
"""

if '#reading-progress' not in css_content:
    # Prepend import and append new styles
    css_content = css_content.replace('body {', 'body {\n  font-family: "Inter", -apple-system, sans-serif;')
    css_content = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');\n" + css_content + new_css
    
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)

# 4. Inject script into all HTML files
html_files = glob.glob(os.path.join(base_dir, 'topics', 'csharp', '*.html'))

script_tag = '<script src="../../js/ui-enhancements.js"></script>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if script_tag not in content:
        content = content.replace('</body>', f'    {script_tag}\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
