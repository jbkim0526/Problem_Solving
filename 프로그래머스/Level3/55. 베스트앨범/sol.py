from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_names = set()
    genre_plays = defaultdict(list)
 
    for i in range(len(genres)):
        genre = genres[i]
        genre_names.add(genre)
        genre_plays[genre].append((plays[i],i))

    l = [(genre, sum([t[0] for t in genre_plays[genre]])) for genre in genre_names]
    l.sort(key = lambda x: x[1])

    for i in range(1,len(l)+1):
        genre = l[-i][0]
        genre_play = genre_plays[genre]
        if len(genre_play) == 1:
            answer.append(genre_play[0][1])
            continue
        genre_play.sort(key = lambda x : (x[0],-x[1]))
        answer.append(genre_play[-1][1])
        answer.append(genre_play[-2][1])

    return answer

print(solution(	["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 800, 2500]))


    
    



   