from flask import Flask, render_template, request
import json
import requests


app = Flask(__name__)


def carFunc(result):


    name=[]
    description=[]
    car_list = []
    photo=[]
    names=[]
    price=[]
    image=[]
    price=[]
    age=[]
    carInfo=[]
    county=[]
    friendlyUrl=[]
    count = 0;



    for each in result['ads']:
        if(each['spotlight'] == True):
            pass
        else:
            count=count+1
            if(each['age'].endswith("mins")):
                if('keyInfo' in each):
                    carInfo.append(each['keyInfo'])
                name.append(each['header'])
                description.append(each['description'])
                photo.append(each['photos'][0]['small'])
                price.append(each['price'])
                age.append(each['age'])
                county.append(each['county'])
                friendlyUrl.append(each['friendlyUrl'])
            elif(each['age'].endswith("hour")):
                if('keyInfo' in each):
                    carInfo.append(each['keyInfo'])
                name.append(each['header'])
                description.append(each['description'])
                photo.append(each['photos'][0]['small'])
                price.append(each['price'])
                age.append(each['age'])
                county.append(each['county'])
                friendlyUrl.append(each['friendlyUrl'])
            elif(each['age'].endswith("hours")):
                if('keyInfo' in each):
                    carInfo.append(each['keyInfo'])
                name.append(each['header'])
                description.append(each['description'])
                photo.append(each['photos'][0]['small'])
                price.append(each['price'])
                age.append(each['age'])
                county.append(each['county'])
                friendlyUrl.append(each['friendlyUrl'])
            elif(each['age'].endswith("day")):
                if('keyInfo' in each):
                    carInfo.append(each['keyInfo'])
                name.append(each['header'])
                description.append(each['description'])
                photo.append(each['photos'][0]['small'])
                price.append(each['price'])
                age.append(each['age'])
                county.append(each['county'])
                friendlyUrl.append(each['friendlyUrl'])
            elif(each['age'].endswith("days")):
                if('keyInfo' in each):
                    carInfo.append(each['keyInfo'])
                #name.append(each['header'])
                description.append(each['description'])
                photo.append(each['photos'][0]['small'])
                price.append(each['price'])
                age.append(each['age'])
                county.append(each['county'])
                friendlyUrl.append(each['friendlyUrl'])
                days = each['age'][:-4]
                if(int(days) <= 4):
                    name.append(each['header'])
                



    cars =  zip(name, description, photo, price, age, county, friendlyUrl, carInfo)
    return cars


@app.route("/")
def main():

    url = 'https://www.donedeal.ie/search/api/v4/find/?'
    payload = {"words":"levin","area":["Ireland"],"section":"all","adType":"forsale","sort":"publishdate desc","priceType":"Euro","mileageType":"Kilometres","max":49,"start":0,"price_from":"1000","price_to":"2000"}

    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    result = r.json()

    return render_template('levin.html', cars=carFunc(result))


@app.route("/glanza", methods=['GET','POST'])
def glanza():

    url = 'https://www.donedeal.ie/search/api/v4/find/?'

    payload = {"words":"glanza","area":["Ireland"],"section":"all","adType":"forsale","sort":"publishdate desc","priceType":"Euro","mileageType":"Kilometres","max":49,"start":0,"price_from":"1000","price_to":"2000"}

    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    result = r.json()

    print request.form.get("tester")

    return render_template('glanza.html', cars=carFunc(result))


@app.route("/corolla")
def corolla():

    url = 'https://www.donedeal.ie/search/api/v4/find/?'

    payload = {"words":"corolla","area":["Ireland"],"section":"all","adType":"forsale","sort":"publishdate desc","priceType":"Euro","mileageType":"Kilometres","max":49,"start":0,"price_from":"2000","price_to":"6000"}

    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    result = r.json()

    return render_template('corolla.html', cars=carFunc(result))

@app.route("/me", methods=['GET', 'POST'])
def me():
    if request.method == 'POST':
        date = request.form['tester']
        print date
        return
    else:
        return render_template('me.html')



@app.route("/test", methods=['GET','POST'])
def test():
    select = request.form.get('option')
    return(str(select))

if __name__ == "__main__":
    app.run()



