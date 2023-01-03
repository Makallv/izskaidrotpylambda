def main(text: str):
    info = {
        'words': (words := text.split()),
        'characters': (chars := len(''.join(words))),
        'avg_char_per_word': round(chars / len(words), 2)
    }

    print(info)


if __name__ == '__main__':
    main("This is a very long sentence.")
    main("This is a very long text.")
