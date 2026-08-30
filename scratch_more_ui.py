import os

base_dir = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website'
js_file = os.path.join(base_dir, 'js', 'ui-enhancements.js')
css_file = os.path.join(base_dir, 'css', 'global.css')

additional_js = """
    // 4. Reading Time Estimator
    if (mainContent) {
        const text = mainContent.innerText || mainContent.textContent;
        const wordCount = text.split(/\s+/).length;
        const readingTime = Math.ceil(wordCount / 200); // Average 200 WPM
        
        const metaTag = document.querySelector('.metadata');
        if (metaTag && !metaTag.innerHTML.includes('min read')) {
            metaTag.innerHTML += ` | ⏱ ${readingTime} min read`;
        }
    }

    // 5. ScrollSpy for Table of Contents (Highlights where you are)
    if (mainContent) {
        const headings = mainContent.querySelectorAll("h2, h3");
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    document.querySelectorAll('.toc-panel a').forEach(link => {
                        link.classList.remove('active-toc');
                        if (link.getAttribute('href').substring(1) === entry.target.id) {
                            link.classList.add('active-toc');
                        }
                    });
                }
            });
        }, { rootMargin: "-10% 0px -80% 0px" });

        if (headings.length > 0) {
            headings.forEach(h => observer.observe(h));
        }
    }

    // 6. Smooth 'Back to Top' Button
    const topBtn = document.createElement("button");
    topBtn.innerHTML = "↑ Top";
    topBtn.className = "back-to-top";
    document.body.appendChild(topBtn);

    window.addEventListener("scroll", () => {
        if (window.scrollY > 500) {
            topBtn.style.opacity = "1";
            topBtn.style.pointerEvents = "auto";
            topBtn.style.transform = "translateY(0)";
        } else {
            topBtn.style.opacity = "0";
            topBtn.style.pointerEvents = "none";
            topBtn.style.transform = "translateY(10px)";
        }
    });

    topBtn.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
"""

with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Insert the new code right before the closing "});" of the DOMContentLoaded event
if 'Reading Time Estimator' not in js_content:
    js_content = js_content[:js_content.rfind('});')] + additional_js + '\n});\n'
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)


additional_css = """
/* Enhancements styling */
.toc-panel a.active-toc {
    color: #38bdf8;
    font-weight: 700;
}

.toc-panel a.active-toc::before {
    content: "▸ ";
    color: #38bdf8;
    position: absolute;
    left: 5px;
}

.toc-panel li {
    position: relative;
    padding-left: 10px;
}

.back-to-top {
    position: fixed;
    bottom: 30px;
    right: 180px; /* Placed safely to the left of the Notes button */
    background: #1e293b;
    color: #94a3b8;
    border: 1px solid #334155;
    padding: 10px 20px;
    border-radius: 50px;
    cursor: pointer;
    opacity: 0;
    pointer-events: none;
    transform: translateY(10px);
    transition: all 0.3s ease;
    z-index: 999;
    font-weight: bold;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.back-to-top:hover {
    background: #334155;
    color: white;
    transform: translateY(-2px) !important;
}
"""

with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.active-toc' not in css_content:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write(additional_css)
