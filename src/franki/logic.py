from franki.wordminer import get_hard_words, load_b1_wordlist
from franki.ankigen import ensure_deck, add_card
from franki.larousse import get_translation

b1_words = load_b1_wordlist()
ensure_deck("Franki")


def handle_subtitle(subtitle):
    print(f"\n New subtitle: {subtitle}")
    hard_words = get_hard_words(subtitle, b1_words)
    print("Hard words found:", hard_words)

    for word in hard_words:
        definition = get_translation(word)
        print(f"Adding card: {word} — {definition}")
        if definition:
            front = f"<div style='font-size: 1.6em; font-weight: bold;'>{word}</div>"
            back = f"""
            <div style='font-size: 1.2em; margin-bottom: 12px;'>📺 <i>{subtitle}</i></div>
            <hr style='margin: 12px 0;'>
            <div style='font-size: 1.1em;'>📖 {format_definition(definition)}</div>
            """
            add_card(front, back)


def format_definition(def_text):
    replacements = [
        ("Synonymes :", "<br><b>Synonymes</b> :"),
        ("Contraires :", "<br><b>Contraires</b> :"),
    ]
    for target, repl in replacements:
        def_text = def_text.replace(target, repl)
    return def_text.strip()
