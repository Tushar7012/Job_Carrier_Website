from flask import Flask,render_template
app = Flask(__name__)

JOBS = [
    {
        "id" : 1,
        "title" : "Software Engineer",
        "location" : "Bangalore",
        "salary" : "10LPA"
    },
    
    {
        "id" : 2,
        "title" : "ML Engineer",
        "location" : "Pune",
        "salary" : "25LPA"
    },
    
    {
        "id" : 3,
        "title" : "Data Engineer",
        "location" : "Mumbai",
        "salary" : "17LPA"
    },

    {
        "id" : 4,
        "title" : "Data Scientist",
        "location" : "Kolkata",
        "salary" : "20LPA"
    },

    {
        "id" : 5,
        "title" : "Product Manager",
        "location" : "San Francisco",
        "salary" : "55LPA"
    }
]


# Remember the __name__ is  the variable which will print the __main__
@app.route("/")
def hello():
    return render_template("home.html",jobs = JOBS,company_name = "Job")

if __name__ == "__main__":
    app.run(host = '0.0.0.0' ,debug = True)