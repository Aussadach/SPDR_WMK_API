from flask import Flask, render_template
from xml.etree import ElementTree
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import scoped_session, sessionmaker
import datetime
import pytz
import operator

Host = "ec2-3-222-11-129.compute-1.amazonaws.com"
Database = "dddtvj83ts4s11"
User = "tcddcasvpynvte"
Port = "5432"
Password = "d2da9d5e29706ba51b3e5e30acb0fdcbaae972dd7916e66ddc6ee227f0ff7200"
URI = "postgresql://tcddcasvpynvte:d2da9d5e29706ba51b3e5e30acb0fdcbaae972dd7916e66ddc6ee227f0ff7200@ec2-3-222-11-129.compute-1.amazonaws.com:5432/dddtvj83ts4s11"
HerokuCLI = "heroku pg:psql postgresql-regular-39411 --app spdrgoldupdate"


engine = create_engine(
    "postgresql://tcddcasvpynvte:d2da9d5e29706ba51b3e5e30acb0fdcbaae972dd7916e66ddc6ee227f0ff7200@ec2-3-222-11-129.compute-1.amazonaws.com:5432/dddtvj83ts4s11")
db = scoped_session(sessionmaker(bind=engine))

# sql_string = """select * from spdr_gold_data order by cast(date_ as date) DESC LIMIT 8"""
# result = db.execute(sql_string)
# # db.commit()
# # db.close()

# for i in result:
#     # print(i.date_, i.last_sale, i.total_net_ounces,
#     #       i.total_net_tonnes, i.net_asset_value_in_trust)
#     # print(type(i.date_))
#     detail = {}
#     detail['date_'] = i.date_
#     detail['last_sale'] = float(i.last_sale)
#     detail['total_net_ounces'] = float(i.total_net_ounces)
#     detail['total_net_tonnes'] = float(i.total_net_tonnes)
#     detail['net_asset_value_in_trust'] = float(i.net_asset_value_in_trust)

#     print(detail)



app = Flask(__name__)







@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Diff')
def diff_day():
    # read data of today - 8
        # Get date today - 8 
        # Query Where date >= today - 8
    sql_string = """select * from spdr_gold_data order by cast(date_ as date) DESC LIMIT 8"""
    result = db.execute(sql_string)

    print(result)
    dates = []
    Current_val = []
    for i in result :
        
        dates.append(str(i.date_))
        Current_val.append(float(i.total_net_tonnes))


    print(dates)
    print(Current_val)

    Past_val = Current_val 
    print(Current_val[1:])
    print(Past_val[:-1])
    Diff = list(map(operator.sub, Current_val[1:], Past_val[:-1]))
    dates = dates[1:]
    print(Diff)
    Diff.reverse()
    print(Diff)
    print(dates)
    dates.reverse()
    print(dates)
    Result = {}
    Result['Dates'] = dates
    Result['Value'] = Diff
    #Result = list(zip(dates,Diff))

    print(Result)
    # for i in result:
    #     # print(i.date_, i.last_sale, i.total_net_ounces,
    #     #       i.total_net_tonnes, i.net_asset_value_in_trust)
    #     # print(type(i.date_))
    #     dates = []
    #     dates.append()
    #     dates['date_'] = i.date_
    #     # detail['last_sale'] = float(i.last_sale)
    #     # detail['total_net_ounces'] = float(i.total_net_ounces)
    #     dates['total_net_tonnes'] = float(i.total_net_tonnes)
    #     # detail['net_asset_value_in_trust'] = float(i.net_asset_value_in_trust)

    # return detail

    # calculate each date diff (today-yesterday) show in array
        # Split date and val
        # for i in enumerate(data) :
            #  Current = data[1:]
            #  Yesterday = data[:-1]
            #  Diff = list(map(operator.sub, A, B))
            #  Result = zip(date,Diff)

    # return array in json 
    return Result


@app.route('/data')
def week_data():

    return True



if __name__ == '__main__': app.run(debug=True)