import streamlit as st
import pandas as pd
from datetime import datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EV ChargeFinder",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL PAGE
       ======================================================== */

    .stApp {
        background-color: #f5f8f6;
        color: #17231d;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 3.2rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       STREAMLIT TOP BAR
       ======================================================== */

    header[data-testid="stHeader"] {
        background-color: transparent;
        height: 0;
    }

    header[data-testid="stHeader"] * {
        display: none;
    }

    div[data-testid="stToolbar"] {
        display: none;
    }


    /* ========================================================
       MAIN HEADER
       ======================================================== */

    .main-title {
        font-size: 3.1rem;
        line-height: 1.15;
        font-weight: 850;
        color: #17231d !important;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }

    .main-subtitle {
        color: #5f7067 !important;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 2rem;
    }


    /* ========================================================
       SEARCH CONTAINER
       ======================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-color: #d7e3db !important;
        border-radius: 16px !important;
        background-color: #ffffff !important;
    }


    /* ========================================================
       SECTION TITLES
       ======================================================== */

    .section-title {
        color: #17231d !important;
        font-size: 1.55rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
    }

    .section-subtitle {
        color: #64746b !important;
        font-size: 0.92rem;
        margin-bottom: 1rem;
    }


    /* ========================================================
       NORMAL STREAMLIT TEXT
       ======================================================== */

    .stApp p,
    .stApp label,
    .stApp span,
    .stApp div {
        color: #17231d;
    }


    /* ========================================================
       INPUT LABELS
       ======================================================== */

    label[data-testid="stWidgetLabel"] p {
        color: #405047 !important;
        font-weight: 650 !important;
    }


    /* ========================================================
       INPUT BOXES
       ======================================================== */

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border-color: #cbd9d0 !important;
        color: #17231d !important;
    }

    div[data-baseweb="input"] input {
        color: #17231d !important;
    }

    div[data-baseweb="select"] span {
        color: #17231d !important;
    }


    /* ========================================================
       BUTTON
       ======================================================== */

    .stButton > button {
        background-color: #168043 !important;
        color: #ffffff !important;
        border: 1px solid #168043 !important;
        border-radius: 10px !important;
        min-height: 44px;
        font-weight: 750;
    }

    .stButton > button p {
        color: #ffffff !important;
    }

    .stButton > button:hover {
        background-color: #116b37 !important;
        border-color: #116b37 !important;
    }


    /* ========================================================
       METRICS
       ======================================================== */

    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: 1px solid #d7e3db !important;
        border-radius: 12px !important;
        padding: 16px !important;
    }

    div[data-testid="stMetric"] label {
        color: #63746b !important;
    }

    div[data-testid="stMetric"] label p {
        color: #63746b !important;
    }

    div[data-testid="stMetricValue"] {
        color: #17231d !important;
        font-weight: 800 !important;
    }

    div[data-testid="stMetricValue"] div {
        color: #17231d !important;
    }

    div[data-testid="stMetricDelta"] {
        color: #168043 !important;
    }


    /* ========================================================
       HEADINGS
       ======================================================== */

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: #17231d !important;
    }


    /* ========================================================
       GENERAL CAPTIONS
       ======================================================== */

    .stCaption,
    [data-testid="stCaptionContainer"] {
        color: #718078 !important;
    }

    [data-testid="stCaptionContainer"] p {
        color: #718078 !important;
    }


    /* ========================================================
       SUCCESS MESSAGE
       ======================================================== */

    div[data-testid="stAlert"] {
        border-radius: 12px !important;
    }

    div[data-testid="stAlert"] p {
        color: #176b3a !important;
        font-weight: 650;
    }


    /* ========================================================
       WARNING / INFO
       ======================================================== */

    div[data-testid="stAlert"] p {
        color: #39473f !important;
    }


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {
        border-color: #d9e3dd !important;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        text-align: center;
        color: #7b8982 !important;
        font-size: 0.8rem;
        line-height: 1.6;
        padding-top: 25px;
        padding-bottom: 10px;
    }

    .footer p {
        color: #7b8982 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("ev_charging_station_data_deploy.csv")


df = load_data()


# ============================================================
# HELPER FUNCTION
# ============================================================

def convert_time_to_hour(time_string):
    return datetime.strptime(
        time_string,
        "%I:%M %p"
    ).hour


# ============================================================
# TIME OPTIONS
# ============================================================

time_options = [
    datetime.strptime(
        f"{hour}:00",
        "%H:00"
    ).strftime("%I:%M %p")
    for hour in range(24)
]


# ============================================================
# CITY OPTIONS
# ============================================================

cities = sorted(
    df["city"].dropna().unique()
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">⚡ EV ChargeFinder</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Find available EV charging stations and discover the most '
    'suitable option for your preferred time and location.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SEARCH SECTION
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-title">'
        'Find a charging station'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Choose when and where you want to charge your EV.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3, col4 = st.columns(
        [1.15, 1.15, 1.15, 0.75],
        gap="medium"
    )

    with col1:

        selected_date = st.date_input(
            "📅 Date",
            value=datetime.today().date()
        )

    with col2:

        selected_time = st.selectbox(
            "🕐 Preferred Time",
            time_options,
            index=time_options.index("05:00 PM")
        )

    with col3:

        selected_city = st.selectbox(
            "📍 City",
            cities
        )

    with col4:

        st.write("")
        st.write("")

        search_button = st.button(
            "Find Stations",
            use_container_width=True
        )


# ============================================================
# SEARCH RESULTS
# ============================================================

if search_button:

    formatted_date = selected_date.strftime(
        "%d-%m-%Y"
    )

    hour = convert_time_to_hour(
        selected_time
    )

    filtered = df[
        (df["hour_of_day"] == hour) &
        (df["city"] == selected_city) &
        (df["ports_available"] > 0)
    ]


    # ========================================================
    # NO RESULTS
    # ========================================================

    if filtered.empty:

        st.write("")

        st.warning(
            "No charging stations are available "
            "for your selected criteria."
        )

        st.info(
            "Try selecting another time or city."
        )


    # ========================================================
    # RESULTS
    # ========================================================

    else:

        # ----------------------------------------------------
        # SORT STATIONS
        # ----------------------------------------------------

        recommended = filtered.sort_values(
            by=[
                "ports_available",
                "utilization_rate"
            ],
            ascending=[
                False,
                True
            ]
        )


        # ----------------------------------------------------
        # UNIQUE STATIONS
        # ----------------------------------------------------

        recommended = recommended.drop_duplicates(
            subset=["station_id"],
            keep="first"
        )


        # ----------------------------------------------------
        # BEST STATION
        # ----------------------------------------------------

        best_station = recommended.iloc[0]


        # ====================================================
        # RESULT HEADER
        # ====================================================

        st.write("")

        st.markdown(
            f'<div class="section-title">'
            f'Charging options in {selected_city}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="section-subtitle">'
            f'{formatted_date} · {selected_time} · '
            f'{len(recommended)} available stations'
            f'</div>',
            unsafe_allow_html=True
        )

        st.write("")


        # ====================================================
        # BEST RECOMMENDATION
        # ====================================================

        st.success(
            "⭐ Recommended for you"
        )

        with st.container(border=True):

            st.subheader(
                best_station["station_name"]
            )

            # Darker Station ID + Charger Type
            st.markdown(
                f"""
                <div style="
                    color:#405047;
                    font-size:15px;
                    font-weight:600;
                    margin-top:-5px;
                    margin-bottom:15px;
                ">
                    {best_station['charger_type']}
                    · Station ID: {best_station['station_id']}
                </div>
                """,
                unsafe_allow_html=True
            )

            best_col1, best_col2, best_col3 = st.columns(3)

            with best_col1:

                st.metric(
                    "Available Points",
                    int(
                        best_station["ports_available"]
                    )
                )

            with best_col2:

                st.metric(
                    "Occupied Points",
                    int(
                        best_station["ports_occupied"]
                    )
                )

            with best_col3:

                st.metric(
                    "Estimated Wait",
                    f"{int(best_station['estimated_wait_time_mins'])} min"
                )


        # ====================================================
        # AVAILABLE STATIONS
        # ====================================================

        st.write("")

        st.markdown(
            '<div class="section-title">'
            'Available stations'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Top stations ranked by available charging points.'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")


        # ====================================================
        # TOP 5 STATIONS
        # ====================================================

        for _, row in recommended.head(5).iterrows():

            with st.container(border=True):

                st.subheader(
                    f"🔌 {row['station_name']}"
                )

                # Darker Station ID
                st.markdown(
                    f"""
                    <div style="
                        color:#405047;
                        font-size:14px;
                        font-weight:600;
                        margin-top:-5px;
                        margin-bottom:12px;
                    ">
                        Station ID: {row['station_id']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.success(
                    f"● {int(row['ports_available'])} "
                    f"charging points available"
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.markdown(
                        '<div style="'
                        'color:#405047;'
                        'font-size:14px;'
                        'font-weight:600;'
                        'margin-bottom:4px;">'
                        'Charger Type'
                        '</div>',
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f'<div style="'
                        f'color:#26362e;'
                        f'font-size:16px;'
                        f'font-weight:700;">'
                        f'{row["charger_type"]}'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                with col2:

                    st.caption("Available")

                    st.write(
                        f"**{int(row['ports_available'])}**"
                    )

                with col3:

                    st.caption("Occupied")

                    st.write(
                        f"**{int(row['ports_occupied'])}**"
                    )

                with col4:

                    st.caption("Estimated Wait")

                    st.write(
                        f"**{int(row['estimated_wait_time_mins'])} min**"
                    )


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.write("")
st.divider()

info_col1, info_col2, info_col3 = st.columns(3)

with info_col1:

    st.metric(
        "Dataset Records",
        f"{len(df):,}"
    )

with info_col2:

    st.metric(
        "Cities",
        df["city"].nunique()
    )

with info_col3:

    st.metric(
        "Charging Stations",
        df["station_id"].nunique()
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        EV Charging Station Availability Prediction
        <br>
        Supervised Machine Learning · EV ChargeFinder
    </div>
    """,
    unsafe_allow_html=True
)
