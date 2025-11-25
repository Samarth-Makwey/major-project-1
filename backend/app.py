from flask import Flask,jsonify,request
from collections import OrderedDict
import netflix
import happiness
import energy

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to Netflix, World Happiness Report and Global Energy Comsumption Dataset API service."

#-----------------------------Netflix Dataset APIS-------------------------------------

@app.route('/api/movie-title')
def movie_title():
    title = request.args.get("title")
    return jsonify(netflix.movie_by_titleAPI(title))

@app.route('/api/tv-title')
def tv_title():
    title = request.args.get("title")
    return jsonify(netflix.tvshow_by_titleAPI(title))

@app.route('/api/movie-tv-distribution', methods=['GET'])
def movie_tv_distribution_api():
    result = netflix.movie_tv_distributionAPI()
    response = {
        "message": "Distribution of Movies and TV Shows on Netflix",
        "data": result
    }
    return jsonify(response)

@app.route('/api/top-directors', methods=['GET'])
def top_directors_api():
    result = netflix.top_10_directorsAPI()
    return jsonify(result)

@app.route('/api/country-stats', methods=['GET'])
def country_stats_api():
    result = netflix.country_statsAPI()
    
    response = OrderedDict()
    response["data"] = result
    return jsonify(response)

@app.route('/api/rating-distribution', methods=['GET'])
def rating_distribution_api():
    result = netflix.rating_distributionAPI()
    response = {
        "message": "Distribution of Netflix titles by rating type (in percentage)",
        "data": result
    }
    return jsonify(response)

#-----------------------------World Happiness Report Dataset APIs--------------------------------

@app.route('/api/top-countries', methods=['GET'])
def top_countries():
    limit = int(request.args.get('limit', 10))
    result = happiness.top_countriesAPI(limit)
    return jsonify(result)

@app.route('/api/factor-impact', methods=['GET'])
def factor_impact():
    result = happiness.factor_impactAPI()
    return jsonify(result)

@app.route('/api/country-info', methods=['GET'])
def country_info():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Please provide ?name=country_name parameter."})
    result = happiness.country_infoAPI(name)
    return jsonify(result)

@app.route('/api/compare-countries', methods=['GET'])
def compare_countries():
    c1 = request.args.get('country1')
    c2 = request.args.get('country2')
    if not c1 or not c2:
        return jsonify({"error": "Please provide ?country1= and ?country2= parameters."})
    result = happiness.compare_countriesAPI(c1, c2)
    return jsonify(result)

@app.route('/api/happiness-gap', methods=['GET'])
def happiness_gap():
    region = request.args.get('region')
    result = happiness.happiness_gapAPI(region)
    return jsonify(result)

@app.route('/api/country-rank-trend', methods=['GET'])
def country_rank_trend():
    country = request.args.get('country')
    result = happiness.country_rank_trendAPI(country)
    return jsonify(result)  

@app.route('/api/factor-averages', methods=['GET'])
def factor_averages():
    result = happiness.factor_averagesAPI()
    return jsonify(result)

#-----------------------Global Energy Consumption dataset APIs----------------------------

@app.route("/api/global-summary")
def global_summary():
    return jsonify(energy.global_energy_summaryAPI())

@app.route("/api/renewable-leaders")
def renewable_leaders():
    limit = int(request.args.get("limit", 10))
    return jsonify(energy.renewable_leadersAPI(limit))

@app.route("/api/cleanest-country")
def cleanest():
    limit = int(request.args.get("limit", 10))
    return jsonify(energy.cleanest_countriesAPI(limit))

@app.route("/api/compare-price")
def compare_price():
    c1 = request.args.get("country1")
    c2 = request.args.get("country2")
    return jsonify(energy.energy_price_comparisonAPI(c1, c2))

@app.route("/api/energy-mix")
def energy_mix():
    country = request.args.get("country")
    return jsonify(energy.energy_mixAPI(country))

@app.route("/api/factor-summary")
def factor_summary():
    return jsonify(energy.factor_summaryAPI())

app.run(debug=True)


