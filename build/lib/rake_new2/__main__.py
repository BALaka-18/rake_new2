from rake_new2 import Rake

def main():
    text = "Keyword extraction is not that difficult after all. There are many libraries that can help you with keyword extraction. Rapid automatic keyword extraction is one of those."
    rake_obj = Rake()
    rake_obj.get_keywords_from_raw_text(text)
    kw_s = rake_obj.get_keywords_with_scores()
    print(kw_s)

if __name__ == "__main__":
    main()