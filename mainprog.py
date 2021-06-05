from flask import Flask, render_template,request,session,flash
import sqlite3 as sql
import os
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/gohome')
def homepage():
    return render_template('index.html')

@app.route('/service')
def servicepage():
    return render_template('services.html')

@app.route('/coconut')
def coconutpage():
    return render_template('Coconut.html')

@app.route('/cocoa')
def cocoapage():
    return render_template('cocoa.html')

@app.route('/arecanut')
def arecanutpage():
    return render_template('arecanut.html')

@app.route('/paddy')
def paddypage():
    return render_template('paddy.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')





@app.route('/enternew')
def new_user():
   return render_template('signup.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['Name']
            phonno = request.form['MobileNumber']
            email = request.form['email']
            unm = request.form['Username']
            passwd = request.form['password']
            with sql.connect("agricultureuser.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO agriuser(name,phono,email,username,password)VALUES(?, ?, ?, ?,?)",(nm,phonno,email,unm,passwd))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()

@app.route('/userlogin')
def user_login():
   return render_template("login.html")

@app.route('/logindetails',methods = ['POST', 'GET'])
def logindetails():
    if request.method=='POST':
            usrname=request.form['username']
            passwd = request.form['password']

            with sql.connect("agricultureuser.db") as con:
                cur = con.cursor()
                cur.execute("SELECT username,password FROM agriuser where username=? ",(usrname,))
                account = cur.fetchall()

                for row in account:
                    database_user = row[0]
                    database_password = row[1]
                    if database_user == usrname and database_password==passwd:
                        session['logged_in'] = True
                        return render_template('home.html')
                    else:
                        flash("Invalid user credentials")
                        return render_template('login.html')

@app.route('/predictinfo')
def predictin():
   return render_template('info.html')



@app.route('/predict',methods = ['POST', 'GET'])
def predcrop():
    if request.method == 'POST':
        comment = request.form['comment']
        comment1 = request.form['comment1']
        comment2 = request.form['comment2']
        data = comment
        data1 = comment1
        data2 = int(comment2)
        # type(data2)
        print(data)
        print(data1)
        print(data2)

        dff = pd.read_csv("data/maindata.csv")
        df1 = dff[dff['Location'].str.contains(data)]
        df2 = df1[df1['Soil'].str.contains(data1)]
        # print("df2:",df2)

        area = (df2['Area'])
        yeilds = (df2['yeilds'])
        price = (df2['price'])

        res2 = price / yeilds
        print("res2", res2)

        area_input = data2
        res3 = res2 * area_input
        print("res3:", res3)

        res = yeilds / area
        # print(res)

        res4 = res * area_input
        print("res4:", res4)

        df2.insert(11, "calculation", res3)
        df2.to_csv('data/file.csv', index=False)

        df2.insert(12, "res4", res4)
        df2.to_csv('data/file.csv', index=False)

        data = pd.read_csv("data/file.csv", usecols=range(13))
        Type_new = pd.Series([])

        for i in range(len(data)):
            if data["Crops"][i] == "Coconut":
                Type_new[i] = "Coconut"

            elif data["Crops"][i] == "Cocoa":
                Type_new[i] = "Cocoa"

            elif data["Crops"][i] == "Coffee":
                Type_new[i] = "Coffee"

            elif data["Crops"][i] == "Cardamum":
                Type_new[i] = "Cardamum"

            elif data["Crops"][i] == "Pepper":
                Type_new[i] = "Pepper"

            elif data["Crops"][i] == "Arecanut":
                Type_new[i] = "Arecanut"

            elif data["Crops"][i] == "Ginger":
                Type_new[i] = "Ginger"

            elif data["Crops"][i] == "Tea":
                Type_new[i] = "Tea"

            else:
                Type_new[i] = data["Crops"][i]

        data.insert(13, "Crop val", Type_new)
        data.drop(["Year", "Location", "Soil", "Irrigation", "Crops", "yeilds", "calculation", "price"], axis=1,
                  inplace=True)
        data.to_csv("data/train.csv", header=False, index=False)
        data.head()

        avg1 = data['Rainfall'].mean()
        print('Rainfall avg:', avg1)
        avg2 = data['Temperature'].mean()
        print('Temperature avg:', avg2)
        avg3 = data['Humidity'].mean()
        print('Humidity:', avg3)

        testdata = {'Area': area_input,
                    'Rainfall': avg1,
                    'Temperature': avg2,
                    'Humidity': avg3}

        df7 = pd.DataFrame([testdata])
        df7.to_csv('data/test.csv', header=False, index=False)

        import csv
        import math
        import operator

        def euclideanDistance(instance1, instance2, length):
            distance = 0
            for x in range(length):
                distance += (pow((float(instance1[x]) - float(instance2[x])), 2))
            return math.sqrt(distance)

        def getNeighbors(trainingSet, testInstance, k):
            distances = []
            length = len(testInstance) - 1

            for x in range(len(trainingSet)):
                dist = euclideanDistance(testInstance, trainingSet[x], length)
                distances.append((trainingSet[x], dist))
            distances.sort(key=operator.itemgetter(1))
            neighbors = []
            for x in range(k):
                neighbors.append(distances[x][0])
            return neighbors

        def getResponse(neighbors):
            classVotes = {}
            for x in range(len(neighbors)):
                response = neighbors[x][-1]
                if response in classVotes:
                    classVotes[response] += 1
                else:
                    classVotes[response] = 1
            sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
            return sortedVotes[0][0]

        trainingSet = []
        testSet = []
        with open('data/train.csv', 'r') as csvfile:
            lines = csv.reader(csvfile)
            dataset = list(lines)
            # print(dataset)



            for x in range(len(dataset) - 1):
                for y in range(5):
                    dataset[x][y] = float(dataset[x][y])
                trainingSet.append(dataset[x])

        with open('data/test.csv', 'r') as csvfile1:
            lines1 = csv.reader(csvfile1)
            # print(lines1)
            dataset1 = list(lines1)
            # print(dataset1)

            for p in range(len(dataset1)):
                for q in range(4):
                    dataset[p][q] = float(dataset[p][q])
                testSet.append(dataset1[p])

        print("trainingset:", trainingSet)
        print("testingset:", testSet)
        # print("1:",len(trainingSet))
        # print("2:",len(testSet))
        k = 1
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
        response = getResponse(neighbors)
        print("\nNeighbors:", neighbors)
        print('\nResponse:', response)

        res10 = [lis[4] for lis in neighbors]
        res12 = str(res10).strip('[]')
        print(res12)

        rem = response

        data1 = pd.read_csv("data/file.csv", usecols=range(13))

        for row in csv.reader(data1):
            val = data1[data1.Crops != rem]
            val.insert(13, "Cropval", Type_new)
            val.drop(["Year", "Location", "Soil", "Irrigation", "Crops", "yeilds", "calculation", "price"], axis=1,
                     inplace=True)
            val.to_csv("data/train1.csv", header=False, index=False)
            val.head()

        import csv
        import math
        import operator

        def euclideanDistance(instance1, instance2, length):
            distance = 0
            for x in range(length):
                distance += (pow((float(instance1[x]) - float(instance2[x])), 2))
            return math.sqrt(distance)

        def getNeighbors(trainingSet, testInstance, k):
            distances = []
            length = len(testInstance) - 1

            for x in range(len(trainingSet)):
                dist = euclideanDistance(testInstance, trainingSet[x], length)
                distances.append((trainingSet[x], dist))
            distances.sort(key=operator.itemgetter(1))
            neighbors = []
            for x in range(k):
                neighbors.append(distances[x][0])
            return neighbors

        def getResponse(neighbors):
            classVotes = {}
            for x in range(len(neighbors)):
                response = neighbors[x][-1]
                if response in classVotes:
                    classVotes[response] += 1
                else:
                    classVotes[response] = 1
            sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
            return sortedVotes[0][0]

        trainingSet = []
        testSet = []
        with open('data/train1.csv', 'r') as csvfile:
            lines = csv.reader(csvfile)
            dataset = list(lines)
            # print(dataset)



            for x in range(len(dataset) - 1):
                for y in range(5):
                    dataset[x][y] = float(dataset[x][y])
                trainingSet.append(dataset[x])

        with open('data/test.csv', 'r') as csvfile1:
            lines1 = csv.reader(csvfile1)
            # print(lines1)
            dataset1 = list(lines1)
            # print(dataset1)

            for p in range(len(dataset1)):
                for q in range(4):
                    dataset[p][q] = float(dataset[p][q])
                testSet.append(dataset1[p])

        print("trainingset:", trainingSet)
        print("testingset:", testSet)

        k = 1
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
        response2 = getResponse(neighbors)
        print("\nNeighbors:", neighbors)
        print('\nResponse:', response2)

        res11 = [lis[4] for lis in neighbors]
        res13 = str(res11).strip('[]')
        print(res13)

        print("\nSuggested crop 1:", response, ",", res12)
        print("\nSuggested crop 2:", response2, ",", res13)

    return render_template('resultpred.html', prediction=response, price=res12, prediction1=response2, price1=res13)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('login.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
