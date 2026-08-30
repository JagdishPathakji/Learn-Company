import os
import glob

base_dir = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp'
filepath = os.path.join(base_dir, '13-lambda-expressions.html')

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>C# Lambda Expressions</title>
    <link rel="stylesheet" href="../../css/global.css">
    <style>
        .concept-block { background: #1e293b; padding: 25px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border-left: 4px solid #38bdf8; }
        .concept-title { color: #38bdf8; font-size: 1.5rem; margin-top: 0; margin-bottom: 15px; border-bottom: 1px solid #334155; padding-bottom: 10px; }
        .concept-section { margin-bottom: 15px; }
        .concept-label { font-weight: bold; color: #94a3b8; display: inline-block; width: 150px; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px;}
        .concept-value { color: #f8fafc; }
        .mistake-box { background: #450a0a; border-left: 4px solid #ef4444; padding: 15px; margin-top: 15px; border-radius: 4px; }
        .mistake-title { color: #fca5a5; font-weight: bold; margin-bottom: 5px; display: block; }
        
        .evolution-step { background: #0f172a; padding: 15px; margin-bottom: 15px; border-radius: 4px; border: 1px solid #334155; }
        .evolution-step h4 { margin-top: 0; color: #10b981; }

        details { background: #334155; padding: 10px 15px; border-radius: 4px; margin-bottom: 10px; cursor: pointer; }
        summary { font-weight: bold; color: #e2e8f0; outline: none; }
        details > div { margin-top: 15px; padding-top: 15px; border-top: 1px solid #475569; color: #f1f5f9; cursor: text; }
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
            <li><a href="11-generics.html">11. Generics</a></li>
            <li><a href="12-file-system.html">12. File System</a></li>
            <li><a href="13-lambda-expressions.html" class="active">13. Lambda Expressions</a></li>
        </ul>
        <div class="sidebar-category">Deep Dives (Custom)</div>
        <ul>
            <li><a href="custom-01-top-level-statements.html">Top-Level Statements vs Main</a></li>
        </ul>
    </aside>
    
    <main class="main-content">
        <div class="topic-header">
            <h1>Lambda Expressions (Pre-LINQ)</h1>
            <p class="metadata">Difficulty: Intermediate | Category: C# Fundamentals</p>
        </div>

        <div class="callout callout-info">
            <span class="callout-title">The Gateway to LINQ</span>
            <p>Before you can understand LINQ (Language Integrated Query), you absolutely must master <strong>Lambda Expressions</strong>. This module uses the Knowledge Base domain (Articles, Users, Categories, and Roles) to explain what lambdas are, how they evolved, and how to pass them as data.</p>
        </div>

        <div class="topic-tabs">
            <button class="topic-tab-btn active" onclick="switchTopicTab('tab-basics')">1. Core Concepts & Evolution</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-delegates')">2. Action, Func, Predicate</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-lists')">3. List&lt;T&gt; & Closures</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-demo')">4. Final Demo & Exercises</button>
        </div>

        <!-- TAB 1: CORE CONCEPTS & EVOLUTION -->
        <div id="tab-basics" class="topic-tab-content active">
            
            <!-- 1. What is a Lambda Expression -->
            <div class="concept-block">
                <h3 class="concept-title">1. What is a Lambda Expression?</h3>
                <div class="concept-section"><span class="concept-label">What it is:</span><span class="concept-value">An anonymous function (a method without a name) that you can write inline and treat as data.</span></div>
                <div class="concept-section"><span class="concept-label">Why it exists:</span><span class="concept-value">To save you from writing dozens of tiny, single-use methods. It makes code shorter, more readable, and enables functional programming (passing logic to other methods).</span></div>
                <div class="concept-section"><span class="concept-label">Syntax:</span><span class="concept-value"><code>parameter => expression</code> (The <code>=></code> is the "goes to" or "lambda" operator).</span></div>
                <div class="concept-section"><span class="concept-label">How it works:</span><span class="concept-value">The compiler automatically creates a hidden method behind the scenes and maps your lambda to it.</span></div>
                <div class="concept-section"><span class="concept-label">KB Example:</span><span class="concept-value"><code>article => article.Status == EnmArticleStatus.Published</code> (Takes an article, returns true if published).</span></div>
                <div class="mistake-box">
                    <span class="mistake-title">Common Mistake</span>
                    Reading <code>=></code> as "greater than or equal to". It is NOT <code>>=</code>. The <code>=></code> symbol explicitly means "lambda operator".
                </div>
            </div>

            <!-- 2. Understand the Evolution -->
            <div class="concept-block">
                <h3 class="concept-title">2. Understand the Evolution</h3>
                <p style="color:#cbd5e1; margin-bottom: 20px;">To appreciate lambdas, you need to see how painful C# 1.0 used to be when trying to filter a list of Knowledge Base Articles.</p>
                
                <div class="evolution-step">
                    <h4>Step 1: Normal Named Method (C# 1.0)</h4>
                    <pre><code class="language-csharp">public bool IsPublished(Article article) {
    return article.Status == EnmArticleStatus.Published;
}
// You had to write a full method for every tiny check!</code></pre>
                </div>
                
                <div class="evolution-step">
                    <h4>Step 2: Delegate Instance (C# 1.0)</h4>
                    <pre><code class="language-csharp">Predicate&lt;Article&gt; filter = new Predicate&lt;Article&gt;(IsPublished);
// You had to wrap the method in a delegate object just to pass it around.</code></pre>
                </div>

                <div class="evolution-step">
                    <h4>Step 3: Anonymous Method (C# 2.0)</h4>
                    <pre><code class="language-csharp">Predicate&lt;Article&gt; filter = delegate(Article article) {
    return article.Status == EnmArticleStatus.Published;
};
// Removed the need for a separate named method, but still very wordy with 'delegate' and types.</code></pre>
                </div>

                <div class="evolution-step">
                    <h4>Step 4: Lambda Expression (C# 3.0+)</h4>
                    <pre><code class="language-csharp">Predicate&lt;Article&gt; filter = article => article.Status == EnmArticleStatus.Published;
// Clean, beautiful. The compiler INFERS that 'article' is of type Article, and infers the return!</code></pre>
                </div>
            </div>

            <!-- 3. Lambda Syntax -->
            <div class="concept-block">
                <h3 class="concept-title">3. Lambda Syntax Variations</h3>
                <div class="concept-section"><span class="concept-label">What it is:</span><span class="concept-value">The different ways you can write the left side (parameters) and right side (body) of a lambda.</span></div>
                <div class="concept-section"><span class="concept-label">Why it exists:</span><span class="concept-value">Some logic requires multiple parameters or multiple lines of code, requiring slightly different syntax.</span></div>
                
                <table style="width: 100%; text-align: left; margin-top: 15px; border-collapse: collapse; color: #e2e8f0;">
                    <tr style="border-bottom: 1px solid #475569;">
                        <th style="padding: 10px;">Scenario</th>
                        <th style="padding: 10px;">Syntax</th>
                    </tr>
                    <tr style="border-bottom: 1px solid #475569;">
                        <td style="padding: 10px;"><strong>No Parameters</strong></td>
                        <td style="padding: 10px;"><code>() => Console.WriteLine("Knowledge Base Started");</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid #475569;">
                        <td style="padding: 10px;"><strong>One Parameter</strong><br><small>(Parentheses optional)</small></td>
                        <td style="padding: 10px;"><code>article => article.Title == "C# Lambdas"</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid #475569;">
                        <td style="padding: 10px;"><strong>Multiple Parameters</strong><br><small>(Parentheses REQUIRED)</small></td>
                        <td style="padding: 10px;"><code>(article, user) => article.AuthorId == user.Id</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid #475569;">
                        <td style="padding: 10px;"><strong>Expression Body</strong><br><small>(One line, auto-returns)</small></td>
                        <td style="padding: 10px;"><code>article => article.ViewCount > 100</code></td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;"><strong>Statement Body</strong><br><small>(Multi-line, requires {} and return)</small></td>
                        <td style="padding: 10px;">
<pre style="margin:0;"><code class="language-csharp" style="padding:0;">article => {
    Console.WriteLine($"Checking {article.Title}");
    return article.ViewCount > 100;
}</code></pre>
                        </td>
                    </tr>
                </table>
            </div>

        </div>

        <!-- TAB 2: DELEGATES, ACTION, FUNC, PREDICATE -->
        <div id="tab-delegates" class="topic-tab-content">
            
            <!-- 4. Lambdas and Delegates -->
            <div class="concept-block">
                <h3 class="concept-title">4. Lambdas and Delegates</h3>
                <div class="concept-section"><span class="concept-label">What it is:</span><span class="concept-value">A delegate is a variable that holds a function instead of a value. A lambda is the function you assign to it.</span></div>
                <div class="concept-section"><span class="concept-label">Why it exists:</span><span class="concept-value">You cannot just write <code>var myLogic = article => article.Title;</code>. C# is strongly typed. The compiler needs to know exactly what the lambda takes and returns. It needs a Delegate Type.</span></div>
                
                <pre><code class="language-csharp">using System;

class Program {
    // 1. Define a custom delegate type (a contract)
    public delegate bool ArticleFilterDelegate(Article article);

    static void Main() {
        // 2. Assign a lambda to the delegate variable
        ArticleFilterDelegate isDraft = article => article.Status == EnmArticleStatus.Draft;

        Article testArticle = new Article { Status = EnmArticleStatus.Draft };
        
        // 3. Invoke the delegate just like a method
        bool result = isDraft(testArticle); 
        Console.WriteLine(result); // True
    }
}</code></pre>
            </div>

            <!-- 5. Action, Func, Predicate -->
            <div class="concept-block">
                <h3 class="concept-title">5. Action, Func, and Predicate (Built-in Delegates)</h3>
                <p style="color:#cbd5e1;">Because declaring custom delegates for every lambda was annoying, Microsoft built three generic delegates into the .NET framework.</p>

                <div class="evolution-step">
                    <h4>1. Action&lt;T&gt; (Always returns void)</h4>
                    <p>Used when you want to <strong>DO</strong> something, but don't need an answer back.</p>
                    <pre><code class="language-csharp">// Action&lt;Article&gt; takes an Article, returns void.
Action&lt;Article&gt; printArticle = article => Console.WriteLine(article.Title);

printArticle(myArticle);</code></pre>
                </div>

                <div class="evolution-step">
                    <h4>2. Func&lt;TInput, TOutput&gt; (Always returns a value)</h4>
                    <p>Used when you want to transform data or calculate something. <strong>The LAST generic parameter is ALWAYS the return type.</strong></p>
                    <pre><code class="language-csharp">// Func&lt;Article, string&gt; takes an Article, returns a string.
Func&lt;Article, string&gt; getTitle = article => article.Title.ToUpper();

// Func&lt;User, Article, bool&gt; takes User and Article, returns bool.
Func&lt;User, Article, bool&gt; canEdit = (user, article) => user.Role == EnmRole.Editor || article.AuthorId == user.Id;</code></pre>
                </div>

                <div class="evolution-step">
                    <h4>3. Predicate&lt;T&gt; (Always returns a bool)</h4>
                    <p>A specialized version of Func used strictly for True/False testing (filtering).</p>
                    <pre><code class="language-csharp">// Predicate&lt;Article&gt; takes an Article, returns a bool.
Predicate&lt;Article&gt; isPopular = article => article.ViewCount > 1000;</code></pre>
                </div>

                <div class="mistake-box">
                    <span class="mistake-title">Common Mistake</span>
                    Writing <code>Func&lt;string, Article&gt;</code> when you meant "Takes an Article, returns a string". Remember: The RETURN type is always the last argument in Func! It should be <code>Func&lt;Article, string&gt;</code>.
                </div>
            </div>

            <!-- 6. Passing Lambdas to Methods -->
            <div class="concept-block">
                <h3 class="concept-title">6. Passing Lambdas to Methods</h3>
                <div class="concept-section"><span class="concept-label">What it is:</span><span class="concept-value">Methods can accept <code>Action</code>, <code>Func</code>, or <code>Predicate</code> as parameters.</span></div>
                <div class="concept-section"><span class="concept-label">Why it exists:</span><span class="concept-value">This is the heart of functional programming. Instead of hardcoding the filtering logic inside the method, you let the CALLER inject the logic!</span></div>
                
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;

class KnowledgeBaseEngine {
    
    // We don't hardcode the filter. We ask the caller to give us the rule (Predicate).
    public List&lt;Article&gt; FilterArticles(List&lt;Article&gt; allArticles, Predicate&lt;Article&gt; condition) {
        List&lt;Article&gt; results = new List&lt;Article&gt;();
        
        foreach (Article article in allArticles) {
            // We EXECUTE the lambda the caller passed in!
            if (condition(article)) {
                results.Add(article);
            }
        }
        return results;
    }
}

class Program {
    static void Main() {
        KnowledgeBaseEngine engine = new KnowledgeBaseEngine();
        List&lt;Article&gt; database = GetArticles(); // Assume this gets 100 articles

        // Caller 1 wants only Drafts
        List&lt;Article&gt; drafts = engine.FilterArticles(database, article => article.Status == EnmArticleStatus.Draft);

        // Caller 2 wants only popular articles
        List&lt;Article&gt; popular = engine.FilterArticles(database, article => article.ViewCount > 5000);
    }
}</code></pre>
            </div>

        </div>

        <!-- TAB 3: LIST<T>, CLOSURES, LINQ -->
        <div id="tab-lists" class="topic-tab-content">
            
            <!-- 7. Lambdas with List<T> -->
            <div class="concept-block">
                <h3 class="concept-title">7. Built-in List&lt;T&gt; Lambda Methods</h3>
                <p style="color:#cbd5e1;">Because passing logic is so powerful, Microsoft built methods directly into <code>List&lt;T&gt;</code> that accept <code>Predicate</code> and <code>Action</code>.</p>
                
                <pre><code class="language-csharp">List&lt;Article&gt; articles = GetKnowledgeBaseArticles();

// 1. Find (Returns the FIRST matching item, or null)
Article firstDraft = articles.Find(article => article.Status == EnmArticleStatus.Draft);

// 2. FindAll (Returns a NEW LIST of all matching items)
List&lt;Article&gt; allDrafts = articles.FindAll(article => article.Status == EnmArticleStatus.Draft);

// 3. Exists (Returns true if AT LEAST ONE item matches)
bool hasRejected = articles.Exists(article => article.Status == EnmArticleStatus.Rejected);

// 4. RemoveAll (Deletes all matching items from the list, returns count of removed)
int removedCount = articles.RemoveAll(article => article.Status == EnmArticleStatus.Rejected);

// 5. ForEach (Executes an Action on every item in the list)
articles.ForEach(article => Console.WriteLine(article.Title));</code></pre>
            </div>

            <!-- 8. Variable Capture (Closures) -->
            <div class="concept-block">
                <h3 class="concept-title">8. Variable Capture (Closures)</h3>
                <div class="concept-section"><span class="concept-label">What it is:</span><span class="concept-value">A lambda expression can "reach outside" its own curly braces and use variables from the method that created it.</span></div>
                <div class="concept-section"><span class="concept-label">Why it exists:</span><span class="concept-value">Lambdas wouldn't be very useful if they could only use hardcoded data. We need to pass dynamic parameters into the lambda's logic.</span></div>
                
                <pre><code class="language-csharp">public void FindUserArticles(List&lt;Article&gt; articles, int targetAuthorId) {
    
    // The lambda "captures" the targetAuthorId variable from the parent method!
    // This creates a "Closure" ?" the compiler permanently binds that variable to the lambda.
    List&lt;Article&gt; userArticles = articles.FindAll(article => article.AuthorId == targetAuthorId);
    
    userArticles.ForEach(article => Console.WriteLine(article.Title));
}</code></pre>

                <div class="mistake-box">
                    <span class="mistake-title">Common Mistake: The "For Loop" Capture Trap</span>
                    If you create lambdas inside a <code>for</code> loop (using the loop variable <code>i</code>), all the lambdas capture the <strong>reference</strong> to <code>i</code>, not the value at that moment. When they finally execute later, they will all use the final value of <code>i</code>! (Note: C# fixed this for <code>foreach</code> loops in C# 5, but the trap remains for standard <code>for</code> loops).
                </div>
            </div>

            <!-- 9. Lambda vs Named Method -->
            <div class="concept-block">
                <h3 class="concept-title">9. When NOT to use Lambdas</h3>
                <div class="concept-section"><span class="concept-label">Use a Lambda:</span><span class="concept-value">When the logic is 1 to 3 lines long, only used in one place, and extremely obvious (e.g., filtering a status).</span></div>
                <div class="concept-section"><span class="concept-label">Use a Named Method:</span><span class="concept-value">When the logic is 10+ lines long, involves complex `if/else` rules, or needs to be reused across 5 different files.</span></div>
                
                <pre><code class="language-csharp">// BAD: Don't write massive multi-line lambdas like this inline
articles.FindAll(article => {
    if (article.Status == EnmArticleStatus.Published) {
        if (article.ViewCount > 1000) {
            return true;
        }
    }
    return false;
});

// GOOD: Pass a named method for complex logic
articles.FindAll(IsHighlyRatedPublishedArticle);</code></pre>
            </div>

            <!-- 10. LINQ Connection -->
            <div class="concept-block">
                <h3 class="concept-title">10. The LINQ Connection (Preview)</h3>
                <p>Up until now, we used <code>List&lt;T&gt;.FindAll()</code>. But what if our data is in an Array? Or a Database? Or XML? <code>FindAll</code> only exists on Lists.</p>
                <p>This is why <strong>LINQ</strong> was invented. LINQ relies heavily on Lambdas to query <em>any</em> data source using the exact same syntax (like <code>.Where()</code>, <code>.Select()</code>). If you understand how <code>article => article.Status == Published</code> works, you already know 90% of LINQ!</p>
                <pre><code class="language-csharp">// List.FindAll (Only works on Lists)
var drafts = list.FindAll(article => article.Status == EnmArticleStatus.Draft);

// LINQ .Where (Works on Arrays, Lists, Databases, HashSets, everything!)
var drafts = collection.Where(article => article.Status == EnmArticleStatus.Draft);</code></pre>
            </div>

        </div>

        <!-- TAB 4: FINAL DEMO & PRACTICE -->
        <div id="tab-demo" class="topic-tab-content">
            
            <h2>Knowledge Base Lambda Demo</h2>
            <p>This complete, traditional <code>Program.cs</code> file demonstrates everything covered above in a single cohesive system.</p>

            <div class="code-container" style="border-radius: 6px 6px 0 0; margin-bottom: 30px;">
                <div class="code-header"><span>C# - Program.cs</span><button class="copy-btn">Copy</button></div>
                <pre><code class="language-csharp">using System;
using System.Collections.Generic;

namespace KnowledgeBase {
    
    #region Enums
    /// &lt;summary&gt;Defines the lifecycle status of an article.&lt;/summary&gt;
    public enum EnmArticleStatus { Draft, PendingReview, NeedsImprovement, Rejected, Published }
    
    /// &lt;summary&gt;Defines the security role of a user.&lt;/summary&gt;
    public enum EnmRole { Author, Reviewer, Editor }
    #endregion

    #region Domain Classes
    public class User {
        public int Id { get; set; }
        public string Name { get; set; }
        public EnmRole Role { get; set; }
    }

    public class Article {
        public int Id { get; set; }
        public string Title { get; set; }
        public int AuthorId { get; set; }
        public EnmArticleStatus Status { get; set; }
        public int ViewCount { get; set; }
    }
    #endregion

    class Program {
        static void Main(string[] args) {
            
            List&lt;Article&gt; articles = new List&lt;Article&gt; {
                new Article { Id = 1, Title = "C# Basics", AuthorId = 101, Status = EnmArticleStatus.Published, ViewCount = 1500 },
                new Article { Id = 2, Title = "OOP Guide", AuthorId = 101, Status = EnmArticleStatus.Draft, ViewCount = 0 },
                new Article { Id = 3, Title = "Advanced SQL", AuthorId = 102, Status = EnmArticleStatus.PendingReview, ViewCount = 0 },
                new Article { Id = 4, Title = "APIs in C#", AuthorId = 103, Status = EnmArticleStatus.Published, ViewCount = 500 }
            };

            User currentEditor = new User { Id = 999, Name = "Alice", Role = EnmRole.Editor };

            Console.WriteLine("=== 1. FILTERING (Predicate) ===");
            // FindAll requires a Predicate&lt;Article&gt; (returns bool)
            List&lt;Article&gt; publishedArticles = articles.FindAll(article => article.Status == EnmArticleStatus.Published);
            Console.WriteLine($"Found {publishedArticles.Count} published articles.");

            Console.WriteLine("\n=== 2. FINDING SINGLE ITEM (Predicate) ===");
            // Find returns the first match or null
            Article sqlArticle = articles.Find(article => article.Title.Contains("SQL"));
            Console.WriteLine($"Found SQL Article ID: {sqlArticle?.Id}");

            Console.WriteLine("\n=== 3. CHECKING EXISTENCE (Predicate) ===");
            bool hasDrafts = articles.Exists(article => article.Status == EnmArticleStatus.Draft);
            Console.WriteLine($"System has drafts: {hasDrafts}");

            Console.WriteLine("\n=== 4. DISPLAYING (Action) ===");
            // ForEach requires an Action&lt;Article&gt; (returns void)
            publishedArticles.ForEach(article => Console.WriteLine($"- {article.Title} ({article.ViewCount} views)"));

            Console.WriteLine("\n=== 5. VARIABLE CAPTURE (Closure) ===");
            int searchAuthorId = 101; 
            // The lambda reaches outside to grab searchAuthorId
            List&lt;Article&gt; author101Articles = articles.FindAll(article => article.AuthorId == searchAuthorId);
            Console.WriteLine($"Author 101 has {author101Articles.Count} articles.");

            Console.WriteLine("\n=== 6. CALCULATION (Func) ===");
            // Func&lt;Article, double&gt; takes an Article and returns a double (Ad Revenue calculation)
            Func&lt;Article, double&gt; calculateAdRevenue = article => article.ViewCount * 0.05;
            Console.WriteLine($"Revenue for '{articles[0].Title}': ${calculateAdRevenue(articles[0])}");
            
            // Wait for user
            Console.ReadLine();
        }
    }
}</code></pre>
            </div>

            <hr style="border: 1px solid #334155; margin: 40px 0;">

            <h2>Practice & Validation</h2>
            <p style="color:#94a3b8; margin-bottom: 20px;">Try answering these mentally before expanding the solution.</p>

            <h3>Beginner Exercises (Write the Lambda)</h3>
            <details>
                <summary>1. Write a lambda that takes an Article and returns true if its ViewCount is greater than 100.</summary>
                <div><code>article => article.ViewCount > 100</code></div>
            </details>
            <details>
                <summary>2. Write a lambda that takes a User and returns their Name.</summary>
                <div><code>user => user.Name</code></div>
            </details>
            <details>
                <summary>3. Write an Action lambda that takes an Article and prints "Reviewing: [Title]" to the console.</summary>
                <div><code>article => Console.WriteLine($"Reviewing: {article.Title}")</code></div>
            </details>
            <details>
                <summary>4. Write a lambda that takes two parameters (Article, User) and returns true if the User's Id matches the Article's AuthorId.</summary>
                <div><code>(article, user) => article.AuthorId == user.Id</code></div>
            </details>
            <details>
                <summary>5. Write a lambda with NO parameters that returns the string "Hello KB".</summary>
                <div><code>() => "Hello KB"</code></div>
            </details>

            <h3 style="margin-top:30px;">Intermediate Exercises (Signatures & Blocks)</h3>
            <details>
                <summary>1. You have a method `void ProcessUser(Action&lt;User&gt; action)`. Call it, passing a lambda that changes a user's Role to Author.</summary>
                <div><code>ProcessUser(user => user.Role = EnmRole.Author);</code></div>
            </details>
            <details>
                <summary>2. Write a statement lambda (using curly braces) that takes an Article. If Status is Draft, return false. Otherwise, return true.</summary>
                <div><pre><code class="language-csharp">article => {
    if (article.Status == EnmArticleStatus.Draft) return false;
    return true;
}</code></pre></div>
            </details>
            <details>
                <summary>3. Declare a variable of type `Func&lt;Article, bool&gt;` and assign a lambda that checks if it is Rejected.</summary>
                <div><code>Func&lt;Article, bool&gt; isRejected = article => article.Status == EnmArticleStatus.Rejected;</code></div>
            </details>
            <details>
                <summary>4. Use `RemoveAll` on a `List&lt;Article&gt;` to delete all articles where the AuthorId is 404.</summary>
                <div><code>articles.RemoveAll(article => article.AuthorId == 404);</code></div>
            </details>
            <details>
                <summary>5. You have a local variable `int threshold = 500;`. Write a closure lambda inside `articles.FindAll()` to get articles with views above this threshold.</summary>
                <div><code>articles.FindAll(article => article.ViewCount > threshold);</code></div>
            </details>

            <h3 style="margin-top:30px;">Output Prediction</h3>
            <details>
                <summary>1. What prints here? <br><code>Func&lt;int, int&gt; math = x => x * 2;<br>Console.WriteLine(math(5));</code></summary>
                <div><strong>10</strong></div>
            </details>
            <details>
                <summary>2. What happens to the list here? <br><code>articles.ForEach(article => article.ViewCount = 0);</code></summary>
                <div>Every single article in the list will have its ViewCount reset to 0. (ForEach mutates the objects directly).</div>
            </details>
            <details>
                <summary>3. What prints here? <br><code>Predicate&lt;User&gt; isAdmin = user => user.Role == EnmRole.Editor;<br>User u = new User { Role = EnmRole.Author };<br>Console.WriteLine(isAdmin(u));</code></summary>
                <div><strong>False</strong></div>
            </details>

            <h3 style="margin-top:30px;">Find the Error</h3>
            <details>
                <summary>1. <code>Func&lt;Article, string&gt; getTitle = article => Console.WriteLine(article.Title);</code></summary>
                <div><strong>Error:</strong> Func expects a return value of type string. Console.WriteLine returns <code>void</code>. This should be an <code>Action&lt;Article&gt;</code>.</div>
            </details>
            <details>
                <summary>2. <code>Predicate&lt;Article&gt; isDone = article => { article.Status == EnmArticleStatus.Published };</code></summary>
                <div><strong>Error:</strong> If you use curly braces <code>{}</code> (Statement Lambda), you MUST use the <code>return</code> keyword. Correct: <code>{ return article.Status == EnmArticleStatus.Published; }</code></div>
            </details>
            <details>
                <summary>3. <code>Action&lt;User, Article&gt; log = user, article => Console.WriteLine(user.Name);</code></summary>
                <div><strong>Error:</strong> When you have multiple parameters, you MUST wrap them in parentheses: <code>(user, article) => ...</code></div>
            </details>

            <h3 style="margin-top:30px;">Interview & Revision Questions</h3>
            <details>
                <summary>1. What is the fundamental difference between an Action and a Func?</summary>
                <div>Action ALWAYS returns void (it performs a task). Func ALWAYS returns a value (it calculates or retrieves something).</div>
            </details>
            <details>
                <summary>2. What is a Predicate, and how does it relate to Func?</summary>
                <div>A Predicate is just a specialized Func that always returns a boolean. <code>Predicate&lt;T&gt;</code> is essentially identical to <code>Func&lt;T, bool&gt;</code>.</div>
            </details>
            <details>
                <summary>3. Explain what a "Closure" or "Variable Capture" is in the context of Lambdas.</summary>
                <div>It is when a lambda expression uses a variable that was declared outside of the lambda (in the parent method's scope). The compiler captures that variable so the lambda can still use it even if it executes later.</div>
            </details>
            <details>
                <summary>4. Why was the lambda operator (=>) introduced to C#?</summary>
                <div>To provide a highly concise, readable syntax for creating anonymous functions, reducing the boilerplate of C# 2.0 anonymous delegates, and paving the way for LINQ.</div>
            </details>
            <details>
                <summary>5. What does the last generic parameter in a Func&lt;&gt; declaration always represent?</summary>
                <div>The return type of the method. For example, in <code>Func&lt;int, string, bool&gt;</code>, it takes an int and a string, and returns a bool.</div>
            </details>
            <details>
                <summary>6. If a lambda contains an if-statement, can you use Expression-body syntax (without curly braces)?</summary>
                <div>No. You can only use a ternary operator <code>(condition ? true : false)</code> without curly braces. If you write an actual <code>if</code> keyword, you must use a Statement body with <code>{}</code> and <code>return</code>.</div>
            </details>
            <details>
                <summary>7. What happens if <code>List.Find()</code> cannot find any item matching the lambda condition?</summary>
                <div>It returns the default value for the type. For reference types (like classes), it returns <code>null</code>. For value types (like structs), it returns the zero-initialized struct.</div>
            </details>
            <details>
                <summary>8. In C#, is a lambda expression executed immediately when it is defined?</summary>
                <div>No. A lambda expression is just data (a delegate or expression tree). It only executes when the method it is passed into decides to invoke it (e.g., <code>condition(article)</code>).</div>
            </details>

        </div>

        <div class="nav-buttons">
            <a href="12-file-system.html">&larr; Previous: File System (Advanced)</a>
            <a href="#">Next: Extension Methods &rarr;</a>
        </div>
    </main>
    
    <script src="../../js/ui-enhancements.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-csharp.min.js"></script>
    
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
</body>
</html>
'''

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_content)
