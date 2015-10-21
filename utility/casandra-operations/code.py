#!/usr/bin/python

'''
@author: Yogesh Kumar
@summary: To add/update/delete/select data from cassandra.
@resourse-1: http://www.guguncube.com/603/pycassa-gettting-started-with-apache-cassandra-using-python
@resourse-2: http://pycassa.github.io/pycassa/tutorial.html
'''

from pycassa.system_manager import *
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

class CassandraDemo(object):
    def __init__(self, database, table):
        self.database = database
        self.table = table

    def create_connections(self):
        self.pool = ConnectionPool(self.database)
        self.cf = ColumnFamily(self.pool, self.table)

    def create_database_and_table(self):
        super_cf = False # consider super columns to be deprecated
        s = SystemManager()

        # create keyspace if it doesn't exist
        if database not in s.list_keyspaces():
            s.create_keyspace(database, SIMPLE_STRATEGY, {'replication_factor': '1'})

        # delete column family from the keyspace if it does exist.
        if table in s.get_keyspace_column_families(database):
            s.drop_column_family(database, table)

        # create coulmn family in the keyspace
        if table not in s.get_keyspace_column_families(database):
            print("table is creating...")
            s.create_column_family(database, table, super = super_cf, comparator_type = ASCII_TYPE)
        s.close()

        return True

    def insert_data(self):
        print '\nemployee data is inserting...'
        self.cf.insert('1', {'fn':'yogesh', 'ln':'kumar', 'ct': 'Ajmer', 'em': 'yoku2010@gmail.com'})
        self.cf.insert('2', {'fn':'amit', 'ln':'pandita', 'ct': 'Delhi', 'em': 'apandita@gmail.com'})
        self.cf.insert('3', {'fn':'sandeep', 'ln':'tak', 'ct': 'Ajmer', 'em': 'sandeep@gmail.com', 'mb': '8890467032'})


    def get_data(self):
        print '\nemployee data is featching...'
        data1 = self.cf.get('1')
        data2 = self.cf.get('2', columns = ['fn', 'ln', 'em'])
        data3 = self.cf.get('3', column_start = 'ct', column_finish = 'fn')
        data4 = self.cf.get('1', column_reversed = False, column_count = 3)
        data5 = self.cf.get('1', column_reversed = True, column_count = 3)
        print data1
        print data2
        print data3
        print data4
        print data5

    def get_multiple_data(self):
        print '\ngetting multiple employees data...'
        row_keys = ['1','2','3']
        data = self.cf.multiget(row_keys)
        print data

    def get_data_by_range(self):
        '''
        if you get an error don't worry about this, it's a Cassandra limitation Issue
        '''
        print '\ngetting employees data by range...'
        start_row_key = '1'
        end_row_key = '3'
        data = self.cf.get_range(start = start_row_key, finish = end_row_key)
        for key, columns in data:
            print key,coulmns

    def get_count(self):
        print '\nget employee row\'s colunm count'
        print self.cf.get_count('1')
        print self.cf.get_count('1', columns = ['fn', 'ln'])
        print self.cf.get_count('1', column_start = 'em')

    def get_multi_count(self):
        print '\nget multiple employees row\'s colunm count'
        row_keys = ['1','2','3']
        columns = ['fn', 'ln', 'mb']
        column_start = 'ct'
        column_finish = 'fn'
        print self.cf.multiget_count(row_keys)
        print self.cf.multiget_count(row_keys, columns = columns)
        print self.cf.multiget_count(row_keys, column_start = column_start, column_finish = column_finish)

    def update_data(self):
        print '\nemployee data is updating...'
        self.cf.insert('1', {'pwd':'yoku@2010', 'ct':'Noida'})


    def delete_data(self):
        print '\ndelete data from employee'
        row = '2'
        self.cf.remove(row)

    def get_all_rows(self):
        print '\ngetting rows name...'
        print [v[0] for v in self.cf.get_range()]

    def get_all_columns_of_row(self):
        print '\ngetting columns name of a row'
        row = '1'
        data = self.cf.get(row)
        print data.keys()

if '__main__' == __name__:
    database = 'demo'
    table = 'employees'
    cd = CassandraDemo(database, table)
    cd.create_database_and_table()
    cd.create_connections()
    cd.insert_data()
    cd.get_data()
    cd.get_multiple_data()
    #cd.get_data_by_range()
    cd.get_count()
    cd.get_multi_count()
    cd.update_data()
    cd.get_data()
    cd.get_all_rows()
    cd.get_all_columns_of_row()
    #cd.delete_data()
    #cd.get_data() you will get an exception to get row number 2