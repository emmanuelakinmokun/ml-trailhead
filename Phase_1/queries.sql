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

-- Window Function : Ranking CFU counts within each Organism Type group
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

-- Window Function : Comparing each sample's CFU count to the average of its Nutrient Media
SELECT 
    s.ID,
    r.Nutrient_media,
    r.CFU_count,
    ROUND(AVG(r.CFU_count) OVER (PARTITION BY r.Nutrient_media), 2) AS Media_Avg_CFU,
    ROUND(r.CFU_count - AVG(r.CFU_count) OVER (PARTITION BY r.Nutrient_media), 2) AS Deviation_From_Avg
FROM Results r
JOIN Samples s ON r.ID = s.ID;

-- Multi-Table JOIN with HAVING: Sources that have recorded > 50 CFU findings
SELECT
SELECT 
    s.Source,
    COUNT(r.ID) AS High_Contamination_Count
FROM Samples s
JOIN Results r ON s.ID = r.ID
WHERE r.CFU_count > 50
GROUP BY s.Source
HAVING COUNT(r.ID) > 2;

-- Common Table Expression (CTE): Summarize average CFU counts per Source and Organism Type
WITH SourceSummary AS (
    SELECT 
        s.Source,
        r.Organism_Type,
        AVG(r.CFU_count) AS Avg_CFU
    FROM Samples s
    JOIN Results r ON s.ID = r.ID
    GROUP BY s.Source, r.Organism_Type
)
SELECT 
    Source, 
    Organism_Type, 
    ROUND(Avg_CFU, 2) AS Avg_CFU
FROM SourceSummary
WHERE Avg_CFU > 0
ORDER BY Source;