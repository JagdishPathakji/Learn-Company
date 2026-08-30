import os

filepath = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\15-linq.html'

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>C# LINQ (Language Integrated Query)</title>
    <link rel="stylesheet" href="../../css/global.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
    <style>
        .concept-block { background: var(--bg-surface); padding: 25px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); border-left: 4px solid var(--accent); color: var(--text-primary); line-height: 1.7; }
        .concept-title { color: var(--accent); font-size: 1.5rem; margin-top: 0; margin-bottom: 15px; border-bottom: 1px solid var(--border-color); padding-bottom: 10px; font-weight: 700; }
        
        .mistake-box { background: var(--callout-danger-bg); border-left: 4px solid var(--callout-danger-border); padding: 15px; margin-top: 15px; border-radius: 4px; color: var(--text-primary); line-height: 1.6; }
        .mistake-title { color: var(--callout-danger-border); font-weight: bold; margin-bottom: 5px; display: block; }
        
        .advanced-box { background: rgba(139, 92, 246, 0.1); border-left: 4px solid #8b5cf6; padding: 15px; margin-top: 15px; border-radius: 4px; color: #ddd6fe; line-height: 1.6; }
        .advanced-title { color: #c4b5fd; font-weight: bold; margin-bottom: 5px; display: block; }
        
        .evolution-step { background: var(--bg-main); padding: 15px; margin-bottom: 15px; border-radius: 4px; border: 1px solid var(--border-color); color: var(--text-primary); line-height: 1.6; }
        .evolution-step h4 { margin-top: 0; color: #10b981; font-size: 1.2rem; margin-bottom: 10px; }

        details { background: var(--border-color); padding: 10px 15px; border-radius: 4px; margin-bottom: 10px; cursor: pointer; }
        summary { font-weight: bold; color: var(--text-primary); outline: none; }
        details > div { margin-top: 15px; padding-top: 15px; border-top: 1px solid var(--bg-surface); color: var(--text-secondary); cursor: text; line-height: 1.6; }
        
        .diagram-box { background: var(--bg-main); padding: 20px; border-radius: 6px; font-family: monospace; color: var(--accent); margin: 15px 0; border: 1px solid var(--border-color); white-space: pre; overflow-x: auto; font-size: 0.95rem; line-height: 1.4; }
        
        table.linq-table { width: 100%; border-collapse: collapse; margin-top: 15px; color: #e2e8f0; font-size: 0.9rem; }
        table.linq-table th, table.linq-table td { padding: 10px; border-bottom: 1px solid var(--border-color); text-align: left; }
        table.linq-table th { background: var(--bg-main); color: var(--accent); }
    </style>
</head>
<body>
    <button class="sidebar-toggle-btn" onclick="toggleSidebar()">☰</button>
    <aside class="sidebar">
        <h2>Knowledge Base</h2>
        <div class="sidebar-category">C# Training</div>
        <ul>
            <li><a href="01-visual-studio-2022.html">1. VS 2022 Overview</a></li>
            <li><a href="02-programming-guidelines.html">2. Guidelines & Commenting</a></li>
            <li><a href="13-lambda-expressions.html">13. Lambda Expressions</a></li>
            <li><a href="14-extension-methods.html">14. Extension Methods</a></li>
            <li><a href="15-linq.html" class="active">15. LINQ</a></li>
        </ul>
    </aside>
    
    <main class="main-content">
        <div class="topic-header">
            <h1>LINQ (Language Integrated Query)</h1>
            <p class="metadata">Difficulty: Intermediate | Category: C# Data Processing</p>
        </div>

        <div class="callout callout-info">
            <span class="callout-title">The Power of "What", Not "How"</span>
            <p>You know Lambda Expressions (how to pass logic) and Extension Methods (how to call it elegantly). Now, you will combine them to master <strong>LINQ</strong>. By the end of this module, you will be able to slice, filter, group, and query massive amounts of data with single, readable lines of code.</p>
        </div>

        <div class="topic-tabs">
            <button class="topic-tab-btn active" onclick="switchTopicTab('tab-fundamentals')">1. Fundamentals</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-operators')">2. Operators</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-architecture')">3. Under the Hood</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-demo')">4. Demo & Mistakes</button>
            <button class="topic-tab-btn" onclick="switchTopicTab('tab-practice')">5. Practice & Cheat Sheets</button>
        </div>

        <!-- TAB 1: FUNDAMENTALS -->
        <div id="tab-fundamentals" class="topic-tab-content active">
            
            <div class="concept-block">
                <h3 class="concept-title">1. The Problem LINQ Solves</h3>
                <p>Imagine we have a <code>List&lt;Article&gt;</code> and we want to find all published articles.</p>
                
                <div class="evolution-step">
                    <h4>Before LINQ (The "How" approach)</h4>
                    <p>We have to manually write the looping and filtering logic, telling the computer <em>how</em> to do the work step-by-step.</p>
                    <pre><code class="language-csharp">List&lt;Article&gt; publishedArticles = new List&lt;Article&gt;();
foreach (Article article in articles)
{
    if (article.Status == EnmArticleStatus.Published)
    {
        publishedArticles.Add(article);
    }
}</code></pre>
                </div>

                <div class="evolution-step">
                    <h4>With LINQ (The "What" approach)</h4>
                    <p>LINQ allows us to describe <em>what</em> data we want, leaving the underlying iteration mechanics to C#.</p>
                    <pre><code class="language-csharp">List&lt;Article&gt; publishedArticles = articles
    .Where(article => article.Status == EnmArticleStatus.Published)
    .ToList();</code></pre>
                </div>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">2. What Is LINQ?</h3>
                <p><strong>Language Integrated Query</strong> provides a consistent way to work with data.</p>
                <ul>
                    <li><strong>Language Integrated:</strong> The query syntax is built directly into C#. You get autocomplete, compile-time checking, and refactoring support.</li>
                    <li><strong>Query:</strong> A request for data (filtering, transforming, sorting).</li>
                </ul>
                <p>LINQ can be used with Arrays, <code>List&lt;T&gt;</code>, XML, and Database ORMs (like Entity Framework). Here is the mental model:</p>

                <div class="diagram-box">Data (List, Array, Database)
 ↓
LINQ Operators (Extension Methods)
 ↓
Filter / Transform / Sort / Group / Aggregate
 ↓
Result</div>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">3. The Foundation: LINQ, Lambdas, and Extension Methods</h3>
                <p>Look at the statement below. It relies entirely on the two previous modules you learned.</p>
                
                <div class="diagram-box">articles
   ↓
extension method
   ↓
Where(...)
   ↓
lambda expression
   ↓
condition applied to articles</div>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">4. IEnumerable&lt;T&gt; Before LINQ</h3>
                <p>Almost all LINQ methods operate on <code>IEnumerable&lt;T&gt;</code>. This is simply an interface that means: <em>"I am a collection that can be looped over one-by-one."</em></p>
                <p>Because <code>List&lt;Article&gt;</code> and <code>Article[]</code> (arrays) both implement <code>IEnumerable&lt;Article&gt;</code>, LINQ works seamlessly on both. LINQ-to-Objects operates over these in-memory sequences.</p>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">5. Where() — Filtering</h3>
                <div class="diagram-box">IEnumerable&lt;Article&gt; (Input)
     ↓
Where(article => article.Status == Published)
     ↓
IEnumerable&lt;Article&gt; (Output)</div>
                
                <p><strong>What it does:</strong> Filters a sequence based on a true/false condition.<br>
                <strong>The Lambda:</strong> Must return a <code>bool</code> (a <code>Predicate&lt;T&gt;</code>).</p>
                
                <pre><code class="language-csharp">// Single condition
var drafts = articles.Where(a => a.Status == EnmArticleStatus.Draft);

// Multiple conditions using && and ||
var popularPublished = articles.Where(a => 
    a.Status == EnmArticleStatus.Published && 
    a.ViewCount > 1000);</code></pre>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">6. Select() — Projection</h3>
                <p>Projection is one of the most important LINQ concepts. It means transforming the shape of the data.</p>

                <div class="diagram-box">IEnumerable&lt;Article&gt; (Input)
     ↓
Select(article => article.Title)
     ↓
IEnumerable&lt;string&gt; (Output)</div>

                <p><strong>What it does:</strong> Decides WHAT each item becomes. Notice the output type changes!<br>
                <strong>The Lambda:</strong> Returns whatever new shape you want (a <code>Func&lt;TInput, TOutput&gt;</code>).</p>

                <pre><code class="language-csharp">// Extracting a single property (Article -> string)
var titles = articles.Select(a => a.Title);

// Projecting into a new Anonymous Object (Article -> AnonymousType)
var summaries = articles.Select(a => new {
    a.Id,
    a.Title
});</code></pre>

                <div class="advanced-box">
                    <strong>Crucial Distinction:</strong><br>
                    <code>Where()</code> decides WHICH items remain (Input type = Output type).<br>
                    <code>Select()</code> decides WHAT each item becomes (Input type → New Output type).
                </div>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">7. Filtering + Projection (Chaining)</h3>
                <p>Because <code>Where</code> returns an <code>IEnumerable</code>, and <code>Select</code> operates on an <code>IEnumerable</code>, you can chain them infinitely.</p>
                
                <pre><code class="language-csharp">var publishedTitles = articles
    .Where(article => article.Status == EnmArticleStatus.Published)
    .Select(article => article.Title)
    .ToList();</code></pre>

                <div class="diagram-box">All Articles (List&lt;Article&gt;)
    ↓ Where
Published Articles (IEnumerable&lt;Article&gt;)
    ↓ Select
Article Titles (IEnumerable&lt;string&gt;)
    ↓ ToList
List&lt;string&gt;</div>
            </div>

        </div>

        <!-- TAB 2: OPERATORS -->
        <div id="tab-operators" class="topic-tab-content">
            
            <div class="concept-block">
                <h3 class="concept-title">8. Sorting</h3>
                <p>Sorting in LINQ is non-destructive (it returns a new sorted sequence, it doesn't modify the original list).</p>
                
                <pre><code class="language-csharp">// Primary Sort
var sorted = articles.OrderBy(a => a.Title);
var sortedDesc = articles.OrderByDescending(a => a.ViewCount);

// Secondary Sort (Use ThenBy, NEVER a second OrderBy)
var multiSorted = articles
    .OrderBy(a => a.Status)
    .ThenBy(a => a.Title);</code></pre>
                
                <div class="mistake-box">
                    <span class="mistake-title">Common Mistake</span>
                    Writing <code>.OrderBy(a => a.Status).OrderBy(a => a.Title)</code> is completely wrong. The second OrderBy destroys the first sort. Always use <code>ThenBy()</code> for secondary sorting.
                </div>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">9. Element Operators (First, Single, etc.)</h3>
                <p>These extract a specific item from a sequence.</p>

                <table class="linq-table">
                    <tr>
                        <th>Method</th>
                        <th>If Sequence is Empty / No Match</th>
                        <th>If Multiple Matches Exist</th>
                    </tr>
                    <tr>
                        <td><code>First()</code></td>
                        <td style="color:#ef4444;">Throws Exception</td>
                        <td>Returns first item</td>
                    </tr>
                    <tr>
                        <td><code>FirstOrDefault()</code></td>
                        <td>Returns default (e.g., <code>null</code> for objects, <code>0</code> for ints)</td>
                        <td>Returns first item</td>
                    </tr>
                    <tr>
                        <td><code>Single()</code></td>
                        <td style="color:#ef4444;">Throws Exception</td>
                        <td style="color:#ef4444;">Throws Exception</td>
                    </tr>
                    <tr>
                        <td><code>SingleOrDefault()</code></td>
                        <td>Returns default</td>
                        <td style="color:#ef4444;">Throws Exception</td>
                    </tr>
                </table>

                <pre><code class="language-csharp">// Finds the first published article. If none exist, returns null.
Article firstPub = articles.FirstOrDefault(a => a.Status == EnmArticleStatus.Published);

if (firstPub != null) { ... } // Always check for null after FirstOrDefault!</code></pre>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">10. Any() and All()</h3>
                <p>These return a <code>bool</code>.</p>
                
                <pre><code class="language-csharp">// True if AT LEAST ONE draft exists
bool hasDrafts = articles.Any(a => a.Status == EnmArticleStatus.Draft);

// True if EVERY article has views >= 0
bool allValid = articles.All(a => a.ViewCount >= 0);</code></pre>

                <div class="advanced-box">
                    <strong>Empty Sequence Rule:</strong> <code>All()</code> returns <strong>true</strong> on an empty sequence (because 0 items fail the condition). <code>Any()</code> returns <strong>false</strong> on an empty sequence.
                </div>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">11. Aggregation</h3>
                <pre><code class="language-csharp">int totalArticles = articles.Count();
int draftCount = articles.Count(a => a.Status == EnmArticleStatus.Draft);

int totalViews = articles.Sum(a => a.ViewCount);
double avgViews = articles.Average(a => a.ViewCount);</code></pre>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">12. Pagination & Partitioning (Skip, Take)</h3>
                <div class="diagram-box">Skip(10) → Ignore first 10 items
Take(10) → Take the next 10 items and stop</div>
                
                <pre><code class="language-csharp">// Get Page 2 (assuming 10 items per page)
var page2 = articles
    .OrderBy(a => a.Title) // ALWAYS order before pagination!
    .Skip(10)
    .Take(10)
    .ToList();</code></pre>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">13. GroupBy() — Grouping Data</h3>
                <p><code>GroupBy</code> partitions your data into chunks based on a key.</p>
                
                <div class="diagram-box">Articles
   ↓
GroupBy(article => article.Status)
   ↓
Group 1 (Key: Draft) -> [Article1, Article4]
Group 2 (Key: Published) -> [Article2, Article3]</div>

                <pre><code class="language-csharp">var grouped = articles.GroupBy(a => a.Status);

foreach (var group in grouped)
{
    Console.WriteLine($"Status: {group.Key}"); // The key is the Status
    foreach (Article article in group)
    {
        Console.WriteLine($" - {article.Title}");
    }
}</code></pre>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">14. SelectMany() — Flattening</h3>
                <p>If <code>Select()</code> creates a list of lists, <code>SelectMany()</code> flattens them into a single list.</p>

                <div class="diagram-box">Select(article => article.Tags)
    Article 1 → ["C#", "LINQ"]
    Article 2 → [".NET"]
    Result: IEnumerable&lt;List&lt;string&gt;&gt; (A list of lists)

SelectMany(article => article.Tags)
    Article 1 → ["C#", "LINQ"]
    Article 2 → [".NET"]
    Result: IEnumerable&lt;string&gt; ("C#", "LINQ", ".NET")</div>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">15. Joining Data</h3>
                <p>LINQ can join two sequences together based on matching keys, similar to SQL.</p>

                <div class="diagram-box">Article.AuthorId
       matches
User.Id</div>

                <pre><code class="language-csharp">var articleAuthors = articles.Join(
    users, // the sequence to join with
    article => article.AuthorId, // key from articles
    user => user.Id, // key from users
    (article, user) => new { // what to project when a match is found
        article.Title,
        user.Name
    });</code></pre>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">16. Set Operations</h3>
                <ul>
                    <li><code>Distinct()</code>: Removes duplicates. <em>(Note: For custom classes, you must implement equality/IEquatable, or LINQ uses reference equality)</em>.</li>
                    <li><code>Union(other)</code>: Combines two sequences, removing duplicates.</li>
                    <li><code>Intersect(other)</code>: Returns only items present in BOTH sequences.</li>
                    <li><code>Except(other)</code>: Returns items in the first sequence that are NOT in the second.</li>
                </ul>
            </div>

        </div>

        <!-- TAB 3: ARCHITECTURE -->
        <div id="tab-architecture" class="topic-tab-content">
            
            <div class="concept-block">
                <h3 class="concept-title">17. Deferred Execution (Crucial)</h3>
                <p>Most LINQ operators (like <code>Where</code>, <code>Select</code>, <code>OrderBy</code>) <strong>do not execute immediately</strong>. They merely build a set of instructions (a query). The query only actually runs when you iterate over it (e.g., in a <code>foreach</code> loop, or by calling <code>ToList()</code>).</p>

                <div class="diagram-box">Create query: var query = articles.Where(...)
     ↓
No enumeration yet (the list has not been searched)
     ↓
Change source: articles.Add(new Article(...))
     ↓
Enumerate query: foreach(var a in query)
     ↓
Current source data is observed! The new article IS included!</div>

                <div class="mistake-box">
                    <span class="mistake-title">Multiple Enumeration Danger</span>
                    <p>If you have a deferred query and you do: <br><code>int count = query.Count();</code><br><code>Article first = query.First();</code><br>The query fully executes <strong>twice</strong>! If the query is expensive, this is a major performance bug. Fix this by materializing the query once.</p>
                </div>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">18. Materialization (Executing the Query)</h3>
                <p>To force a deferred query to execute immediately and save the results into memory, use a materialization operator.</p>
                
                <table class="linq-table">
                    <tr><th>Operator</th><th>Purpose</th></tr>
                    <tr><td><code>ToList()</code></td><td>Executes query, returns a concrete <code>List&lt;T&gt;</code>.</td></tr>
                    <tr><td><code>ToArray()</code></td><td>Executes query, returns a concrete array <code>T[]</code>.</td></tr>
                    <tr><td><code>ToDictionary()</code></td><td>Executes query, creates a Dictionary. <em>Throws if duplicate keys exist.</em></td></tr>
                    <tr><td><code>ToHashSet()</code></td><td>Executes query, returns a unique HashSet.</td></tr>
                </table>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">19. Query Syntax vs Method Syntax</h3>
                <p>Everything you've learned so far is <strong>Method Syntax</strong>. LINQ also offers <strong>Query Syntax</strong>, which looks a lot like SQL.</p>
                
                <pre><code class="language-csharp">// Method Syntax
var published = articles
    .Where(a => a.Status == EnmArticleStatus.Published)
    .OrderByDescending(a => a.ViewCount)
    .Select(a => a.Title);

// Query Syntax (compiles to the exact same code above)
var published = from a in articles
                where a.Status == EnmArticleStatus.Published
                orderby a.ViewCount descending
                select a.Title;</code></pre>
                
                <p>Method syntax is more common today, and many operators (like <code>First</code>, <code>Skip</code>, <code>Count</code>) do not have query syntax equivalents.</p>
            </div>

            <div class="concept-block">
                <h3 class="concept-title">20. IEnumerable&lt;T&gt; vs IQueryable&lt;T&gt;</h3>
                <p>This is the secret to how LINQ connects to databases.</p>

                <div class="diagram-box">IEnumerable&lt;T&gt; (LINQ to Objects)
    ↓
Executes inside your application's RAM.
The delegates (lambdas) are compiled C# code.

IQueryable&lt;T&gt; (LINQ to Databases / EF Core)
    ↓
Does NOT execute C# lambdas in RAM.
Builds an "Expression Tree" (a data structure describing your code).
A Query Provider translates that tree into SQL!</div>

                <p>When you do <code>dbContext.Articles.Where(a => a.Title == "SQL")</code>, the Entity Framework provider looks at your lambda, translates it to <code>SELECT * FROM Articles WHERE Title = 'SQL'</code>, and executes it on the database server. It does NOT download the entire table into memory first!</p>
            </div>

        </div>

        <!-- TAB 4: DEMO & MISTAKES -->
        <div id="tab-demo" class="topic-tab-content">

            <div class="concept-block">
                <h3 class="concept-title">21. Practical Mistakes & Performance Guidance</h3>
                
                <details>
                    <summary>1. Confusing Where() and Select()</summary>
                    <div><code>Where</code> filters rows. <code>Select</code> shapes columns. Don't try to change the object shape inside a <code>Where</code> clause.</div>
                </details>
                <details>
                    <summary>2. Calling First() when empty</summary>
                    <div>If a list might be empty, use <code>FirstOrDefault()</code>, then check if the result is default/null.</div>
                </details>
                <details>
                    <summary>3. Using Single() when multiple items exist</summary>
                    <div><code>Single</code> asserts that EXACTLY ONE item matches. If two items match, it throws an exception. If you just want the first one, use <code>First()</code>.</div>
                </details>
                <details>
                    <summary>4. Confusing Count() with Any()</summary>
                    <div><strong>Bad:</strong> <code>if (articles.Count() > 0)</code> (This iterates the entire list to count them all).<br><strong>Good:</strong> <code>if (articles.Any())</code> (This stops the millisecond it finds one item).</div>
                </details>
                <details>
                    <summary>5. Calling ToList() too early</summary>
                    <div><strong>Bad:</strong> <code>articles.ToList().Where(...)</code>. The <code>ToList()</code> materializes the massive list into memory BEFORE filtering. Put <code>ToList()</code> at the absolute end of the chain.</div>
                </details>
                <details>
                    <summary>6. Skip/Take without OrderBy</summary>
                    <div>Databases and HashSets do not guarantee order. Always apply deterministic ordering before pagination.</div>
                </details>
            </div>
            
            <div class="concept-block">
                <h3 class="concept-title">22. Complete Knowledge Base LINQ Demo</h3>
                <p>A full program combining everything into practical, real-world queries.</p>
                
                <div class="code-container" style="border-radius: 6px 6px 0 0;">
                    <div class="code-header"><span>C# - Program.cs</span><button class="copy-btn">Copy</button></div>
                    <pre><code class="language-csharp">using System;
using System.Collections.Generic;
using System.Linq;

namespace KnowledgeBase 
{
    public enum EnmArticleStatus { Draft, Published }

    public class User { public int Id { get; set; } public string Name { get; set; } }

    public class Article 
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public int AuthorId { get; set; }
        public EnmArticleStatus Status { get; set; }
        public int ViewCount { get; set; }
        public List&lt;string&gt; Tags { get; set; } = new List&lt;string&gt;();
    }

    class Program 
    {
        static void Main() 
        {
            var users = new List&lt;User&gt; {
                new User { Id = 1, Name = "Alice" },
                new User { Id = 2, Name = "Bob" }
            };

            var articles = new List&lt;Article&gt; {
                new Article { Id = 10, Title = "C# Basics", AuthorId = 1, Status = EnmArticleStatus.Published, ViewCount = 500, Tags = new List&lt;string&gt;{"C#", "Beginner"} },
                new Article { Id = 11, Title = "LINQ Guide", AuthorId = 1, Status = EnmArticleStatus.Draft, ViewCount = 0, Tags = new List&lt;string&gt;{"C#", "LINQ"} },
                new Article { Id = 12, Title = "SQL Tips", AuthorId = 2, Status = EnmArticleStatus.Published, ViewCount = 1200, Tags = new List&lt;string&gt;{"SQL"} }
            };

            // 1. Where, OrderByDescending, Select, ToList (The classic chain)
            var report = articles
                .Where(a => a.Status == EnmArticleStatus.Published)
                .OrderByDescending(a => a.ViewCount)
                .Select(a => new { a.Title, a.ViewCount })
                .ToList();

            Console.WriteLine("--- Top Published Articles ---");
            report.ForEach(r => Console.WriteLine($"{r.Title} ({r.ViewCount} views)"));

            // 2. SelectMany (Flattening all tags)
            var allUniqueTags = articles
                .SelectMany(a => a.Tags)
                .Distinct()
                .ToList();
                
            Console.WriteLine($"\nSystem Tags: {string.Join(", ", allUniqueTags)}");

            // 3. GroupBy
            var groupedByAuthor = articles.GroupBy(a => a.AuthorId);
            Console.WriteLine("\n--- Articles by Author ID ---");
            foreach(var group in groupedByAuthor) {
                Console.WriteLine($"Author {group.Key} wrote {group.Count()} articles.");
            }

            // 4. Join
            var articleAuthors = articles.Join(
                users,
                article => article.AuthorId,
                user => user.Id,
                (article, user) => $"{article.Title} by {user.Name}"
            ).ToList();

            Console.WriteLine("\n--- Join Result ---");
            articleAuthors.ForEach(Console.WriteLine);
            
            Console.ReadLine();
        }
    }
}</code></pre>
                </div>
                <div class="console-output"><strong>Console Output:</strong><pre>--- Top Published Articles ---
SQL Tips (1200 views)
C# Basics (500 views)

System Tags: C#, Beginner, LINQ, SQL

--- Articles by Author ID ---
Author 1 wrote 2 articles.
Author 2 wrote 1 articles.

--- Join Result ---
C# Basics by Alice
LINQ Guide by Alice
SQL Tips by Bob</pre></div>
            </div>
        </div>

        <!-- TAB 5: PRACTICE & CHEAT SHEETS -->
        <div id="tab-practice" class="topic-tab-content">
            
            <div class="concept-block">
                <h3 class="concept-title">Cheat Sheets</h3>
                <div class="diagram-box">Where      → Which items?
Select     → What shape?
SelectMany → Flatten what?
OrderBy    → How sorted?
GroupBy    → How grouped?
Any        → Does at least one exist?
All        → Do all satisfy?
First      → Give me the first (or crash)
Single     → There must be exactly one (or crash)
ToList     → Execute/materialize into a concrete List</div>
            </div>

            <h2>Practice & Validation</h2>

            <h3>Beginner (Write the LINQ)</h3>
            <details><summary>1. Get all articles with a ViewCount > 100.</summary><div><code>articles.Where(a => a.ViewCount > 100)</code></div></details>
            <details><summary>2. Extract just the IDs from a list of articles.</summary><div><code>articles.Select(a => a.Id)</code></div></details>
            <details><summary>3. Sort articles alphabetically by Title.</summary><div><code>articles.OrderBy(a => a.Title)</code></div></details>
            <details><summary>4. Check if ANY article is in Draft status.</summary><div><code>articles.Any(a => a.Status == EnmArticleStatus.Draft)</code></div></details>
            <details><summary>5. Get the total number of articles.</summary><div><code>articles.Count()</code></div></details>
            <details><summary>6. Get the first article, or null if none exist.</summary><div><code>articles.FirstOrDefault()</code></div></details>
            <details><summary>7. Get a list of unique AuthorIds.</summary><div><code>articles.Select(a => a.AuthorId).Distinct()</code></div></details>
            <details><summary>8. Skip the first 5 articles.</summary><div><code>articles.Skip(5)</code></div></details>
            <details><summary>9. Take only 3 articles.</summary><div><code>articles.Take(3)</code></div></details>
            <details><summary>10. Combine Skip and Take for page 3 (10 per page).</summary><div><code>articles.Skip(20).Take(10)</code></div></details>

            <h3 style="margin-top:30px;">Intermediate</h3>
            <details><summary>1. Get the Titles of all Published articles, sorted by Title.</summary><div><code>articles.Where(a => a.Status == EnmArticleStatus.Published).OrderBy(a => a.Title).Select(a => a.Title)</code></div></details>
            <details><summary>2. Group articles by Status.</summary><div><code>articles.GroupBy(a => a.Status)</code></div></details>
            <details><summary>3. Create a Dictionary where the Key is the Article Id and the Value is the Article itself.</summary><div><code>articles.ToDictionary(a => a.Id)</code></div></details>
            <details><summary>4. Convert this method syntax to query syntax: `articles.Where(a => a.Id == 1).Select(a => a.Title)`</summary><div><code>from a in articles where a.Id == 1 select a.Title</code></div></details>

            <h3 style="margin-top:30px;">Find the Error</h3>
            <details><summary>1. `var first = articles.First(a => a.Id == -99);` (Assume no such ID exists)</summary><div><strong>Error:</strong> `First()` throws an exception if no item matches. Use `FirstOrDefault()` if a miss is expected.</div></details>
            <details><summary>2. `var titles = articles.Select(a => a.Title).Where(a => a.ViewCount > 10);`</summary><div><strong>Error:</strong> Once you `Select(a => a.Title)`, the sequence becomes strings. Strings don't have a `ViewCount`. You must `Where` BEFORE you `Select`.</div></details>
            <details><summary>3. `articles.OrderBy(a => a.Status).OrderBy(a => a.Title)`</summary><div><strong>Error:</strong> The second `OrderBy` destroys the first sort. Use `.ThenBy(a => a.Title)`.</div></details>
            <details><summary>4. `var page = articles.Skip(10).Take(10).ToList();`</summary><div><strong>Error:</strong> Pagination without `OrderBy` is dangerous. The data order is not guaranteed. Always `OrderBy` first.</div></details>

            <h3 style="margin-top:30px;">Interview Questions</h3>
            <details><summary>1. What is the difference between IEnumerable and IQueryable?</summary><div>IEnumerable represents an in-memory sequence of data, executing LINQ delegates via C#. IQueryable represents a query expression tree, typically translated by a provider (like Entity Framework) into SQL to run on a database.</div></details>
            <details><summary>2. What is Deferred Execution?</summary><div>The concept where building a LINQ query does not actually execute it or fetch data. The query only executes when it is enumerated (e.g., via foreach or ToList).</div></details>
            <details><summary>3. Explain FirstOrDefault() vs SingleOrDefault().</summary><div>Both return default (null) if no match is found. However, `FirstOrDefault()` simply returns the first match if there are multiple. `SingleOrDefault()` enforces uniqueness; if multiple matches exist, it throws an exception.</div></details>

        </div>

        <div class="nav-buttons">
            <a href="14-extension-methods.html">&larr; Previous: Extension Methods</a>
            <a href="#">Next: Databases & ORM &rarr;</a>
        </div>
    </main>
    
    <script src="../../js/ui-enhancements.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-csharp.min.js"></script>
    
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
