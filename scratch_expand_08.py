import os

filepath = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\08-date-string-math.html'

new_main_html = r'''
    <main class="main-content">
        <div class="topic-header">
            <h1>Date, String, and Math (The Core Toolkit)</h1>
            <p class="metadata">Difficulty: Beginner | Category: C# Base Libraries</p>
        </div>

        <div class="callout callout-info">
            <span class="callout-title">Mental Model</span>
            <p>Think of <code>DateTime</code>, <code>string</code>, and <code>Math</code> as your core utility belt. You never write your own logic to calculate the square root of a number, figure out how many days are in a leap year, or change a word to uppercase. Microsoft has already written millions of lines of highly-optimized code to do this for you. Your job is simply to know which tool to pull from the belt.</p>
        </div>

        <h2>A. Why Does This Exist?</h2>
        <p>Before standard libraries existed, developers had to manually write code to handle basic things like finding the absolute value of a number, extracting words from sentences, or formatting a date for a database. C# provides robust, globally-tested classes packed with dozens of functions for these exact operations so you can focus on your business logic.</p>

        <h3>COMPLETE EXAMPLE 1: Comprehensive String Manipulation</h3>
        <p>Strings in C# are <strong>Immutable</strong>. This means when you call a string function, it does not change the original string variable; it returns a completely <em>new</em> string. Let's look at the most heavily used string functions in enterprise applications.</p>
        
        <div class="code-container" style="border-radius: 6px 6px 0 0;">
            <div class="code-header"><span>C# - String Utilities</span><button class="copy-btn">Copy</button></div>
            <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Core
{
    /// &lt;summary&gt;
    /// Demonstrates the most critical string functions used in daily programming.
    /// &lt;/summary&gt;
    public class StringHelper
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// Formats and analyzes raw user input.
        /// &lt;/summary&gt;
        public void ProcessUserInput()
        {
            string rawEmail = "   John.Doe@Company.com   ";
            string bio = "Senior C# Developer";
            
            // 1. Cleaning & Formatting
            string cleanEmail = rawEmail.Trim(); // Removes edge spaces
            string lowerEmail = cleanEmail.ToLower(); // "john.doe@company.com"
            
            // 2. Searching & Validation
            bool hasDomain = lowerEmail.Contains("@company.com");
            bool startsWithJohn = lowerEmail.StartsWith("john");
            
            // 3. Null Checking (CRITICAL for databases)
            // Checks if a string is null, "", or just "    "
            bool isBioEmpty = string.IsNullOrWhiteSpace(bio); 
            
            // 4. Extraction (Substring)
            // Start at index 7, grab 2 characters
            string language = bio.Substring(7, 2); // "C#"
            
            // 5. String Interpolation (The $ sign)
            // The modern way to combine strings and variables effortlessly
            string profileCard = $"User {lowerEmail} codes in {language}.";

            Console.WriteLine("Cleaned Email: " + lowerEmail);
            Console.WriteLine("Is Valid Company Email: " + hasDomain);
            Console.WriteLine("Extracted Language: " + language);
            Console.WriteLine("Profile Card: " + profileCard);
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
            StringHelper helper = new StringHelper();
            helper.ProcessUserInput();
        }
        #endregion
    }
}</code></pre>
        </div>
        <div class="console-output"><strong>Console Output:</strong><pre>Cleaned Email: john.doe@company.com
Is Valid Company Email: True
Extracted Language: C#
Profile Card: User john.doe@company.com codes in C#.</pre></div>

        <h3>COMPLETE EXAMPLE 2: Math Operations (Beyond Basic Arithmetic)</h3>
        <p>The <code>Math</code> class is <strong>Static</strong>, meaning you don't use the <code>new</code> keyword. It contains functions for advanced rounding, powers, and comparisons.</p>
        
        <div class="code-container" style="border-radius: 6px 6px 0 0;">
            <div class="code-header"><span>C# - The Static Math Class</span><button class="copy-btn">Copy</button></div>
            <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Core
{
    /// &lt;summary&gt;
    /// Demonstrates how to use the static Math class for explicit rounding and calculations.
    /// &lt;/summary&gt;
    public class MathHelper
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// Performs various mathematical operations.
        /// &lt;/summary&gt;
        public void PerformCalculations()
        {
            double rawPrice = 19.99;
            double rating = 4.1;

            // 1. Explicit Rounding (Ceiling always rounds UP, Floor always rounds DOWN)
            double highestPossibleRating = Math.Ceiling(rating); // 5
            double lowestPossibleRating = Math.Floor(rating); // 4
            
            // 2. Standard Rounding (with Midpoint behavior specified)
            double roundedPrice = Math.Round(rawPrice, 1); // 20.0
            
            // 3. Absolute Value (Removes negative signs)
            int distance = Math.Abs(-500); // 500
            
            // 4. Powers and Roots
            double squared = Math.Pow(5, 2); // 5 to the power of 2 (25)
            double root = Math.Sqrt(144); // Square root of 144 (12)

            Console.WriteLine($"Ceiling of {rating}: {highestPossibleRating}");
            Console.WriteLine($"Floor of {rating}: {lowestPossibleRating}");
            Console.WriteLine($"5 Squared: {squared}");
            Console.WriteLine($"Square Root of 144: {root}");
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
            MathHelper mathTools = new MathHelper();
            mathTools.PerformCalculations();
        }
        #endregion
    }
}</code></pre>
        </div>
        <div class="console-output"><strong>Console Output:</strong><pre>Ceiling of 4.1: 5
Floor of 4.1: 4
5 Squared: 25
Square Root of 144: 12</pre></div>

        <h3>COMPLETE EXAMPLE 3: DateTime, Formats, and Database Timestamps</h3>
        <p>In enterprise applications, dates must be formatted perfectly to be saved in a database (like MySQL) or displayed to a user. The <code>ToString()</code> method accepts custom format codes to output dates exactly how you need them.</p>
        
        <div class="code-container" style="border-radius: 6px 6px 0 0;">
            <div class="code-header"><span>C# - DateTime Formatting and DB Timestamps</span><button class="copy-btn">Copy</button></div>
            <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Core
{
    /// &lt;summary&gt;
    /// Demonstrates how to format dates for databases and users.
    /// &lt;/summary&gt;
    public class DateHelper
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// Formats dates and calculates durations.
        /// &lt;/summary&gt;
        public void CalculateAndFormatDates()
        {
            // 1. Get the current exact time
            DateTime currentTime = DateTime.Now;
            
            // 2. THE DATABASE TIMESTAMP FORMAT
            // MySQL and most databases expect dates in exactly this format:
            // yyyy (4-digit year), MM (2-digit month), dd (2-digit day)
            // HH (24-hour clock), mm (minutes), ss (seconds)
            string dbTimestamp = currentTime.ToString("yyyy-MM-dd HH:mm:ss");
            
            // 3. Human Readable Formats
            string friendlyDate = currentTime.ToString("MMMM dd, yyyy"); // "August 30, 2026"
            string justTime = currentTime.ToString("hh:mm tt"); // "02:30 PM"
            
            // 4. Calculating Time in the Future/Past
            DateTime deadlineDate = currentTime.AddDays(7).AddHours(5);
            
            // 5. Calculating Duration (TimeSpan)
            TimeSpan timeRemaining = deadlineDate - currentTime;

            Console.WriteLine($"Database Timestamp: {dbTimestamp}");
            Console.WriteLine($"Friendly Date: {friendlyDate}");
            Console.WriteLine($"Time: {justTime}");
            Console.WriteLine($"Total Hours Remaining: {Math.Round(timeRemaining.TotalHours)}");
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
            DateHelper calendar = new DateHelper();
            calendar.CalculateAndFormatDates();
        }
        #endregion
    }
}</code></pre>
        </div>
        <div class="console-output"><strong>Console Output:</strong><pre>Database Timestamp: 2026-08-30 19:45:00
Friendly Date: August 30, 2026
Time: 07:45 PM
Total Hours Remaining: 173</pre></div>

        <h2>B. Edge Cases & What Ifs</h2>
        
        <div class="callout callout-warn">
            <span class="callout-title">What if I do Math.Round(2.5)?</span>
            <p><strong>Scenario:</strong> You try to round 2.5 expecting it to become 3.</p>
            <p><strong>Behavior:</strong> In C#, <code>Math.Round(2.5)</code> actually returns <strong>2</strong>! This is called "Banker's Rounding" (rounding to the nearest even number). It is used globally in finance to prevent statistical bias. If you want standard math class rounding, you must explicitly tell it: <code>Math.Round(2.5, MidpointRounding.AwayFromZero)</code>.</p>
        </div>

        <div class="callout callout-danger">
            <span class="callout-title">What if I use DateTime.Now on a global server?</span>
            <p><strong>Scenario:</strong> You save an article's publish time as <code>DateTime.Now</code> on a server in London, but a user reads it in Tokyo.</p>
            <p><strong>Behavior:</strong> The time will be completely wrong for the user in Tokyo. You should <strong>never</strong> use <code>DateTime.Now</code> to save time in a database. Always use <code>DateTime.UtcNow</code> (Universal Coordinated Time) to save the time globally, and only convert it to the local timezone when displaying it on the user's screen.</p>
        </div>

        <div class="nav-buttons">
            <a href="07-datatable.html">&larr; Previous: DataTable</a>
            <a href="#">Next: File Operations &rarr;</a>
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
        new_content = content[:start_idx] + new_main_html + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
