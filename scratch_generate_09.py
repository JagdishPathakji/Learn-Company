import os
import glob

base_dir = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp'
filepath = os.path.join(base_dir, '09-file-operations.html')

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>File Operations</title>
    <link rel="stylesheet" href="../../css/global.css">
    <style>
        .arch-diagram { display: flex; flex-direction: column; gap: 20px; background: #1e293b; padding: 40px; border-radius: 8px; margin: 30px 0; color: #fff; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        .arch-phase { border: 2px dashed #64748b; padding: 25px; border-radius: 8px; background: #0f172a; position: relative; }
        .arch-phase-title { font-size: 1.2rem; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px; border-bottom: 1px solid #334155; padding-bottom: 10px; }
        
        .exception-table { width: 100%; border-collapse: collapse; margin-top: 20px; margin-bottom: 30px; font-size: 0.95rem; }
        .exception-table th { background: #3b82f6; color: white; padding: 12px; text-align: left; }
        .exception-table td { background: #1e293b; color: #cbd5e1; padding: 12px; border-bottom: 1px solid #334155; }
        .exception-table td strong { color: #f87171; }
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
            <li><a href="09-file-operations.html" class="active">9. File Operations</a></li>
        </ul>
        <div class="sidebar-category">Deep Dives (Custom)</div>
        <ul>
            <li><a href="custom-01-top-level-statements.html">Top-Level Statements vs Main</a></li>
        </ul>
    </aside>
    
    <main class="main-content">
        <div class="topic-header">
            <h1>File & Directory Operations (System.IO)</h1>
            <p class="metadata">Difficulty: Intermediate | Category: C# Base Libraries</p>
        </div>

        <div class="callout callout-info">
            <span class="callout-title">Mental Model</span>
            <p>Think of your C# program as a busy factory (your RAM), and your computer's hard drive as a massive warehouse. The <code>File</code> and <code>Directory</code> static classes are the forklift drivers. Their entire job is to carry finished data from the factory and drop it into a box in the warehouse, or fetch an existing box from the warehouse and bring it into the factory to be processed.</p>
        </div>

        <h2>A. The Golden Rule of File Operations</h2>
        <p>Before doing <strong>anything</strong> with files, you must add <code>using System.IO;</code> at the top of your file. "I/O" stands for Input/Output. Furthermore, interacting with the hard drive is the <strong>most common cause of crashes</strong> in any application. Files get locked, folders get deleted by users, and hard drives run out of space. You must understand <em>exactly</em> what exceptions can be thrown.</p>

        <h3>COMPLETE EXAMPLE 1: Reading, Writing, and Appending</h3>
        <p>We use the <code>File</code> class to manipulate data inside a file. This example covers overwriting, adding to the bottom (appending), and reading lines back into memory.</p>
        
        <div class="code-container" style="border-radius: 6px 6px 0 0;">
            <div class="code-header"><span>C# - File Content Management</span><button class="copy-btn">Copy</button></div>
            <pre><code class="language-csharp">using System;
using System.IO; // Required for File and Directory classes!

namespace KnowledgeBase.FileIO
{
    /// &lt;summary&gt;
    /// Demonstrates overwriting, appending, and reading file contents.
    /// &lt;/summary&gt;
    public class TextFileHandler
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// Creates a log file, appends new entries, and reads them back.
        /// &lt;/summary&gt;
        public void ProcessLogs()
        {
            // If we don't provide a folder like "C:\", this saves directly 
            // inside the bin/Debug folder next to your .exe file!
            string logFilePath = "application_logs.txt";
            
            // 1. OVERWRITE (WriteAllText)
            // If the file doesn't exist, this creates it. 
            // If it DOES exist, this wipes out all existing text and replaces it!
            // EXCEPTION: Throws DirectoryNotFoundException if the parent folder doesn't exist.
            File.WriteAllText(logFilePath, "--- SYSTEM START ---\n");
            
            // 2. APPEND (AppendAllText)
            // This safely adds text to the very bottom without destroying the old data.
            File.AppendAllText(logFilePath, "User Admin logged in.\n");
            File.AppendAllText(logFilePath, "Database connection successful.\n");
            
            // 3. READ (ReadAllLines)
            // ALWAYS check if the file exists before reading to prevent a massive crash.
            if (File.Exists(logFilePath))
            {
                // ReadAllLines reads the file and perfectly splits each line into an array
                string[] allLines = File.ReadAllLines(logFilePath);
                
                Console.WriteLine($"Total Log Entries Found: {allLines.Length}");
                Console.WriteLine($"Last Log Entry: {allLines[allLines.Length - 1]}");
            }
        }
        #endregion
    }

    /// &lt;summary&gt;
    /// The main execution program.
    /// &lt;/summary&gt;
    class Program
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// The main entry point of the program.
        /// &lt;/summary&gt;
        static void Main()
        {
            TextFileHandler handler = new TextFileHandler();
            handler.ProcessLogs();
        }
        #endregion
    }
}</code></pre>
        </div>
        <div class="console-output"><strong>Console Output:</strong><pre>Total Log Entries Found: 3
Last Log Entry: Database connection successful.</pre></div>

        <h3>COMPLETE EXAMPLE 2: Copy, Move, and Delete (File Management)</h3>
        <p>Sometimes you don't care about what is <em>inside</em> the file; you just want to manage the file itself (renaming, backing up, or destroying it).</p>
        
        <div class="code-container" style="border-radius: 6px 6px 0 0;">
            <div class="code-header"><span>C# - File Relocation and Deletion</span><button class="copy-btn">Copy</button></div>
            <pre><code class="language-csharp">using System;
using System.IO;

namespace KnowledgeBase.FileIO
{
    /// &lt;summary&gt;
    /// Demonstrates how to copy, move, and safely delete files.
    /// &lt;/summary&gt;
    public class BackupManager
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// Backs up a report and cleans up old files.
        /// &lt;/summary&gt;
        public void ManageBackups()
        {
            string sourceFile = "financial_report.txt";
            string backupFile = "financial_report_backup.txt";
            string archiveFile = "archive_report.txt";
            
            // Create a dummy file so our code has something to work with
            File.WriteAllText(sourceFile, "Confidential Revenue Data");
            
            // 1. COPY (Source, Destination, Overwrite Flag)
            // The 'true' flag means if the backup file already exists, overwrite it.
            // EXCEPTION: If we passed 'false' and the file existed, it would throw an IOException.
            File.Copy(sourceFile, backupFile, true);
            
            // 2. MOVE (Rename / Relocate)
            // Move deletes the original file and creates it at the new destination.
            // EXCEPTION: Throws IOException if the destination file already exists!
            if (!File.Exists(archiveFile))
            {
                File.Move(sourceFile, archiveFile);
            }
            
            // 3. DELETE
            // Safely destroys a file. 
            // NOTE: If the file doesn't exist, File.Delete does NOT crash! It just ignores you.
            File.Delete(backupFile);
            
            Console.WriteLine($"Does Original Exist? {File.Exists(sourceFile)}");
            Console.WriteLine($"Does Archive Exist? {File.Exists(archiveFile)}");
            Console.WriteLine($"Does Backup Exist? {File.Exists(backupFile)}");
        }
        #endregion
    }

    /// &lt;summary&gt;
    /// The main execution program.
    /// &lt;/summary&gt;
    class Program
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// The main entry point of the program.
        /// &lt;/summary&gt;
        static void Main()
        {
            BackupManager manager = new BackupManager();
            manager.ManageBackups();
        }
        #endregion
    }
}</code></pre>
        </div>
        <div class="console-output"><strong>Console Output:</strong><pre>Does Original Exist? False
Does Archive Exist? True
Does Backup Exist? False</pre></div>

        <h3>COMPLETE EXAMPLE 3: Directory (Folder) Operations</h3>
        <p>Before you can write a file to a specific path (like <code>Reports/Q1/data.txt</code>), the folders <em>must</em> exist. If they don't, C# will crash.</p>
        
        <div class="code-container" style="border-radius: 6px 6px 0 0;">
            <div class="code-header"><span>C# - Directory Management</span><button class="copy-btn">Copy</button></div>
            <pre><code class="language-csharp">using System;
using System.IO;

namespace KnowledgeBase.FileIO
{
    /// &lt;summary&gt;
    /// Demonstrates creating directories and querying their contents.
    /// &lt;/summary&gt;
    public class FolderManager
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// Creates a folder, populates it, and lists the contents.
        /// &lt;/summary&gt;
        public void ProcessFolders()
        {
            string folderPath = "UserUploads";
            
            // 1. CREATE DIRECTORY
            // Safe to call even if the folder exists (it won't crash, it just skips).
            // It will also build multi-level folders instantly (e.g., "FolderA/FolderB/FolderC").
            Directory.CreateDirectory(folderPath);
            
            // Put some dummy files inside the new folder
            File.WriteAllText(folderPath + "/image1.png", "fake image data");
            File.WriteAllText(folderPath + "/image2.png", "fake image data");
            
            // 2. GET FILES
            // Returns an array of strings representing the full paths of every file inside the folder.
            string[] uploadedFiles = Directory.GetFiles(folderPath);
            
            Console.WriteLine($"Total Files in '{folderPath}': {uploadedFiles.Length}");
            
            // 3. DELETE DIRECTORY (Path, Recursive Flag)
            // The 'true' flag is CRITICAL. It means "delete the folder AND everything inside it".
            // EXCEPTION: If you pass 'false' and the folder is not completely empty, it throws an IOException.
            Directory.Delete(folderPath, true);
            
            Console.WriteLine($"Folder Deleted? {!Directory.Exists(folderPath)}");
        }
        #endregion
    }

    /// &lt;summary&gt;
    /// The main execution program.
    /// &lt;/summary&gt;
    class Program
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// The main entry point of the program.
        /// &lt;/summary&gt;
        static void Main()
        {
            FolderManager manager = new FolderManager();
            manager.ProcessFolders();
        }
        #endregion
    }
}</code></pre>
        </div>
        <div class="console-output"><strong>Console Output:</strong><pre>Total Files in 'UserUploads': 2
