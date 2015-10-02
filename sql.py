from  dbinfo import dbinfo
from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy.orm import mapper
from sqlalchemy.orm import create_session
from flask import Flask


app = lask(__name__)

engine = create_engine('mysql://{}:{}@{}/test?charset=utf8'.format(dbinfo['USER'], dbinfo['PASSWORD'], dbinfo['HOST_IP']))
metadata = MetaData(engine)

db_table = Table('b000001', metadata, autoload=True)
#s = users_table.select()
#r = s.execute()
#print r.fetchall()

class db(object):
    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.date, self.open)


db_table = Table('b000001', metadata, autoload=True)
dbmapper = mapper(db, db_table)

session = create_session()
query = session.query(db)
#db_info = query.filter_by(date='2015-09-21')
#print db_info
#print db_info.open

@app.route('/')
def show_info():
    db_info = query.filter_by(date='2015-09-21').first()
    output = ''
    output += str(db_info.open)
    output += str(db_info.close)

    return output 

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
