SELECT * FROM daily_generation
LIMIT 20;

SELECT 
    MIN(period) AS earliest_entry,
    MAX(period) AS latest_entry
FROM 
    daily_generation;

SELECT 
    period,
    fueltype,
    value,
    SUM(value) OVER (
        PARTITION BY fueltype
        ORDER BY PERIOD
    ) AS fueltype_generation_total
FROM 
    daily_generation;