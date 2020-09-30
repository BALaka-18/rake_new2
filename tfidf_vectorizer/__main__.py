'''
Example usage of the TF_IDF_Scratch class
'''

from extract_keywords_tfidf_scratch import TF_IDF_Scratch


def main():
    # Example corpus
    docs = [
        "Java is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is a general-purpose programming language intended to let application developers write once, run anywhere, meaning that compiled Java code can run on all platforms that support Java without the need for recompilation.",
        "C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or 'C with Classes'. The language has expanded significantly over time, and modern C++ now has object-oriented, generic, and functional features in addition to facilities for low-level memory manipulation.",
        "Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.",
    ]

    # # Constructing the tf-idf runner object
    tfidf_obj = TF_IDF_Scratch()

    # Set the index of the document to be extracted
    doc_idx = 0
    # Set the maximum number of keywords, or don't pass it in
    # to extract all the keywords
    max_num = 10

    print(tfidf_obj.get_keywords(docs, doc_idx, max_num))


if __name__ == "__main__":
    main()
