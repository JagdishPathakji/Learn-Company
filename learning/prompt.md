You are building and maintaining a PERSONAL ENGINEERING KNOWLEDGE BASE WEBSITE for me.

This is NOT a normal tutorial website.
This is NOT a short notes website.
This is NOT a cheat-sheet generator.

The objective is to create extremely deep, technically rigorous documentation for every topic in my learning roadmap so that, after studying the generated page, I should rarely need another tutorial to understand that topic.

Think of the quality level as a combination of:

- official documentation
- a senior engineer explaining internals
- a university textbook
- practical production engineering experience
- debugging documentation
- architecture documentation
- implementation examples
- interview-level conceptual depth

The explanations must prioritize UNDERSTANDING over brevity.

============================================================
1. INPUT / CURRICULUM SOURCE
============================================================

I will provide an Excel workbook.

The workbook contains MULTIPLE SHEETS/TABS.

Each Excel sheet represents a different technology/domain.

Examples may include:

- MySQL
- C#
- .NET
- JavaScript
- HTML/CSS
- System Design
- etc.

Each ROW inside a sheet represents a topic/subtopic that I need to learn.

The Excel workbook is the SOURCE OF TRUTH for:

1. Technologies
2. Topic order
3. Topic names
4. Progression

DO NOT randomly reorganize the curriculum unless something is technically necessary.

DO NOT generate documentation for the entire Excel workbook at once.

============================================================
2. GENERATION RULE
============================================================

On the FIRST execution:

Generate documentation for ONLY THE FIRST 3 UNPROCESSED TOPICS of the technology/sheet I tell you to work on.

After that:

Whenever I say:

"prepare for next"

generate ONLY THE NEXT 2 UNPROCESSED TOPICS.

Never generate more than 2 topics after the initial batch unless I explicitly request a different number.

Therefore:

Initial request:
3 topics

Every subsequent:
2 topics

Process topics IN EXCEL ROW ORDER.

Do NOT skip ahead.

Do NOT regenerate completed topics unnecessarily.

Do NOT rewrite the entire website every time.

Add the newly generated topics into the existing website.

Maintain persistent progress/state so you know which Excel rows have already been converted into documentation.

============================================================
3. WEBSITE ARCHITECTURE
============================================================

Build this as a proper documentation website using:

HTML
CSS
JavaScript

Use a clean modular structure.

For example:

/
  index.html

  /css
      global.css
      docs.css
      code.css

  /js
      app.js
      navigation.js
      search.js

  /topics
      /mysql
      /csharp
      /dotnet
      ...

  /assets
      /images
      /diagrams

Exact structure may be improved if appropriate.

The site must remain maintainable as hundreds of topics are added.

Do NOT put the entire application into one gigantic HTML file.

============================================================
4. WEBSITE NAVIGATION
============================================================

The documentation website must make the Excel hierarchy visible.

There should be:

Technology navigation
    ↓
Topic navigation
    ↓
Topic documentation

For example:

MySQL
 ├── Database Basics
 ├── Data Types
 ├── Constraints
 ├── Joins
 ├── Stored Procedures
 ├── Indexing
 ├── Transactions
 ├── Backup / Restore
 └── ...

C#
 ├── Variables
 ├── Classes
 ├── Generics
 └── ...

Each Excel SHEET becomes a technology/category.

Each processed Excel ROW becomes a topic inside that technology.

When a new topic is generated:

1. Create its documentation page.
2. Add it automatically to the appropriate navigation.
3. Update previous/next topic navigation.
4. Update search/index metadata if applicable.
5. Do NOT break existing pages.

============================================================
5. DOCUMENTATION QUALITY REQUIREMENT
============================================================

THIS IS THE MOST IMPORTANT REQUIREMENT.

Documentation must be VERY VERY DEEP.

Do NOT write shallow explanations such as:

"An index improves query speed."

Instead explain:

- why searching without it may require scanning
- storage structures involved
- B+ tree organization
- page navigation
- key ordering
- clustered/nonclustered concepts where applicable
- optimizer decisions
- cardinality
- selectivity
- composite key ordering
- prefix behavior
- covering behavior
- write cost
- page splits
- memory/cache effects
- failure cases
- EXPLAIN interpretation
- examples
- edge cases

