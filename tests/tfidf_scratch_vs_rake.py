# Hacky fix to remove top-level import errors
import sys
sys.path.append("..")

from tfidf_vectorizer.extract_keywords_tfidf_scratch import TF_IDF_Scratch
from rake_new2 import Rake

from timeit import default_timer as timer

docs = [
        "Java is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is a general-purpose programming language intended to let application developers write once, run anywhere, meaning that compiled Java code can run on all platforms that support Java without the need for recompilation.",
        "C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or 'C with Classes'. The language has expanded significantly over time, and modern C++ now has object-oriented, generic, and functional features in addition to facilities for low-level memory manipulation.",
        "Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.",
        "Haskell is a general-purpose, statically typed, purely functional programming language with type inference and lazy evaluation. Developed to be suitable for teaching, research and industrial application, Haskell has pioneered a number of advanced programming language features such as type classes, which enable type-safe operator overloading.",
        "Kotlin is a cross-platform, statically typed, general-purpose programming language with type inference. Kotlin is designed to interoperate fully with Java, and the JVM version of Kotlin's standard library depends on the Java Class Library, but type inference allows its syntax to be more concise. Kotlin mainly targets the JVM, but also compiles to JavaScript or native code (via LLVM), e.g. for native iOS apps sharing business logic with Android apps. Language development costs are borne by JetBrains, while the Kotlin Foundation protects the Kotlin trademark."
]

start_tfidf = timer()
tfidf = TF_IDF_Scratch()
tfidf_res = tfidf.get_keywords(docs, 2)
end_tfidf = timer()

start_rake = timer()
rake = Rake()
rake.get_keywords_from_raw_text(docs[2])
rake_res = rake.get_keywords_with_scores()
end_rake = timer()

print(tfidf_res)
print()
print(rake_res)
print()
print('tf-idf (scratch) time: ' + str(end_tfidf - start_tfidf))
print('rake time: ' + str(end_rake - start_rake))