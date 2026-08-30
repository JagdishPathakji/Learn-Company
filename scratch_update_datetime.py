import os

filepath = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\website\topics\csharp\08-date-string-math.html'

new_example_3 = r'''
        <h3>COMPLETE EXAMPLE 3: DateTime, UTC, and Database Timestamps</h3>
        <p>A very common question is: <em>"How does a Timestamp data type look in C#?"</em> The answer is: <strong>It doesn't exist.</strong> C# does not have a <code>Timestamp</code> keyword. Whether your database uses a <code>DATETIME</code> or a <code>TIMESTAMP</code>, they both map directly to the C# <code>DateTime</code> struct.</p>
        <p>Furthermore, when saving a DateTime to a database, you must <strong>always use UTC time</strong> to avoid global timezone bugs.</p>
        
        <div class="code-container" style="border-radius: 6px 6px 0 0;">
            <div class="code-header"><span>C# - DateTime, UTC, and Formats</span><button class="copy-btn">Copy</button></div>
            <pre><code class="language-csharp">using System;

namespace KnowledgeBase.Core
{
    /// &lt;summary&gt;
    /// Demonstrates the critical difference between Local Time and UTC Time, 
    /// and how to format them as Database Timestamps.
    /// &lt;/summary&gt;
    public class DateHelper
    {
        #region Public Methods
        /// &lt;summary&gt;
        /// Explains how DateTime generates SQL Timestamps and handles timezones.
        /// &lt;/summary&gt;
        public void ProcessTimestamps()
        {
            // 1. LOCAL TIME (DateTime.Now)
            // Grabs the time based on where the physical server is located (e.g., India).
            // DANGER: If you move your server to New York, this time will change!
            DateTime localTime = DateTime.Now;
            
            // 2. UNIVERSAL TIME (DateTime.UtcNow) -> ALWAYS USE THIS FOR DATABASES!
            // Grabs the time at GMT 0 (London). This NEVER changes, no matter where 
            // the server is located or if Daylight Savings Time happens.
            DateTime utcTime = DateTime.UtcNow;
            
            // 3. THE DATABASE TIMESTAMP FORMAT
            // Because C# has no 'Timestamp' type, we just format the DateTime into a strict string.
            // yyyy (4-digit year), MM (2-digit month), dd (2-digit day)
            // HH (24-hour clock), mm (minutes), ss (seconds)
            string dbTimestampLocal = localTime.ToString("yyyy-MM-dd HH:mm:ss");
            string dbTimestampUtc = utcTime.ToString("yyyy-MM-dd HH:mm:ss");
            
            // 4. Human Readable Formats
            // For displaying to the user on the frontend
            string friendlyDate = localTime.ToString("MMMM dd, yyyy"); // "August 30, 2026"
            
            Console.WriteLine("--- SERVER TIMES ---");
            Console.WriteLine($"Local Time (Unsafe for DB): {dbTimestampLocal}");
            Console.WriteLine($"UTC Time (Safe for DB):     {dbTimestampUtc}");
            Console.WriteLine();
            Console.WriteLine($"Friendly UI Date: {friendlyDate}");
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
            calendar.ProcessTimestamps();
        }
        #endregion
    }
}</code></pre>
        </div>
        <div class="console-output"><strong>Console Output:</strong><pre>--- SERVER TIMES ---
Local Time (Unsafe for DB): 2026-08-30 19:55:00
UTC Time (Safe for DB):     2026-08-30 14:25:00

Friendly UI Date: August 30, 2026</pre></div>

'''

if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where Example 3 starts and ends
    start_str = '<h3>COMPLETE EXAMPLE 3:'
    end_str = '<h2>B. Edge Cases & What Ifs</h2>'
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + new_example_3 + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
