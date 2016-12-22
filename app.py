from flask import Flask, render_template, request
import json
import requests


app = Flask(__name__)


@app.route("/")
def main():

    url = 'https://www.donedeal.ie/search/api/v4/find/?'
    #payload = {'source':'trade','section':'cars','adType':'forsale','sort':'relevance #desc','priceType':'Euro','mileageType':'Kilometres','area':['Kilkenny'],'max':30,'start':0,'dependant':[]}

    #payload = {"words":"levin","area":["Ireland"],"section":"all","adType":"forsale","sort":"publishdate desc","priceType":"Euro","mileageType":"Kilometres","max":30,"start":0}

    payload = {"words":"levin","area":["Ireland"],"section":"all","adType":"forsale","sort":"publishdate desc","priceType":"Euro","mileageType":"Kilometres","max":30,"start":0,"price_from":"1000","price_to":"2000"}

    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    result = r.json()

    option_list=[]
    description=[]
    car_list = []
    photo=[]
    names=[]
    price=[]
    image=[]
    price=[]
    age=[]
    keyInfo=[]
    county=[]
    friendlyUrl=[]
    count = 0;

    #for each in result['ads']:
        #print each['photos'][0]['small']
    #print result

    """for each in result['ads']:
        if('price' in each):
            if(int(each['price'].replace(',','')) > 1000 and int(each['price'].replace(',','')) < 2000):
                car_list = ("Name: ", each["header"],"Price: ",each["price"], "Image: ", each['photos'][0]['small'])
                names.append(each["header"])
                price.append(each["price"])
                image.append(each["photos"][0]["small"])
                #print("Name: ", each["header"],"Price: ",each["price"], "Image: ", each['photos'][0]['small'])
    print names
    """
    for each in result['ads']:
        if(each['age'].endswith("days")):
            days = each['age'][:-4]
            if(int(days) < 11):
                option_list.append(each['header'])
                description.append(each['description'])
                photo.append(each['photos'][0]['small'])
                price.append(each['price'])
                age.append(each['age'])
                keyInfo.append(each['keyInfo'])
                county.append(each['county'])
                friendlyUrl.append(each['friendlyUrl'])
    car_list.append(option_list)
    #car_list.append(description)
    car_list.append(photo)

    print friendlyUrl

    #dict_d = {"name":option_list, "description":description, "photo":photo}

    cars =  zip(option_list, description, photo, price, age, keyInfo, county, friendlyUrl)

    #print dict_e

    #print dict_d["name"]

    #for cur in result['ads']:
        #option_list.append(cur['header'])
        #description.append(cur['description'])
        #photo.append(cur['photos'][0]['small'])


    return render_template('levin.html', option_list = option_list, description=description, photo=photo, car_list=car_list, cars=cars)


@app.route("/glanza")
def glanza():

    url = 'https://www.donedeal.ie/search/api/v4/find/?'
    #payload = {'source':'trade','section':'cars','adType':'forsale','sort':'relevance #desc','priceType':'Euro','mileageType':'Kilometres','area':['Kilkenny'],'max':30,'start':0,'dependant':[]}

    #payload = {"words":"levin","area":["Ireland"],"section":"all","adType":"forsale","sort":"publishdate desc","priceType":"Euro","mileageType":"Kilometres","max":30,"start":0}

    payload = {"words":"glanza","area":["Ireland"],"section":"all","adType":"forsale","sort":"publishdate desc","priceType":"Euro","mileageType":"Kilometres","max":30,"start":0,"price_from":"1000","price_to":"2500"}

    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    result = r.json()

    option_list=[]
    description=[]
    photo=[]
    price=[]
    age=[]
    keyInfo=[]
    county=[]

"""
    for each in result['ads']:
        if(each['age'].endswith("mins")):
            if(each['age'].endswith("days")):
                days = each['age'][:-4]
                if(int(days) < 11):
                    option_list.append(each['header'])
                    description.append(each['description'])
                    photo.append(each['photos'][0]['small'])
                    price.append(each['price'])
                    age.append(each['age'])
                    keyInfo.append(each['keyInfo'])
                    county.append(each['county'])
"""

    for each in result['ads']:
        if(each['age'].endswith("mins")):
            if(each['age'].endswith("days")):
                days = each['age'][:-4]
                if(int(days) < 11):
                    option_list.append(each['header'])
                    description.append(each['description'])
                    photo.append(each['photos'][0]['small'])
                    price.append(each['price'])
                    age.append(each['age'])
                    keyInfo.append(each['keyInfo'])
                    county.append(each['county'])   

    cars =  zip(option_list, description, photo, price, age, keyInfo, county)


    return render_template('glanza.html', option_list = option_list, cars=cars)


@app.route("/test", methods=['GET','POST'])
def test():
    select = request.form.get('option')
    return(str(select))

if __name__ == "__main__":
    app.run()
