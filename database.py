from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, DateTime, Boolean
from sqlalchemy.sql import select
from datetime import datetime

engine=create_engine('sqlite:///bee_experiments.db')
metadata=MetaData()
experiment_table=Table('shb_bee_circadian', metadata,
                       Column('point_id', Integer,primary_key=True),
                       Column('box', Integer),
                       Column('correct', Boolean),
                       Column('datetime',DateTime), 
                       )

def create_table():
    metadata.create_all(engine, checkfirst=True)

def add_to_table(box, is_box_correct):
    conn=engine.connect()
    ins=experiment_table.insert()
    conn.execute(ins, box=str(box), correct=is_box_correct, datetime=datetime.today())

def show_table():
    conn=engine.connect()    
    s=select([experiment_table])
    result= conn.execute(s)
    r=result.fetchall()
    ret_dict=[]
    for item in r:
        ret_dict.append(dict(zip(['id','box', 'correct?', 'datetime'],item)))
    return ret_dict


def drop_table():
    experiment_table.drop(engine, checkfirst=True)
    print "table dropped"
