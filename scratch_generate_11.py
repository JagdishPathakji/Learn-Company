import os
import glob

base_dir = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp'
filepath = os.path.join(base_dir, '11-generics.html')

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Generics</title>
    <link rel="stylesheet" href="../../css/global.css">
    <style>
        .arch-diagram { display: flex; flex-direction: column; gap: 20px; background: #1e293b; padding: 40px; border-radius: 8px; margin: 30px 0; color: #fff; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        .arch-phase { border: 2px dashed #64748b; padding: 25px; border-radius: 8px; background: #0f172a; position: relative; }
        .arch-phase-title { font-size: 1.2rem; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px; border-bottom: 1px solid #334155; padding-bottom: 10px; }
        
        .catch-list { list-style: none; padding: 0; }
        .catch-item { background: #fecaca; border-left: 5px solid #ef4444; padding: 20px; margin-bottom: 20px; border-radius: 4px; color: #7f1d1d; }
        .catch-item h3 { margin-top: 0; color: #991b1b; display: flex; align-items: center; gap: 10px; font-size: 1.2rem; margin-bottom: 10px; }
        .catch-item p { margin-bottom: 0; font-size: 1.05rem; }
        .catch-item code { background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px; color: #991b1b; font-weight: bold; }
    </style>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
</head>
<body>
    <button class="sidebar-toggle-btn" onclick="toggleSidebar()">☰</button>
    <aside class="sidebar">
        <h2>Knowledge Base</h2>
        <div class="sidebar-category">C# Training</div>
        <ul>
            <li><a href="01-visual-studio-2022.html">1. VS 2022 Overview</a></li>
            <li><a href="02-programming-guidelines.html">2. Guidelines & Commenting</a></li>
            <li><a href="03-csharp-dotnet-history.html">3. C# Fundamentals - Intro</a></li>
            <li><a href="04-scope-and-accessibility.html">4. Scope & Accessibility</a></li>
            <li><a href="05-namespace-and-libraries.html">5. Namespace & Libraries</a></li>
            <li><a href="06-enumerations.html">6. Enumerations (Enums)</a></li>
            <li><a href="07-datatable.html">7. DataTable</a></li>
            <li><a href="08-date-string-math.html">8. Date/String/Math</a></li>
            <li><a href="09-file-operations.html">9. File Operations</a></li>
            <li><a href="10-advanced-types.html">10. Types (AEIP)</a></li>
            <li><a href="11-generics.html" class="active">11. Generics</a></li>
        </ul>
        <div class="sidebar-category">Deep Dives (Custom)</div>
        <ul>
            <li><a href="custom-01-top-level-statements.html">Top-Level Statements vs Main</a></li>
        </ul>
    </aside>
    
    <main class="main-content">
        <div class="topic-header">
            <h1>Generics in C#</h1>
            <p class="metadata">Difficulty: Advanced | Category: C# Object-Oriented Programming</p>
        </div>

        <div class="callout callout-info">
            <span class="callout-title">Mental Model</span>
            <p>Imagine building a shipping box. Without generics, you have to build a "BookBox" that only holds books, a "ShoeBox" that only holds shoes, and a "PhoneBox" that only holds phones. <br><br><strong>Generics <code>&lt;T&gt;</code></strong> allow you to build a single "Magic Box". When you use it, you declare <code>MagicBox&lt;Shoe&gt;</code>, and the C# compiler instantly morphs it into a box that strictly accepts <em>only</em> shoes. You get 100% Type Safety without rewriting the same code 50 times.</p>
        </div>

        <!-- NEW TABBED UI -->
        <div class="topic-tabs">
            <button class="topic-tab-btn active" onclick="switchTopicTab('tab-basics')">1. Generic Classes & Methods</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-constraints')">2. Generic Constraints (where)</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-collections')">3. Boxing & Collections</button>
            <button class="topic-tab-btn danger-tab" onclick="switchTopicTab('tab-catches')">⚠️ Generics Catches</button>
        </div>

        <!-- TAB 1: BASICS -->
        <div id="tab-basics" class="topic-tab-content active">
            <h2>Generic Classes and Methods</h2>
            <p>The <code>&lt;T&gt;</code> syntax stands for "Type". It is a placeholder. When you instantiate the class or call the method, you replace <code>T</code> with the actual data type (like <code>string</code>, <code>int</code>, or a custom class like <code>User</code>).</p>
            
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - The Magic Box</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Generics
{
    /// &lt;summary&gt;
    /// A generic class that can store ANY data type securely.
    /// &lt;/summary&gt;
    public class DataStore&lt;T&gt;
    {
        private T storedData;

        public void SaveData(T data)
        {
            storedData = data;
            Console.WriteLine($"Saved data of type: {typeof(T).Name}");
        }

        public T GetData()
        {
            return storedData;
        }
    }

    class Program
    {
        static void Main()
        {
            // 1. Using the class with a String
            DataStore&lt;string&gt; stringStore = new DataStore&lt;string&gt;();
            stringStore.SaveData("Hello Generics");
            
            // 2. Using the EXACT SAME class with an Integer
            DataStore&lt;int&gt; intStore = new DataStore&lt;int&gt;();
            intStore.SaveData(404);

            // CATCH: Strict Type Safety is enforced!
            // intStore.SaveData("This will cause a compiler error!");
        }
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>Saved data of type: String
Saved data of type: Int32</pre></div>
        </div>

        <!-- TAB 2: CONSTRAINTS -->
        <div id="tab-constraints" class="topic-tab-content">
            <h2>Generic Constraints (The <code>where</code> Keyword)</h2>
            <p>Sometimes, <code>&lt;T&gt;</code> is <em>too</em> open. What if you build a <code>DataSaver&lt;T&gt;</code> class, but you only want it to accept classes that implement an <code>IEntity</code> interface? You use constraints to lock down exactly what <code>T</code> is allowed to be.</p>
            
            <div class="callout callout-info">
                <span class="callout-title">Common Constraints</span>
                <ul>
                    <li><code>where T : class</code> - T must be a reference type (a class).</li>
                    <li><code>where T : struct</code> - T must be a value type (int, bool, struct).</li>
                    <li><code>where T : new()</code> - T must have a parameterless constructor so we can do <code>new T()</code>.</li>
                    <li><code>where T : IEntity</code> - T must implement a specific interface.</li>
                </ul>
            </div>

            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Constraints in Action</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Generics
{
    public interface IEntity 
    { 
        int Id { get; set; } 
    }

    public class User : IEntity
    {
        public int Id { get; set; }
        public string Name { get; set; } = "Jagdish";
    }

    /// &lt;summary&gt;
    /// This generic class has STRICT constraints.
    /// T must implement IEntity, AND it must have a parameterless constructor.
    /// &lt;/summary&gt;
    public class Repository&lt;T&gt; where T : IEntity, new()
    {
        public T CreateNewRecord()
        {
            // We are only allowed to use 'new T()' because of the 'new()' constraint!
            T newObj = new T();
            
            // We are only allowed to access .Id because of the 'IEntity' constraint!
            newObj.Id = 999; 
            
            Console.WriteLine($"Created new {typeof(T).Name} with ID: {newObj.Id}");
            return newObj;
        }
    }

    class Program
    {
        static void Main()
        {
            Repository&lt;User&gt; userRepo = new Repository&lt;User&gt;();
            userRepo.CreateNewRecord();

            // CATCH: Repository&lt;string&gt; strRepo = new Repository&lt;string&gt;();
            // This crashes because 'string' does not implement IEntity!
        }
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>Created new User with ID: 999</pre></div>
        </div>

        <!-- TAB 3: COLLECTIONS & BOXING -->
        <div id="tab-collections" class="topic-tab-content">
            <h2>The Boxing / Unboxing Performance Killer</h2>
            <p>Before C# 2.0 (Generics), developers used <code>ArrayList</code> to store lists of objects. Because <code>ArrayList</code> accepted <em>anything</em>, it forced value types (like <code>int</code>) to be wrapped in an <code>object</code> wrapper. This is called <strong>Boxing</strong>. When you take the int back out, it has to be stripped out of the object wrapper (<strong>Unboxing</strong>).</p>

            <div class="callout callout-danger">
                <span class="callout-title">The Danger of Boxing</span>
                <p>Boxing and Unboxing completely destroys CPU performance and memory. If you loop through an <code>ArrayList</code> of 1,000,000 integers, the CPU has to build and destroy 1,000,000 object wrappers in RAM. <br><br><strong>The Fix:</strong> ALWAYS use Generic Collections (like <code>List&lt;int&gt;</code>). The compiler knows it holds an integer, so zero boxing occurs.</p>
            </div>

            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - List&lt;T&gt; vs ArrayList</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;
using System.Collections;
using System.Collections.Generic;

namespace KnowledgeBase.Generics
{
    public class PerformanceDemo
    {
        public void DemonstrateBoxing()
        {
            int myNumber = 50;

            // 1. THE OLD WAY (BAD PERFORMANCE)
            ArrayList oldList = new ArrayList();
            // BOXING happens here: The int '50' is wrapped inside an 'object' shell.
            oldList.Add(myNumber); 
            // UNBOXING happens here: The object is forced back into an int.
            int retrievedOld = (int)oldList[0]; 

            // 2. THE MODERN GENERIC WAY (MAXIMUM PERFORMANCE)
            List&lt;int&gt; modernList = new List&lt;int&gt;();
            // ZERO BOXING: The List strictly accepts an int in memory.
            modernList.Add(myNumber);
            // ZERO UNBOXING: The compiler knows it is already an int.
            int retrievedModern = modernList[0];

            Console.WriteLine("Generic List successfully bypassed boxing!");
        }
    }
    
    class Program
    {
        static void Main()
        {
            PerformanceDemo demo = new PerformanceDemo();
            demo.DemonstrateBoxing();
        }
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>Generic List successfully bypassed boxing!</pre></div>
        </div>

        <!-- TAB 4: CATCHES -->
        <div id="tab-catches" class="topic-tab-content">
            <h2>⚠️ Generics Master Catch List</h2>
            <p>These are the core traps and compiler errors developers face when working with Generics in Enterprise codebases.</p>
            
            <ul class="catch-list">
                <li class="catch-item">
                    <h3>1. The default(T) Trap</h3>
                    <p><strong>The Catch:</strong> Inside a generic class, you cannot write <code>T myValue = null;</code>. Why? Because <code>T</code> might be an <code>int</code> (which cannot be null). The compiler will crash.<br><br><strong>The Fix:</strong> You must write <code>T myValue = default(T);</code>. If T is a class, it assigns <code>null</code>. If T is an int, it assigns <code>0</code>.</p>
                </li>
                
                <li class="catch-item">
                    <h3>2. The ArrayList Ban</h3>
                    <p><strong>The Catch:</strong> Never use <code>ArrayList</code>, <code>Hashtable</code>, or any class from <code>System.Collections</code>. They cause massive CPU spikes due to Boxing/Unboxing. <br><br><strong>The Fix:</strong> Always use <code>System.Collections.Generic</code> (e.g., <code>List&lt;T&gt;</code>, <code>Dictionary&lt;TKey, TValue&gt;</code>).</p>
                </li>
                
                <li class="catch-item">
                    <h3>3. The new() Constraint Limitation</h3>
                    <p><strong>The Catch:</strong> The <code>where T : new()</code> constraint guarantees that the type has a parameterless constructor (e.g., <code>new User()</code>). However, C# does <strong>NOT</strong> support a constraint for constructors with parameters. You cannot do <code>where T : new(string)</code>.</p>
                </li>
                
                <li class="catch-item">
                    <h3>4. The typeof(T) Trap</h3>
                    <p><strong>The Catch:</strong> If you need to know what Type is currently inside your magic box, you cannot use <code>T.GetType()</code> if T hasn't been instantiated yet. <br><br><strong>The Fix:</strong> Use <code>typeof(T)</code> to get the metadata of the Type directly.</p>
                </li>
            </ul>
        </div>

        <div class="nav-buttons">
            <a href="10-advanced-types.html">&larr; Previous: Types (AEIP)</a>
            <a href="#">Next: File System (Advanced) &rarr;</a>
        </div>
    </main>
    
    <script src="../../js/ui-enhancements.js"></script>

    <!-- Prism Syntax Highlighting -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-csharp.min.js"></script>

    <!-- Personal Notes Panel -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <button class="notes-toggle-btn" onclick="toggleNotes()">📝 My Notes</button>
    <div class="notes-panel" id="notesPanel">
        <div class="notes-header">
            <span>Personal Notes</span>
            <span class="notes-close" onclick="toggleNotes()">&times;</span>
        </div>
        <div class="notes-tabs">
            <button id="tabWrite" class="notes-tab active" onclick="switchNoteTab('write')">Write</button>
            <button id="tabPreview" class="notes-tab" onclick="switchNoteTab('preview')">Preview (Markdown)</button>
        </div>
        <textarea class="notes-textarea" id="personalNotes" placeholder="Supports Markdown!&#10;&#10;Wrap code in triple backticks like this:&#10;```csharp&#10;int x = 5;&#10;```"></textarea>
        <div class="notes-preview" id="notesPreview"></div>
        <div class="notes-save-status" id="saveStatus">Auto-saved!</div>
    </div>

    <script>
        function toggleNotes() {
            if (window.hasDragged) { window.hasDragged = false; return; }
            document.getElementById('notesPanel').classList.toggle('open');
            document.body.classList.toggle('notes-open');
        }
        
        function switchNoteTab(mode) {
            const ta = document.getElementById('personalNotes');
            const prev = document.getElementById('notesPreview');
            const tabW = document.getElementById('tabWrite');
            const tabP = document.getElementById('tabPreview');
            
            if(mode === 'preview') {
                ta.style.display = 'none';
                prev.style.display = 'block';
                tabW.classList.remove('active');
                tabP.classList.add('active');
                
                prev.innerHTML = marked.parse(ta.value);
                
                if (window.Prism) {
                    Prism.highlightAllUnder(prev);
                }
            } else {
                ta.style.display = 'block';
                prev.style.display = 'none';
                tabW.classList.add('active');
                tabP.classList.remove('active');
            }
        }

        const notesTextarea = document.getElementById('personalNotes');
        const saveStatus = document.getElementById('saveStatus');
        
        let fileName = window.location.pathname.split('/').pop();
        if (!fileName) fileName = 'index.html';
        const pageKey = 'kb_notes_' + fileName;
        
        if(localStorage.getItem(pageKey)) {
            notesTextarea.value = localStorage.getItem(pageKey);
        }

        let saveTimeout = null;
        notesTextarea.addEventListener('input', function() {
            localStorage.setItem(pageKey, notesTextarea.value);
            saveStatus.style.opacity = 1;
            clearTimeout(saveTimeout);
            saveTimeout = setTimeout(() => { saveStatus.style.opacity = 0; }, 1000);
        });
    </script>

    <!-- Sidebar Toggle Script -->
    <script>
        function toggleSidebar() {
            document.body.classList.toggle('sidebar-collapsed');
            localStorage.setItem('kb_sidebar_collapsed', document.body.classList.contains('sidebar-collapsed'));
        }
        if(localStorage.getItem('kb_sidebar_collapsed') === 'true') {
            document.body.classList.add('sidebar-collapsed');
        }
    </script>

    <!-- Draggable Notes Button Script -->
    <script>
        const dragBtn = document.querySelector('.notes-toggle-btn');
        let isDragging = false;
        window.hasDragged = false; 
        let offsetX, offsetY;

        const savedX = localStorage.getItem('kb_notes_btn_x');
        const savedY = localStorage.getItem('kb_notes_btn_y');
        if (savedX && savedY) {
            dragBtn.style.left = savedX + 'px';
            dragBtn.style.top = savedY + 'px';
            dragBtn.style.bottom = 'auto'; 
            dragBtn.style.right = 'auto';  
        }

        dragBtn.addEventListener('mousedown', (e) => {
            isDragging = true;
            window.hasDragged = false; 
            offsetX = e.clientX - dragBtn.getBoundingClientRect().left;
            offsetY = e.clientY - dragBtn.getBoundingClientRect().top;
            dragBtn.style.cursor = 'grabbing';
        });

        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            window.hasDragged = true; 
            
            let newX = e.clientX - offsetX;
            let newY = e.clientY - offsetY;
            
            newX = Math.max(0, Math.min(newX, window.innerWidth - dragBtn.offsetWidth));
            newY = Math.max(0, Math.min(newY, window.innerHeight - dragBtn.offsetHeight));

            dragBtn.style.left = newX + 'px';
            dragBtn.style.top = newY + 'px';
            dragBtn.style.bottom = 'auto';
            dragBtn.style.right = 'auto';
        });

        document.addEventListener('mouseup', () => {
            if (isDragging) {
                isDragging = false;
                dragBtn.style.cursor = 'grab';
                localStorage.setItem('kb_notes_btn_x', dragBtn.style.left.replace('px', ''));
                localStorage.setItem('kb_notes_btn_y', dragBtn.style.top.replace('px', ''));
            }
        });
    </script>
</body>
</html>
'''

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Update Sidebars Globally
html_files = glob.glob(os.path.join(base_dir, '*.html'))
link_to_add = '\n            <li><a href="11-generics.html">11. Generics</a></li>'

for fpath in html_files:
    if '11-generics.html' in fpath:
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if '11-generics.html' in content:
        continue
    
    target_active = '<li><a href="10-advanced-types.html" class="active">10. Types (AEIP)</a></li>'
    target_inactive = '<li><a href="10-advanced-types.html">10. Types (AEIP)</a></li>'
    
    if target_active in content:
        content = content.replace(target_active, target_active + link_to_add)
    elif target_inactive in content:
        content = content.replace(target_inactive, target_inactive + link_to_add)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

