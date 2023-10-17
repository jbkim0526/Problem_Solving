import re 

text = "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\">"
pattern = "<meta property=\"og:url\" content=\"https://.+\"/>"
print(len("<a href=\"https://"))

p = re.compile(pattern)
m = p.search(text)

print(text)
print(p)


print(m.group())
