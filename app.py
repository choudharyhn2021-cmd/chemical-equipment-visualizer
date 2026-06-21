from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

REQUIRED_COLUMNS = {
    "Equipment Name",
    "Type",
    "Flowrate",
    "Pressure",
    "Temperature"
}


def analyze_csv(file):

    df = pd.read_csv(file)

    if not REQUIRED_COLUMNS.issubset(df.columns):
        missing = REQUIRED_COLUMNS - set(df.columns)
        raise ValueError(
            f"Missing columns: {', '.join(missing)}"
        )

    df = df.dropna()

    for col in ["Flowrate", "Pressure", "Temperature"]:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    df = df.dropna()

    summary = {
        "total_equipment": int(len(df)),
        "average_flowrate": round(df["Flowrate"].mean(), 2),
        "average_pressure": round(df["Pressure"].mean(), 2),
        "max_temperature": float(df["Temperature"].max()),
        "equipment_type_distribution":
            df["Type"].value_counts().to_dict()
    }

    return summary


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["file"]

    summary = analyze_csv(file)

    return render_template(
        "result.html",
        summary=summary
    )


if __name__ == "__main__":
    app.run(debug=True)