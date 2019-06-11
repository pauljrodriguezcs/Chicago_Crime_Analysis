SELECT Q1.count AS count,Q1.crime FROM (
SELECT TOP 5 COUNT(*) AS count,[Primary Type] AS crime
FROM dbo.[Crimes_-_2001_to_present]
WHERE Year<2019
GROUP BY [Primary Type]
ORDER BY COUNT DESC
) AS Q1
UNION ALL SELECT SUM(T.count) AS count, T.crime from(SELECT COUNT([Primary Type]) AS count,'OTHER' AS crime
 FROM dbo.[Crimes_-_2001_to_present]
WHERE [Primary Type] NOT IN
(SELECT TOP 5 [Primary Type] AS crime
FROM dbo.[Crimes_-_2001_to_present]
WHERE Year < 2019 
GROUP BY [Primary Type]
) GROUP BY [Primary Type] )  AS T
GROUP BY T.crime

SELECT COUNT(*) AS Count, Year,FORMAT(CAST(Date AS DATETIME),'MM') AS month FROM dbo.[Crimes_-_2001_to_present]
WHERE YEAR<2019 
AND [Primary Type]='ASSAULT' 
GROUP BY Year,FORMAT(CAST(Date AS DATETIME),'MM')
ORDER BY Year,month