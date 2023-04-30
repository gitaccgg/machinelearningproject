from django.shortcuts import render

from joblib import load


model = load('./savedModels/model.joblib')


# Create your views here.
def predictor(request):
     if request.method =='POST':
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']
        y_pred =  model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        if y_pred[0]==0:
                y_pred = 'Setosa'
        if y_pred[0]==1:
                y_pred = 'versicolor'
        else:
                y_pred = 'Virginica' 

     else: 
        y_pred = "None"


        # try:
        #    converted = float(input_string)

        # except ValueError:
        #    converted = 0
               
     return render(request,'irisModel.htm',{'result':y_pred})