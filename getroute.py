@app.route("/getroute")
def getroute():
    missions = request.args.get('missions')
    nullsec = request.args.get('nullsec')
    f = open("missions.txt", "w")
    f.write(missions)
    f.close()
    results = travelingmissionman.main()
    return results
