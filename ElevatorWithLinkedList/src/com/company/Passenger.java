package com.company;

public class Passenger {
    protected int passengerID;
    protected int floor;
    protected int destinationFloor;

    public Passenger(int passengerID, int floor, int destinationFloor) {
        this.passengerID = passengerID;
        this.floor = floor;
        this.destinationFloor = destinationFloor;
    }

    public Passenger() {
    }

    public int getPassengerID() {
        return passengerID;
    }

    public void setPassengerID(int passengerID) {
        this.passengerID = passengerID;
    }

    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }

    public int getDestinationFloor() {
        return destinationFloor;
    }

    public void setDestinationFloor(int destinationFloor) {
        this.destinationFloor = destinationFloor;
    }

    @Override
    public String toString() {
        return "Passenger{" +
                "passengerID=" + passengerID +
                ", floor=" + floor +
                ", destinationFloor=" + destinationFloor +
                '}';
    }
}
