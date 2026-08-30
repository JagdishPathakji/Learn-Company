import os
import re

filepath = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\11-generics.html'

new_main = r'''
    <main class="main-content">
        <div class="topic-header">
            <h1>Generics & The Collections Framework</h1>
            <p class="metadata">Difficulty: Advanced | Category: C# Object-Oriented Programming</p>
        </div>

        <div class="callout callout-info">
            <span class="callout-title">Why Generics?</span>
            <p>Generics (<code>&lt;T&gt;</code>) allow you to write a class or method once, and use it securely with any data type. More importantly, Generics power the <strong>System.Collections.Generic</strong> namespace, which completely replaced the old, slow non-generic collections by eliminating Boxing and Unboxing.</p>
        </div>

        <div class="topic-tabs">
            <button class="topic-tab-btn active" onclick="switchTopicTab('tab-basics')">1. Generic Classes & Methods</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-interfaces')">2. Collection Interfaces (Deep Dive)</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-concrete')">3. Concrete Collections</button>
            <button class="topic-tab-btn danger-tab" onclick="switchTopicTab('tab-engine')">4. Collection Engines & Rules</button>
        </div>

        <!-- TAB 1: GENERIC CLASSES & METHODS -->
        <div id="tab-basics" class="topic-tab-content active">
            <h2>Generic Classes, Methods, and Constraints</h2>
            
            <h3>Generic Classes</h3>
            <p>You can create a class that works with any data type, while still enforcing constraints.</p>
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Generic Classes</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;

public interface IEntity {
    Guid Id { get; }
}

public class Article : IEntity {
    public Guid Id { get; set; }
    public string Title { get; set; }
    public Article(Guid id, string title) { Id = id; Title = title; }
}

public class ArticleVersion : IEntity {
    public Guid Id { get; set; }
    public int VersionNumber { get; set; }
    public ArticleVersion(Guid id, int versionNumber) { Id = id; VersionNumber = versionNumber; }
}

// Constraint: T MUST implement IEntity
public class ChangeTracker&lt;T&gt; where T : IEntity {
    private T entity;
    public ChangeTracker(T entity) { this.entity = entity; }

    public void Track() {
        Console.WriteLine("Tracking entity: " + entity.Id);
    }
}

class Program {
    static void Main() {
        Article article = new Article(Guid.NewGuid(), "C# Interfaces");
        ArticleVersion version = new ArticleVersion(Guid.NewGuid(), 3);

        ChangeTracker&lt;Article&gt; articleTracker = new ChangeTracker&lt;Article&gt;(article);
        ChangeTracker&lt;ArticleVersion&gt; versionTracker = new ChangeTracker&lt;ArticleVersion&gt;(version);

        articleTracker.Track();
        versionTracker.Track();
    }
}</code></pre>
            </div>

            <h3>Generic Methods</h3>
            <p>You can make individual methods generic, even inside a non-generic class.</p>
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Generic Methods</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;

interface IEntity { int Id { get; } }

class Article : IEntity {
    public int Id { get; set; }
    public string Title { get; set; }
    public Article(int id, string title) { Id = id; Title = title; }
}

class KnowledgeBase {
    // Generic Method checking through a Generic Collection
    public T FindById&lt;T&gt;(List&lt;T&gt; items, int id) where T : IEntity {
        foreach (T item in items) {
            if (item.Id == id) {
                return item;
            }
        }
        return default; // returns null for reference types, 0 for value types
    }
}

class Program {
    static void Main() {
        List&lt;Article&gt; articles = new List&lt;Article&gt; {
            new Article(1, "C# Interfaces"),
            new Article(2, "C# Generics")
        };

        KnowledgeBase kb = new KnowledgeBase();
        Article article = kb.FindById(articles, 2);
        
        Console.WriteLine("Found: " + article.Title);
    }
}</code></pre>
            </div>
        </div>

        <!-- TAB 2: COLLECTION INTERFACES -->
        <div id="tab-interfaces" class="topic-tab-content">
            <h2>The Generic Collection Interfaces (Deep Dive)</h2>
            <p>The C# Collections framework is built on a strict hierarchy of interfaces. Here is the exact theory and implementation for each.</p>

            <h3>1. ICollection&lt;T&gt;</h3>
            <div class="callout callout-info">
                <span class="callout-title">Theory</span>
                <p>If a class implements ICollection&lt;T&gt;, it promises: <em>"You can Add(), Remove(), and check my Count."</em> It does <strong>not</strong> guarantee any specific order or index.</p>
            </div>
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;

class Program {
    public static void Main() {
        ICollection&lt;string&gt; shoppingCart = new List&lt;string&gt;();

        shoppingCart.Add("Milk");
        shoppingCart.Add("Eggs");
        shoppingCart.Add("Bread");
        
        Console.WriteLine($"Items in cart: {shoppingCart.Count}");

        if (shoppingCart.Contains("Eggs")) {
            shoppingCart.Remove("Eggs");
        }

        Console.WriteLine($"Items after removal: {shoppingCart.Count}");

        foreach (string item in shoppingCart) {
            Console.WriteLine(item);
        }

        // CATCH: still can't do this with ICollection!
        // string firstItem = shoppingCart[0];
    }
}</code></pre>
            </div>

            <br>
            <h3>2. IList&lt;T&gt;</h3>
            <div class="callout callout-info">
                <span class="callout-title">Theory</span>
                <p>IList&lt;T&gt; inherits from ICollection&lt;T&gt;. If a class implements IList&lt;T&gt;, it promises: <em>"I keep all items in a specific order, and you can access or change any item instantly if you know its index number."</em></p>
                <ul>
                    <li><code>[index]</code>: The indexer. Can access items via index.</li>
                    <li><code>.Insert(index,item)</code>: shoves a new item into a specific position pushing everything else down.</li>
                    <li><code>.RemoveAt(index)</code>: Deletes whatever is at that index.</li>
                    <li><code>.IndexOf(item)</code>: Searches for an item and tells you its exact index number or returns -1 if it is not there.</li>
                </ul>
            </div>
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;

class Program {
    public static void Main() {
        IList&lt;string&gt; topMovies = new List&lt;string&gt;();
        topMovies.Add("The Matrix");
        topMovies.Add("Inception");

        topMovies.Insert(0, "Jurassic Park");
        Console.WriteLine($"The number 1 movie is: {topMovies[0]}");

        topMovies[1] = "The Matrix Reloaded";
        topMovies.RemoveAt(2); // Removes "Inception"

        int index = topMovies.IndexOf("Jurassic Park");
        Console.WriteLine($"Jurassic Park is at index: {index}");        
    }
}</code></pre>
            </div>

            <br>
            <h3>3. IDictionary&lt;TKey, TValue&gt;</h3>
            <div class="callout callout-info">
                <span class="callout-title">Theory</span>
                <p>IDictionary&lt;TKey,TValue&gt; dictates how any key-value collection must act. If a class signs this contract, it promises: <em>"I map unique key to values and you can instantly look up a value if you give me its key."</em></p>
                <ul>
                    <li><code>[key]</code>: The key-based indexer (e.g., myDict["user123"]).</li>
                    <li><code>.Add(key, value)</code>: Adds a new pair.</li>
                    <li><code>.ContainsKey(key)</code>: Fast check to see if a key exists.</li>
                    <li><code>.Keys</code> and <code>.Values</code>: Lets you grab just the list of keys or just the list of values.</li>
                </ul>
            </div>
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;

class Program {
    public static void Main() {
        IDictionary&lt;string,string&gt; serverConfigs = new Dictionary&lt;string,string&gt;();

        serverConfigs.Add("Database", "192.168.1.10");
        serverConfigs.Add("Web", "192.168.1.20");
        serverConfigs["API"] = "192.168.1.30"; // Adds a new key
        serverConfigs["Web"] = "192.168.1.25"; // Overwrites the existing "Web" key

        if (serverConfigs.ContainsKey("Database")) {
            Console.WriteLine($"Database IP is: {serverConfigs["Database"]}");
        }

        // If you want to add or remove items, you must do it through the IDictionary itself. 
        // The collections returned by .Keys and .Values are strictly for looking at the data.
        ICollection&lt;string&gt; justTheKeys = serverConfigs.Keys;
        Console.WriteLine("\nAll Server Roles:");
        foreach (string role in justTheKeys) {
            Console.WriteLine(role);
        }

        // Iterating through an IDictionary gives you KeyValuePair objects
        Console.WriteLine("\nFull Configuration:");
        foreach (KeyValuePair&lt;string, string&gt; config in serverConfigs) {
            Console.WriteLine($"Role: {config.Key} -> IP: {config.Value}");
        }
    }
}</code></pre>
            </div>

            <br>
            <h3>4. ISet&lt;T&gt;</h3>
            <div class="callout callout-info">
                <span class="callout-title">Theory</span>
                <p>ISet&lt;T&gt; completely ignores order and indexing. If a class implements ISet&lt;T&gt;, it promises: <em>"I absolutely will not allow duplicates, and I am heavily optimized for math-like Set operations."</em></p>
                <ul>
                    <li><strong>Uniqueness:</strong> If you try to add "Apple" 100 times to a HashSet, it will only keep one "Apple". It silently ignores duplicates.</li>
                    <li><strong>No Order, No Index:</strong> You cannot ask a HashSet for item [0]. It treats items like a chaotic bag.</li>
                    <li><strong>Blazing Fast .Contains():</strong> Checking a List takes O(N) time. A HashSet uses a "hash code" to instantly know if the item is there in O(1) time.</li>
                </ul>
            </div>
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;

public class Program {
    public static void Main() {
        // 1. Instantiate a concrete HashSet, interact with it via the ISet interface
        ISet&lt;string&gt; authorizedUsers = new HashSet&lt;string&gt;();

        // 2. ISet's .Add() returns true if added, false if it's a duplicate!
        bool firstAdd = authorizedUsers.Add("Alice");  // Returns true
        bool secondAdd = authorizedUsers.Add("Alice"); // Returns false (Ignored!)
        
        authorizedUsers.Add("Bob");
        authorizedUsers.Add("Charlie");

        Console.WriteLine($"First add success: {firstAdd}");
        Console.WriteLine($"Second add success: {secondAdd}");
        Console.WriteLine($"Total users: {authorizedUsers.Count}\n"); // Count is 3, not 4

        // 3. Fast checking 
        if (authorizedUsers.Contains("Bob")) {
            Console.WriteLine("Bob is verified.\n");
        }

        // 4. Mathematical Set Operations (Unique to ISet)
        ISet&lt;string&gt; currentlyLoggedOn = new HashSet&lt;string&gt; { "Alice", "David" };

        // IntersectWith modifies the first set to ONLY keep items that exist in BOTH sets
        authorizedUsers.IntersectWith(currentlyLoggedOn); 
        
        Console.WriteLine("Users who are BOTH authorized AND logged on:");
        foreach(string user in authorizedUsers) {
            Console.WriteLine(user); // Only "Alice" prints
        }
    }
}</code></pre>
            </div>
        </div>

        <!-- TAB 3: CONCRETE COLLECTIONS -->
        <div id="tab-concrete" class="topic-tab-content">
            <h2>Concrete Collection Classes (Implementation)</h2>
            <p>Here is exactly how to instantiate and use every major collection class.</p>
            
            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;
using System.Linq; // Added for Min/Max extension methods

class Program
{
    static void Main()
    {
        DemoList();
        DemoDictionary();
        DemoSortedDictionary();
        DemoHashSet();
        DemoSortedSet();
        DemoStack();
        DemoQueue();
    }

    // ==========================================
    // 1. LIST<T>
    // ==========================================
    static void DemoList()
    {
        Console.WriteLine("--- 1. LIST DEMO ---");
        List&lt;string&gt; fruits = new List&lt;string&gt;();

        fruits.Add("Apple");                          
        fruits.AddRange(new string[] { "Banana", "Cherry" }); 
        fruits.Insert(0, "Mango");                    
        
        fruits.Remove("Banana");                      
        fruits.RemoveAt(0);                           
        
        fruits.Sort();                                

        Console.WriteLine($"Contains Apple? {fruits.Contains("Apple")}");
        Console.WriteLine($"Item at index 0: {fruits[0]}\n");
    }

    // ==========================================
    // 2. DICTIONARY<TKey, TValue>
    // ==========================================
    static void DemoDictionary()
    {
        Console.WriteLine("--- 2. DICTIONARY DEMO ---");
        Dictionary&lt;int, string&gt; employees = new Dictionary&lt;int, string&gt;();

        employees.Add(101, "Alice");                  
        employees.TryAdd(101, "Bob");                 
        employees[102] = "Charlie";                   
        
        employees.Remove(101);                        

        if (employees.TryGetValue(102, out string name))
        {
            Console.WriteLine($"Found employee 102: {name}");
        }

        Console.WriteLine($"Does ID 999 exist? {employees.ContainsKey(999)}\n");
    }

    // ==========================================
    // 3. SORTED DICTIONARY<TKey, TValue>
    // ==========================================
    static void DemoSortedDictionary()
    {
        Console.WriteLine("--- 3. SORTED DICTIONARY DEMO ---");
        SortedDictionary&lt;string, int&gt; gameScores = new SortedDictionary&lt;string, int&gt;();

        gameScores.Add("Charlie", 85);
        gameScores.Add("Alice", 95);
        gameScores.Add("Bob", 70);

        // It automatically prints Alice, Bob, Charlie (Alphabetical by Key!)
        foreach (KeyValuePair&lt;string, int&gt; entry in gameScores)
        {
            Console.WriteLine($"{entry.Key} scored {entry.Value}");
        }
        Console.WriteLine();
    }

    // ==========================================
    // 4. HASHSET<T>
    // ==========================================
    static void DemoHashSet()
    {
        Console.WriteLine("--- 4. HASHSET DEMO ---");
        HashSet&lt;int&gt; activeUsers = new HashSet&lt;int&gt;();

        activeUsers.Add(1);
        activeUsers.Add(2);
        bool addedAgain = activeUsers.Add(1);         

        activeUsers.Remove(2);

        HashSet&lt;int&gt; premiumUsers = new HashSet&lt;int&gt; { 1, 3, 5 };
        activeUsers.IntersectWith(premiumUsers); 

        Console.WriteLine($"Was duplicate added? {addedAgain}");
        Console.WriteLine($"Is User 1 still active? {activeUsers.Contains(1)}\n");
    }

    // ==========================================
    // 5. SORTED SET<T>
    // ==========================================
    static void DemoSortedSet()
    {
        Console.WriteLine("--- 5. SORTED SET DEMO ---");
        SortedSet&lt;int&gt; ages = new SortedSet&lt;int&gt;();

        ages.Add(50);
        ages.Add(10);
        ages.Add(99);
        ages.Add(10); // Duplicate ignored

        Console.WriteLine($"Youngest: {ages.Min}");
        Console.WriteLine($"Oldest: {ages.Max}");

        Console.Write("All ages in order: ");
        foreach (int age in ages) Console.Write(age + " "); 
        Console.WriteLine("\n");
    }

    // ==========================================
    // 6. STACK<T>
    // ==========================================
    static void DemoStack()
    {
        Console.WriteLine("--- 6. STACK DEMO ---");
        Stack&lt;string&gt; undoHistory = new Stack&lt;string&gt;();

        undoHistory.Push("Typed 'Hello'");            
        undoHistory.Push("Typed 'World'");

        string topItem = undoHistory.Peek();          
        string removedItem = undoHistory.Pop();       

        Console.WriteLine($"Peeked at: {topItem}");
        Console.WriteLine($"Popped (Undid): {removedItem}");
        Console.WriteLine($"Now on top: {undoHistory.Peek()}\n");
    }

    // ==========================================
    // 7. QUEUE<T>
    // ==========================================
    static void DemoQueue()
    {
        Console.WriteLine("--- 7. QUEUE DEMO ---");
        Queue&lt;string&gt; printerLine = new Queue&lt;string&gt;();

        printerLine.Enqueue("Document1.pdf");         
        printerLine.Enqueue("Image.png");

        string nextInLine = printerLine.Peek();       
        string finishedItem = printerLine.Dequeue();  

        Console.WriteLine($"Peeked at front: {nextInLine}");
        Console.WriteLine($"Dequeued (Printed): {finishedItem}");
        Console.WriteLine($"Now at front: {printerLine.Peek()}\n");
    }
}</code></pre>
            </div>
        </div>

        <!-- TAB 4: ENGINES & RULES -->
        <div id="tab-engine" class="topic-tab-content">
            <h2>Collection Engines & Global Rules</h2>

            <div class="callout callout-warn">
                <span class="callout-title">The Golden Rule of Collections</span>
                <p>You should almost never use the old non-generic collections. Always use Generics.</p>
                <ul style="font-size: 0.95rem; margin-top:10px;">
                    <li><strong>The IList&lt;T&gt; Family:</strong> <code>List&lt;T&gt;</code> (Standard array). Regular arrays like <code>int[]</code> secretly implement IList&lt;T&gt; under the hood!</li>
                    <li><strong>The IDictionary&lt;TKey, TValue&gt; Family:</strong> <code>Dictionary&lt;TKey, TValue&gt;</code> (Hash table). <code>SortedDictionary</code> (Auto-sorts by key). <code>SortedList</code> (Uses less memory, implements IDictionary).</li>
                    <li><strong>The ISet&lt;T&gt; Family:</strong> <code>HashSet&lt;T&gt;</code> (Fast, random order). <code>SortedSet&lt;T&gt;</code> (Auto-sorts unique items).</li>
                    <li><strong>The ICollection&lt;T&gt; Family:</strong> <code>LinkedList&lt;T&gt;</code> (Chain of items).</li>
                    <li><strong>The IEnumerable&lt;T&gt; Family:</strong> <code>Stack&lt;T&gt;</code> (LIFO). <code>Queue&lt;T&gt;</code> (FIFO).</li>
                </ul>
            </div>

            <br>
            <h3>How the HashSet Engine Works (Hash Table Engine)</h3>
            <p><strong>When you INSERT an item:</strong></p>
            <ol>
                <li>C# calculates the mathematical <strong>Hash Code</strong> of the item (e.g., 837291).</li>
                <li>It divides that hash code by the number of available memory buckets to get a specific bucket index (e.g., Bucket 4).</li>
                <li>It jumps straight to Bucket 4.</li>
                <li>If the bucket is empty, it drops the item in.</li>
                <li>If the bucket already has items (a collision), it checks if the exact item is already there. If yes, it aborts (no duplicates). If no, it links the new item to the end of that bucket's short list.</li>
            </ol>
            <p><strong>When you SEARCH for an item:</strong></p>
            <ol>
                <li>C# calculates the Hash Code of the item you are looking for.</li>
                <li>It calculates the bucket index using the same math.</li>
                <li>It jumps directly to that specific bucket, skipping the rest of the collection entirely.</li>
                <li>It searches only the items residing inside that one bucket.</li>
            </ol>

            <br>
            <h3>How the SortedSet Engine Works (Red-Black Tree Engine)</h3>
            <p><strong>When you INSERT an item:</strong></p>
            <ol>
                <li>C# starts at the very top of the tree (the Root node).</li>
                <li>It compares your new item to the current node.</li>
                <li>If your item is smaller, it moves down to the <strong>Left</strong> branch. If it is larger, it moves down to the <strong>Right</strong> branch. (If it is exactly the same, it aborts to prevent duplicates).</li>
                <li>It repeats this Left/Right comparison until it hits an empty spot at the bottom of the tree, and attaches the new item there.</li>
                <li>C# instantly checks the tree's balance. If one side is getting too long, it automatically "rotates" the nodes to keep the tree perfectly balanced.</li>
            </ol>
            <p><strong>When you SEARCH for an item:</strong></p>
            <ol>
                <li>C# starts at the Root node.</li>
                <li>It compares the item you are searching for with the current node.</li>
                <li>If it matches, the search is over.</li>
                <li>If it doesn't match, it goes Left (if smaller) or Right (if larger).</li>
                <li>It repeats this until it either finds the item or hits a dead end (meaning the item doesn't exist).</li>
            </ol>
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
