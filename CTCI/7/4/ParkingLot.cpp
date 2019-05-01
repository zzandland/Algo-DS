#include <algorithm>
#include <iostream>
#include <set>
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

enum class VehicleSize { MOTORCYCLE, COMPACT, LARGE };

std::ostream& operator<<(std::ostream& ostr, VehicleSize size) {
  std::string name_arr[] = {"Motorcycle", "Compact", "Large"};
  ostr << name_arr[(int)size];
  return ostr;
}

class Vehicle {
 public:
  std::string GetVehicleID() { return vehicle_id_; };

  void SetLicenseID(std::string license_id) { license_id_ = license_id; };

  VehicleSize GetVehicleSize() { return size_; };

  friend std::ostream& operator<<(std::ostream& ostr, const Vehicle& v);

 protected:
  Vehicle(int n_wheel, Date d, std::string vehicle_id, std::string brand,
          std::string name, VehicleSize size)
      : n_wheel_(n_wheel),
        prod_date_(d),
        vehicle_id_(vehicle_id),
        license_id_("No owner"),
        brand_(brand),
        name_(name),
        size_(size){};

  virtual std::ostream& print(std::ostream& ostr) const {
    ostr << brand_ << " " << name_ << std::endl
         << "Vehicle registration ID: " << vehicle_id_ << std::endl
         << "License ID: " << license_id_ << std::endl
         << "Number of wheels: " << n_wheel_ << std::endl
         << "Production date: " << prod_date_ << std::endl
         << "Vehicle size: " << size_;
    return ostr;
  };

  unsigned short n_wheel_;
  Date prod_date_;
  std::string vehicle_id_;
  std::string license_id_;
  std::string brand_;
  std::string name_;
  VehicleSize size_;
};

std::ostream& operator<<(std::ostream& ostr, const Vehicle& v) {
  return v.print(ostr);
};

class Car : public Vehicle {
 protected:
  Car(Date d, std::string vehicle_id, std::string brand, std::string name,
      VehicleSize size, int n_seat)
      : Vehicle(4, d, vehicle_id, brand, name, size), n_seat_(n_seat){};

  unsigned short n_seat_;
};

class MotorCycle : public Vehicle {
 public:
  MotorCycle(Date d, std::string vehicle_id, std::string brand,
             std::string name)
      : Vehicle(2, d, vehicle_id, brand, name, VehicleSize::MOTORCYCLE){};
};

class Sedan : public Car {
 public:
  Sedan(Date d, std::string vehicle_id, std::string brand, std::string name)
      : Car(d, vehicle_id, brand, name, VehicleSize::COMPACT, 4){};
};

class Coup : public Car {
 public:
  Coup(Date d, std::string vehicle_id, std::string brand, std::string name)
      : Car(d, vehicle_id, brand, name, VehicleSize::COMPACT, 2){};
};

class Truck : public Car {
 public:
  Truck(Date d, std::string vehicle_id, std::string brand, std::string name,
        unsigned short n_seat, int weight)
      : Car(d, vehicle_id, brand, name, VehicleSize::LARGE, n_seat),
        cargo_(weight){};

 private:
  virtual std::ostream& print(std::ostream& ostr) const {
    Vehicle::print(ostr);
    ostr << "\nMaximum load: " << cargo_ << " lb.";
    return ostr;
  };

  unsigned int cargo_;
};

class Bus : public Car {
 public:
  Bus(Date d, std::string vehicle_id, std::string brand, std::string name,
      unsigned short n_seat)
      : Car(d, vehicle_id, brand, name, VehicleSize::LARGE, n_seat){};
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

struct Ticket {
  int slot;
  int floor;
  VehicleSize size;
};

class ParkingLot {
 public:
  ParkingLot(unsigned int n_floors, unsigned int mc_cap,
             unsigned int compact_cap, unsigned int large_cap)
      : floors_(n_floors) {
    storage_ = std::vector<Floor*>(n_floors);
    for (size_t i = 0; i < storage_.size(); ++i)
      storage_[i] = new Floor(mc_cap, compact_cap, large_cap);
  };

  Ticket* AddVehicle(Vehicle* v) {
    for (int i = 0; i < floors_; ++i) {
      Ticket* t = storage_[i]->AddVehicle(v);
      if (t != nullptr) {
        t->floor = i;
        return t;
      }
    }
    return nullptr;
  };

  Vehicle* RemoveVehicle(Ticket* ticket) {
    return storage_[ticket->floor]->RemoveVehicle(ticket);
  };

  void PrintVehicles() {
    for (unsigned int i = 0; i < floors_; ++i) {
      std::cout << "Floor " << i + 1 << ":" << std::endl;
      storage_[i]->PrintVehicles();
    }
  }

