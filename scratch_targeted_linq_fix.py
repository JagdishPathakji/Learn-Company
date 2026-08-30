import os

filepath = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\15-linq.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. GroupJoin Section
old_groupjoin = """// GroupJoin (Left Join Concept)
// Groups all articles belonging to each user. If a user has no articles, 
// the user is still included, but their 'userArticles' collection is empty.
var usersWithArticles = users.GroupJoin(
    articles,
    user => user.Id,
    article => article.AuthorId,
    (user, userArticles) => new { 
        user.Name, 
        Articles = userArticles.DefaultIfEmpty() // Ensures empty collections are handled
    });"""

new_groupjoin = """// GroupJoin (Grouped Matching / Left Join pattern)
// GroupJoin produces each element from the outer sequence together with a collection of matching elements from the inner sequence.
// By itself, it is "grouped matching". We can use it to create a left-join-like result where every user is included, even if they have 0 articles.
var usersWithArticles = users.GroupJoin(
    articles,
    user => user.Id,
    article => article.AuthorId,
    (user, userArticles) => new { 
        UserName = user.Name, 
        // userArticles will be empty if the user wrote nothing. 
        // DefaultIfEmpty() ensures we can still iterate over a default value if needed in complex left joins.
        Articles = userArticles 
    });"""
content = content.replace(old_groupjoin, new_groupjoin)

# 2. Distinct Equality Explanation
old_distinct = """<p><code>Distinct()</code> uses equality comparison to determine whether two elements are equal. For custom objects, the result depends on the equality implementation being used (if value-based equality isn't defined, separate objects with identical property values are treated as different objects based on reference equality).</p>"""

new_distinct = """<p><code>Distinct()</code> determines duplicates using equality comparison. For reference types (like classes), if value equality has not been implemented, different object instances with identical property values are normally considered different objects in memory.</p>
                <p>LINQ relies on the <code>Equals()</code> and <code>GetHashCode()</code> methods (or the <code>IEquatable&lt;T&gt;</code> interface) to determine this. LINQ also provides overloads that accept a custom equality comparer.</p>
                <pre><code class="language-csharp">var a1 = new Article { Id = 1, Title = "C#" };
var a2 = new Article { Id = 1, Title = "C#" };
var list = new List&lt;Article&gt; { a1, a2 };

// Distinct() will return BOTH articles! 
// Because they are two separate objects in memory, LINQ sees them as different unless you implement IEquatable&lt;Article&gt;.
var unique = list.Distinct();</code></pre>"""
content = content.replace(old_distinct, new_distinct)

# 3. IEnumerable vs IQueryable
old_iqueryable = """<p>With EF Core, LINQ operations that the provider can translate are normally converted into SQL and executed by the database, allowing filtering/projection to happen in the database instead of first loading all rows into application memory. <em>(Note: Not every arbitrary C# expression can necessarily be translated by every provider).</em></p>"""

new_iqueryable = """<p>With EF Core, LINQ operations that the provider can translate are normally converted into SQL and executed by the database, allowing filtering/projection to happen in the database instead of first loading all rows into application memory. <em>(Note: Not every arbitrary C# expression can necessarily be translated by every provider).</em></p>
                
                <p>Understanding this boundary is critical for performance:</p>
                <pre><code class="language-csharp">// 1. IQueryable: Query can continue being translated into SQL by the provider
var query = dbContext.Articles.Where(a => a.ViewCount > 100);

// 2. AsEnumerable: Subsequent LINQ-to-Objects operations happen in application memory
var memoryQuery = dbContext.Articles.AsEnumerable().Where(a => a.ViewCount > 100);

// 3. ToList: Query executes immediately and results are materialized into memory
var list = dbContext.Articles.ToList();</code></pre>"""
content = content.replace(old_iqueryable, new_iqueryable)

# 4. Deferred Execution (Streaming vs Buffering)
old_deferred = """<p>Note: Different operators have different internal behaviors upon enumeration. For example, <code>OrderBy()</code> must obtain all the elements needed to produce sorted results before yielding the first item.</p>"""

new_deferred = """<p>While deferred queries do not execute until enumeration, different operators behave differently when enumeration finally happens:</p>
                <ul>
                    <li><strong>Streaming behavior:</strong> Operators like <code>Where</code>, <code>Select</code>, <code>Skip</code>, and <code>Take</code> process and yield elements one-by-one as they enumerate the source.</li>
                    <li><strong>Buffering behavior:</strong> Operators like <code>OrderBy</code> and <code>GroupBy</code> must consume significant (or all) input elements before they can produce their first result (e.g., you can't know what the alphabetically first item is until you look at all of them).</li>
                </ul>"""
content = content.replace(old_deferred, new_deferred)

# 5. FirstOrDefault Explanation
old_first = """<p>These extract a specific item from a sequence.</p>"""

new_first = """<p>These extract a specific item from a sequence. Methods ending in <code>OrDefault</code> (like <code>FirstOrDefault()</code>, <code>SingleOrDefault()</code>, and <code>ElementAtOrDefault()</code>) return the type's default value when no result exists. For reference types, this is normally <code>null</code>. For value types, it can be <code>0</code> or <code>false</code>. <em>(Note: If nullable reference types are enabled, the compiler may flag this, and you must handle the possibility of a no-result scenario).</em></p>"""
content = content.replace(old_first, new_first)

