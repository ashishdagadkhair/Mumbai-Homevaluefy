from flask import Flask,render_template,url_for,request,flash,redirect
import util
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mumbaihousing'

# Home Page
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')



# Result Page
@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        location = str(request.form['locationSelect'])
        area = int(request.form['sqftInput'])
        bhk_rk = str(request.form['bhkOrRk'])
        no_bedrooms=1 #if it is rk, then by default no of rooms is 1
        if bhk_rk == 'BHK': 
            no_bedrooms = int(request.form['bedroomsInput'])
        property_type = str(request.form['propertyType'])
        
        output = util.predict_price(area,no_bedrooms,location,property_type,bhk_rk)
        unit='Lakhs' #By default o/p is in lakhs.
        if(output>=100):
            unit='Cr'
            output = output/100
        output = round(output,2)
            
        return render_template('result.html',price=output,unit=unit)
    return redirect('/')


# Model Evaluation
@app.route('/modelEvaluation')
def model_evaluation():
    return render_template('MEval.html')


if __name__ == "__main__":
    app.run(debug=True,port=5000)







