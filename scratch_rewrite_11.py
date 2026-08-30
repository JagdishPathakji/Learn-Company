import os

filepath = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\11-generics.html'

new_main = r'''
    <main class="main-content">
        <div class="topic-header">
            <h1>Generics & The Collections Framework</h1>
            <p class="metadata">Difficulty: Advanced | Category: C# Object-Oriented Programming</p>
        </div>

        <div class="callout callout-info">
            <span class="callout-title">Why Generics?</span>
            <p>Generics (<code>&lt;T&gt;</code>) allow you to write a class or method once, and use it securely with any data type. More importantly, Generics power the <strong>System.Collections.Generic</strong> namespace, which completely replaced the old, slow non-generic collections (like <code>ArrayList</code>) by eliminating the performance-killing process known as Boxing and Unboxing.</p>
        </div>

        <div class="topic-tabs">
            <button class="topic-tab-btn active" onclick="switchTopicTab('tab-classes')">1. Generic Classes & Methods</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-interfaces')">2. Collection Interfaces</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-concrete1')">3. Lists & Dictionaries</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-concrete2')">4. Sets, Stacks & Queues</button>
        </div>

        <!-- TAB 1: GENERIC CLASSES & METHODS -->
        <div id="tab-classes" class="topic-tab-content active">
            <h2>Generic Classes, Methods, and Constraints</h2>
            <p>You can create your own Generic classes and methods using the <code>&lt;T&gt;</code> placeholder. To prevent developers from passing in invalid types, you use the <code>where</code> keyword to enforce strict constraints.</p>
            
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Classes & Methods</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;

namespace KnowledgeBase.Generics
{
    public interface IEntity { int Id { get; } }

    public class Article : IEntity
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public Article(int id, string title) { Id = id; Title = title; }
    }

    // 1. GENERIC CLASS WITH CONSTRAINT
    // The class only accepts types that implement IEntity
    public class ChangeTracker&lt;T&gt; where T : IEntity 
    {
        private T entity;
        public ChangeTracker(T entity) { this.entity = entity; }

        public void Track() 
        {
            // We can safely access .Id because the constraint guarantees it exists!
            Console.WriteLine($"Tracking changes for Entity ID: {entity.Id}");
        }
    }

    class KnowledgeBaseDB
    {
        // 2. GENERIC METHOD
        // The method itself is generic, allowing it to search any list of IEntities
        public T FindById&lt;T&gt;(List&lt;T&gt; items, int id) where T : IEntity
        {
            foreach (T item in items)
            {
                if (item.Id == id) return item;
            }
            
            // 'default' returns null for classes, or 0 for numeric structs.
            return default; 
        }
    }

    class Program
    {
        static void Main()
        {
            Article article = new Article(101, "Generics in C#");
            
            ChangeTracker&lt;Article&gt; tracker = new ChangeTracker&lt;Article&gt;(article);
            tracker.Track();
        }
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>Tracking changes for Entity ID: 101</pre></div>
        </div>

        <!-- TAB 2: COLLECTION INTERFACES -->
        <div id="tab-interfaces" class="topic-tab-content">
            <h2>The Generic Collection Interfaces</h2>
            <p>The C# Collections framework is built on a strict hierarchy of interfaces. Understanding these interfaces is critical to understanding what each collection is capable of.</p>
            
            <ul class="catch-list">
                <li class="catch-item" style="background:#e0f2fe; border-left-color:#0ea5e9; color:#0369a1;">
                    <h3 style="color:#075985;">1. IEnumerable&lt;T&gt; (The Grandparent)</h3>
                    <p>The absolute base. If a collection implements this, it simply means <em>"You can use a foreach loop on me."</em> It does not guarantee you can add or remove items, only that you can read them one by one.</p>
                </li>
                
                <li class="catch-item" style="background:#e0f2fe; border-left-color:#0ea5e9; color:#0369a1;">
                    <h3 style="color:#075985;">2. ICollection&lt;T&gt; (The Parent)</h3>
                    <p>Inherits from IEnumerable. If a class implements this, it promises: <em>"You can Add(), Remove(), and check my Count."</em> But it does <strong>not</strong> guarantee any specific order or index.</p>
                </li>
                
                <li class="catch-item" style="background:#fef08a; border-left-color:#eab308; color:#854d0e;">
                    <h3 style="color:#713f12;">3. IList&lt;T&gt; (The Indexed Array)</h3>
                    <p>Inherits from ICollection. It promises: <em>"I keep items in a specific order. You can use an index <code>[0]</code> to access them, <code>Insert()</code> into the middle, and <code>RemoveAt()</code>."</em></p>
                </li>
                
                <li class="catch-item" style="background:#fef08a; border-left-color:#eab308; color:#854d0e;">
                    <h3 style="color:#713f12;">4. IDictionary&lt;TKey, TValue&gt; (The Key Mapper)</h3>
                    <p>Promises: <em>"I map unique keys to values. You can instantly look up data using my key indexer <code>dict["user123"]</code>, check <code>ContainsKey()</code>, or grab just my <code>.Keys</code> or <code>.Values</code>."</em></p>
                </li>
                
                <li class="catch-item" style="background:#fef08a; border-left-color:#eab308; color:#854d0e;">
                    <h3 style="color:#713f12;">5. ISet&lt;T&gt; (The Unique Bag)</h3>
                    <p>Promises: <em>"I absolutely will not allow duplicates. I have no order and no index. I am optimized for blazing fast <code>Contains()</code> checks and math operations like <code>IntersectWith()</code>."</em></p>
                </li>
            </ul>
        </div>

        <!-- TAB 3: LISTS & DICTIONARIES -->
        <div id="tab-concrete1" class="topic-tab-content">
            <h2>Concrete Collections: Lists & Dictionaries</h2>
            <p>These are the physical classes you instantiate using the <code>new</code> keyword to actually store your data.</p>
            
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Lists and Dictionaries</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;

namespace KnowledgeBase.Generics
{
    class Program
    {
        static void Main()
        {
            // ==========================================
            // 1. LIST<T> (Implements IList)
            // ==========================================
            Console.WriteLine("--- LIST DEMO ---");
            List&lt;string&gt; fruits = new List&lt;string&gt;();

            fruits.Add("Apple");                          
            fruits.AddRange(new string[] { "Banana", "Cherry" }); 
            fruits.Insert(0, "Mango"); // Pushes everything down
            
            fruits.RemoveAt(1); // Removes "Apple"
            fruits.Sort();      // Alphabetical sort

            Console.WriteLine($"Contains Mango? {fruits.Contains("Mango")}");
            Console.WriteLine($"Item at index 0: {fruits[0]}\n");

            // ==========================================
            // 2. DICTIONARY<TKey, TValue> (Implements IDictionary)
            // ==========================================
            Console.WriteLine("--- DICTIONARY DEMO ---");
            Dictionary&lt;int, string&gt; employees = new Dictionary&lt;int, string&gt;();

            employees.Add(101, "Alice");                  
            employees.TryAdd(101, "Bob"); // Safe add (ignores if 101 exists)
            employees[102] = "Charlie";   // Adds or Overwrites
            
            // Safe reading (Outputs to 'name', returns false if missing)
            if (employees.TryGetValue(102, out string name))
            {
                Console.WriteLine($"Found employee 102: {name}");
            }

            // ==========================================
            // 3. SORTED DICTIONARY (Auto-sorts by Key)
            // ==========================================
            Console.WriteLine("\n--- SORTED DICTIONARY DEMO ---");
            SortedDictionary&lt;string, int&gt; scores = new SortedDictionary&lt;string, int&gt;();

            scores.Add("Charlie", 85);
            scores.Add("Alice", 95);

            // Automatically prints Alice first because it sorts by Key alphabetically!
            foreach (KeyValuePair&lt;string, int&gt; entry in scores)
            {
                Console.WriteLine($"{entry.Key} scored {entry.Value}");
            }
        }
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>--- LIST DEMO ---
Contains Mango? True
Item at index 0: Banana

--- DICTIONARY DEMO ---
Found employee 102: Charlie

--- SORTED DICTIONARY DEMO ---
Alice scored 95
Charlie scored 85</pre></div>
        </div>

        <!-- TAB 4: SETS, STACKS, QUEUES -->
        <div id="tab-concrete2" class="topic-tab-content">
            <h2>Sets, Stacks, and Queues</h2>
            <p>These specialized collections are built for extreme performance in specific scenarios (uniqueness, LIFO, and FIFO).</p>
            
            <div class="callout callout-danger">
                <span class="callout-title">The Engineering Behind Sets</span>
                <p><strong>HashSet Engine:</strong> When you add an item, C# generates a mathematical <em>Hash Code</em>, divides it by the bucket count, and drops it straight into a specific memory bucket. When searching, it uses the exact same math to jump directly to that bucket in <code>O(1)</code> time, completely ignoring the rest of the list!</p>
                <p><strong>SortedSet Engine:</strong> Uses a <em>Red-Black Tree</em>. It starts at a Root node. If your new item is smaller, it goes down the Left branch; if larger, it goes Right. It automatically rotates branches to keep the tree perfectly balanced. Searching follows the same Left/Right logic, eliminating half the data every step.</p>
            </div>

            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Advanced Collections</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;

namespace KnowledgeBase.Generics
{
    class Program
    {
        static void Main()
        {
            // ==========================================
            // 1. HASHSET<T> (Implements ISet)
            // ==========================================
            Console.WriteLine("--- HASHSET DEMO ---");
            HashSet&lt;int&gt; activeUsers = new HashSet&lt;int&gt;();

            activeUsers.Add(1);
            activeUsers.Add(2);
            bool addedAgain = activeUsers.Add(1); // Returns false, duplicate ignored!

            HashSet&lt;int&gt; premiumUsers = new HashSet&lt;int&gt; { 1, 3, 5 };
            
            // Math Set Operation: ONLY keeps numbers that are in BOTH sets (User 1)
            activeUsers.IntersectWith(premiumUsers); 

            Console.WriteLine($"Was duplicate added? {addedAgain}");
            Console.WriteLine($"Is User 1 still active? {activeUsers.Contains(1)}\n");

            // ==========================================
            // 2. SORTED SET<T> (Implements ISet, auto-sorts)
            // ==========================================
            Console.WriteLine("--- SORTED SET DEMO ---");
            SortedSet&lt;int&gt; ages = new SortedSet&lt;int&gt;();

            ages.Add(50);
            ages.Add(10);
            ages.Add(99);

            Console.WriteLine($"Youngest (Min): {ages.Min} | Oldest (Max): {ages.Max}\n");

            // ==========================================
            // 3. STACK<T> (Last-In, First-Out - LIFO)
            // ==========================================
            Console.WriteLine("--- STACK DEMO (LIFO) ---");
            Stack&lt;string&gt; history = new Stack&lt;string&gt;();

            history.Push("Page 1");
            history.Push("Page 2"); // Page 2 is now on top
            
            Console.WriteLine($"Popping top item (Undo): {history.Pop()}");
            Console.WriteLine($"Now on top: {history.Peek()}\n");

            // ==========================================
            // 4. QUEUE<T> (First-In, First-Out - FIFO)
            // ==========================================
            Console.WriteLine("--- QUEUE DEMO (FIFO) ---");
            Queue&lt;string&gt; printerLine = new Queue&lt;string&gt;();

            printerLine.Enqueue("Doc1.pdf"); // Goes to the front
            printerLine.Enqueue("Image.png"); // Goes to the back

            Console.WriteLine($"Dequeuing front item (Print): {printerLine.Dequeue()}");
            Console.WriteLine($"Now at front: {printerLine.Peek()}");
        }
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>--- HASHSET DEMO ---
Was duplicate added? False
Is User 1 still active? True

--- SORTED SET DEMO ---
Youngest (Min): 10 | Oldest (Max): 99

--- STACK DEMO (LIFO) ---
Popping top item (Undo): Page 2
Now on top: Page 1

--- QUEUE DEMO (FIFO) ---
Dequeuing front item (Print): Doc1.pdf
Now at front: Image.png</pre></div>
        </div>

        <div class="nav-buttons">
            <a href="10-advanced-types.html">&larr; Previous: Types (AEIP)</a>
            <a href="#">Next: File System (Advanced) &rarr;</a>
        </div>
    </main>
'''

if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('<main class="main-content">')
    end_idx = content.find('</main>')
    
    if start_idx != -1 and end_idx != -1:
        end_idx += len('</main>')
        new_content = content[:start_idx] + new_main + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
