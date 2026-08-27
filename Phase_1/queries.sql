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