Every concept should answer not only:

"What?"

but also:

"Why?"
"How?"
"What happens internally?"
"What happens if...?"
"When should I NOT use this?"
"What changes when the data becomes large?"
"What does MySQL actually do?"
"What happens on disk?"
"What happens in memory?"
"What does the optimizer/engine/runtime do?"
"How can this fail?"
"How do I debug it?"

============================================================
6. REQUIRED STRUCTURE FOR EVERY TOPIC
============================================================

Every generated topic MUST contain the following sections.

The exact headings can be improved, but ALL concepts must be covered.

------------------------------------------------------------
A. WHY DOES THIS EXIST?
------------------------------------------------------------

Start from the PROBLEM.

Explain in great depth:

- What problem existed before this feature/concept?
- Why was the feature needed?
- What becomes difficult without it?
- What would developers otherwise have to do manually?
- What scalability/reliability/maintainability problem does it solve?
- Give intuitive examples.
- Give technical examples.
- Show the naive approach first where appropriate.
- Then show why the topic exists.

The learner should understand the motivation BEFORE learning syntax.

------------------------------------------------------------
B. WHAT IS IT?
------------------------------------------------------------

Give an extremely clear but technically accurate definition.

Explain:

- terminology
- components
- related concepts
- terminology differences
- conceptual model
- implementation model

Separate:

"Conceptually"

from:

"Internally"

when useful.

------------------------------------------------------------
C. WHEN SHOULD IT BE USED?
------------------------------------------------------------

Explain:

- appropriate use cases
- inappropriate use cases
- alternatives
- trade-offs
- production scenarios
- small application scenarios
- large application scenarios
- decision criteria

Provide examples such as:

USE THIS WHEN...

DO NOT USE THIS WHEN...

CONSIDER X INSTEAD WHEN...

------------------------------------------------------------
D. INTERNAL WORKING
------------------------------------------------------------

This section must be one of the largest sections.

Explain HOW THE SYSTEM ACTUALLY EXECUTES THE FEATURE.

Where applicable cover:

Application
    ↓
SQL/API/compiler/runtime
    ↓
parser
    ↓
optimizer/planner
    ↓
execution engine
    ↓
memory
    ↓
cache/buffer
    ↓
storage engine
    ↓
filesystem/disk

Use diagrams.

Use Mermaid where appropriate or prefer html css for better views and UX.

For example:

