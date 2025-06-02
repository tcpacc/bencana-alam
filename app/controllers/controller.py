from flask import Blueprint, render_template, request, redirect
from ..models.models import Negara, BencanaAlam

controller_bp = Blueprint('controller_bp', __name__)

@controller_bp.route('/', methods=["GET", "POST"])
def index():
    selectedDisasters = BencanaAlam.query.all()
    selectedCountryId = 0
    countries = Negara.get_all()
    countriesNegaraList = []
    countriesTotalList = []
    for i in countries:
        if i.totalBencanaAlam >0:
            countriesNegaraList.append(i.negara)
            countriesTotalList.append(i.totalBencanaAlam)
    if request.method =='POST':
        countriesId = request.form["countries"]
        if countriesId != '0':
            selectedDisasters = BencanaAlam.query.filter_by(id_negara= countriesId ).all()
            selectedCountryId = int(countriesId)
    totals = [item.tahun for item in selectedDisasters]
    graphLabels = []
    graphValues = []
    for i in range(1990,2026):
        graphLabels.append(i)
        graphValues.append(totals.count(i))
    # if request.method == "POST":
    #     product = Product( name=request.form["name"], price=request.form["price"], category_id=request.form["category_id"]  )
    #     product.save()
    #     return redirect("/")
    bencanaAlam = BencanaAlam.get_all()
    # categories = Category.get_all()
    return render_template("index.html",bencanaAlam = bencanaAlam,countries=countries,graphLabels=graphLabels,graphValues=graphValues,selectedCountryId = selectedCountryId,countriesNegaraList=countriesNegaraList,countriesTotalList=countriesTotalList,selectedDisasters = selectedDisasters)

@controller_bp.route('/addCountry',methods = ['POST','GET'])
def addCountry():
    if request.method == 'POST':
        if Negara.query.filter_by(negara = request.form["country"].capitalize()).first() == None:
            negara = Negara(negara = request.form["country"].capitalize(),totalBencanaAlam = 0)
            negara.save()
            return redirect('/')
        return render_template("addCountry.html",wrong = True)
    return render_template("addCountry.html",wrong = False)

@controller_bp.route('/addDisaster',methods = ['POST','GET'])
def addDisaster():
    if request.method == 'POST':
        if BencanaAlam.query.filter_by(nama = request.form['name'],id_negara = request.form['countries'],tahun = request.form["year"]).first() ==None:
            bencana = BencanaAlam(nama = request.form["name"],tipe = request.form["type"],tahun = request.form["year"],id_negara = request.form['countries'])
            bencana.save()
            chosenCountry = Negara.query.filter_by(id = request.form['countries']).first()
            chosenCountry.add_total()
            return redirect('/')
    return render_template("addDisaster.html",countries=sorted(Negara.get_all(),key = lambda x : x.negara))