# 6. Add Other Useful Operators
other_operators = """
            <div class="concept-block">
                <h3 class="concept-title">16b. Other Useful LINQ Operators</h3>
                <p>These supporting operators are highly useful for specific scenarios:</p>
                <ul>
                    <li><code>OfType&lt;T&gt;()</code>: Filters elements based on their ability to be cast to a specified type. <em>(e.g., <code>users.OfType&lt;Author&gt;()</code>)</em></li>
                    <li><code>Cast&lt;T&gt;()</code>: Casts all elements to a specified type (throws an exception if cast fails).</li>
                    <li><code>DefaultIfEmpty()</code>: Returns the elements of the sequence, or a default valued singleton collection if the sequence is empty.</li>
                    <li><code>Reverse()</code>: Inverts the order of the elements.</li>
                    <li><code>Zip()</code>: Applies a specified function to the corresponding elements of two sequences, producing a sequence of the results.</li>
                    <li><code>Aggregate()</code>: Applies an accumulator function over a sequence (e.g., building a custom comma-separated string).</li>
                    <li><code>LongCount()</code>: Returns an <code>Int64</code> count for massively large sequences.</li>
                    <li><code>ElementAt(index)</code> / <code>ElementAtOrDefault(index)</code>: Returns the element at a specific index.</li>
                    <li><code>DistinctBy(a => a.Title)</code>: Removes duplicates based on a specific key selector.</li>
                    <li><code>MinBy(a => a.ViewCount)</code> / <code>MaxBy(a => a.ViewCount)</code>: Returns the element that has the minimum/maximum value for a specific key.</li>
                    <li><code>Chunk(10)</code>: Splits the elements of a sequence into chunks of size at most <code>size</code>.</li>
                </ul>
            </div>
"""
content = content.replace('        </div>\n\n        <!-- TAB 3: ARCHITECTURE -->', other_operators + '        </div>\n\n        <!-- TAB 3: ARCHITECTURE -->')


# 7. ToDictionary vs ToLookup
old_lookup = """// ToLookup (Immediate materialization)
var articlesByAuthor = articles.ToLookup(a => a.AuthorId);
var bobArticles = articlesByAuthor[2]; // Fast retrieval of AuthorId 2's articles"""

new_lookup = """// ToDictionary vs ToLookup
// ToDictionary: Expects exactly ONE value per key. Duplicate keys throw an exception!
// ToLookup: Allows MULTIPLE values per key. Perfect for one-to-many lookups!

// If Author 1 has written 3 articles, this THROWS an Exception:
// var dict = articles.ToDictionary(a => a.AuthorId);

// This works perfectly, grouping all 3 articles under Author 1:
var articlesByAuthor = articles.ToLookup(a => a.AuthorId);
var bobArticles = articlesByAuthor[2]; // Fast retrieval of AuthorId 2's articles"""
content = content.replace(old_lookup, new_lookup)

# 8. Query Syntax
old_query = """<p>Method syntax is more common today, and many operators (like <code>First</code>, <code>Skip</code>, <code>Count</code>) do not have query syntax equivalents.</p>"""

new_query = """<p>Method syntax is generally more commonly encountered in modern C# code, and many operators (like <code>First</code>, <code>Skip</code>, <code>Count</code>) do not have direct query syntax keywords. However, query syntax is still highly useful to understand because it appears in existing code and can cleanly express complex queries using keywords like <code>join</code>, <code>group</code>, <code>let</code>, and <code>into</code>:</p>
                <pre><code class="language-csharp">var complexQuery = from a in articles
                   join u in users on a.AuthorId equals u.Id
                   group a by u.Name into authorGroup
                   select new { Author = authorGroup.Key, Count = authorGroup.Count() };</code></pre>"""
content = content.replace(old_query, new_query)

# 9. Contains Comparer
old_contains = """// Contains: Checks if an item exists based on equality
bool hasId101 = authorIds.Contains(101);"""

new_contains = """// Contains: Checks if an item exists based on equality
bool hasId101 = authorIds.Contains(101);
// Note: Contains() can also accept an equality comparer when custom equality behavior is required."""
content = content.replace(old_contains, new_contains)


# 10. Program.cs GroupJoin addition
old_program_join = """            // 5. Join (Inner) & GroupJoin (Left Concept)
            var articleAuthors = articles.Join(
                users, a => a.AuthorId, u => u.Id,
                (a, u) => $"{a.Title} by {u.Name}"
            ).ToList();"""
            
new_program_join = """            // 5. Join (Inner) & GroupJoin (Grouped Matching / Left Join Concept)
            var articleAuthors = articles.Join(
                users, a => a.AuthorId, u => u.Id,
                (a, u) => $"{a.Title} by {u.Name}"
            ).ToList();
            
            var authorsWithArticles = users.GroupJoin(
                articles, u => u.Id, a => a.AuthorId,
                (u, aList) => new { Author = u.Name, ArticleCount = aList.Count() }
            ).ToList();"""
content = content.replace(old_program_join, new_program_join)


# 11. Practice additions
old_practice_intermediate = """<h3 style="margin-top:30px;">Intermediate</h3>"""
new_practice_intermediate = """<h3 style="margin-top:30px;">Intermediate</h3>
            <details><summary>0. You need a fast lookup structure mapping `AuthorId` to their many `Articles`. Do you use `ToDictionary` or `ToLookup`?</summary><div><code>ToLookup</code>. `ToDictionary` throws an exception if multiple items share the same key.</div></details>
            <details><summary>0b. Explain the behavioral difference between an `IQueryable` query and an `IEnumerable` query.</summary><div>An `IEnumerable` query executes C# delegates in application memory. An `IQueryable` query builds an expression tree that a provider (like EF Core) translates into a native query (like SQL) to be executed by the database.</div></details>"""
content = content.replace(old_practice_intermediate, new_practice_intermediate)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
