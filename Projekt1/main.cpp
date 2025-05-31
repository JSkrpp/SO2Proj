#include <iostream>

#include "DiningPhilosophers.h"

int main(int argc, char* argv[]) {
    int num_philosophers = std::stoi(argv[1]);

    DiningPhilosophers dp(num_philosophers);

    std::vector<std::thread> philosophers;
    for (int i = 0; i < num_philosophers; ++i) {
        philosophers.emplace_back(&DiningPhilosophers::philosopher, &dp, i);
    }

    //initializes threads which will reproduce wanted behavior
    for (auto& philosopher : philosophers) {
        philosopher.join();
    }
    system("pause");
    return 0;
}