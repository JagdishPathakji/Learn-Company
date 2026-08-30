import os

filepath = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\15-linq.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. GroupJoin / Left Join Expansion
old_join = """// GroupJoin produces each element from the outer sequence together with a collection of matching elements from the inner sequence.
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

new_join = """// 1. GroupJoin (Grouped Matching)
// Produces each outer element together with a collection of matching inner elements.
var groupedMatches = users.GroupJoin(
    articles, user => user.Id, article => article.AuthorId,
    (user, userArticles) => new { User = user, Articles = userArticles }
);

// 2. Traditional Left Outer Join (GroupJoin + SelectMany + DefaultIfEmpty)
// To get a flat "SQL-style" left join, we flatten the grouped matches, providing a null article if the collection is empty.
var leftJoin = users.GroupJoin(
    articles, user => user.Id, article => article.AuthorId,
    (user, userArticles) => new { user, userArticles }
).SelectMany(
    x => x.userArticles.DefaultIfEmpty(), 
    (x, article) => new { x.user.Name, ArticleTitle = article?.Title ?? "No Articles" }
);

// 3. .NET 10 LeftJoin and RightJoin
// Modern .NET 10+ introduces dedicated operators to simplify this exact pattern natively:
// var modernLeftJoin = users.LeftJoin(articles, u => u.Id, a => a.AuthorId, (u, a) => new { u.Name, a?.Title });"""
content = content.replace(old_join, new_join)

# 2. Aggregation Empty Sequences Precision
old_agg = """<p><em>Warning: Calling Average, Min, or Max on an empty sequence will throw an exception unless the type is nullable.</em></p>"""

new_agg = """<p><em>Warning: Calling <code>Average()</code>, <code>Min()</code>, or <code>Max()</code> on an empty sequence of non-nullable value types will throw an <code>InvalidOperationException</code>. However, <code>Sum()</code> safely returns 0 on an empty sequence. If you expect empty sequences, consider projecting to nullable types (e.g., <code>articles.Max(a => (int?)a.ViewCount)</code>) which will safely return <code>null</code> instead of throwing.</em></p>"""
content = content.replace(old_agg, new_agg)


# 3. Count vs Any Technical Precision
old_mistake4 = """<details><summary>4. Confusing Count() with Any()</summary><div><strong>Need the number?</strong> → <code>Count()</code><br><strong>Only need to know whether something exists?</strong> → <code>Any()</code> (Any communicates intent better and can stop as soon as it finds a match).</div></details>"""

new_mistake4 = """<details><summary>4. Confusing Count() with Any()</summary><div><strong>Need the number?</strong> → <code>Count()</code><br><strong>Only need existence?</strong> → <code>Any()</code>. <br><em>Precision Note:</em> If the underlying source implements <code>ICollection&lt;T&gt;</code> (like a <code>List&lt;T&gt;</code>), <code>Count()</code> is an O(1) fast property lookup. However, if applied to a deferred LINQ query (e.g., after a <code>Where</code>), <code>Count()</code> must fully traverse and evaluate the entire remaining sequence. <code>Any()</code> strictly halts evaluation the millisecond the first match is found, making it vastly superior for existence checks on queries.</div></details>"""
content = content.replace(old_mistake4, new_mistake4)


# 4. Query Syntax Expansion (let, into)
old_query = """<pre><code class="language-csharp">var complexQuery = from a in articles
                   join u in users on a.AuthorId equals u.Id
                   group a by u.Name into authorGroup
                   select new { Author = authorGroup.Key, Count = authorGroup.Count() };</code></pre>"""

new_query = """<pre><code class="language-csharp">var complexQuery = from a in articles
                   join u in users on a.AuthorId equals u.Id
                   let viewScore = a.ViewCount * 1.5 // 'let' introduces a new local variable
                   group a by u.Name into authorGroup // 'group ... into' continues the query pipeline
                   select new { Author = authorGroup.Key, Count = authorGroup.Count() };</code></pre>"""
