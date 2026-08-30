-- upsert 


-- replace into
-- REPLACE INTO looks similar to an Upsert, but it is much more aggressive under the hood. If it finds a duplicate key, it completely DELETES the old row and INSERTS a brand new one.


-- decimal vs float
FLOAT (or DOUBLE): Stores an approximate value -- not 100% accurate
DECIMAL (or NUMERIC): Stores the exact value -- 100% accurate