```mermaid
flowchart TD
    A[Client sends query]
    --> B[MySQL Parser]
    --> C[Optimizer]
    --> D[Execution Plan]
    --> E[InnoDB]
    --> F[Buffer Pool]
    --> G[Disk Pages]

But diagrams must be explained afterward.

Never include a diagram without explaining what each important step means.

E. EXECUTION WALKTHROUGH

Take a realistic example and walk through it STEP BY STEP.

Example format:

Step 1
Client sends ...

Step 2
Parser ...

Step 3
Optimizer ...

Step 4
Storage engine ...

Step 5
...

Explain what data exists at each stage.

F. HOW TO USE IT

Teach syntax and usage.

Start simple.

Then gradually increase complexity.

Use multiple examples.

For EACH important code example provide:

Problem
Code
Explanation
What happens internally
Expected output/result
Important observations
Common mistake

Do not dump code without explanation.

G. MULTIPLE REAL USE CASES

Provide several realistic use cases.

Not meaningless examples like:

users(id, name)

unless a simplified example genuinely improves understanding.

Prefer engineering scenarios.

H. KNOWLEDGE_BASE PROJECT INTEGRATION

For EVERY programming/database topic where applicable:

Create EXACTLY TWO meaningful examples using my Knowledge Base project.

My project is an internal company Knowledge Base / FAQ system.

Core concepts include:

Article
ArticleVersion
Category
Tag
Rating
User
Role
Status
Content Blocks
Approval workflow

Typical workflow:

Author
↓
Draft
↓
Pending Editor Review
↓
Editor evaluates
↓
Published / Needs Improvement / Rejected

Useful known lookup concepts include:

ROLE
1 Reviewer
2 Author
3 Editor

STATUS
1 Draft
2 Pending Editor Review
3 Needs Improvement
4 Rejected
5 Published

BLOCK_TYPE
1 Text
2 Code
etc.

The examples MUST make architectural sense.

Do NOT force the Knowledge Base project into an example where it makes no sense.

For each Knowledge Base example explain:

WHY this particular feature makes sense here.

Then explain the implementation.

Then explain its internal behavior.

Then explain alternatives.

Then explain possible mistakes.

============================================================
7. EDGE CASES

Every major topic must have an extensive:

"Edge Cases, Failure Modes and What If...?"

section.

I want questions such as:

What if X happens?

What if X is NULL?

What if data is empty?

What if two users do this simultaneously?

What if millions of rows exist?

What if transaction fails halfway?

What if server crashes?

What if index is missing?

What if cache does not contain the page?

What if constraint fails?

What if duplicate values exist?

What if connection closes?

What if rollback occurs?

What if disk write happens after a crash?

What if a parameter is omitted?

What if wrong datatype is supplied?

What if optimizer chooses another plan?

What if character encoding is incompatible?

Not every question applies to every topic.

Choose relevant ones intelligently.

For every important edge case explain:

CAUSE
BEHAVIOR
WHY IT HAPPENS
HOW TO DETECT IT
HOW TO SOLVE/PREVENT IT

============================================================
8. COMMON MISTAKES

Include common developer mistakes.

For each mistake show:

WRONG

...

WHY IT IS WRONG

CORRECT

...

WHY THE CORRECTION WORKS

Also explain cases where something technically works but is still a bad engineering decision.

============================================================
9. DEBUGGING / TROUBLESHOOTING

Where applicable include:

Symptoms
Possible causes
How to investigate
Commands/tools
How to interpret results
Fix
Prevention

For MySQL especially use tools such as:

SHOW
EXPLAIN
EXPLAIN ANALYZE
SHOW INDEX
INFORMATION_SCHEMA
performance_schema
SHOW ENGINE INNODB STATUS
appropriate logs

when relevant.

============================================================
10. PERFORMANCE

For topics with performance implications explain:

Time complexity where meaningful
I/O implications
Memory implications
Disk implications
Network implications
Concurrency implications
Locking implications
CPU implications
Caching implications
Scaling behavior

Explain how behavior changes between:

10 rows
10,000 rows
1,000,000 rows
100,000,000 rows

where relevant.

============================================================
11. PRODUCTION ENGINEERING PERSPECTIVE

Add a section:

"Production Engineering Perspective"

Explain:

what junior developers commonly misunderstand
what experienced developers watch for
scalability considerations
maintainability
observability
safety
deployment considerations
migration implications
rollback concerns
production failure scenarios
============================================================
12. INTERVIEW / MENTAL MODEL SECTION

At the end create:

"Final Mental Model"

Summarize HOW I SHOULD THINK ABOUT THE TOPIC.

Do NOT simply repeat definitions.

Create a mental model connecting:

WHY
WHAT
HOW
WHEN
INTERNALS
TRADE-OFFS

Then provide important questions I should now be able to answer.

============================================================
13. DO NOT SACRIFICE DEPTH

There is NO requirement to keep pages short.

If a topic requires:

3,000 words
5,000 words
10,000 words
or more

use whatever length is necessary.

DO NOT shorten content because the topic looks large.

However:

Do not add meaningless filler.

Depth != repetition.

Every paragraph must teach something.

============================================================
14. VISUAL EXPLANATIONS

Use visual elements extensively where they genuinely improve learning:

architecture diagrams
sequence diagrams
flowcharts
state diagrams
tables
comparison tables
timelines
execution flows
storage diagrams
B+ tree diagrams
transaction diagrams
memory diagrams
annotated examples
callouts
expandable details
code snippets
command output
pseudo-code

Use Mermaid or native HTML/CSS diagrams where appropriate.

For concepts where an actual image significantly improves understanding, include an appropriate image asset/reference.

Do not add decorative stock images.

Technical visuals only.

============================================================
15. PAGE UX

Every large topic should have:

topic title
difficulty indicator
technology/category
table of contents
estimated reading time if useful
previous topic
next topic
searchable headings
section anchors
code-copy buttons
collapsible deep-dive sections where useful
highlighted warning/note/tip boxes
syntax highlighting
responsive design

The table of contents should remain usable for very long pages.

Prefer a sticky table of contents on desktop.

============================================================
16. CODE QUALITY

All generated examples must be valid.

Do NOT intentionally use pseudo-code while presenting it as executable code.

Label pseudo-code explicitly.

For SQL examples use MySQL syntax unless another technology is being documented.

All code must use consistent formatting.

Explain important lines.

Do not add comments to every obvious line.

============================================================
17. MYSQL SPECIAL INSTRUCTIONS

The MySQL documentation is especially important.

For MySQL:

Teach topics at the level expected from a strong senior backend/database engineer.

Assume I don't merely want to remember SQL syntax.

I want to understand MySQL as a database system.

Discuss relevant differences between:

MySQL Server
SQL layer
InnoDB
Buffer Pool
Disk storage
Indexes
Optimizer
Redo log
Undo log
Binary log
MVCC
Locks
Transactions
Connection/session
Filesystem

whenever appropriate.

Explain exactly WHICH COMPONENT is responsible for a behavior.

For example, do not casually say:

"MySQL stores X"

when the technically meaningful explanation is:

"InnoDB stores..."

Make these distinctions clear.

============================================================
18. MYSQL EXISTING CODE RULE

For MySQL, my code/schema has ALREADY BEEN WRITTEN.

DO NOT redesign the project unnecessarily.

DO NOT invent a completely different Knowledge Base database.

Use my existing MySQL code/schema/examples from the supplied project/files wherever possible.

Analyze existing code before creating examples.

If an existing table, query, procedure, function, view, trigger, transaction, index, etc. is available and relevant:

USE IT.

Explain the existing implementation in depth.

You may add small demonstration queries around it when necessary for teaching.

For OTHER TECHNOLOGIES, you may write new code where necessary according to the existing Knowledge Base project's requirements.

============================================================
19. STORED PROCEDURES — REQUIRED EXTRA COVERAGE

When the Excel reaches STORED PROCEDURES, make sure the documentation contains an extremely deep explanation of parameter types:

IN
OUT
INOUT

Explain:

memory/value flow
caller → procedure
procedure → caller
initialization behavior
scope
variable assignment
examples
NULL behavior
type compatibility
calling syntax
session variables where applicable
differences
real-world use cases
anti-patterns

Provide execution diagrams such as:

Caller
|
| IN
v
Procedure

Procedure
|
| OUT
v
Caller

and explain actual behavior.

Include several examples plus TWO meaningful Knowledge Base examples.

============================================================
20. INDEXING — REQUIRED EXTRA COVERAGE

When indexing is covered, include VERY deep coverage of:

SINGLE COLUMN INDEX
COMPOSITE INDEX
UNIQUE INDEX
PRIMARY KEY
COVERING INDEX
PREFIX INDEX
FULLTEXT when relevant
BTREE implementation
HASH where relevant

Especially explain:

INDEX PREFIXING / PREFIX INDEX

Example concept:

INDEX idx_title(title(20))

Explain:

what prefix length means
why it exists
storage benefits
selectivity trade-off
limitations
comparison with full-column indexing
effect on ORDER BY
effect on covering indexes
text/blob indexing considerations
how prefix selectivity can be measured

Also explain COMPOSITE INDEX behavior in very deep detail.

For:

INDEX(a, b, c)

Explain exactly when indexes can be used for:

WHERE a = ...
WHERE a = ... AND b = ...
WHERE a = ... AND b = ... AND c = ...
WHERE b = ...
WHERE c = ...
WHERE b = ... AND c = ...
WHERE a = ... AND c = ...
WHERE a > ... AND b = ...
ORDER BY
GROUP BY

Teach the LEFTMOST PREFIX PRINCIPLE.

But DO NOT teach it as a rule to memorize.

Explain WHY it exists based on B+ tree ordering.

Show an actual conceptual tree/order.

Explain:

equality
range predicates
sorting
cardinality
selectivity
optimizer behavior
covering
index condition pushdown where relevant
skip scan if relevant to the target MySQL version
why an apparently suitable index can still be ignored

Use EXPLAIN examples.

============================================================
21. DATABASE CREATION / CHARACTER SET

When CREATE DATABASE / schema creation is covered, explain in depth:

DEFAULT CHARACTER SET
DEFAULT COLLATE

For example:

CREATE DATABASE knowledge_base
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

Explain:

character
character set
encoding
Unicode
utf8 vs utf8mb4
bytes per character
collation
sorting
comparison
case sensitivity
accent sensitivity
inheritance

Explain hierarchy such as:

Server default
↓
Database default
↓
Table default
↓
Column definition
↓
Expression/session behavior where applicable

Explain what happens when defaults are omitted.

Explain character-set mismatches.

Explain conversion.

Explain index-size implications when relevant.

============================================================
22. TRANSACTIONS / DATA DURABILITY INTERNALS

When transactions are reached, give exceptionally deep coverage of:

REDO LOG
UNDO LOG
BINARY LOG

Do not lump them together.

For each explain:

What it is
Why it exists
Which component manages it
When it is written
What it contains conceptually
Where it exists
How it participates in recovery
How it relates to transactions

REDO LOG:

Explain concepts including:

write-ahead logging
dirty pages
buffer pool
checkpointing
crash recovery
redo records
commit durability

UNDO LOG:

Explain:

rollback
old row versions
MVCC
consistent reads
transaction visibility
purge

BINARY LOG:

Explain:

MySQL server layer
replication
point-in-time recovery
statement/row/mixed concepts if applicable

Clearly explain:

REDO != UNDO != BINLOG.

Provide diagrams showing what happens during:

BEGIN

UPDATE

COMMIT

ROLLBACK

SERVER CRASH

SERVER RESTART

Explain a transaction's complete journey.

Example:

Application
↓
MySQL
↓
InnoDB modifies Buffer Pool page
↓
Undo generated
↓
Redo generated
↓
Commit
↓
Durability
↓
Dirty pages eventually flushed

Make the actual behavior/version caveats accurate.

============================================================
23. BACKUP AND RESTORE — EXTREMELY IMPORTANT

When Backup / Restore is reached, use the screenshots I provide from MySQL Workbench.

DO NOT merely teach:

mysqldump database > backup.sql

I want COMPLETE understanding of the MySQL Workbench interface.

For EVERY BUTTON / CHECKBOX / OPTION visible in my supplied Data Export and Data Import/Restore screenshots:

explain:

What the UI control means.
What it actually causes Workbench/MySQL utilities to do.
When to use it.
When not to use it.
What files it creates/uses.
Advantages.
Disadvantages.
Restore implications.
Example.

The supplied Data Export screenshot currently includes concepts such as:

Tables to Export
Schema selection
Schema Objects
Dump Structure and Data
Select Views
Select Tables
Unselect All

Objects to Export:
Dump Stored Procedures and Functions
Dump Events
Dump Triggers

Export Options:
Export to Dump Project Folder
Export to Self-Contained File
Create Dump in a Single Transaction
Include Create Schema
Advanced Options
Start Export

Explain EVERY ONE OF THEM.

Also explain differences among:

Dump Structure Only
Dump Data Only
Dump Structure and Data

Explain what SQL/object definitions are actually generated.

Explain:

Self-Contained File

vs

Dump Project Folder

including:

file organization
restore granularity
portability
large database implications
version control implications
performance implications

Explain:

Include Create Schema

with exact restore consequences.

Explain:

Create Dump in a Single Transaction

including:

consistent snapshot
transactional tables
InnoDB
concurrent writes
limitations with non-transactional tables
locking implications
large transactions where applicable

Explain backup of:

tables
views
indexes
constraints
procedures
functions
triggers
events
data
database/schema creation

Explain what gets restored and in what logical order where relevant.

When I provide the RESTORE screenshot, inspect it carefully and explain EVERY visible option similarly.

If a screenshot or UI control is not available, DO NOT INVENT ITS EXACT LABEL.

Wait for/properly inspect the supplied image.

============================================================
24. LOGICAL VS PHYSICAL BACKUPS

Backup documentation must also teach:

Logical backup
Physical backup

mysqldump
MySQL Shell dump utilities where relevant
Workbench export
filesystem/physical backup concepts
hot backup
cold backup
consistent backup
full backup
incremental concepts
point-in-time recovery

Explain which Workbench Data Export approach belongs to which category.

============================================================
25. RESTORE INTERNAL WORKING

Do not describe restore as:

"Import the SQL file."

Explain what happens.

Example:

SQL dump read
↓
CREATE DATABASE
↓
USE database
↓
CREATE TABLE
↓
constraints/indexes
↓
INSERT data
↓
views/routines/triggers/events
↓
completion

Actual ordering may vary according to generated dump; explain accurately.

Explain failures including:

schema already exists
table already exists
foreign-key issues
duplicate key
missing DEFINER user
collation mismatch
character set mismatch
version incompatibility
permissions
large dump timeout
packet size
disk space
corrupted/incomplete dump

Explain recovery strategies.

============================================================
26. DATABASE BACKUP DISASTER SCENARIOS

Include practical scenarios.

For example:

SCENARIO 1
Developer accidentally runs DELETE without WHERE.

SCENARIO 2
Entire database is dropped.

SCENARIO 3
Server crashes during a transaction.

SCENARIO 4
Backup exists but production continued receiving transactions afterward.

SCENARIO 5
Need database state from yesterday at exactly 3:42 PM.

Explain which mechanism helps:

backup
undo
redo
binary log
point-in-time recovery

and WHY.

============================================================
27. VERSION AWARENESS

MySQL features can differ between versions.

When something is version-dependent:

clearly mention it.

Do not present historical behavior as current behavior.

Assume modern MySQL 8.x unless the supplied environment indicates otherwise.

============================================================
28. TECHNICALLY PRECISE LANGUAGE

Avoid misleading simplifications.

Bad:

"Indexes make queries fast."

Better:

"An index provides an alternative ordered access path that may allow the optimizer to avoid examining a large portion of the table, but whether it improves a query depends on selectivity, predicates, ordering requirements, table statistics, access costs and the optimizer's chosen plan."

The second style is what I want.

============================================================
29. LEARNING PROGRESSION INSIDE EACH PAGE

Each topic should progress approximately like:

Problem
↓
Intuition
↓
Definition
↓
Simple example
↓
Internal architecture
↓
Detailed execution
↓
Syntax
↓
Practical usage
↓
Knowledge Base examples
↓
Advanced behavior
↓
Performance
↓
Concurrency
↓
Edge cases
↓
Debugging
↓
Production concerns
↓
Mental model

Do not start with huge syntax tables without explaining why the feature exists.

============================================================
30. CROSS-LINK RELATED CONCEPTS

When another completed topic is relevant, create internal links.

For example:

Indexing
→ Query Optimization
→ EXPLAIN
→ B+ Trees

Transactions
→ Locks
→ MVCC
→ Undo Logs
→ Isolation Levels

Stored Procedures
→ Variables
→ Parameters
→ Transactions

Do not duplicate an entire previous chapter when linking is more appropriate.

However, include enough local explanation so the current topic remains understandable.

============================================================
31. TERMINOLOGY CALLOUTS

For important terminology provide callouts such as:

TERM: Cardinality

Definition:
...

Why engineers care:
...

Related concepts:
...

Common misunderstanding:
...

============================================================
32. COMPARISON TABLES

Whenever two concepts are commonly confused, compare them.

Examples:

DELETE vs TRUNCATE vs DROP

WHERE vs HAVING

Procedure vs Function

IN vs OUT vs INOUT

Clustered vs Secondary Index

Redo vs Undo vs Binary Log

Self-contained Dump vs Dump Project Folder

Logical Backup vs Physical Backup

CHARACTER SET vs COLLATION

UNIQUE KEY vs PRIMARY KEY

But do not create comparison tables simply for visual decoration.

============================================================
33. QUESTIONS THE DOCUMENTATION MUST ANTICIPATE

Act like I am sitting beside a senior engineer and interrupting constantly.

Anticipate questions like:

"But why?"

"Where is that stored?"

"Who performs this operation?"

"What happens before this step?"

"What happens afterward?"

"What happens if this fails?"

"What happens if two transactions do this?"

"Does this happen in RAM or disk?"

"Is this handled by MySQL Server or InnoDB?"

"Does this survive a crash?"

"Why can't MySQL use this index?"

"What happens with NULL?"

"What happens with 10 million rows?"

"Why would I choose this instead of X?"

"What exactly happens when I click this Workbench button?"

Answer these questions proactively.

============================================================
34. RESEARCH / ACCURACY REQUIREMENT

Technical correctness matters more than speed.

When external research is available:

prefer authoritative sources such as:

official MySQL documentation
Microsoft documentation
official language/framework documentation
standards/specifications
reliable engineering references

Do not blindly copy documentation.

SYNTHESIZE it into a coherent teaching explanation.

If authoritative sources disagree or behavior is version-dependent:

mention the distinction.

Do not invent internals.

If something cannot be confirmed, state the uncertainty rather than manufacturing an explanation.

============================================================
35. REFERENCES

At the end of advanced chapters include:

Further Reading / References

with high-quality authoritative references where useful.

This documentation itself must remain understandable without requiring me to open them.

References are for verification/deeper exploration, NOT replacements for explanation.

============================================================
36. CONTENT PRESENTATION

Use:

HTML
Markdown rendering if useful
CSS
JavaScript
syntax-highlighted code
Mermaid
technical diagrams
tables
callout boxes

Callout types can include:

NOTE
IMPORTANT
WARNING
INTERNALS
PERFORMANCE
PRODUCTION
COMMON MISTAKE
INTERVIEW
DEBUGGING

============================================================
37. CODE BLOCK EXPERIENCE

Code blocks should display:

language
copy button
optional filename/context

Example:

SQL
knowledge_base — composite index example

[Copy]

CREATE INDEX ...


For long examples, explain relevant sections immediately after the code.

============================================================
38. DO NOT DO THESE THINGS
============================================================

DO NOT:

- generate shallow blog-style content
- create 10-line explanations
- summarize complicated internals into one paragraph
- skip WHY
- skip internals
- skip edge cases
- dump code without explanation
- create meaningless Knowledge Base examples
- invent MySQL behavior
- create the whole Excel curriculum at once
- process later rows before earlier rows
- regenerate the website from scratch every time
- remove previously generated content
- create duplicate navigation entries
- reduce existing documentation quality
- redesign my existing MySQL Knowledge Base schema without reason
- describe database behavior vaguely when the responsible component is known
- sacrifice explanation because a page becomes long
- create decorative imagery with no educational value

============================================================
39. EXISTING WEBSITE UPDATE RULE
============================================================

Before generating new topics:

1. Inspect the existing project.
2. Understand its navigation architecture.
3. Determine completed topics.
4. Inspect the Excel workbook.
5. Determine the requested technology.
6. Determine the next unprocessed rows.
7. Generate only the allowed number.
8. Add their files.
9. Update navigation.
10. Update previous/next links.
11. Update search/index.
12. Verify existing pages still work.
13. Verify the new pages render correctly.
14. Verify code highlighting.
15. Verify Mermaid/diagrams.
16. Verify mobile and desktop navigation.

DO NOT delete working functionality merely because you would have implemented it differently.

============================================================
40. PROGRESS TRACKING
============================================================

Maintain a lightweight progress mechanism.

For example a JSON file:

{
  "MySQL": {
    "completedTopics": [
      "...",
      "..."
    ],
    "lastProcessedRow": 14
  },
  "CSharp": {
    "completedTopics": [],
    "lastProcessedRow": 0
  }
}

The exact implementation may be improved.

The important requirement is:

You MUST know which Excel rows have already been processed.

Do not rely only on conversation memory.

============================================================
41. TOPIC COMPLETION CHECKLIST
============================================================

Before considering EACH topic complete, verify:

[ ] Why does it exist?
[ ] What is it?
[ ] When is it used?
[ ] When should it not be used?
[ ] Internal architecture explained?
[ ] Execution lifecycle explained?
[ ] Syntax explained?
[ ] Multiple examples?
[ ] Examples explained line-by-line where necessary?
[ ] Two meaningful Knowledge Base use cases?
[ ] Edge cases?
[ ] Failure scenarios?
[ ] Common mistakes?
[ ] Debugging?
[ ] Performance implications?
[ ] Concurrency implications where relevant?
[ ] Security implications where relevant?
[ ] Production engineering perspective?
[ ] Diagrams where useful?
[ ] Comparison with alternatives?
[ ] Final mental model?
[ ] Related-topic links?
[ ] Technically verified?

If an applicable checkbox is missing, the topic IS NOT COMPLETE.

============================================================
42. DEPTH CHECK
============================================================

Before finishing a topic ask:

"If the learner asks WHY one more time at each stage, does the page answer it?"

If not:

expand the explanation.

Ask:

"If the learner wants to understand what the database/runtime actually does internally, is that explained?"

If not:

expand it.

Ask:

"If something goes wrong in production, would this chapter help diagnose it?"

If not:

add the relevant failure/debugging explanation.

============================================================
43. INITIAL TASK BEHAVIOR
============================================================

When I initially provide the Excel workbook/project and tell you the technology:

Process ONLY THE FIRST 3 UNPROCESSED ROWS for that technology.

Before writing, inspect:

- existing website
- Excel sheet
- existing project code
- supplied diagrams/screenshots
- existing Knowledge Base MySQL schema/code

Then implement those 3 chapters completely.

Do not merely show me proposed content.

Actually create/update the HTML/CSS/JS documentation website.

============================================================
44. "PREPARE FOR NEXT" COMMAND
============================================================

THIS COMMAND HAS SPECIAL MEANING.

Whenever I later say:

prepare for next

perform the following automatically:

1. Read progress.
2. Identify the currently active Excel technology/sheet.
3. Find the next TWO unprocessed topic rows.
4. Read those exact rows.
5. Analyze existing related documentation/code.
6. Research technical internals where required.
7. Generate the two full-depth documentation chapters.
8. Integrate them into the existing website.
9. Update navigation/search/previous-next links.
10. Update progress state.
11. Test for broken references/rendering.
12. Stop.

DO NOT ask me which rows come next if the Excel order already answers that.

DO NOT process three topics.

DO NOT process the rest of the sheet.

ONLY TWO.

============================================================
45. WHEN I CHANGE TECHNOLOGY
============================================================

If I explicitly say something such as:

"Start C#"

then switch the active technology to the corresponding Excel sheet.

Process its first THREE unprocessed topics because this is the initial batch for that technology, unless I explicitly specify otherwise.

Subsequent:

"prepare for next"

means the next TWO topics of that technology.

============================================================
46. FINAL OUTPUT AFTER EACH GENERATION
============================================================

After implementation, give me only a concise implementation report containing:

Generated:
- Topic A
- Topic B
[- Topic C only for initial batch]

Updated:
- navigation
- search/index
- progress tracking
- related links

Next Excel topics:
- next upcoming topic
- topic after that

Do NOT paste the entire documentation into chat if it already exists in the generated website.

The website is the documentation.

============================================================
47. MOST IMPORTANT PRINCIPLE
============================================================

I am creating this documentation because I want a SINGLE PRIMARY LEARNING RESOURCE.

For every topic, I should be able to:

open the topic
→ understand why it exists
→ understand what it is
→ understand its syntax
→ understand its internal implementation
→ understand how execution flows
→ understand practical usage
→ understand its usage in my Knowledge Base project
→ understand edge cases
→ understand failures
→ debug problems
→ understand performance
→ understand production implications
→ build a strong mental model
→ move confidently to the next topic

That is the standard.

If a generated page feels like something I could get from a short tutorial/blog article, it is NOT deep enough.

Build documentation that I can keep referring to throughout my engineering career.