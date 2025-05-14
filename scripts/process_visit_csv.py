import pandas as pd


def process_visit_csv(raw_df):
    """TODO: Add docstring."""
    raw_df["Date"] = pd.to_datetime(raw_df["Date"].str.rsplit(" ", n=1).str[0])
    raw_df["Formatted_Date"] = raw_df["Date"].dt.strftime("%m-%d-%Y")

    raw_df["Visit ID"] = (
        raw_df["Client Name"].str.split(" ").str[0].str[0]
        + raw_df["Client Name"].str.split(" ").str[-1].str[0]
        + "_VS-"
        + raw_df["Formatted_Date"]
    )

    raw_df["🤒 Patient"] = raw_df["Client Name"]
    raw_df["Provider Name"] = raw_df["Provider"]

    raw_df["Provider Name"] = [s.replace("Dr. ", "") for s in raw_df["Provider Name"]]

    def map_appt_type(appt_type):
        if "Initial" in appt_type:
            return "Initial"
        elif "Discovery Call" in appt_type:
            return "Discovery Call"
        elif "Follow-up" in appt_type:
            return "Follow-Up"
        else:
            return ""

    raw_df["Type"] = raw_df["Appointment Type"].apply(map_appt_type)
    raw_df["📄 Claim"] = raw_df["Visit ID"].str.replace("VS", "CL")
    raw_df["💰 Cash Payment"] = raw_df["Visit ID"].str.replace("VS", "PAY")

    processed_df = raw_df[
        [
            "Visit ID",
            "Formatted_Date",
            "🤒 Patient",
            "📄 Claim",
            "Status",
            "Type",
            "Actual Duration",
            "Provider Name",
            "💰 Cash Payment",
        ]
    ]
    processed_df = processed_df.rename(
        columns={
            "Formatted_Date": "Date",
            "Actual Duration": "Duration (mins)",
        }
    )
    return processed_df
