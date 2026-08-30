# KNOWLEDGE BASE GENERATION STANDARD (The 11/10 Standard)

This file serves as the absolute, unbreakable rulebook for all future C# topic generations in this project. The agent MUST read and apply this context before preparing any new topic.

## 1. THE "NORMAL FLOW" (CODE SIMPLICITY)
*   **Keep It Simple (NO PROD ARCHITECTURE):** Do NOT write production-level code, Repositories, Services, Dependency Injection, or complex offline-sync mechanisms. 
*   **In-Memory Only:** Never require NuGet packages or `MySqlConnection`. All code must run instantly in a blank Console App.
*   **Normal Flow:** The code must flow top-to-bottom in a way that is incredibly easy for a beginner to understand. Focus ONLY on explaining the raw C# concept using simple domain objects (e.g., a simple `Article` or `User` class).

## 2. THE 3-EXAMPLE PROGRESSION
Every topic MUST include exactly **3 code examples**:
*   **Example 1 (Basic):** Explains the raw C# keyword/concept in isolation.
*   **Example 2 (Intermediate):** Applies the concept to a simple Knowledge Base scenario (e.g., adding a rule to a DataTable, casting an Enum).
*   **Example 3 (Advanced Concept):** Shows an advanced usage of the *raw concept* (e.g., using an Enum inside a Switch statement). Do NOT introduce advanced architectural patterns here.

## 3. STRICT CODING GUIDELINES & COMMENTING
Even in the simplest code examples, you must perfectly emulate production-level formatting:
*   **XML Comments:** Every single class, method, property, and enum MUST have `/// <summary>` documentation.
*   **Regions Required:** Every class MUST organize its members using exactly: `#region Private Members`, `#region Public Properties`, `#region Constructors`, `#region Public Methods`.
*   **Variable Naming:** NEVER use single-character variables (like `a`, `u`, `i`) except in loops. Use strict `camelCase` (e.g., `currentArticle`).
*   **Enum Naming:** All Enums MUST be prefixed with `Enm` (e.g., `EnmUserRole`).
*   **Boolean Naming:** Prefix all booleans with `is`, `has`, or `can` (e.g., `isPublished`).
*   **No Authors:** NEVER include `<author>` or `/// Original Author:` tags. This is a solo project.

## 4. EXECUTION & OUTPUT
*   **Execution Required:** Every code block must contain a `class Program` with a `static void Main()` method to prove exactly how it is instantiated.
*   **Console Output Boxes (CRITICAL):** Immediately following EVERY `<div class="code-container">`, you MUST provide a styled output box showing exactly what prints to the terminal: 
    `<div class="console-output"><strong>Console Output:</strong><pre>...</pre></div>`
*   **Syntax Highlighting:** All code blocks must use `<pre><code class="language-csharp">` for Prism.js.

## 5. THE PEDAGOGICAL APPROACH
*   **De-Jargon Everything:** Map senior-level jargon to plain-English, real-world analogies (e.g., "The Cache is like a sticky note on your monitor").
*   **Edge Cases:** Every topic must answer "What If...?" scenarios.
*   **Visual Flowcharts:** Use pure HTML/CSS flexbox-based architecture diagrams (NO Mermaid.js).

## RULE 6: EXTREME CONCEPTUAL DEPTH (NO FLUFF)
* **The Distinction:** The user hates "Architectural Complexity" (e.g., massive database connections, 5-file repository patterns), but they DEMAND "Extreme Conceptual Depth".
* **What this means:** The code itself must remain simple and self-contained in a Console App, BUT the theory, rules, catches, and edge cases must be exhaustive.
* **Requirements for every topic:**
  * Do NOT write basic "beginner" tutorials. Write "Senior Developer Reference Guides".
  * Explicitly list all exceptions that can be thrown and exactly what triggers them.
  * Explicitly cover obscure edge cases (e.g., Explicit Interface Implementation, Banker's Rounding, `RowState.Deleted` vs `Remove()`).
  * If a topic has multiple sub-concepts, use the Tabbed UI layout to break them down into exhaustive deep-dives.
  * You MUST provide this level of depth proactively, even if the user does not provide reference code!
