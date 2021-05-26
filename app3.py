from flask import Flask,request,render_template,make_response,send_file
import os
import pandas as pd
import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import linkage
from sklearn.cluster import AgglomerativeClustering

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home1.html")

@app.route('/cluster',methods=["POST"])
def cluster():
        if request.method=="POST":
            file=request.files["file"]
            file.save(os.path.join("uploads",file.filename))
            Univ=pd.read_csv("F:/Universities/uploads/Universities.csv")

            #file=request.files["file"]
            #file.save(os.path.join("uploads",file.filename)
            #Univ=pd.read_csv("F:/Universities/Universities.csv")

            df=Univ.iloc[:,1:]
            def df_normalise(i):
                x=(i-i.mean())/i.std()
                return x
            df_norm=df_normalise(df)
            hcluster=AgglomerativeClustering(n_clusters=3,affinity="euclidean").fit(df_norm)
            hcluster_labels=pd.Series(hcluster.labels_)
            Univ["Cluster"]=hcluster_labels
            #Univ.to_csv("Universities_new.csv")
            #Univ.save(os.path.join("uploads",Universities_new.csv))
            #resp = make_response(Univ.to_csv())
            #resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
            #resp.headers["Content-Type"] = "text/csv"
            Univ.to_csv("F:/Universities/uploads/Universities_new.csv")
        return render_template("download.html")

@app.route('/download',methods=["GET","POST"])
def download():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "F:/Universities/uploads/Universities_new.csv"
    return send_file(path, as_attachment=True)

if __name__=="__main__":
    app.run(debug=True)
