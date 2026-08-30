-- upsert 
The database tries to INSERT a new row. If that row already exists (based on a PRIMARY KEY or UNIQUE constraint), it doesn't throw an error; instead, it automatically switches to doing an UPDATE on the existing row.


-- replace into
-- REPLACE INTO looks similar to an Upsert, but it is much more aggressive under the hood. If it finds a duplicate key, it completely DELETES the old row and INSERTS a brand new one.
-- (dangerous if applied ON DELETE CASCADE)

-- decimal vs float
-- FLOAT (or DOUBLE): Stores an approximate value -- not 100% accurate
-- DECIMAL (or NUMERIC): Stores the exact value -- 100% accurate