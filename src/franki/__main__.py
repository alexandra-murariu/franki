from franki.clipboard import process_subtitles, watch_clipboard
from franki.logic import handle_subtitle


def main():
    watch_clipboard()
    process_subtitles(handle_subtitle)

    print(" Franki is running — press Ctrl+C to stop")

    import time
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n Franki stopped.")


if __name__ == "__main__":
    main()
