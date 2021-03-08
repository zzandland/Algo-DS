#define SIZE 10001

class MyHashMap {
public:
    vector<pair<int, int>> arr;
    /** Initialize your data structure here. */
    MyHashMap() : arr(SIZE, {-1, -1}) {}
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        int idx;
        for (int i = 0; pow(2, i) <= SIZE; ++i) {
            idx = (key + (int)pow(2, i)) % SIZE;
            if (arr[idx].first == key || arr[idx].first <= -1) break;
        }
        arr[idx] = {key, value};
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int idx;
        for (int i = 0; pow(2, i) <= SIZE; ++i) {
            idx = (key + (int)pow(2, i)) % SIZE;
            if (arr[idx].first == key || arr[idx].first == -1) break;
        }
        return arr[idx].second;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int idx;
        for (int i = 0; pow(2, i) <= SIZE; ++i) {
            idx = (key + (int)pow(2, i)) % SIZE;
            if (arr[idx].first == key || arr[idx].first == -1) break;
        }
        arr[idx] = {-2, -1};
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */