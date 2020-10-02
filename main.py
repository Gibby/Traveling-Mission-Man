import os
import precompute
import travelingmissionman
import sys
import io
from flask import Flask, send_file, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    index_path = os.path.join(app.static_folder, "index.html")
    return send_file(index_path)

@app.route("/getroute", methods=['GET', 'POST'])
def getroute():
    missions = request.form.get('missions')
    nullsec = request.form.get('nullsec')
    mission_lines = '''\
{lines}
'''.format(lines=missions)
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    travelingmissionman.main(mission_lines)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    output = output.replace('\n', '<br>')
    return render_template('results.html',output=output)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
