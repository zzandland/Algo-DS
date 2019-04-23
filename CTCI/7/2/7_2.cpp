#include <unistd.h>
#include <chrono>
#include <iostream>
#include <list>
#include <queue>
#include <random>
#include <thread>

typedef struct {
  unsigned short year_;
  unsigned char month_;
  unsigned char date_;
} Date;

class Complaint {
 public:
  Complaint(int complexity, int duration)
      : complexity_(complexity), duration_(duration) {
    passed_ = 1;
  }
  unsigned short complexity_;
  unsigned short duration_;
  unsigned short passed_;
};

class Employee {
 public:
  Employee(std::string name, Date dob, Date hire_date, int salary)
      : name_(name),
        dob_(dob),
        hire_date_(hire_date),
        salary_((unsigned int)salary) {
    is_available_ = true;
  };

  bool IsBusy() {
    if (is_available_) {
      return true;
    }
    return false;
  };

  virtual bool CanHandle(Complaint* call) = 0;

  Complaint* ReceiveCall(Complaint* call) {
    std::cout << name_ << " received the call" << std::endl;
    is_available_ = false;
    std::this_thread::sleep_for(std::chrono::seconds(3));
    if (CanHandle(call)) {
      std::this_thread::sleep_for(std::chrono::seconds(call->duration_));
      std::cout << name_ << " handled the call." << std::endl;
      return nullptr;
    } else {
      std::cout << name_ << " cannot handle the call." << std::endl;
      call->passed_ = level_id_ + 1;
      return call;
    }
    is_available_ = true;
  };

 public:
  std::string name_;
  Date dob_;
  Date hire_date_;
  unsigned int salary_;
  bool is_available_;
  unsigned short level_id_;
};

class Respondent : public Employee {
 public:
  Respondent(std::string name, Date dob, Date hire_date, int salary)
      : Employee(name, dob, hire_date, salary) {
    level_id_ = 1;
  };
  virtual ~Respondent(){};

  bool CanHandle(Complaint* call) { return call->complexity_ < 3; };
};

class Manager : public Employee {
 public:
  Manager(std::string name, Date dob, Date hire_date, int salary)
      : Employee(name, dob, hire_date, salary) {
    level_id_ = 2;
  }
  virtual ~Manager(){};

  bool CanHandle(Complaint* call) { return call->complexity_ < 6; }
};

class Director : public Employee {
 public:
  Director(std::string name, Date dob, Date hire_date, int salary)
      : Employee(name, dob, hire_date, salary) {
    level_id_ = 3;
  };
  virtual ~Director(){};

  bool CanHandle(Complaint* call) { return true; };
};

class CallCenter {
 public:
  CallCenter() {
    Date dob = {1993, 8, 24};
    Date hire_date = {2019, 8, 24};
    for (int i = 0; i < 30; ++i) {
      Respondent* r = new Respondent("Respondent " + std::to_string(i), dob,
                                     hire_date, 35000);
      respondents_.push(r);
    }

    for (int i = 0; i < 5; ++i) {
      Manager* r =
          new Manager("Manager " + std::to_string(i), dob, hire_date, 35000);
      managers_.push(r);
    }

    Director* r = new Director("David", dob, hire_date, 35000);
    directors_.push(r);
  };

  ~CallCenter() {
    while (!respondents_.empty()) {
      Respondent* r = respondents_.front();
      respondents_.pop();
      delete r;
    }

    while (!managers_.empty()) {
      Manager* m = managers_.front();
      managers_.pop();
      delete m;
    }

    while (!directors_.empty()) {
      Director* d = directors_.front();
      directors_.pop();
      delete d;
    }
  }

  void Init() {
    while (!call_queue_.empty()) {
      std::thread t1(&CallCenter::DispatchCall, this);
      std::thread t2(&CallCenter::DispatchCall, this);
      std::thread t3(&CallCenter::DispatchCall, this);
      std::thread t4(&CallCenter::DispatchCall, this);
      std::thread t5(&CallCenter::DispatchCall, this);
      std::thread t6(&CallCenter::DispatchCall, this);
      std::thread t7(&CallCenter::DispatchCall, this);
      std::thread t8(&CallCenter::DispatchCall, this);
      std::thread t9(&CallCenter::DispatchCall, this);
      std::thread t10(&CallCenter::DispatchCall, this);
      t1.join();
      t2.join();
      t3.join();
      t4.join();
      t5.join();
      t6.join();
      t7.join();
      t8.join();
      t9.join();
      t10.join();
    }
  }

  void QueueCall(Complaint* call) {
    std::cout << "A new call." << std::endl;
    call_queue_.push_back(call);
  }

  void DispatchCall() {
    if (call_queue_.empty()) return;
    Complaint* call = call_queue_.front();
    call_queue_.pop_front();
    if (call->passed_ < 2 && !respondents_.empty()) {
      Respondent* r = respondents_.front();
      respondents_.pop();
      if (r->ReceiveCall(call) != nullptr) {
        call_queue_.push_front(call);
      }
      respondents_.push(r);
    } else if (respondents_.empty() ||
               (call->passed_ < 3 && !managers_.empty())) {
      Manager* m = managers_.front();
      managers_.pop();
      if (m->ReceiveCall(call) != nullptr) {
        call_queue_.push_front(call);
      }
      managers_.push(m);
    } else if (!directors_.empty()) {
      Director* d = directors_.front();
      directors_.pop();
      if (d->ReceiveCall(call) != nullptr) {
        call_queue_.push_front(call);
      }
      directors_.push(d);
    } else {
      call_queue_.push_front(call);
    }
  }

 private:
  std::queue<Respondent*> respondents_;
  std::queue<Manager*> managers_;
  std::queue<Director*> directors_;
  std::list<Complaint*> call_queue_;
};

int main(void) {
  CallCenter* c = new CallCenter();
  for (int i = 0; i < 40; ++i) {
    int diff = rand() % 6 + 1;
    int dur = rand() % 15 + 10;
    Complaint* call = new Complaint(diff, dur);
    c->QueueCall(call);
  }
  c->Init();
  delete c;
  return 0;
}
