#  Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

#  Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

#  The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

#  Example 1:

#  Input:
userSongs1 = {
"David": ["song1", "song2", "song3", "song4", "song8"],
"Emma":  ["song5", "song6", "song7"]
}
songGenres1 = {
"Rock":    ["song1", "song3"],
"Dubstep": ["song7"],
"Techno":  ["song2", "song4"],
"Pop":     ["song5", "song6"],
"Jazz":    ["song8", "song9"]
}

#  Output: {
#  "David": ["Rock", "Techno"],
#  "Emma":  ["Pop"]
#  }

#  Explanation:
#  David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
#  Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
#  Example 2:

#  Input:
userSongs2 = {
"David": ["song1", "song2"],
"Emma":  ["song3", "song4"]
}
songGenres2 = {}

#  Output: {
#  "David": [],
#  "Emma":  []
#  }

#  from collections import defaultdict
#  import heapq

#  def favorite_genre(userSongs, songGenres):
    #  output = { user: [] for user in userSongs }
    #  if not userSongs or not songGenres or songGenres == set(): return output
    #  genreDic = { song: genre for genre, songList in songGenres.items() for song in songList }
    #  for user in userSongs:
        #  freqDic = defaultdict(int)
        #  for song in userSongs[user]:
            #  try:
                #  freqDic[genreDic[song]] += 1
            #  except KeyError:
                #  continue
        #  hp = sorted([(-freq, genre) for genre, freq in freqDic.items()])
        #  maxFreq, genre = heapq.heappop(hp)
        #  output[user].append(genre)
        #  while hp:
            #  freq, genre = heapq.heappop(hp)
            #  if freq > maxFreq: break;
            #  output[user].append(genre)
    #  return output

from typing import List, Dict
from collections import Counter

def favorite_genres(userSongs: Dict[str, List[str]],
                    songGenres: Dict[str, List[str]]) -> Dict[str, List[str]]:
    '''
    >>> favorite_genres(userSongs1, songGenres1)
    {'David': ['Rock', 'Techno'], 'Emma': ['Pop']}
    >>> favorite_genres(userSongs2, songGenres2)
    {'David': [], 'Emma': []}
    '''
    # dict of song as key and genre as val O(genre * songList)
    song2Genre = {}
    for genre, songList in songGenres.items():
        for song in songList:
            song2Genre[song] = genre

    # for each user store freq of each genre and track fav genre O(user * songList)
    res = {}
    for user, songList in userSongs.items():
        fav, favFreq = set(), 0
        freq = Counter()
        for song in songList:
            if song not in song2Genre: continue
            genre = song2Genre[song]
            freq[genre] += 1
            if freq[genre] > favFreq:
                fav.clear()
                favFreq = freq[genre]
            if freq[genre] == favFreq:
                fav.add(genre)
        res[user] = sorted(list(fav))

    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod()
