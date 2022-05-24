from turtle import clear
import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=GWTN141-10;"
    "Database=AdventureWorks2019;"
    "Trust_Connection=yes;"
)

class sqljson:
    cursor = conn.cursor()
    def __init__(self, connectdb):
        self.connectdb = connectdb 

    def read(self):
        print("Read")
        sqljson.cursor.execute("select top 3 BusinessEntityID, FirstName, MiddleName, LastName from [Person].[Person]")
        for row in sqljson.cursor:
            print(row)
        print()

    def likeqry(self):
        print("Like Query")
        sqljson.cursor.execute("SELECT top 5 [BusinessEntityID], [JobTitle] FROM [HumanResources].[Employee] e WHERE JobTitle LIKE 'Design%'")
        for row in sqljson.cursor:
            print(row)
        print()
    
    def INqry(self):
        print("In Query")
        sqljson.cursor.execute("SELECT top 5 [BusinessEntityID],JobTitle FROM [HumanResources].[Employee] e WHERE JobTitle in ('Engineering Manager','Senior Tool Designer')")
        for row in sqljson.cursor:
            print(row)
        print()
    def betweenqry(self):
        print("Between Query")
        sqljson.cursor.execute("SELECT top 5 SalesOrderID, OrderDate, DueDate FROM Sales.SalesOrderHeader WHERE [OrderDate] BETWEEN '4/16/2011' AND '12/15/2011'")
        for row in sqljson.cursor:
            print(row)
        print()
    def lessthanqry(conn):
        print("Between Query")
        sqljson.cursor.execute("SELECT BusinessEntityID, FirstName, LastName FROM [Person].[Person] WHERE BusinessEntityID <= 10")
        for row in sqljson.cursor:
            print(row)
        print()
    def joinqry(conn):
        print("Join Tables")
        sqljson.cursor.execute("SELECT top 5 E.NationalIDNumber,   E.JobTitle,   P.FirstName,   P.LastName FROM [HumanResources].[Employee] as E INNER JOIN [Person].[Person] as P on E.BusinessEntityID = P.BusinessEntityID")
        for row in sqljson.cursor:
            print(row)
        print()
    def ConverttOjson(conn):
        print("Convert to Json")
        sqljson.cursor.execute("select top 3 BusinessEntityID, FirstName, MiddleName, LastName from [Person].[Person] For JSON PATH, ROOT('Person')")
        for row in sqljson.cursor:
            print(row)
        print()
    
    def queryjson(self):
        print("Query Json Data")
        sqljson.cursor.execute('''DECLARE @json NVARCHAR(1000)
        SELECT @json = N'{
            "Person": [
                {
                    "BusinessEntityID": 285,
                    "FirstName": "Syed",
                    "LastName": "Abbas"
                    },
                    {
                    "BusinessEntityID": 293,
                    "FirstName": "Catherine",
                    "LastName": "Abel"
                    },
                    {
                        "BusinessEntityID": 295,
                        "FirstName": "Kim",
                        "LastName": "Abercrombie"
                    }
                    ]
                    }'
                select BusinessEntityID, FirstName, LastName
                FROM OPENJSON(@json, '$.Person')
                WITH(
                    BusinessEntityID INT,
                    FirstName varchar(500),
                    LastName varchar(500)
                    ) as Person ''')
        for row in sqljson.cursor:
            print(row)
        print()

      
obj1 = sqljson("converter")
testprog=int(input("Enter any value to test options or 0 to end::"))
while(testprog!=0):
    print("Sql and Json Queries Options \n1. Read Sql Server Data \n2. Like Query")
    print("3. IN Query \n4. Between Query \n5. Logical Operation Query")
    print("6. Join Query \n7. Convert to Json \n8. Query Json")
    option=int(input("Enter your choice of query::"))
    if(option==1):
        obj1.read()
    elif(option==2):
        obj1.likeqry()
    elif(option==3):
        obj1.INqry()
    elif(option==4):
        obj1.betweenqry()
    elif(option==5):
        obj1.lessthanqry()
    elif(option==6):
        obj1.joinqry()
    elif(option==7):
        obj1.ConverttOjson()
    elif(option==8):
        obj1.queryjson()
    testprog=int(input("\n Enter any value to test options or 0 to end::"))