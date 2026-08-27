-- Multi Table Join
SELECT * FROM Samples
JOIN Results on Samples.ID = Results.ID

-- GROUP BY & Aggregation of CFU Count
SELECT 
    Results.Organism_Type,
    COUNT(Results.ID)  AS Total_Samples,
    ROUND(AVG(Result.CFU_count), 2) AS Avg_CFU_Count,
    MAX(Result.CFU_count) AS Max_CFU_Count
FROM Results
GROUP BY Results.Organism_Type
ORDER BY Avg_CFU_Count DESC;

-- GROUP BY & Aggregation of Sample Count
SELECT 
    s.Source,
    COUNT(s.ID) AS Sample_Count
FROM Samples s
GROUP BY s.Source
ORDER BY Sample_Count DESC;

-- SUBQUERY > average cfu_count
SELECT 
    s.ID, 
    s.Source, 
    r.Probable_organism, 
    r.CFU_count
FROM Samples s
JOIN Results r ON s.ID = r.ID
WHERE r.CFU_count > (
    SELECT AVG(CFU_count)
    FROM Results
) 
ORDER BY r.CFU_count DESC;

-- SUBQUERY -- Sources with cfu_count > 100
SELECT DISTINCT 
    s.Source
FROM Samples s
WHERE s.ID IN (
    SELECT ID 
    FROM Results 
    WHERE CFU_count > 100
);

-- Window Function : Rank CFU counts within each Organism Type group
SELECT 
    r.Organism_Type,
    s.ID,
    s.Source,
    r.Probable_organism,
    r.CFU_count,
    DENSE_RANK() OVER (
        PARTITION BY r.Organism_Type 
        ORDER BY r.CFU_count DESC
    ) AS CFU_Rank
FROM Results r
JOIN Samples s ON r.ID = s.ID;