import pyodbc

con = pyodbc.connect('DRIVER={SQL Server};SERVER=11.111.0.11;PORT=1433;DATABASE=MSAX;UID=User;PWD=password!!')


cur = con.cursor()
query = """\
DECLARE @myDate DATE
SET @myDate = GETDATE()

INSERT INTO	SANDBOX.dbo.tblSIXMOACTIVECUST
(COUNTDATE, ACTIVECUST)
SELECT		CAST (CONVERT(CHAR(11), @myDate,113) AS DATETIME)
		,	COUNT (DISTINCT (CUSTACCOUNT))

FROM PRODUCTION.dbo.SALESTABLE
WHERE CREATEDDATETIME BETWEEN DATEADD(m, -6, @myDate) AND @myDate
AND DATAAREAID <> 'QDMX'
"""
cur.execute(query)
cur.commit()
