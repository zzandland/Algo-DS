class UndergroundSystem {
public:
    UndergroundSystem() {};
    
    void checkIn(int id, string stationName, int t) {
        id2checkIn[id] = {stationName, t};
    }
    
    void checkOut(int id, string stationName, int t) {
        auto [fromStation, fromT] = id2checkIn[id];
        pair<string, string> travel = {fromStation, stationName};
        if (!times.count(travel)) times[travel] = {0, 0};
        auto [totalT, cnt] = times[travel];
        times[travel] = {totalT + t - fromT, cnt + 1};
        id2checkIn.erase(id);
    }
    
    double getAverageTime(string startStation, string endStation) {
        auto [totalT, cnt] = times[{startStation, endStation}];
        return (double)totalT / cnt;
    }
private:
    unordered_map<int, pair<string, int>> id2checkIn;   
    map<pair<string, string>, pair<int, int>> times;
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */