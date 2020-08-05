class FileSharing {
public:
    priority_queue<int, vector<int>, greater<int>> ids;
    unordered_map<int, unordered_set<int>> user2chunk;
    vector<set<int>> chunk2user;
    
    FileSharing(int m): chunk2user(m+1) {
        ids.emplace(1);
    }
    
    int join(vector<int> ownedChunks) {
        int id_ = ids.top();
        ids.pop();
        unordered_set<int> tmp;
        for (int chunk: ownedChunks) {
            tmp.emplace(chunk);
            chunk2user[chunk].emplace(id_);
        }
        if (ids.empty()) ids.emplace(id_+1);
        user2chunk[id_] = tmp;
        return id_;
    }
    
    void leave(int userID) {
        for (auto it = user2chunk[userID].begin(); it != user2chunk[userID].end(); ++it) {
            chunk2user[*it].erase(userID);
        }
        user2chunk.erase(userID);
        ids.emplace(userID);
    }
    
    vector<int> request(int userID, int chunkID) {
        set<int> tmp = chunk2user[chunkID];
        if (!tmp.empty()) {
            user2chunk[userID].emplace(chunkID);
            chunk2user[chunkID].emplace(userID);
        }
        vector<int> res(tmp.begin(), tmp.end());
        return res;
    }
};

/**
 * Your FileSharing object will be instantiated and called as such:
 * FileSharing* obj = new FileSharing(m);
 * int param_1 = obj->join(ownedChunks);
 * obj->leave(userID);
 * vector<int> param_3 = obj->request(userID,chunkID);
 */