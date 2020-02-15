dataset = {
    "action" : ["matrix","batman","superman","dabang","avengers","thor","hulk",
                "krrish","ironman","uri"],
    "comedy" : ["the mask","dhamaal","bala","housefull","golmaal","hera pheri",
                "golmaal 2","dhamaal 2","hera pheri 2","bhootnath"],
    "drama" : ["dabang","krrish","hera pheri","bala","kahani","batla house",
               "kgf","zero","sultan"],
    "thriller" : ["kahani","kgf","batla house","madras cafe","uri","raw",
                  "lucy","the ring","oculus"],
    "horror" : ["oculus","the ring","it","the ring 2","evil dead","conjuring",
                "conjuring 2","bhootnath","aatma"]
}

user_1 = {"krrish","ironman","sultan","it","bhootnath","uri","raw","thor","hulk"}

scores = {}
for key in dataset:
    scores[key] = 0.0

for key in dataset:
    intersection = set(dataset[key]).intersection(user_1)
    union = set(dataset[key]).union(user_1)
    similarityScore = len(intersection) / len(union)
    scores[key] = round(similarityScore * 100,2)

print(scores)

max_score = max(scores.values())
cat = ""
for key in scores:
    if scores[key] == max_score:
        cat = key
        break

rec_movies = set(dataset[cat]) - user_1
print("Recommended Movies",rec_movies)




