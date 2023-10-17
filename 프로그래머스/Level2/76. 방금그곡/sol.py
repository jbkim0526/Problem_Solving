# 12 15 19

def minute(x):
    h,m = map(int,x.split(":"))
    return 60*h+m

def solution(m, musicinfos):
    answer = []

    for musicinfo in musicinfos:
        st,et,name,melody = musicinfo.split(",")
        dt = minute(et)-minute(st)
        n = len(melody) ; count = 0 ; i = 0
        music_melody = ""
        while count < dt:
            music_melody += melody[i]
            count += 1
            if melody[(i+1)%n] == "#":
                music_melody += "#"
                i = (i+2) % n
            else:
                i = (i+1) % n

        melody = music_melody
        melody_len = len(melody)
        if m in melody:
            m_len = len(m)
            res = [i for i in range(melody_len) if melody.startswith(m, i)]
            for i in res:
                if i+m_len < melody_len:
                    if melody[i+m_len] != "#": 
                        answer.append((name,dt))
                        break
                else:
                    answer.append((name,dt))
                    break

    if len(answer) == 0:
        return "(None)"
    answer.sort(key = lambda x: -x[1])
    return answer[0][0]


#print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "02:00,02:20,FOO3,CC#B","02:00,02:30,FOO2,CC#B"]))
#print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("A",["12:00,12:01,HELLO3,A#B","12:01,12:08,HELLO2,CDEFGA#"]))