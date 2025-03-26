//
// Created by Admin on 26.03.2025.
//

#ifndef SO2PROJ_DININGPHILOSOPHERS_H
#define SO2PROJ_DININGPHILOSOPHERS_H

#include <iostream>
#include <thread>
#include <vector>
#include <unistd.h>

class DiningPhilosophers{
public:
    DiningPhilosophers(int num_philosophers);
    void philosopher(int id);

private:
    int num_philosophers;
    std::vector<bool> forks;
    bool lock, stop;
    std::vector<int> eat_count;

    void think(int id);
    void eat(int id);
    bool try_acquire_lock(bool &expected);
    void release_lock();
    void acquire_lock();
};

#endif //SO2PROJ_DININGPHILOSOPHERS_H
