
def latin_ish_words(text):
    """
    English has words from Latin (or Spanish, Italian, French, etc.) and from
    German (or Dutch, etc.). They are often easy to tell apart. This function
    picks up some of the Latin sounding words based on some of their features.

    Latin features:
        - tion (as in navigation, isolation, or mitigation)
        - ex (as in explanation, exfiltrate, or expert)
        - ph (as in philosophy, philanthropy, or ephemera)
        - ost, ist, ast (as in hostel, distribute, past)

    NOTE: this matching method is not exact, many Germanic words include those
    features, and many Latin words lack them.
    NOTE: matching this way should ignore case. For the purpose of this exercise,
    we want to match any word containing at least one of the strings above.
    NOTE: the latin feature can be in the middle of the word, it can be a suffix,
    a prefix or a full word on its own.

    E.g., latin_ish_words("This works well") is []
    E.g., latin_ish_words("This functions as expected")
    is ["functions", "expected"]

    :param text: string that forms English text
    :return: list of words present in the text that have any of the Latin
    features listed above. Order of the words in the list should be the same as
    how they appear in the text.
    :rtype: list
    """
    words_with_latin =[]
    latin_features =["tion", "ex", "ph", "ost", "ist", "ast"]
    text = text.split()
    print(text)

    for i in range(len(text)):
        pim = text[i]
        for word in latin_features:
            if word in pim.lower():
                print(pim)
                words_with_latin.append(pim)
    print(words_with_latin)
    return words_with_latin
latin_ish_words(text="Paul - Ex Marine")