from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/offer_cal',methods=['POST'])
def offer_operation():
    if (request.method=='POST'):
        cost1=int(request.form['cost1'])
        cost2=int(request.form['cost2'])
        cost3=int(request.form['cost3'])
        cost4=int(request.form['cost4'])
        cost5=int(request.form['cost5'])
        Total_cost=cost1+cost2+cost3+cost4+cost5
        if Total_cost<=1000:
           price=Total_cost-(0.1*Total_cost)
        if (Total_cost>1000) and (Total_cost<=2000):
           price=Total_cost-(0.2*Total_cost)
        if Total_cost>2000:
            price=Total_cost-(0.3*Total_cost)   
        return render_template('result.html',result=price)       











if __name__=='__main__':
    app.run(debug=True)