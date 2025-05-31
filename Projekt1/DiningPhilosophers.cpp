//
// Created by Admin on 26.03.2025.
//

#include "DiningPhilosophers.h"

#include "DiningPhilosophers.h"
#include <random>
#include <chrono>
#include <iostream>
#include <thread>
#include <vector>
#include <unistd.h>


DiningPhilosophers::DiningPhilosophers(int num_philosophers) : num_philosophers(num_philosophers) {
    forks.resize(num_philosophers, true);
    eat_count.resize(num_philosophers, 0);
    lock = false; // lock variable makes sure two threads won`t access forks at the same time
    stop = false;
}

void DiningPhilosophers::philosopher(int id) {  // when calles, reproduces philosopher behavior for a certain amount of time

    auto start_time = std::chrono::high_resolution_clock::now(); // start timestamp
    while (true) {
        auto curr_time = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed = curr_time - start_time;
        if (elapsed > std::chrono::seconds(10)){ //runtime of 10 secs for presentation purposes
            break;
        }
        think(id);
        eat(id);
    }
    stop = true;
    sleep(1); // makes the final output clearer, not a neccesary line
    std::cout << "Philosopher " << id << " ate " << eat_count[id] << " times." << std::endl;
}

void DiningPhilosophers::think(int id) { //state in which the thread sleeps without holding the forks
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<int> dist(500, 1000); // generate random think time from 500ms to 1000ms
    int timer = dist(mt);
    std::cout << "Philosopher " << id << " is thinking for " << timer << " ms." << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(timer));
}

void DiningPhilosophers::eat(int id) { // state in which the thread sleeps while using the forks
    int left = id;
    int right = (id + 1) % num_philosophers;

    std::cout << "Philosopher " << id << " is hungry." << std::endl;

    while (!stop) {
        acquire_lock();

        if (forks[left] && forks[right]) {
            forks[left] = false;
            forks[right] = false;
            release_lock();

            // Eating
            eat_count[id]++;
            std::random_device rd;
            std::mt19937 mt(rd());
            std::uniform_int_distribution<int> dist(300, 600); // generate random eat time from 300ms to 600ms
            int timer = dist(mt);
            std::cout << "Philosopher " << id << " is eating for " << timer << " ms." << std::endl;
            std::this_thread::sleep_for(std::chrono::milliseconds(timer));

            // Return forks and exit while-loop
            acquire_lock();
            forks[left] = true;
            forks[right] = true;
            release_lock();
            break;

        } else {
            release_lock();
            // without this pause, during testing situations happened in which some philosophers never ateS
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
        }
    }
}

// Custom spinlock acquire mechanism
bool DiningPhilosophers::try_acquire_lock(bool& expected) {
    //wait until the lock is free
    while (lock) {

    }
    expected = false;
    lock = true; //Acquire the lock
    return true;
}

void DiningPhilosophers::acquire_lock() {
    while (true) {
        // Busy wait until lock is available
        bool expected = false;
        if (try_acquire_lock(expected)) {
            break;
        }

    }
}

// Custom spinlock release mechanism
void DiningPhilosophers::release_lock() {
    lock = false;
}