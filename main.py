import pprint
from models import Session, APOD
from nasa.apod import APODFetcher
from utils.formatter import format_full_report

def main():
    apod = APODFetcher()

    print("\n--- Fetching Data ---")
    data = apod.fetch_data()
    apod.save_to_db(data)

    print("\n--- Formatting Report ---")
    session = Session()
    apod_data = session.query(APOD).order_by(APOD.date.desc()).limit(1).all()
    session.close()

    report = format_full_report(apod_data[0])

    with open("static_site/preview.html", "w", encoding="utf-8") as f:
        f.write(report)

    print("✅ Preview saved to static_site/preview.html")


if __name__ == "__main__":
    main()
