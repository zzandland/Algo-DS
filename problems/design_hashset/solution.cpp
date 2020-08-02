#define SIZE 1000003

class MyHashSet {
public:
    const int size;
    vector<int> arr;
    const hash<string> hashifier;

    /** Initialize your data structure here. */
    MyHashSet(int k = SIZE): size(k), arr(k, -1) {};
    
    void add(int key) {
        int idx = hashifier(to_string(key)) % size;
        int run = 1;
        while (arr[idx] != -1) {
            idx = (idx+run) % size;
            run <<= 1;
        }
        arr[idx] = key;
    }
    
    void remove(int key) {
        int idx = hashifier(to_string(key)) % size;
        int run = 1;
        while (arr[idx] != -1 && arr[idx] != key) {
            idx = (idx+run) % size;
            run <<= 1;
        }
        if (arr[idx] == key) arr[idx] = -1;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int idx = hashifier(to_string(key)) % size;
        int run = 1;
        while (arr[idx] != -1 && arr[idx] != key) {
            idx = (idx+run) % size;
            run <<= 1;
        }
        return arr[idx] == key;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */