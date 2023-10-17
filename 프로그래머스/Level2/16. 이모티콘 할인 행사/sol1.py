
possible_prices = []
possible_comb = []

def generate_emo(emoticons,l,l2, depths, maxd):

    if depths >= maxd:
        possible_prices.append(l)
        possible_comb.append(l2)
        return l
    p = emoticons[depths]
    newp = [(9*p // 10),(8*p//10),(7*p//10),(6*p//10)]
    for i in range(4):
        generate_emo(emoticons,l+[newp[i]],l2+[i+1],depths+1,maxd)


def solution(users, emoticons):
    answer = []

    
    m = len(emoticons)
    generate_emo(emoticons,[],[],0,m)
    max_list = []
    max_register = 0


    for i, prices in enumerate(possible_prices):
        register = 0
        total_income = 0

        for limit_rate, limit_price in users:
            person_price = 0

            for j, index in enumerate(possible_comb[i]):
                if 10*index >= limit_rate:
                    person_price += prices[j]

            if person_price >= limit_price:
                register += 1
            else:
                total_income += person_price

        if register > max_register:
            max_register = register
            max_list = [total_income]
        elif register == max_register:
            max_list.append(total_income)
        


    answer.append(max_register)
    answer.append(max(max_list))
    return answer





print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],	[1300, 1500, 1600, 4900]))