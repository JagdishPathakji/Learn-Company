import os

filepath = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\10-advanced-types.html'

new_main = r'''
    <main class="main-content">
        <div class="topic-header">
            <h1>Advanced Types (Abstract, Interfaces, Sealed)</h1>
            <p class="metadata">Difficulty: Advanced | Category: C# Object-Oriented Programming</p>
        </div>

        <div class="callout callout-info">
            <span class="callout-title">Core OOP Concepts</span>
            <p>These advanced types are the foundation of modern C# architecture. They allow developers to build strict rules for how classes should behave, what data they must contain, and who is allowed to inherit from them.</p>
        </div>

        <!-- NEW TABBED UI -->
        <div class="topic-tabs">
            <button class="topic-tab-btn active" onclick="switchTopicTab('tab-abstract')">1. Abstract Classes</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-sealed')">2. Sealed Classes & Methods</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-interfaces')">3. Interfaces (Rules & Props)</button>
            <button class="topic-tab-btn danger-tab" onclick="switchTopicTab('tab-interfaces-adv')">4. Interfaces (Advanced Edge Cases)</button>
        </div>

        <!-- TAB 1: ABSTRACT CLASSES -->
        <div id="tab-abstract" class="topic-tab-content active">
            <h2>Abstract Classes</h2>
            <p>An abstract class acts as a foundational base. It contains common data and methods that every subclass gets, but it <strong>forces</strong> derived classes to provide their own specific behavior for certain methods.</p>
            
            <div class="callout callout-warn">
                <span class="callout-title">Core Rules of Abstraction</span>
                <ul>
                    <li>You <strong>cannot</strong> create an object of an abstract class directly (e.g., <code>new User()</code> is blocked).</li>
                    <li>If a class contains even one <code>abstract</code> member, the entire class <strong>must</strong> be declared abstract.</li>
                    <li>If a class contains only <code>virtual</code> members, the class does <strong>NOT</strong> need to be abstract.</li>
                    <li><strong>Late Binding:</strong> If you do <code>Parent p = new Child(); p.show();</code>, it will call the child's overridden method!</li>
                </ul>
            </div>

            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Abstract Classes (User Roles)</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Types
{
    // The Base class contains common data. No User creation without a specific role!
    abstract class User 
    {
        public Guid UserId { get; }
        public string Username { get; set; }
        public string Email { get; set; }

        // Protected constructor ensures only child classes can trigger this setup
        protected User(string username, string email) 
        {
            Username = username;
            Email = email;
            UserId = Guid.NewGuid();
        }

        // Concrete method: Every subclass inherits this exactly as is
        public void DisplayBasicInfo() 
        {
            Console.WriteLine($"User ID: {UserId} | Username: {Username}");
        }

        // Abstract method: NO body. Forces the derived class to provide the behavior.
        public abstract void DisplayRole();
    }

    class Author : User 
    {
        public Author(string username, string email) : base(username, email) { }

        // Must use 'override' keyword to fulfill the abstract contract
        public override void DisplayRole() 
        {
            Console.WriteLine("Role: Author");
        }

        public void CreateDraftArticle() 
        {
            Console.WriteLine(Username + " is creating an article draft.");
        }
    }

    class Program 
    {
        static void Main() 
        {
            Author author = new Author("jagdish", "jagdish@example.com");
            author.DisplayRole();        // Executed from child
            author.DisplayBasicInfo();   // Inherited from abstract parent
            author.CreateDraftArticle();
        }
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>Role: Author
User ID: 3f2b1a... | Username: jagdish
jagdish is creating an article draft.</pre></div>
        </div>

        <!-- TAB 2: SEALED CLASSES -->
        <div id="tab-sealed" class="topic-tab-content">
            <h2>Sealed Classes and Methods</h2>
            <p>The <code>sealed</code> keyword marks the <strong>final</strong> step in an inheritance hierarchy. Nobody should inherit from a sealed class. A sealed class can have a parent, but it cannot have children.</p>
            
            <div class="callout callout-danger">
                <span class="callout-title">Critical Edge Cases for Sealed</span>
                <ul>
                    <li>A class <strong>cannot</strong> be both abstract and sealed (Abstract requires inheritance, Sealed forbids it).</li>
                    <li>You can also seal <strong>methods</strong>! If you seal an overridden virtual or abstract method, further subclasses cannot override it anymore.</li>
                </ul>
            </div>

            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Sealed Classes</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Types
{
    // KnowledgeBaseRepository is the ONE concrete implementation allowed.
    // By marking it sealed, we prevent malicious or accidental inheritance.
    sealed class KnowledgeBaseRepository
    {
        public void SaveArticle()
        {
            Console.WriteLine("Saving article to database securely...");
        }
    }

    // CATCH: This will throw a fatal compiler error!
    // class HackedRepository : KnowledgeBaseRepository { }

    class Program
    {
        static void Main()
        {
            KnowledgeBaseRepository repository = new KnowledgeBaseRepository();
            repository.SaveArticle();
        }
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>Saving article to database securely...</pre></div>
        </div>

        <!-- TAB 3: INTERFACES (BASICS) -->
        <div id="tab-interfaces" class="topic-tab-content">
            <h2>Interfaces (The Contract)</h2>
            <p>An interface is a strict contract. It says: <em>"Any class that implements me must provide these members."</em> Why not use Abstract classes everywhere? Because a class can implement <strong>multiple interfaces</strong> at a time, whereas it can inherit only one class at a time.</p>

            <div class="callout callout-info">
                <span class="callout-title">The 20 Golden Rules of Interfaces</span>
                <div style="column-count: 2; column-gap: 40px; font-size: 0.9rem;">
                    <ol style="margin-bottom:0;">
                        <li>Declared with <code>interface</code> keyword.</li>
                        <li>Normal method has no body.</li>
                        <li>Normal method is implicitly abstract.</li>
                        <li>Concrete class MUST implement every member.</li>
                        <li>Abstract class doesn't have to implement everything.</li>
                        <li>Implementation must be public.</li>
                        <li>Implementing method doesn't use <code>override</code>.</li>
                        <li>Methods can have parameters.</li>
                        <li>Methods can return values.</li>
                        <li>Methods can be overloaded.</li>
                        <li>Can have multiple methods.</li>
                        <li>Multiple classes can implement the same interface.</li>
                        <li>A class can implement MULTIPLE interfaces.</li>
                        <li>Class can inherit a parent class AND interfaces.</li>
                        <li>Cannot normally be instantiated.</li>
                        <li>References provide polymorphism.</li>
                        <li>Reference can access ONLY interface members.</li>
                        <li>Methods can have default implementations (C# 8.0).</li>
                        <li>Can have static methods.</li>
                        <li>Implementation can participate in inheritance.</li>
                    </ol>
                </div>
            </div>

            <p><strong>Properties in Interfaces:</strong> An interface can declare properties (e.g. <code>string Name { get; }</code>). This does <strong>not</strong> mean the interface contains an instance variable. It simply demands that the implementing class must provide a matching property.</p>

            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Interface Properties</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Types
{
    interface IUser 
    {
        // The contract requires a getter for UserId and a getter/setter for Name
        int UserId { get; }
        string Name { get; set; }
    }

    class Author : IUser 
    {
        // The class provides the actual variables behind the properties
        public int UserId { get; }
        public string Name { get; set; }

        public Author(int userId, string name) 
        {
            // Even though UserId only has a 'get', it can be set in the constructor!
            UserId = userId;
            Name = name;
        }
    }

    class Program 
    {
        static void Main() 
        {
            // Using the Interface as a reference type (Polymorphism)
            IUser author = new Author(101, "Jagdish");
            
            Console.WriteLine("ID: " + author.UserId);
            Console.WriteLine("Name: " + author.Name);
            
            author.Name = "Jagdish Patel";
            Console.WriteLine("Updated Name: " + author.Name);
        }
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>ID: 101
Name: Jagdish
Updated Name: Jagdish Patel</pre></div>
        </div>

        <!-- TAB 4: INTERFACES (ADVANCED EDGE CASES) -->
        <div id="tab-interfaces-adv" class="topic-tab-content">
            <h2>Interfaces (Advanced Edge Cases)</h2>
            <p>Interfaces have strict rules regarding access modifiers, constants, and multiple inheritance conflicts. Let's look at the absolute hardest edge cases developers face.</p>

            <div class="callout callout-warn">
                <span class="callout-title">Edge Case 1: Interface Access Specifiers</span>
                <p><strong>"Everything in an interface is public."</strong> You cannot make a normal interface method private, protected, or internal. It represents a contract; making a contract private makes no sense. <br><br><em>Exception:</em> Modern C# allows <code>private</code> interface methods, but they <strong>must</strong> have a default implementation body (usually used as private helper methods for other default methods).</p>
            </div>

            <div class="callout callout-warn">
                <span class="callout-title">Edge Case 2: Constants in Interfaces</span>
                <p>Constants (e.g., <code>const int Draft = 1;</code>) are automatically public. The implementing class does not need to write code for them. Because they belong to the interface itself, you <strong>must</strong> access them using the interface name: <code>IKnowledgeContent.Draft</code>.</p>
            </div>

            <div class="callout callout-danger">
                <span class="callout-title">Edge Case 3: Explicit Interface Implementation (Name Clashes)</span>
                <p>What happens if a class implements two interfaces (<code>IAuthorReview</code> and <code>IEditorReview</code>), and BOTH interfaces have a method called <code>void Review();</code>? The compiler won't know which one you are calling!</p>
                <p><strong>The Fix:</strong> You must implement them <em>explicitly</em> by attaching the interface name to the method. When you do this, you <strong>cannot</strong> use the <code>public</code> access modifier, and you <strong>cannot</strong> call the method directly from the object! You must cast the object to the interface first.</p>
            </div>

            <div class="code-container" style="border-radius: 6px 6px 0 0;">
                <div class="code-header"><span>C# - Explicit Implementation</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Types
{
    interface IAuthorReview { void Review(); }
    interface IEditorReview { void Review(); }

    class Article : IAuthorReview, IEditorReview
    {
        public string Title { get; set; } = "C# Interfaces";

        // EXPLICIT IMPLEMENTATION 1
        // Notice there is NO 'public' keyword. It is forbidden here.
        void IAuthorReview.Review()
        {
            Console.WriteLine("Author review: checking content correctness.");
        }

        // EXPLICIT IMPLEMENTATION 2
        void IEditorReview.Review()
        {
            Console.WriteLine("Editor review: checking publication readiness.");
        }
    }

    class Program
    {
        static void Main()
        {
            Article article = new Article();

            // CATCH: article.Review(); // This throws a compiler error!

            // To call the methods, you MUST cast the object to the specific interface first:
            IAuthorReview authorReview = article;
            IEditorReview editorReview = article;

            authorReview.Review();
            editorReview.Review();
        }
    }
}</code></pre>
            </div>
            <div class="console-output"><strong>Console Output:</strong><pre>Author review: checking content correctness.
Editor review: checking publication readiness.</pre></div>
        </div>

        <div class="nav-buttons">
            <a href="09-file-operations.html">&larr; Previous: File Operations</a>
            <a href="#">Next: Generics &rarr;</a>
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