Folder Deleted? True</pre></div>

        <h2>B. The Exception Master Cheat Sheet</h2>
        <p>Because the hard drive is completely outside the control of your C# application, things will go wrong. Another program might have the file open, a user might have deleted the folder, or Windows might block your access. Here is exactly what crashes and why:</p>
        
        <table class="exception-table">
            <thead>
                <tr>
                    <th>Exception Name</th>
                    <th>Functions That Throw It</th>
                    <th>Exact Cause (Why it crashed)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>FileNotFoundException</strong></td>
                    <td><code>File.ReadAllText</code><br><code>File.ReadAllLines</code><br><code>File.Copy</code><br><code>File.Move</code></td>
                    <td>You told C# to read, copy, or move a file that literally does not exist on the hard drive. <em>Always use <code>File.Exists()</code> first!</em></td>
                </tr>
                <tr>
                    <td><strong>DirectoryNotFoundException</strong></td>
                    <td><code>File.WriteAllText</code><br><code>File.AppendAllText</code></td>
                    <td>You tried to write a file into a folder (e.g. <code>Reports/data.txt</code>) but the "Reports" folder hasn't been created yet. You must use <code>Directory.CreateDirectory()</code> first.</td>
                </tr>
                <tr>
                    <td><strong>IOException</strong></td>
                    <td><code>File.Copy</code><br><code>File.Move</code><br><code>Directory.Delete</code></td>
                    <td>
                        1. You tried to <strong>Move</strong> a file, but a file with that name already exists at the destination.<br>
                        2. You tried to <strong>Delete a folder</strong> that isn't empty, and forgot to pass the <code>true</code> recursive flag.<br>
                        3. <strong>File In Use:</strong> You tried to edit a text file, but the user currently has it open in Microsoft Excel or Notepad.
                    </td>
                </tr>
                <tr>
                    <td><strong>UnauthorizedAccessException</strong></td>
                    <td><code>File.WriteAllText</code><br><code>File.Delete</code></td>
                    <td>
                        1. The file was right-clicked in Windows and set to <strong>"Read-Only"</strong>.<br>
                        2. You tried to save a file in a restricted System folder (like <code>C:\Windows\</code>) without running your app as an Administrator.
                    </td>
                </tr>
            </tbody>
        </table>

        <div class="nav-buttons">
            <a href="08-date-string-math.html">&larr; Previous: Date/String/Math</a>
            <a href="#">Next: Types (Advanced) &rarr;</a>
        </div>
    </main>
    
    <script src="../../js/ui-enhancements.js"></script>

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
                
                // Parse markdown to HTML
                prev.innerHTML = marked.parse(ta.value);
                
                // Apply Prism.js syntax highlighting to the newly parsed code blocks!
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

        // Auto-save logic
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
        // Persist sidebar state across page loads
        if(localStorage.getItem('kb_sidebar_collapsed') === 'true') {
            document.body.classList.add('sidebar-collapsed');
        }
    </script>

    <!-- Draggable Notes Button Script -->
    <script>
        const dragBtn = document.querySelector('.notes-toggle-btn');
        let isDragging = false;
        window.hasDragged = false; // Global flag to prevent click after drag
        let offsetX, offsetY;

        // Load saved position from localStorage
        const savedX = localStorage.getItem('kb_notes_btn_x');
        const savedY = localStorage.getItem('kb_notes_btn_y');
        if (savedX && savedY) {
            dragBtn.style.left = savedX + 'px';
            dragBtn.style.top = savedY + 'px';
            dragBtn.style.bottom = 'auto'; // override default CSS bottom
            dragBtn.style.right = 'auto';  // override default CSS right
        }

        dragBtn.addEventListener('mousedown', (e) => {
            isDragging = true;
            window.hasDragged = false; // Reset drag flag
            offsetX = e.clientX - dragBtn.getBoundingClientRect().left;
            offsetY = e.clientY - dragBtn.getBoundingClientRect().top;
            dragBtn.style.cursor = 'grabbing';
        });

        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            window.hasDragged = true; // User is moving the mouse, so it's a drag
            
            let newX = e.clientX - offsetX;
            let newY = e.clientY - offsetY;
            
            // Prevent dragging off screen
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
                // Save position for next page load
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

# Update the sidebars in all other files
html_files = glob.glob(os.path.join(base_dir, '*.html'))
link_to_add = '\n            <li><a href="09-file-operations.html">9. File Operations</a></li>'

for fpath in html_files:
    if '09-file-operations.html' in fpath:
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if '09-file-operations.html' in content:
        continue
    
    target_active = '<li><a href="08-date-string-math.html" class="active">8. Date/String/Math</a></li>'
    target_inactive = '<li><a href="08-date-string-math.html">8. Date/String/Math</a></li>'
    
    if target_active in content:
        content = content.replace(target_active, target_active + link_to_add)
    elif target_inactive in content:
        content = content.replace(target_inactive, target_inactive + link_to_add)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

