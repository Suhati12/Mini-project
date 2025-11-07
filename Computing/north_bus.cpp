#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Bus {
    int id;
    string name;
    string route;
    int fare;
    int seats;
};

struct Booking {
    int bookingId;
    string passenger;
    int busId;
    int fare;
};

class BusSystem {
private:
    vector<Bus> buses;
    vector<Booking> bookings;
    int nextBookingId = 1001;

public:
    BusSystem() {
        // Initialize North India buses
        buses = {
            {101, "Delhi Express", "Delhi to Chandigarh", 350, 40},
            {102, "Hill Queen", "Delhi to Shimla", 800, 35},
            {103, "Pink City", "Delhi to Jaipur", 450, 45},
            {104, "Mountain King", "Chandigarh to Manali", 600, 30},
            {105, "Royal Rajasthan", "Jaipur to Delhi", 500, 42}
        };
    }

    void showBuses() {
        cout << "\n🚌 NORTH INDIA BUSES\n";
        cout << "ID   Name            Route                Fare    Seats\n";
        cout << "---------------------------------------------------\n";
        for (auto& bus : buses) {
            cout << bus.id << "  " << bus.name << "  " << bus.route 
                 << "  Rs." << bus.fare << "  " << bus.seats << endl;
        }
    }

    void bookTicket() {
        int busId;
        string name;
        
        cout << "\nEnter Bus ID: ";
        cin >> busId;
        cout << "Enter your name: ";
        cin.ignore();
        getline(cin, name);
        
        for (auto& bus : buses) {
            if (bus.id == busId && bus.seats > 0) {
                bus.seats--;
                bookings.push_back({nextBookingId, name, busId, bus.fare});
                
                cout << "\n✅ BOOKING CONFIRMED!\n";
                cout << "Booking ID: " << nextBookingId << endl;
                cout << "Passenger: " << name << endl;
                cout << "Bus: " << bus.name << endl;
                cout << "Amount: Rs." << bus.fare << endl;
                
                nextBookingId++;
                return;
            }
        }
        cout << "❌ Bus not found or no seats available!\n";
    }

    void viewBooking() {
        int bookingId;
        cout << "\nEnter Booking ID: ";
        cin >> bookingId;
        
        for (auto& booking : bookings) {
            if (booking.bookingId == bookingId) {
                cout << "\n📋 BOOKING DETAILS\n";
                cout << "Booking ID: " << booking.bookingId << endl;
                cout << "Passenger: " << booking.passenger << endl;
                cout << "Bus ID: " << booking.busId << endl;
                cout << "Amount: Rs." << booking.fare << endl;
                return;
            }
        }
        cout << "❌ Booking not found!\n";
    }

    void run() {
        int choice;
        cout << "\n🚌 NORTH INDIA BUS RESERVATION\n";
        
        while (true) {
            cout << "\n1. View Buses\n2. Book Ticket\n3. View Booking\n4. Exit\n";
            cout << "Enter choice: ";
            cin >> choice;
            
            switch (choice) {
                case 1: showBuses(); break;
                case 2: bookTicket(); break;
                case 3: viewBooking(); break;
                case 4: cout << "Thank you!\n"; return;
                default: cout << "Invalid choice!\n";
            }
        }
    }
};

int main() {
    BusSystem system;
    system.run();
    return 0;
}