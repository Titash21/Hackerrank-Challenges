
# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime as dt
def grouping(contents):
    #The first index has the start year and end year!
    start_string=contents[0]
    #They are comma separated !
    date=start_string.split(',')
    #they are dash separtated again !
    Syear=date[0].split('-')
    start_year=int(Syear[0])
    start_month=int(Syear[1]) #08 ---> 8
    starting=str(start_year)+"-"+str(start_month)+"-"+"1"
    #Converting to date format
    start_date=dt.strptime(starting,"%Y-%m-%d")


    Eyear=date[1].split('-')
    end_year=int(Eyear[0])
    end_month=int(Eyear[1])
    #Converting to date format
    ending=str(end_year)+"-"+str(end_month)+"-"+"1"
    end_date=dt.strptime(ending,"%Y-%m-%d")

    final_list=[]
    #Now remove it from the list
    contents.remove(start_string)
    #Also have to remove the new line from the list
    contents.remove("")
    #iterate
    for item in contents:
        date=item.split(',')
        strings=''.join(date[0])
        date=strings.split('-')
        year=date[0]
        month=date[1]
        day=date[2]
        newdate=year+"-"+month+"-"+day
        newdate1=dt.strptime(newdate,"%Y-%m-%d")

        if(newdate1>=start_date and newdate1<(end_date)):
            year_month=year+"-"+month
            string=year_month+item[10:]
            final_list.append(string)


    final_list.sort(reverse=True)

    new_Dict={}
    for item in final_list:
        intermediate = item.split(',')
        new_key=intermediate[0]+intermediate[1]
        new_value=''.join(intermediate[2])
        if new_key in new_Dict:
            int_new_value=int(new_value)
            new_Dict[new_key]=int(new_Dict[new_key])+int_new_value
        else:
            new_Dict[new_key]=int(new_value)

    dictlist=[]
    for key in new_Dict:
        string=key.split()
        temp =string[0]+", "+string[1]+", "+str(new_Dict[key])
        dictlist.append(temp)


    #Combine the lists !!
    d={}
    temp_list=[]
    for item in dictlist:
        intermediate = item.split(',')
        key = intermediate[0]
        value = ','.join(intermediate[1:])
        if key in d:
            #Sort the multiple values as well !
            temp_list=d[key]
            temp_list.append(value)
            temp_list.sort()
            d[key]=temp_list
        else:
            d[key] = [value]



    dictlist=[]
    for key in new_Dict:
        string=key.split()
        temp =string[0]+", "+string[1]+', '+str(new_Dict[key])
        dictlist.append(temp)

    dictlist=[]
    for key in d:
        temp =key+","+','.join(d[key])
        dictlist.append(temp)

    dictlist.sort(reverse=True)
    for item in dictlist:
        print(item)



def main():
    contents = []
    while True:
        try:
            line = input("")
        except EOFError:
            break
        contents.append(line)
    grouping(contents)
main()
