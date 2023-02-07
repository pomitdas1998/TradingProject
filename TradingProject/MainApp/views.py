from django.shortcuts import render,HttpResponse
from .models import*
import pandas as pd





# Create your views here.

#Store the data present in the file in the python list of candle objects.
def create_db(file_path):
    df = pd.read_csv(file_path , delimiter=",")
    list_of_csv = [list(row) for row in df.values]

    for l in list_of_csv:
        Candle.objects.create(
            Index_name = l[0],
            date = l[1],
            time = l[2],
            open = l[3],
            high = l[4],
            low = l[5],
            close = l[6],
            volume = l[7],        
        )


#view data function
def View_all_data(request):
    candle = Candle.objects.all().values()
    print(candle)
    context = {
         'candle' : candle
            }

#logic for convertng the list of candles that will be one minute into a given timeframe
    # dj = pd.DataFrame([vars(s) for s in candle])
    # print(dj)
    
    return render(request,'View.html',context)

#get file and upload in Files folder
def index(request):
    if request.method =="POST":
        file =request.FILES['file']
        obj = File.objects.create(file = file)
        create_db(obj.file)

    return render(request,'index.html')
