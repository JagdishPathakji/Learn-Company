import os
import glob

base_dir = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp'
filepath = os.path.join(base_dir, '10-advanced-types.html')

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Advanced Types (AEIP)</title>
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
            <li><a href="10-advanced-types.html" class="active">10. Types (AEIP)</a></li>
        </ul>
        <div class="sidebar-category">Deep Dives (Custom)</div>
        <ul>
            <li><a href="custom-01-top-level-statements.html">Top-Level Statements vs Main</a></li>
        </ul>
    </aside>
    
    <main class="main-content">
        <div class="topic-header">
            <h1>Advanced Types & AEIP Concepts</h1>
            <p class="metadata">Difficulty: Advanced | Category: C# Object-Oriented Programming</p>
        </div>

        <div class="callout callout-info">
            <span class="callout-title">Mental Model: AEIP</span>
            <p><strong>Abstraction, Encapsulation, Inheritance, and Polymorphism (AEIP)</strong> are the four pillars of Object-Oriented Programming. 
            <ul>
                <li><strong>Abstraction (Abstract Classes):</strong> A half-finished blueprint. Like a car chassis. You can't drive it, but it provides the engine and wheels for other cars to build upon.</li>
                <li><strong>Polymorphism (Interfaces):</strong> A strict legal contract. Like a wall socket. The socket doesn't care if you plug in a TV or a Fridge, as long as it has exactly two prongs.</li>
                <li><strong>Inheritance (Sealed Classes):</strong> Passing traits to children. A Sealed class is the end of the bloodline. It locks the vault so no children can alter it.</li>
            </ul></p>
        </div>

        <!-- NEW TABBED UI -->
        <div class="topic-tabs">
            <button class="topic-tab-btn active" onclick="switchTopicTab('tab-abstract')">1. Abstract Classes</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-interfaces')">2. Interfaces</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-sealed')">3. Sealed Classes</button>
            <button class="topic-tab-btn danger-tab" onclick="switchTopicTab('tab-catches')">⚠️ AEIP Catches</button>
        </div>

        <!-- TAB 1: ABSTRACT CLASSES -->
        <div id="tab-abstract" class="topic-tab-content active">
            <h2>Abstract Classes (The Shared Blueprint)</h2>
            <p>An abstract class is used when you want to write some real, shared code (like connecting to a database), but you want to force child classes to write their own specific logic for other methods. You <strong>cannot</strong> create a direct object of an abstract class.</p>
            
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Abstract Classes</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Types
{
    /// &lt;summary&gt;
    /// The base blueprint. Cannot be instantiated directly using 'new'.
    /// &lt;/summary&gt;
    public abstract class BaseReport
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// A concrete method. All children inherit this exactly as it is.
        /// &lt;/summary&gt;
        public void PrintHeader()
        {
            Console.WriteLine("--- ACME CORP OFFICIAL REPORT ---");
        }
        
        /// &lt;summary&gt;
        /// An abstract method. It has NO body. Every child MUST write their own version.
        /// &lt;/summary&gt;
        public abstract void GenerateContent();
        #endregion
    }

    /// &lt;summary&gt;
    /// A concrete child class that inherits the abstract class.
    /// &lt;/summary&gt;
    public class FinancialReport : BaseReport
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// The 'override' keyword is legally required to fulfill the abstract method.
        /// &lt;/summary&gt;
        public override void GenerateContent()
        {
            Console.WriteLine("Generating Q3 Financial Data: Revenue up 20%.");
        }
        #endregion
    }

    /// &lt;summary&gt;
    /// The main execution program.
    /// &lt;/summary&gt;
    class Program
    {
        #region Public Methods
        static void Main()
        {
            // CATCH: BaseReport report = new BaseReport(); // This causes a compiler crash!
            
            FinancialReport financeData = new FinancialReport();
            financeData.PrintHeader();   // Inherited from Abstract parent
            financeData.GenerateContent(); // Executed from Child
        }
        #endregion
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>--- ACME CORP OFFICIAL REPORT ---
Generating Q3 Financial Data: Revenue up 20%.</pre></div>
        </div>

        <!-- TAB 2: INTERFACES -->
        <div id="tab-interfaces" class="topic-tab-content">
            <h2>Interfaces (The Strict Contract)</h2>
            <p>An Interface is pure Abstraction. It contains <strong>zero</strong> real code (traditionally). It is simply a list of method names. Any class that signs this contract <strong>must</strong> implement every single method exactly as written. Interfaces are the backbone of modern C# Architecture (Dependency Injection).</p>
            
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Interfaces</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Types
{
    /// &lt;summary&gt;
    /// The contract. Standard naming convention requires an 'I' prefix.
    /// &lt;/summary&gt;
    public interface IPaymentProcessor
    {
        // Notice there are no access modifiers (public/private) and no body {}.
        void ProcessPayment(double amount);
    }

    /// &lt;summary&gt;
    /// Class signing the contract. It MUST include ProcessPayment.
    /// &lt;/summary&gt;
    public class PayPalProcessor : IPaymentProcessor
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// Implementing the interface method.
        /// &lt;/summary&gt;
        public void ProcessPayment(double amount)
        {
            Console.WriteLine($"Routing ${amount} securely through PayPal API...");
        }
        #endregion
    }
    
    /// &lt;summary&gt;
    /// Another class signing the exact same contract.
    /// &lt;/summary&gt;
    public class StripeProcessor : IPaymentProcessor
    {
        #region Public Methods
        public void ProcessPayment(double amount)
        {
            Console.WriteLine($"Routing ${amount} securely through Stripe API...");
        }
        #endregion
    }

    /// &lt;summary&gt;
    /// The main execution program demonstrating Polymorphism.
    /// &lt;/summary&gt;
    class Program
    {
        #region Public Methods
        static void Main()
        {
            // POLYMORPHISM IN ACTION: 
            // We use the Interface type as the variable, but inject the specific class!
            IPaymentProcessor currentProcessor = new StripeProcessor();
            
            // The program doesn't care which processor it is, because the Interface 
            // guarantees that ProcessPayment() exists!
            currentProcessor.ProcessPayment(99.50);
        }
        #endregion
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>Routing $99.5 securely through Stripe API...</pre></div>
        </div>

        <!-- TAB 3: SEALED CLASSES -->
        <div id="tab-sealed" class="topic-tab-content">
            <h2>Sealed Classes (Ending Inheritance)</h2>
            <p>Sometimes Inheritance is dangerous. If you write a highly secure class (like a password hasher), you don't want a junior developer creating a child class and accidentally overriding your security checks. You use the <code>sealed</code> keyword to lock it down permanently.</p>
            
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Sealed Classes</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Types
{
    /// &lt;summary&gt;
    /// A locked class. No other class can inherit from this.
    /// &lt;/summary&gt;
    public sealed class SecurityConfig
    {
        #region Public Properties
        public string EncryptionKey { get; set; } = "SUPER_SECRET_KEY_123";
        #endregion
        
        #region Public Methods
        public void AuthenticateSystem()
        {
            Console.WriteLine("System authenticated using core security protocols.");
        }
        #endregion
    }

    // CATCH: The below code would cause a fatal compiler error!
    // public class HackSecurity : SecurityConfig 
    // { 
    //      Cannot inherit from sealed class 'SecurityConfig'
    // }

    /// &lt;summary&gt;
    /// The main execution program.
    /// &lt;/summary&gt;
    class Program
    {
        #region Public Methods
        static void Main()
        {
            // You can still instantiate and use a sealed class normally.
            SecurityConfig config = new SecurityConfig();
            config.AuthenticateSystem();
        }
        #endregion
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>System authenticated using core security protocols.</pre></div>
        </div>

        <!-- TAB 4: AEIP CATCHES (EDGE CASES) -->
        <div id="tab-catches" class="topic-tab-content">
            <h2>⚠️ AEIP Master Catch List</h2>
            <p>These are the absolute most common traps, crashes, and compiler errors developers face when working with advanced OOP concepts in C#.</p>
            
            <ul class="catch-list">
                <li class="catch-item">
                    <h3>1. The Multiple Inheritance Death Trap</h3>
                    <p><strong>The Catch:</strong> A C# class can <strong>only inherit from ONE parent class</strong>. You absolutely cannot write <code>class Car : Vehicle, Machine</code>. This is called the "Diamond Problem" and C# blocks it to prevent memory corruption.<br><br><strong>The Fix:</strong> A class can inherit from ONE class, but it can sign <strong>UNLIMITED</strong> interfaces. (e.g., <code>class Car : Vehicle, IDriveable, IRefuelable</code>).</p>
                </li>
                
                <li class="catch-item">
                    <h3>2. The Virtual vs. Abstract Confusion</h3>
                    <p><strong>The Catch:</strong> Developers often mix these up. 
                    <br><br>If a method is <code>virtual</code>, it <strong>has real code inside it</strong>, but you are <em>allowed</em> to override it if you want. 
                    <br><br>If a method is <code>abstract</code>, it is completely empty and you are <strong>legally forced</strong> to override it, otherwise your app will not compile.</p>
                </li>
                
                <li class="catch-item">
                    <h3>3. Instantiating the Blueprint</h3>
                    <p><strong>The Catch:</strong> You can never write <code>new ILogger()</code> or <code>new BaseReport()</code>. Interfaces and Abstract classes are just blueprints. You can only use <code>new</code> on a <strong>Concrete</strong> class that actually finished the blueprint.</p>
                </li>
                
                <li class="catch-item">
                    <h3>4. Interface Access Modifier Trap</h3>
                    <p><strong>The Catch:</strong> Methods inside an interface are implicitly <code>public</code>. In older versions of C#, if you wrote <code>public void Process()</code> inside an interface, the compiler would crash and say "modifier 'public' is not valid for this item". (C# 8+ allows it, but it is considered bad practice. Just write <code>void Process();</code>).</p>
                </li>
                
                <li class="catch-item">
                    <h3>5. The Sealed Performance Secret</h3>
                    <p><strong>The Catch:</strong> Most developers think <code>sealed</code> is only for security. In reality, it is also for <strong>Performance</strong>. When you mark a class as <code>sealed</code>, the .NET compiler runs special optimizations because it knows absolutely zero children will try to override its methods. If you know a class won't have children, seal it!</p>
                </li>
            </ul>
        </div>

        <div class="nav-buttons">
            <a href="09-file-operations.html">&larr; Previous: File Operations</a>
            <a href="#">Next: Generics &rarr;</a>
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
link_to_add = '\n            <li><a href="10-advanced-types.html">10. Types (AEIP)</a></li>'

for fpath in html_files:
    if '10-advanced-types.html' in fpath:
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if '10-advanced-types.html' in content:
        continue
    
    target_active = '<li><a href="09-file-operations.html" class="active">9. File Operations</a></li>'
    target_inactive = '<li><a href="09-file-operations.html">9. File Operations</a></li>'
    
    if target_active in content:
        content = content.replace(target_active, target_active + link_to_add)
    elif target_inactive in content:
        content = content.replace(target_inactive, target_inactive + link_to_add)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

