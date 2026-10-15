from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)


# --------------------------------------------------
# LOAD TRAINED MODEL
# --------------------------------------------------

with open("predictive_maintenance_model.pkl", "rb") as file:
    model = pickle.load(file)


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# DIAGNOSTIC PAGE
# --------------------------------------------------

@app.route("/diagnostics")
def diagnostics():
    return render_template("predict.html")


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    # ----------------------------------------------
    # GET USER INPUT
    # ----------------------------------------------

    machine_type = request.form["machine_type"]

    air_temperature = float(
        request.form["air_temperature"]
    )

    process_temperature = float(
        request.form["process_temperature"]
    )

    rotational_speed = float(
        request.form["rotational_speed"]
    )

    torque = float(
        request.form["torque"]
    )

    tool_wear = float(
        request.form["tool_wear"]
    )


    # ----------------------------------------------
    # FEATURE ENGINEERING
    # ----------------------------------------------

    temperature_difference = (
        process_temperature - air_temperature
    )

    power_w = (
        torque *
        rotational_speed *
        2 *
        np.pi / 60
    )

    wear_torque_interaction = (
        tool_wear * torque
    )


    # ----------------------------------------------
    # MACHINE TYPE ENCODING
    # ----------------------------------------------

    type_l = 1 if machine_type == "L" else 0
    type_m = 1 if machine_type == "M" else 0


    # ----------------------------------------------
    # CREATE MODEL INPUT
    # EXACT TRAINING FEATURE ORDER
    # ----------------------------------------------

    input_data = pd.DataFrame(
        [[
            air_temperature,
            process_temperature,
            rotational_speed,
            torque,
            tool_wear,
            temperature_difference,
            power_w,
            wear_torque_interaction,
            type_l,
            type_m
        ]],
        columns=[
            "Air temperature [K]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]",
            "Temperature_Difference",
            "Power_W",
            "Wear_Torque_Interaction",
            "Type_L",
            "Type_M"
        ]
    )


    # ----------------------------------------------
    # MODEL PREDICTION
    # ----------------------------------------------

    prediction = int(model.predict(input_data)[0])

    failure_probability = float(
        model.predict_proba(input_data)[0][1]
    )

    probability_percent = round(
        failure_probability * 100,
        2
    )


    # ----------------------------------------------
    # RISK INTELLIGENCE
    # ----------------------------------------------

    if failure_probability < 0.30:

        risk_level = "LOW"
        risk_class = "low"

        recommendation = (
            "Machine conditions indicate a low predicted failure risk. "
            "Continue routine monitoring and scheduled maintenance."
        )

        maintenance_priority = "Routine Monitoring"

    elif failure_probability < 0.60:

        risk_level = "MEDIUM"
        risk_class = "medium"

        recommendation = (
            "Elevated machine failure risk detected. Review operating "
            "conditions and schedule a preventive inspection."
        )

        maintenance_priority = "Preventive Inspection"

    else:

        risk_level = "HIGH"
        risk_class = "high"

        recommendation = (
            "High machine failure risk detected. Prioritize this machine "
            "for inspection and preventive maintenance."
        )

        maintenance_priority = "Priority Inspection"


    predicted_condition = (
        "Potential Failure"
        if prediction == 1
        else "Normal Operation"
    )


    # ----------------------------------------------
    # SEND RESULTS TO HTML
    # ----------------------------------------------

    return render_template(
        "result.html",

        machine_type=machine_type,

        air_temperature=air_temperature,
        process_temperature=process_temperature,
        rotational_speed=rotational_speed,
        torque=torque,
        tool_wear=tool_wear,

        temperature_difference=round(
            temperature_difference,
            2
        ),

        power_w=round(
            power_w,
            2
        ),

        wear_torque_interaction=round(
            wear_torque_interaction,
            2
        ),

        prediction=prediction,

        probability=probability_percent,

        risk_level=risk_level,
        risk_class=risk_class,

        predicted_condition=predicted_condition,

        recommendation=recommendation,

        maintenance_priority=maintenance_priority
    )


# --------------------------------------------------
# ANALYTICS PAGE
# --------------------------------------------------

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)