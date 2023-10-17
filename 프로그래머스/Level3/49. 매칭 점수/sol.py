from collections import defaultdict
import re

def solution(word, pages):
    website_names = []
    external_links = defaultdict(set)
    link_counts = defaultdict(int)
    word_counts = defaultdict(int)
    scores = []
    url_p = re.compile("<meta property=\"og:url\" content=\"https://\S+\"/>")
    body_p = re.compile("<body>.+</body>",re.DOTALL)
    href_p = re.compile("<a href=\"https://\S+\">")

    for page in pages:
        cur_website = url_p.search(page).group()[41:-3]
        website_names.append(cur_website)
        body = body_p.search(page).group()[6:-7]
        word_p = re.compile("(?<=[^a-z]){}(?=[^a-z])".format(word),re.IGNORECASE)
        word_counts[cur_website] += len(word_p.findall(body))
        hrefs = list(map(lambda x: x[17:-2],href_p.findall(body)))
        for href in hrefs:
            link_counts[cur_website] += 1
            external_links[href].add(cur_website)

    for website_name in website_names:
        base_score = word_counts[website_name]
        external_score = 0
        for external_link in external_links[website_name]:
            external_score += word_counts[external_link]/link_counts[external_link]
        scores.append(base_score + external_score)

    max_score = max(scores)
    return scores.index(max_score)





#print(solution(	"blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution(	"Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))