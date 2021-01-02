def processing(text):
    nlp = spacy.load("en_core_web_sm")
    doc2 = nlp(text)
    persons = [ent.text for ent in doc2.ents if ent.label_ == "PERSON"]

    return persons


def spell_checker(text):
    name = processing(text)
    name_word = [i.split(" ") for i in name]
    y = [j for sub in name_word for j in sub]
    y = set(y)
    c = []
    for i in text.split():
        if i not in y:
            t = TextBlob(i)
            c_text = t.correct()
            c.append(str(c_text))
        else:
            c.append(str(i))
    x = " ".join(c)
    return x


def main():
    text = input()
    c_text = spell_checker(text)
    print(c_text)


if __name__ == "__main__":
    from textblob import TextBlob
    import spacy

    main()
