package com.company;

import java.util.*;
/*
Assignment #08
921804582@_HW08
Lily Keus
 */
public class Main {
    public static void initializeBuildingAndStatus(LinkedList<Passenger> wait) {
        System.out.println("Building has 5 floors"); //Starts Status
        int id = 1;
        for (int i = 0; i < 5; i++) {
            int r = (int) Math.floor(Math.random() * (5 + 1) + 0); //generates # of passengers
            System.out.println("========================"); //spacer
            System.out.println("Floor " + (i+1) + " (" + r + ") " + "passengers waiting:");//tells which floor and # of passengers
            for (int j = 0; j < r; j++) { //generates # of passengers
                int r2 = (int) Math.floor(Math.random() * (5-1 + 1) + 1);
                while(r2 == (i + 1)) {
                    r2 = (int) Math.floor(Math.random() * (5-1 + 1) + 1);
                }
                Passenger p = new Passenger(id, i + 1, r2); //makes passenger
                id++;
                System.out.println(p); //Prints passenger for Status
                wait.add(p); //Adds passenger to building
            }
        }
    }
    public static void startElevator(LinkedList<Passenger> wait,LinkedList<Passenger> elev) {
        System.out.println("Elevator started"); //Elevator starts
        for (int j = 0; j < 5; j++) { // for every floor // GOING UP
            int count = 0;
            int rCount = 0;
            //Picking up passengers
            for (int i = 0; i < 5; i++) { //with in floor
                if(!wait.isEmpty()) {
                    if ((wait.peek()).getFloor() == j + 1) { //checks if the waiters are on this floor
                        elev.add(wait.remove()); //if true they are added them to elevator
                        count++;
                    }
                }
            }
            //print status of passengers
            if(j + 1 == 1){ //ONLY FOR FLOOR 1
                if (count != 0) {
                    System.out.println("At floor " + (j + 1) + ", elevator picked " + count + " passengers");
                }
                System.out.println("Going up");
            }
            if (count != 0 && j + 1 != 1) { //OTHER FLOORS
                System.out.println("Stopped at floor " + (j + 1) + ", elevator picked " + count + " passengers" + ", # of passengers now " + elev.size());
            }
            //checking destination
            LinkedList<Passenger> tmp = new LinkedList<>();
            int s = elev.size(); //saves size so it doesn't change
            for (int i = 0; i < s; i++) { //with in floor
                if(!elev.isEmpty()) {
                    if ((elev.peek()).getDestinationFloor() == j + 1) { //checks if current floor is destination
                        elev.remove();
                        rCount++;
                    }
                    else{
                        tmp.add(elev.remove()); //if not add it to temp
                    }
                }
            }
            while(!tmp.isEmpty()){ //put everything back into the list
                elev.add(tmp.remove());
            }
            if (j + 1 != 1 && j + 1 != 5) { //FOR FLOORS 2 - 4
                if(count == 0){
                    System.out.println("Floor: " + (j + 1));
                }
                System.out.println("Elevator served " + rCount + " passengers, # of passengers now " + elev.size());
                System.out.println("Going up");
            }
            if (j + 1 == 5) { //FOR FLOOR 5 ONLY
                if(count == 0){
                    System.out.println("Floor: " + (j + 1));
                }
                System.out.println("Elevator served " + rCount + " passengers, # of passengers now " + elev.size());
                System.out.println("Going down");
            }
            System.out.println("========================");
        }
        //CHECKING PASSENGER PLACEMENT GOING DOWN
        for (int j = 4; j >= 0; j--) { // Going down
            int rCount = 0;
            LinkedList<Passenger> tmp = new LinkedList<>();
            int s = elev.size();//saves size so it doesn't change
            for (int i = 0; i < s; i++) { //with in floor
                if(!elev.isEmpty()) {
                    if ((elev.peek()).getDestinationFloor() == j + 1) { //checks if current floor is destination
                        elev.remove();
                        rCount++;
                    }
                    else{
                        tmp.add(elev.remove());//if not add it to temp
                    }
                }
            }
            while(!tmp.isEmpty()){ //put everything back into the list
                elev.add(tmp.remove());
            }
            if (j + 1 != 5 && j+1 != 1 && rCount != 0) { //FOR FLOORS 2 - 4 ONLY
                System.out.println("Stopped at floor "+(j+1)+". Elevator served " + rCount + " passengers, # of passengers now " + elev.size());
                if(elev.size() != 0) {
                    System.out.println("Going Down");
                    System.out.println("========================");
                }
            }
            if(j+1 == 1 && rCount != 0){ //FOR FLOOR 1 ONLY
                System.out.println("Stopped at floor "+(j+1)+". Elevator served " + rCount + " passengers, # of passengers now " + elev.size());
            }
        }
    }
    public static void main(String[] args) {
        LinkedList<Passenger> wait = new LinkedList<>();// For people who are waiting for the elevator
        LinkedList<Passenger> elev = new LinkedList<>();// For people who are in the elevator

        initializeBuildingAndStatus(wait); // I decided to combine the "Initialize Building" and "Print Building Status"
                                           // because it was easier and saved a lot of space.
        System.out.println();

        startElevator(wait, elev);
    }
}
