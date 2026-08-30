import os

css_file = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\css\global.css'
js_file = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\js\ui-enhancements.js'

tab_css = """
/* Topic Internal Tabs */
.topic-tabs {
    display: flex;
    gap: 10px;
    margin-bottom: 25px;
    border-bottom: 2px solid #334155;
    padding-bottom: 10px;
    flex-wrap: wrap;
}

.topic-tab-btn {
    background: #1e293b;
    color: #94a3b8;
    border: 1px solid #334155;
    padding: 12px 20px;
    border-radius: 6px 6px 0 0;
    cursor: pointer;
    font-weight: 600;
    font-size: 1rem;
    transition: all 0.2s;
    font-family: 'Inter', sans-serif;
    margin-bottom: -12px; /* Pull down over border */
}

.topic-tab-btn:hover {
    background: #334155;
    color: white;
}

.topic-tab-btn.active {
    background: #3b82f6;
    color: white;
    border-color: #3b82f6;
}

.topic-tab-btn.danger-tab.active {
    background: #ef4444;
    border-color: #ef4444;
}

.topic-tab-content {
    display: none;
    animation: fadeIn 0.3s ease-in-out;
}

.topic-tab-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}
"""

with open(css_file, 'r', encoding='utf-8') as f:
    current_css = f.read()

if '.topic-tabs' not in current_css:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write(tab_css)

tab_js = """
// Topic Internal Tabs Logic
window.switchTopicTab = function(tabId) {
    // Hide all contents
    document.querySelectorAll('.topic-tab-content').forEach(content => {
        content.classList.remove('active');
    });
    // Remove active state from all buttons
    document.querySelectorAll('.topic-tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected content
    document.getElementById(tabId).classList.add('active');
    // Highlight clicked button
    const btn = document.querySelector(`button[onclick="switchTopicTab('${tabId}')"]`);
    if (btn) btn.classList.add('active');
    
    // Refresh ScrollSpy observer since height changed
    window.dispatchEvent(new Event('scroll'));
};
"""

with open(js_file, 'r', encoding='utf-8') as f:
    current_js = f.read()

if 'switchTopicTab' not in current_js:
    with open(js_file, 'a', encoding='utf-8') as f:
        f.write(tab_js)