 private:
  class Floor {
   public:
    Floor(int mc_cap, int compact_cap, int large_cap) {
      mc_storage_.reserve(mc_cap);
      compact_storage_.reserve(compact_cap);
      large_storage_.reserve(large_cap);
      for (int i = 0; i < mc_cap; ++i) mc_free_.insert(i);
      for (int i = 0; i < compact_cap; ++i) compact_free_.insert(i);
      for (int i = 0; i < large_cap; ++i) large_free_.insert(i);
    }

    Ticket* AddVehicle(Vehicle* v) {
      VehicleSize size = v->GetVehicleSize();
      Ticket* output = new Ticket();
      if (size == VehicleSize::MOTORCYCLE && !mc_free_.empty()) {
        output->size = VehicleSize::MOTORCYCLE;
        int slot = *mc_free_.begin();
        mc_free_.erase(slot);
        output->slot = slot;
        mc_storage_[slot] = (MotorCycle*)v;
        return output;
      } else if (size != VehicleSize::LARGE && !compact_free_.empty()) {
        output->size = VehicleSize::COMPACT;
        int slot = *compact_free_.begin();
        compact_free_.erase(slot);
        output->slot = slot;
        compact_storage_[slot] = (Car*)v;
        return output;
      } else if (!large_free_.empty()) {
        output->size = VehicleSize::LARGE;
        int slot = *large_free_.begin();
        large_free_.erase(slot);
        output->slot = slot;
        large_storage_[slot] = (Car*)v;
        return output;
      }
      return nullptr;
    }

    Vehicle* RemoveVehicle(Ticket* ticket) {
      VehicleSize size = ticket->size;
      Vehicle* out = nullptr;
      int slot;
      switch (size) {
        case VehicleSize::MOTORCYCLE:
          slot = ticket->slot;
          out = mc_storage_[slot];
          mc_free_.insert(slot);
          mc_storage_[slot] = nullptr;
          break;
        case VehicleSize::COMPACT:
          slot = ticket->slot;
          out = compact_storage_[slot];
          compact_storage_[slot] = nullptr;
          break;
        case VehicleSize::LARGE:
          slot = ticket->slot;
          out = large_storage_[slot];
          large_storage_[slot] = nullptr;
          break;
      }
      return out;
    };

    void PrintVehicles() {
      std::cout << "\nMotorcycles:" << std::endl;
      for (size_t i = 0; i < mc_storage_.capacity(); ++i)
        if (mc_storage_[i] != nullptr)
          std::cout << *mc_storage_[i] << "\n\n";
      std::cout << "\nCompact vehicles: " << std::endl;
      for (size_t i = 0; i < compact_storage_.capacity(); ++i)
        if (compact_storage_[i] != nullptr)
          std::cout << *compact_storage_[i] << "\n\n";
      std::cout << "\nLarge vehicles: " << std::endl;
      for (size_t i = 0; i < large_storage_.capacity(); ++i)
        if (large_storage_[i] != nullptr)
          std::cout << *large_storage_[i] << "\n\n";
      std::cout << std::endl;
    }

   private:
    std::set<int> mc_free_;
    std::set<int> compact_free_;
    std::set<int> large_free_;
    std::vector<MotorCycle*> mc_storage_;
    std::vector<Car*> compact_storage_;
    std::vector<Car*> large_storage_;
  };

  std::vector<Floor*> storage_;
  const unsigned int floors_;
};

int main(void) {
  ParkingLot* p = new ParkingLot(3, 3, 10, 3);
  Sedan* ae86 = new Sedan({1987, 1, 30}, "N392S", "TOYOTA", "AE86");
  Coup* rx5 = new Coup({1995, 3, 25}, "DX92E", "MAZDA", "RX5");
  Truck* x7 = new Truck({2019, 8, 24}, "TWJ9S", "BMW", "X7", 6, 1500);
  MotorCycle* ex5 = new MotorCycle({2045, 2, 11}, "RIW23", "Porsche", "EX5");
  Ticket* t1 = p->AddVehicle(ae86);
  Ticket* t2 = p->AddVehicle(rx5);
  Ticket* t3 = p->AddVehicle(x7);
  Ticket* t4 = p->AddVehicle(ex5);

  Vehicle* out1 = p->RemoveVehicle(t1);
  Vehicle* out2 = p->RemoveVehicle(t2);
  Vehicle* out3 = p->RemoveVehicle(t3);

  std::cout << *out1 << std::endl << *out2 << std::endl << *out3;

  Person* david = new Person("David", "Kim", "QWERTY", {1993, 8, 24});
  david->AddVehicle(ae86);
  david->AddVehicle(x7);
  david->AddVehicle(rx5);

  Person* jack = new Person("Jack", "Phillips", "IDEA32", {1989, 11, 21});
  jack->AddVehicle(ex5);

  david->PassOnVehicles(*jack);
  // p->PrintVehicles();
}
