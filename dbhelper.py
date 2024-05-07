import mysql.connector

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='database-1.cnqnfmdhai0m.ap-northeast-1.rds.amazonaws.com',
                                           user='admin', password='fcbarcelona', database='indigo')
            self.mycursor = self.conn.cursor()
            print('Connection established')

        except:
            print('Connection error')

    def fetch_city_names(self):

        city=[]

        self.mycursor.execute('''
        select distinct Source from flights2
        union
        select distinct Destination from flights2;
        ''')

        data=self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city


    def fetch_all_flights(self,source,destination):
        self.mycursor.execute('''
        select * from flights2 where Source='{}' and Destination='{}';
        '''.format(source,destination))

        data=self.mycursor.fetchall()

        return data


    def fetch_airline_frequency(self):

        airline=[]
        frequency=[]

        self.mycursor.execute('''
        select Airline,count(*) from flights2
        group by Airline;
        ''')

        data=self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency

    def busy_airport(self):

        city=[]
        frequency=[]

        self.mycursor.execute('''
        select Source,count(*) from (select Source from flights2
                             union all 
						     select Destination from flights2) t
        group by t.Source
        order by count(*) desc;
        ''')

        data=self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city,frequency

    def daily_frequency(self):

        date = []
        frequency = []

        self.mycursor.execute('''
        select Date_of_Journey,count(*) from flights2
        group by Date_of_Journey;
        ''')

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency