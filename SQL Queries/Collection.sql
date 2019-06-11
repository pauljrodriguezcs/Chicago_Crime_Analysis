DELETE FROM dbo.[Crimes_-_2001_to_present] WHERE ID IN (
SELECT ID FROM dbo.[Crimes_-_2001_to_present]
WHERE  [Zip Codes]=''
)
SELECT COUNT(*),[Primary Type] FROM dbo.[Crimes_-_2001_to_present]
GROUP BY [Primary Type]


SELECT DISTINCT MAX(T.count) AS tmp, T.[Zip Codes] FROM (
SELECT COUNT(*) AS count,[Zip Codes],[Primary Type] FROM dbo.[Crimes_-_2001_to_present]
WHERE LEN([Zip Codes])=5 AND [Zip Codes]='21273'
GROUP BY [Zip Codes],[Primary Type]) AS T
GROUP BY T.[Zip Codes]
ORDER BY T.[Zip Codes]






SELECT TOP 10 COUNT(*) AS [Crime Count],[Primary Type] AS [Crime Type]
FROM dbo.[Crimes_-_2001_to_present]
GROUP BY [Primary Type]
ORDER BY [Crime count] DESC


SELECT TOP 10 [Location Description],COUNT(*) AS count FROM dbo.[Crimes_-_2001_to_present]
GROUP BY [Location Description]
ORDER BY count DESC


DELETE FROM
dbo.[Crimes_-_2001_to_present]
--SELECT COUNT([Zip Codes]) FROM dbo.[Crimes_-_2001_to_present]
WHERE LEN([Zip Codes])<5