content = content.replace(old_query, new_query)


# 5. Set Operators Expansion
old_set = """var uniqueCombined = list1.Union(list2); // Removes duplicates
var commonOnly = list1.Intersect(list2);
var difference = list1.Except(list2);"""

new_set = """var uniqueCombined = list1.Union(list2); // Removes duplicates
var commonOnly = list1.Intersect(list2);
var difference = list1.Except(list2);

// Modern .NET Key-based Set Operators
var unionByKey = list1.UnionBy(list2, a => a.Id);
var intersectByKey = list1.IntersectBy(list2.Select(a => a.Id), a => a.Id);
var exceptByKey = list1.ExceptBy(list2.Select(a => a.Id), a => a.Id);"""
content = content.replace(old_set, new_set)


# 6. Section 16b Exact Examples Addition
old_16b = """            <div class="concept-block">
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
            </div>"""

new_16b = """            <div class="concept-block">
                <h3 class="concept-title">16b. Other Useful LINQ Operators</h3>
                <p>These supporting operators are highly useful for specific scenarios:</p>
                <details><summary><code>OfType&lt;T&gt;()</code> and <code>Cast&lt;T&gt;()</code></summary><div>Filters (or casts) elements based on type.<br><pre><code class="language-csharp">var authors = allUsers.OfType&lt;Author&gt;(); // Safely ignores non-Authors
var articles = objects.Cast&lt;Article&gt;(); // Throws if cast fails</code></pre></div></details>
                <details><summary><code>DefaultIfEmpty()</code></summary><div>Returns the sequence, or a default-valued singleton collection if empty.<br><pre><code class="language-csharp">var safeList = articles.Where(a => a.Id == -1).DefaultIfEmpty(new Article { Title = "Empty" });</code></pre></div></details>
                <details><summary><code>Reverse()</code></summary><div>Inverts the order of the elements.<br><pre><code class="language-csharp">var backwards = articles.Reverse();</code></pre></div></details>
                <details><summary><code>Zip()</code></summary><div>Pairs up elements of two sequences based on index.<br><pre><code class="language-csharp">var paired = articles.Zip(users, (a, u) => $"{a.Title} by {u.Name}");</code></pre></div></details>
                <details><summary><code>Aggregate()</code></summary><div>Applies a rolling accumulator function over a sequence.<br><pre><code class="language-csharp">var csv = articles.Select(a => a.Title).Aggregate((current, next) => current + ", " + next);</code></pre></div></details>
                <details><summary><code>LongCount()</code></summary><div>Returns an <code>Int64</code> count for massively large sequences (bypassing the 2 billion limit of <code>int</code>).<br><pre><code class="language-csharp">long total = dbContext.Articles.LongCount();</code></pre></div></details>
                <details><summary><code>ElementAt()</code> / <code>ElementAtOrDefault()</code></summary><div>Retrieves an element at a specific index. Throws / returns default if out of bounds.<br><pre><code class="language-csharp">var thirdArticle = articles.ElementAtOrDefault(2);</code></pre></div></details>
                <details><summary><code>DistinctBy()</code></summary><div>Removes duplicates based on a specific key selector (cleaner than custom comparers).<br><pre><code class="language-csharp">var uniqueAuthors = articles.DistinctBy(a => a.AuthorId);</code></pre></div></details>
                <details><summary><code>MinBy()</code> / <code>MaxBy()</code></summary><div>Returns the actual element that possesses the min/max value, not just the value itself.<br><pre><code class="language-csharp">Article mostViewed = articles.MaxBy(a => a.ViewCount);</code></pre></div></details>
                <details><summary><code>Chunk()</code></summary><div>Splits the elements into batches of a specific size.<br><pre><code class="language-csharp">IEnumerable&lt;Article[]&gt; batches = articles.Chunk(10);</code></pre></div></details>
            </div>"""
content = content.replace(old_16b, new_16b)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
