USE	ChicagoCrime
GO


SELECT T.Latitude,T.Longitude,T.[Crime Type], T. Arrest,t.Month,T.[Zip Codes] FROM(
SELECT Latitude,Longitude,
CASE 
WHEN [Primary Type]='THEFT' THEN '1'
WHEN [Primary Type]='BATTERY' THEN '2'
WHEN [Primary Type]='CRIMINAL DAMAGE' THEN '3'
WHEN [Primary Type]='NARCOTICS' THEN '4'
WHEN [Primary Type]='ASSAULT' THEN '5' 
END AS [Crime Type],
CASE 
WHEN Arrest='TRUE' THEN 1
WHEN Arrest='FALSE' THEN -1
END AS Arrest, MONTH(Date) AS Month, [Zip Codes]
FROM dbo.[Crimes_-_2001_to_present]
WHERE LEN([Zip Codes])=5 AND Year<2019) AS T
WHERE T.[Crime Type] IS NOT NULL


DECLARE @year VARCHAR(50)
DECLARE @month VARCHAR(50)
DECLARE @query VARCHAR(max)

SET @year='2013 AND 2018'


SELECT DISTINCT J.count ,
       J.[Zip Codes] ,
       CASE 
WHEN J.[Primary Type]='THEFT' THEN '1'
WHEN J.[Primary Type]='BATTERY' THEN '2'
WHEN J.[Primary Type]='CRIMINAL DAMAGE' THEN '3'
WHEN J.[Primary Type]='NARCOTICS' THEN '4'
WHEN J.[Primary Type]='ASSAULT' THEN '5'
ELSE '6'
END AS [Crime Type]
FROM (SELECT COUNT(*) AS count,[Zip Codes],[Primary Type] FROM dbo.[Crimes_-_2001_to_present]
WHERE Year BETWEEN 2013 AND 2018 AND MONTH(Date) IN (9,10,11)
GROUP BY [Zip Codes],[Primary Type]) AS J
INNER JOIN
    (SELECT k.[Zip Codes], MAX(k.count) AS Maxscore
    FROM (SELECT COUNT(*) AS count,[Zip Codes],[Primary Type] FROM dbo.[Crimes_-_2001_to_present]
WHERE Year BETWEEN 2013 AND 2018 AND MONTH(Date) IN (9,10,11)
GROUP BY [Zip Codes],[Primary Type]) AS K
    GROUP BY K.[Zip Codes]) topscore 
ON j.[Zip Codes] = topscore.[Zip Codes] 
AND j.count = topscore.maxscore
ORDER BY J.count DESC


SELECT COUNT(*) AS count, DATEPART(HOUR,Date) hour FROM dbo.[Crimes_-_2001_to_present]
GROUP BY DATEPART(HOUR,Date)

SELECT COUNT(*) AS Count,year, MONTH(Date) AS Month FROM dbo.[Crimes_-_2001_to_present]
WHERE Arrest='true'
GROUP BY year,MONTH(Date)
ORDER BY year,Month

SELECT TOP 10 * FROM dbo.[Crimes_-_2001_to_present]
WHERE [Primary Type]='ASSAULT'