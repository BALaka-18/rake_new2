from rake_new2 import Rake

r = Rake()

text = "How are your children ?"
r.get_keywords_from_raw_text(text)

print(r.get_keywords_with_scores())