import re

## 
text = " My name is Shyam "
print(repr(text))
print(text.lower())
print(text.upper())
print(text.strip())
print(text.strip().replace(" ", "-"))

## Search
text = "abc123xyz456"
result = re.search(r"\d+", text)
print(result.group())
numbers = re.findall(r"\d+", text)
print(numbers)
new = re.sub(r"\d+", "", text)
print(new)
# print(bool(re.match("name", text)))
# print(bool(re.match("is", text)))
text = "apple,banana;orange grape"
items = re.split(r"[,; ]+", text)
print(items)

text = """
Visit https://google.com
and https://openai.com
"""

print(re.findall(r"https?://\S+", text))
def cleanup(text: str):
    text = text.strip()
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = re.sub(r"[^A-za-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

sample = """ Hello,,,   Python___Developer!! 
   Welcome---to    Agentic     AI.    """

print("\nOriginal:")
print(sample)

print("\nCleaned:")
print(cleanup(sample))