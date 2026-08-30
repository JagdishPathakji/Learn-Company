document.addEventListener("DOMContentLoaded", () => {
    // 1. Table of Contents (Mini-Map)
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

    // 2. Copy Code Buttons Logic
    const copyButtons = document.querySelectorAll(".copy-btn");
    copyButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const codeBlock = btn.parentElement.nextElementSibling.querySelector("code");
            if (codeBlock) {
                navigator.clipboard.writeText(codeBlock.textContent).then(() => {
                    const originalText = btn.textContent;
                    btn.textContent = "Copied!";
                    setTimeout(() => {
                        btn.textContent = originalText;
                    }, 2000);
                });
            }
        });
    });

    // 3. ScrollSpy for Table of Contents (Highlights where you are)
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

    // 4. Smooth 'Back to Top' Button
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
});

// Topic Internal Tabs Logic
window.switchTopicTab = function(tabId) {
    document.querySelectorAll('.topic-tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.querySelectorAll('.topic-tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    document.getElementById(tabId).classList.add('active');
    
    const btn = document.querySelector(`button[onclick="switchTopicTab('${tabId}')"]`);
    if (btn) btn.classList.add('active');
    
    window.dispatchEvent(new Event('scroll'));
};
