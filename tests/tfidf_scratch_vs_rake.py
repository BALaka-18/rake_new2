# Hacky fix to remove top-level import errors
import sys
from timeit import default_timer as timer

from rake_new2 import Rake
from tfidf_vectorizer.extract_keywords_tfidf_scratch import TF_IDF_Scratch

sys.path.append("..")

docs = [
    "Java is a class based, object oriented programming language that is designed to have as few implementation dependencies as possible. It is a general purpose programming language intended to let application developers write once, run anywhere, meaning that compiled Java code can run on all platforms that support Java without the need for recompilation.",
    "C++ is a general purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or 'C with Classes'. The language has expanded significantly over time, and modern C++ now has object oriented, generic, and functional features in addition to facilities for low-level memory manipulation.",
    "Python is an interpreted, high level and general purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object oriented approach aim to help programmers write clear, logical code for small and large scale projects.",
    "Haskell is a general purpose, statically typed, purely functional programming language with type inference and lazy evaluation. Developed to be suitable for teaching, research and industrial application, Haskell has pioneered a number of advanced programming language features such as type classes, which enable type safe operator overloading.",
    "Kotlin is a cross platform, statically typed, general purpose programming language with type inference. Kotlin is designed to interoperate fully with Java, and the JVM version of Kotlin's standard library depends on the Java Class Library, but type inference allows its syntax to be more concise. Kotlin mainly targets the JVM, but also compiles to JavaScript or native code (via LLVM), e.g. for native iOS apps sharing business logic with Android apps. Language development costs are borne by JetBrains, while the Kotlin Foundation protects the Kotlin trademark.",
]

manual_keyphrases = [
    "python",
    "guido van rossum",
    "first released",
    "1991",
    "notable",
    "interpreted",
    "high level",
    "general purpose",
    "design philosophy",
    "code readability",
    "whitespace",
    "language constructs",
    "object oriented",
    "clear",
    "logical",
    "small",
    "large scale projects",
]

start_tfidf = timer()
tfidf = TF_IDF_Scratch()
tfidf_res = set([word[0] for word in tfidf.get_keywords(docs, 2)])
end_tfidf = timer()

start_rake = timer()
rake = Rake()
rake.get_keywords_from_raw_text(docs[2])
rake_res = rake.get_ranked_keywords()
end_rake = timer()

print("tf-idf (scratch) results: ")
print(tfidf_res)
print()
print("rake results: ")
print(rake_res)
print()

tfidf_total = len(tfidf_res)
tfidf_tp = 0
rake_total = len(rake_res)
rake_tp = 0
for keyphrase in manual_keyphrases:
    if keyphrase in tfidf_res:
        tfidf_tp += 1
    if keyphrase in rake_res:
        rake_tp += 1

tfidf_precision = tfidf_tp / tfidf_total * 100
rake_precision = rake_tp / rake_total * 100

print("tf-idf (scratch) precision score: " + str(round(tfidf_precision, 2)) +
      "%")
print("rake precision score: " + str(round(rake_precision, 2)) + "%")
print()

print("tf-idf (scratch) time: " + str(round(end_tfidf - start_tfidf, 3)) + "s")
print("rake time: " + str(round(end_rake - start_rake, 3)) + "s")
