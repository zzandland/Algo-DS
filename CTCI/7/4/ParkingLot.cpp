#include <algorithm>
#include <iostream>
#include <vector>

struct Date {
 public:
  Date(int y, int m, int d) : year_(y), month_(m), date_(d){};

  friend std::ostream& operator<<(std::ostream& ostr, const Date& d) {
    ostr << d.year_ << "/" << d.month_ << "/" << d.date_;
    return ostr;
  };

  unsigned short year_;
  unsigned short month_;
  unsigned short date_;
};

class Vehicle {
 public:
  std::string GetVehicleID() { return vehicle_id_; };

  void SetLicenseID(std::string license_id) { license_id_ = license_id; };

  friend std::ostream& operator<<(std::ostream& ostr, const Vehicle& v);

 protected:
  Vehicle(int n_wheel, Date d, std::string vehicle_id, std::string brand,
          std::string name)
      : n_wheel_(n_wheel),
        prod_date_(d),
        vehicle_id_(vehicle_id),
        license_id_("No owner"),
        brand_(brand),
        name_(name){};

  virtual std::ostream& print(std::ostream& ostr) const {
    ostr << brand_ << " " << name_ << std::endl
         << "Vehicle registration ID: " << vehicle_id_ << std::endl
         << "License ID: " << license_id_ << std::endl
         << "Number of wheels: " << n_wheel_ << std::endl
         << "Production date: " << prod_date_;
    return ostr;
  };

  unsigned short n_wheel_;
  Date prod_date_;
  std::string vehicle_id_;
  std::string license_id_;
  std::string brand_;
  std::string name_;
};

std::ostream& operator<<(std::ostream& ostr, const Vehicle& v) {
  return v.print(ostr);
};

class Car : public Vehicle {
 protected:
  Car(Date d, std::string vehicle_id, std::string brand, std::string name,
      int n_seat)
      : Vehicle(4, d, vehicle_id, brand, name), n_seat_(n_seat){};

  unsigned short n_seat_;
};

class MotorCycle : public Vehicle {
 public:
  MotorCycle(Date d, std::string vehicle_id, std::string brand,
             std::string name)
      : Vehicle(2, d, vehicle_id, brand, name){};
};

class Sedan : public Car {
 public:
  Sedan(Date d, std::string vehicle_id, std::string brand, std::string name)
      : Car(d, vehicle_id, brand, name, 4){};
};

class Coup : public Car {
 public:
  Coup(Date d, std::string vehicle_id, std::string brand, std::string name)
      : Car(d, vehicle_id, brand, name, 2){};
};

class Truck : public Car {
 public:
  Truck(Date d, std::string vehicle_id, std::string brand, std::string name,
        unsigned short n_seat, int weight)
      : Car(d, vehicle_id, brand, name, n_seat), cargo_(weight){};

 private:
  virtual std::ostream& print(std::ostream& ostr) const {
    Vehicle::print(ostr);
    ostr << "\nMaximum load: " << cargo_ << " lb.";
    return ostr;
  };

  unsigned int cargo_;
};

class Person {
 public:
  Person(std::string first_name, std::string last_name, std::string license_id,
         Date dob)
      : first_name_(first_name),
        last_name_(last_name),
        license_id_(license_id),
        dob_(dob){};

  void AddVehicle(Vehicle* v) {
    v->SetLicenseID(license_id_);
    vehicles_.push_back(v);
  };

  Vehicle* RemoveVehicle(std::string vehicle_id) {
    for (Vehicle* v : vehicles_) {
      if (v->GetVehicleID() == vehicle_id) {
        std::swap(v, vehicles_.back());
        Vehicle* out = vehicles_.back();
        vehicles_.pop_back();
        return out;
      }
    }
    return nullptr;
  };

  void PassOnVehicles(Person& p) {
    for (Vehicle* v : vehicles_) p.AddVehicle(v);
    vehicles_.clear();
  };

  void PrintVehicles() {
    std::cout << first_name_ << " " << last_name_
              << "'s vehicles: " << std::endl;
    for (Vehicle* v : vehicles_) std::cout << *v << std::endl << std::endl;
  }

 private:
  std::string first_name_;
  std::string last_name_;
  std::string license_id_;
  Date dob_;
  std::vector<Vehicle*> vehicles_;
};

class ParkingLot {
 public:
  ParkingLot(int capacity) : slot_(0), capacity_(capacity) {
    storage_.resize(capacity);
  };

  int AddVehicle(Vehicle* v) {
    if (slot_ >= capacity_) return -1;
    storage_[slot_++] = v;
    return slot_;
  };

  Vehicle* RemoveVehicle(int slot) {
    if ((unsigned int)slot < slot_) {
      std::swap(storage_[slot], storage_[slot_ - 1]);
      Vehicle* out = storage_[slot_ - 1];
      --slot_;
      return out;
    } else {
      return nullptr;
    }
  };

  Vehicle* RemoveVehicle(std::string vehicle_id) {
    for (unsigned int i = 0; i < slot_; ++i) {
      if (storage_[i]->GetVehicleID() == vehicle_id) {
        std::swap(storage_[i], storage_[slot_ - 1]);
        Vehicle* out = storage_[slot_ - 1];
        --slot_;
        return out;
      }
    }
    return nullptr;
  };

  void PrintVehicles() {
    for (unsigned int i = 0; i < slot_; ++i)
      std::cout << *storage_[i] << "\n\n";
  }

 private:
  std::vector<Vehicle*> storage_;
  unsigned int slot_;
  unsigned int capacity_;
};

int main(void) {
  ParkingLot* p = new ParkingLot(5);
  Sedan* ae86 = new Sedan({1987, 1, 30}, "N392S", "TOYOTA", "AE86");
  Coup* rx5 = new Coup({1995, 3, 25}, "DX92E", "MAZDA", "RX5");
  Truck* x7 = new Truck({2019, 8, 24}, "TWJ9S", "BMW", "X7", 6, 1500);
  MotorCycle* ex5 = new MotorCycle({2045, 2, 11}, "RIW23", "Porsche", "EX5");
  p->AddVehicle(ae86);
  p->AddVehicle(rx5);
  p->AddVehicle(x7);
  p->AddVehicle(ex5);

  Person* david = new Person("David", "Kim", "QWERTY", {1993, 8, 24});
  david->AddVehicle(ae86);
  david->AddVehicle(x7);
  david->AddVehicle(rx5);

  Person* jack = new Person("Jack", "Phillips", "IDEA32", {1989, 11, 21});
  jack->AddVehicle(ex5);

  david->PassOnVehicles(*jack);

  std::cout << "Removed:\n" << *p->RemoveVehicle(0) << std::endl;
  std::cout << "Removed:\n" << *p->RemoveVehicle("TWJ9S") << std::endl;
  p->PrintVehicles();
}
