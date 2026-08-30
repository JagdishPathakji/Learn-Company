import os

filepath = r'c:\Users\patha\OneDrive\Desktop\knowledge-base\learning\agent_generation_rules.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_rule = """
## RULE 6: EXTREME CONCEPTUAL DEPTH (NO FLUFF)
* **The Distinction:** The user hates "Architectural Complexity" (e.g., massive database connections, 5-file repository patterns), but they DEMAND "Extreme Conceptual Depth".
* **What this means:** The code itself must remain simple and self-contained in a Console App, BUT the theory, rules, catches, and edge cases must be exhaustive.
* **Requirements for every topic:**
  * Do NOT write basic "beginner" tutorials. Write "Senior Developer Reference Guides".
  * Explicitly list all exceptions that can be thrown and exactly what triggers them.
  * Explicitly cover obscure edge cases (e.g., Explicit Interface Implementation, Banker's Rounding, `RowState.Deleted` vs `Remove()`).
  * If a topic has multiple sub-concepts, use the Tabbed UI layout to break them down into exhaustive deep-dives.
  * You MUST provide this level of depth proactively, even if the user does not provide reference code!
"""

if "RULE 6: EXTREME CONCEPTUAL DEPTH" not in content:
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(new_rule)
