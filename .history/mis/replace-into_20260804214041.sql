What it is: At first glance, REPLACE INTO looks like it does the exact same thing as Upsert. It says: "Try to insert. If it exists, overwrite it." However, how it does it is completely different and extremely dangerous.

-- Upsert gently modifies the existing row in place.
-- REPLACE INTO aggressively DELETES the old row entirely, and then INSERTS the brand new one.

