import gradio as gr
import pandas as pd
from datetime import datetime

df = pd.read_csv("ev_charging_station_data.csv")


# ----------------------------------------
# Convert AM/PM → 24 Hour
# ----------------------------------------

def convert_time_to_hour(time_string):
    return datetime.strptime(time_string, "%I:%M %p").hour


# ----------------------------------------
# Main Recommendation Function
# ----------------------------------------

def check_availability(selected_date, selected_time, city):

    # Format date to DD-MM-YYYY
    # Correct date handling
    if selected_date is None:
        formatted_date = datetime.today().strftime("%d-%m-%Y")
    else:
        formatted_date = datetime.fromtimestamp(
            float(selected_date)
        ).strftime("%d-%m-%Y")

    # Convert AM/PM time
    hour = convert_time_to_hour(selected_time)

    # Filter dataset
    filtered = df[
        (df['hour_of_day'] == hour) &
        (df['city'] == city) &
        (df['ports_available'] > 0)
    ]

    # No stations available
    if filtered.empty:
        return f"""
        <div style="
            background:#ffffff;
            color:#000000;
            padding:30px;
            border-radius:15px;
            border:1px solid #cccccc;
            font-family:Arial;
        ">
            <h2>No Charging Stations Available</h2>

            <p><b>Date:</b> {formatted_date}</p>
            <p><b>Time:</b> {selected_time}</p>
            <p><b>City:</b> {city}</p>

            <p>Please try another time slot.</p>
        </div>
        """

    # Sort recommendation
    recommended = filtered.sort_values(
        by=['ports_available', 'utilization_rate'],
        ascending=[False, True]
    )

    # Keep only unique stations
    recommended = recommended.drop_duplicates(
        subset=['station_id'],
        keep='first'
    )

    best_station = recommended.iloc[0]

    html = f"""
    <div style="
        background:#ffffff;
        color:#000000;
        padding:35px;
        font-family:Arial, sans-serif;
    ">

    <h1 style="
        font-size:42px;
        border-bottom:2px solid #dddddd;
        padding-bottom:15px;
        margin-bottom:30px;
        color:#000000;
    ">
    EV Charging Recommendation System
    </h1>

    <div style="
        display:flex;
        gap:80px;
        margin-bottom:40px;
        flex-wrap:wrap;
    ">

        <div>
            <h3 style="color:#000000;">
            Date
            </h3>

            <p style="
                font-size:28px;
                font-weight:bold;
                color:#000000;
            ">
            {formatted_date}
            </p>
        </div>

        <div>
            <h3 style="color:#000000;">
            Selected Time
            </h3>

            <p style="
                font-size:28px;
                font-weight:bold;
                color:#000000;
            ">
            {selected_time}
            </p>
        </div>

        <div>
            <h3 style="color:#000000;">
            Selected City
            </h3>

            <p style="
                font-size:28px;
                font-weight:bold;
                color:#000000;
            ">
            {city}
            </p>
        </div>

    </div>

    <h2 style="
        font-size:34px;
        border-bottom:2px solid #dddddd;
        padding-bottom:10px;
        margin-bottom:25px;
        color:#000000;
    ">
    Available Charging Stations
    </h2>
    """

    # Top stations
    for _, row in recommended.head(5).iterrows():

        html += f"""
        <div style="
            border:1px solid #cccccc;
            border-radius:15px;
            padding:25px;
            margin-bottom:25px;
            background:#ffffff;
        ">

        <h3 style="
            font-size:30px;
            margin-bottom:20px;
            color:#000000;
        ">
        {row['station_name']}
        </h3>

        <table style="
            width:100%;
            border-collapse:collapse;
            font-size:22px;
        ">

        <tr>
            <td style="padding:14px;font-weight:bold;background:#f3f4f6;border:1px solid #dddddd;color:#000000;">
            Station ID
            </td>
            <td style="padding:14px;border:1px solid #dddddd;color:#000000;">
            {row['station_id']}
            </td>
        </tr>

        <tr>
            <td style="padding:14px;font-weight:bold;background:#f3f4f6;border:1px solid #dddddd;color:#000000;">
            Charger Type
            </td>
            <td style="padding:14px;border:1px solid #dddddd;color:#000000;">
            {row['charger_type']}
            </td>
        </tr>

        <tr>
            <td style="padding:14px;font-weight:bold;background:#f3f4f6;border:1px solid #dddddd;color:#000000;">
            Available Charging Points
            </td>
            <td style="padding:14px;border:1px solid #dddddd;color:#000000;">
            {row['ports_available']}
            </td>
        </tr>

        <tr>
            <td style="padding:14px;font-weight:bold;background:#f3f4f6;border:1px solid #dddddd;color:#000000;">
            Occupied Points
            </td>
            <td style="padding:14px;border:1px solid #dddddd;color:#000000;">
            {row['ports_occupied']}
            </td>
        </tr>

        <tr>
            <td style="padding:14px;font-weight:bold;background:#f3f4f6;border:1px solid #dddddd;color:#000000;">
            Wait Time
            </td>
            <td style="padding:14px;border:1px solid #dddddd;color:#000000;">
            {row['estimated_wait_time_mins']} mins
            </td>
        </tr>

        </table>
        </div>
        """

    # Best recommendation section
    html += f"""
    <div style="
        border:2px solid #000000;
        border-radius:15px;
        padding:30px;
        background:#ffffff;
        margin-top:40px;
    ">

    <h2 style="
        color:#000000;
        font-size:40px;
        font-weight:700;
        margin-bottom:30px;
    ">
    Best Recommended Station
    </h2>

    <table style="
        width:100%;
        border-collapse:collapse;
        font-size:28px;
    ">

    <tr>
        <td style="padding:18px;font-weight:bold;color:#000000;">
        Station:
        </td>

        <td style="padding:18px;color:#000000;">
        {best_station['station_name']}
        </td>
    </tr>

    <tr>
        <td style="padding:18px;font-weight:bold;color:#000000;">
        City:
        </td>

        <td style="padding:18px;color:#000000;">
        {best_station['city']}
        </td>
    </tr>

    <tr>
        <td style="padding:18px;font-weight:bold;color:#000000;">
        Available Charging Points:
        </td>

        <td style="padding:18px;color:#000000;">
        {best_station['ports_available']}
        </td>
    </tr>

    <tr>
        <td style="padding:18px;font-weight:bold;color:#000000;">
        Recommended Time:
        </td>

        <td style="padding:18px;color:#000000;">
        {selected_time}
        </td>
    </tr>

    <tr>
        <td style="padding:18px;font-weight:bold;color:#000000;">
        Estimated Wait Time:
        </td>

        <td style="padding:18px;color:#000000;">
        {best_station['estimated_wait_time_mins']} mins
        </td>
    </tr>

    </table>
    </div>
    </div>
    """

    return html


# ----------------------------------------
# Time Options
# ----------------------------------------

time_options = [
    datetime.strptime(f"{h}:00", "%H:00").strftime("%I:%M %p")
    for h in range(24)
]


# ----------------------------------------
# Interface
# ----------------------------------------

demo = gr.Interface(
    fn=check_availability,

    inputs=[
        gr.DateTime(
            label="Select Date",
            include_time=False
        ),

        gr.Dropdown(
            choices=time_options,
            value="05:00 PM",
            label="Select Time"
        ),

        gr.Dropdown(
            choices=sorted(df['city'].dropna().unique()),
            label="Select City"
        )
    ],

    outputs=gr.HTML(),

    title="EV Charging Recommendation System",

    description="""
    Select date, preferred charging time,
    and city to get charging station recommendations.
    """,

    submit_btn="Check Availability",
    clear_btn="Reset"
)

demo.launch()