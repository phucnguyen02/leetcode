from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList: return []

        L = len(beginWord)
        all_word_combo = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(L):
                inter = word[:i] + "*" + word[i+1:]

                all_word_combo[inter].append(word)
        seen = set()
        seen.add(endWord)
        dq = deque([(endWord, 1)])
        min_paths = defaultdict(int)

        while dq:
            word, distance = dq.popleft()
            for i in range(L):
                inter = word[:i] + "*" + word[i+1:]
                
                for neighbor in all_word_combo[inter]:
                    if neighbor in seen:
                        continue

                    seen.add(neighbor)
                    min_paths[neighbor] = distance + 1
                    dq.append((neighbor, distance + 1))
        
        if beginWord not in min_paths: return []
        visited = set()
        visited.add(beginWord)
        paths = defaultdict(list)
        
        def backtracking(word, path):
            
            if word == endWord:
                paths[len(path)].append(path[:])
                return
            
            for i in range(L):
                inter = word[:i] + "*" + word[i+1:]

                for neighbor in all_word_combo[inter]:
                    if neighbor in visited:
                        continue

                    if len(path) + min_paths[neighbor] > min_paths[beginWord]:
                        continue
                    path.append(neighbor)
                    visited.add(neighbor)
                    backtracking(neighbor, path)
                    path.pop()
                    visited.remove(neighbor)
        
        backtracking(beginWord, [beginWord])
        return paths[min_paths[beginWord]]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(sol.findLadders("cet", "ism", ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim"]))

# For each word, store words it can transform to in a hash table, like a template. For example, abc, abd are stored in ab* together, but not a*c
# Use BFS with the endWord as the starting node, add all words it can transform into in a queue, then find the minimum steps it takes for the neighbor to become endWord

# Do backtracking from beginWord. Avoid using a neighbor where its min steps + the current path length > the min steps of the beginWord