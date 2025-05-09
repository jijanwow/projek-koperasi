from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Function to search members (same as before)
def find_member(member_id):
    try:
        df = pd.read_excel("MultipleFiles/ahli_koperasi.xlsx")
        id_col = [col for col in df.columns if 'id' in col.lower()][0]
        result = df[df[id_col].astype(str).str.strip() == member_id.strip()]
        return result
    except:
        return pd.DataFrame()

# Homepage route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ic_number = request.form["ic_number"]
        result = find_member(ic_number)
        
        if not result.empty:
            return render_template("result.html", found=True, data=result.to_dict("records"))
        else:
            return render_template("result.html", found=False, ic_number=ic_number)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)