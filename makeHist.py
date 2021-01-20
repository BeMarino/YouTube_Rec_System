from matplotlib import pyplot as plt
from lib import getDataFromDb

query_list={}
query_list["canali suggeriti per categoria"]="select categoryTitle, count(DISTINCT publisher) from video group by(categoryTitle) "
query_list["Numero di volte in cui un canale è stato suggerito"]="select  publisher,sum(suggested_times) as suggested_times from video group by(publisher) order by(suggested_times) desc "
query_list["Numero di volte in cui una categoria è stata suggerita"]="SELECT categoryTitle,sum(suggested_times)as suggested_times FROM `video` GROUP BY(categoryTitle)order by(suggested_times) desc"

for key in query_list.keys():
    to_hist=getDataFromDb(query_list[key])
    print(to_hist.values())
    plt.bar(to_hist.keys(),to_hist.values())
    plt.title(key)
    plt.figure(plt.show())
    
    