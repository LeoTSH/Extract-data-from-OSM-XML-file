import sqlite3
import pprint

#Create DB
sqlite_db = 'OSM_Project.sqlite'

#Create connection
conn = sqlite3.connect(sqlite_db)

#Create cursor
cur = conn.cursor()

#Select data
cur.execute('''select user, count(*) as num
from (select user from nodes union all select user from ways)
group by user
order by num desc
limit 20;''')
for_print = cur.fetchall()

#Close connection
conn.close()

#Set header
header = [tuple[0] for tuple in cur.description]

#Print header and data
pprint.pprint(header)
pprint.pprint(for_print)