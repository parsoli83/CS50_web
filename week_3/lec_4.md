# **Lec_4** SQL models and migrations
## SQL

this is basically how you create a table
```sql

CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);
```
autoincrement means automatically give id

### INSERT

```sql
INSERT INTO flights
    (origin , destination ,duration)
    VALUES ("Tehran","Helsinki",400);

```

## SELECT 
```sql
SELECT * FROM flights;
```
will show everything



```sql
SELECT origin,destination FROM flights;
```
will only show origin and destination

```sql
SELECT * FROM flights WHERE origin = "Tehran";
```
will show the flights with the origin of tehran

```sql
SELECT * FROM flights WHERE origin in 
    ("Tehran","Helsinki");
```
is the origin in the said list

### UPDATE

```sql
UPDATE flights
    SET duration = 450;
    WHERE origin = "Tehran" AND origin = "Helsinki";
```
so yeah a basic update command

### DELETE

```sql
DELETE FROM flights WHERE origin = "Tehran";
```
delets the rows where the said statement is true

### better table aesthetics

```sql
.mode columns;
.headers yes;
```

## Foreign Keys
two connect two different tables with a shared keys
### JOIN

table people has(id,name,car_id)

table cars has (id, brand)
```sql
SELECT name FROM people JOIN cars
ON people.car_id = cars.id WHERE brand="benz";
```