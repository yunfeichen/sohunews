# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import datetime

dbuser = 'root'
dbpass = ''
dbname = 'sohunews'
dbhost = '127.0.0.1'
dbport = '3306'

class SohunewsPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()
        # 清空表：
        # self.cursor.execute("truncate table weather;")
        self.conn.commit()

    def process_item(self, item, spider):
        curTime = datetime.datetime.now()
        try:
            self.cursor.execute("""INSERT INTO sohunews (cname, curl, cdate, csourcename, csourceurl, updateTime)  
                            VALUES (%s, %s, %s, %s, %s, %s)""",
                                (
                                    item['cname'].encode('utf-8'),
                                    item['curl'].encode('utf-8'),
                                    item['cdate'].encode('utf-8'),
                                    item['csourcename'].encode('utf-8'),
                                    item['csourceurl'].encode('utf-8'),
                                    curTime,
                                )
                                )

            self.conn.commit()


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item