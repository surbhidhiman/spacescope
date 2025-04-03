import time
from datetime import datetime
from zoneinfo import ZoneInfo

def format_apod(apod_data):
    """Return a simple HTML/text block for the APOD"""
    return f"""
    <h2>🖼️ Astronomy Picture of the Day – {apod_data.date}</h2>
    <h3>{apod_data.title}</h3>
    <img src="{apod_data.url}" alt="APOD Image" style="max-width: 600px;" />
    <p>{apod_data.explanation}</p>
    <hr>
    """

def format_full_report(apod_data):
    """Combines APOD and DONKI sections into one HTML string"""
    time_generated = datetime.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles")).strftime('%Y-%m-%d %H:%M PT')
    return f"""
    <html>
    <head>
        <title>SpaceScope Daily Digest</title>
        <h3>Note: This is all from NASA's Astronomy Picture of the Day </h3>
    </head>
    <body style="font-family: sans-serif; max-width: 700px; margin: auto;">
        <h1>🚀 SpaceScope Daily Digest</h1>
        {format_apod(apod_data)}
        <footer>
            <p style="font-size: 0.9em;">Generated on {time_generated}</p>
        </footer>
    </body>
    </html>
    """
