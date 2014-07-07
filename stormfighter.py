# ---------------------------------------------------------------------------
# Created by Gerrit Hendriksen (gerrit.hendriksen@deltares.nl)
# v1.0 created on 10-03-2012 (ddmmyyyy)
# v1.1 adapted on 15-03-2012 (ddmmyyyy) added matplotlib to module import for
#      display of graphs
#
# Description: Use of psycopg2 module to query database ICES
# ---------------------------------------------------------------------------

# import modules
import psycopg2
import matplotlib.pyplot as plt

# create connection to ices database
conn = psycopg2.connect("dbname=postgres host=localhost user=postgres password=postgres")

# create a cursor object called cur
cur = conn.cursor()

# construct a query string
strSql = "SELECT * FROM topo_contours_10ft LIMIT 1000"

# execute the query
cur.execute(strSql)

# store the result of the query into Tuple c
c = cur.fetchall()
for x in c[0]:
    print x

# closes the connection
cur.close()

# now store day and avg(cphl) in two separate arrays
cphl = []
days = []

for i in range(len(c)):
    days.append((c[i])[2])
    cphl.append((c[i])[3])

# plot the     
plt.xlabel('days')
plt.plot(cphl)
plt.show()
