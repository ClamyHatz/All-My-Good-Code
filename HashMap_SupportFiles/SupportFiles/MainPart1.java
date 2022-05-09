
package edu.sfsu.cs.datastructures;

import java.util.*;

public class MainPart1 {
    /*
    * Question 1:
    * - In this question you will use the Data.users array that includes
    * a list of users. Formatted as : firstname,lastname,age,email,gender,city,state
    * - Create a User class that should parse all the parameters for each user.
    * - Insert each of the users in a list.
    * - Print out the TOP 10 oldest users.
    * */

    public static void main(String[] args) {
        HashMap<Integer, String[]> mapMap = new HashMap<>();
        mapMap.put(0, Data.users);
        mapMap.put(1, Data.otherUsers);
        ArrayList<User> uList = new ArrayList<>();
        ArrayList<User> uOtherList = new ArrayList<>();
        HashMap<Integer, ArrayList<User>> arMap = new HashMap<>();
        arMap.put(0, uList);
        arMap.put(1, uOtherList);
        HashMap<Integer, String> var = new HashMap<>();
        for(int j = 0; j < 2; j++) {
            for (String str : mapMap.get(j)) {
                char[] ca = new char[1];
                int add = 0;
                int count = 0;
                for (int i = 0; i < str.length(); i++) { //go through the string
                    if (str.charAt(i) != ',') {
                        if (count != 0) {
                            ca = Arrays.copyOf(ca, ca.length + 1);// this is a sin but you gotta due what you gotta due T^T
                        }
                        ca[count] = str.charAt(i);
                        count++;
                    } else {
                        var.put(add, String.valueOf(ca)); //adds the value
                        ca = new char[1];//reset
                        add++;//iterates
                        count = 0;//reset
                    }
                }
                var.put(add, String.valueOf(ca));
                User u = new User(var.get(0), var.get(1), var.get(2), var.get(3), var.get(4), var.get(5), var.get(6));
                arMap.get(j).add(u);
            }
        }
        // --- Task 1
        //Print the oldest
        System.out.println("Old people: ");
        PriorityQueue<User> set = new PriorityQueue<>();
        for(int i = 0; i < uList.size(); i++){
            set.add(uList.get(i));
        }
        for(int i = 0; i < 10; i++){
            System.out.println(set.poll());
        }
        // --- Task 2
        //Create HashMap for states
        HashMap<String, Integer> hState = new HashMap<>();
        for(String s: Data.states){
            hState.put(s, 0);
        }
        for(User u: uList){
            hState.replace(u.getState(), hState.get(u.getState()), hState.get(u.getState()) + 1);
        }
        //Print people in the states
        System.out.println();
        System.out.println("State count: ");
        System.out.println(hState);
        // --- Task 3
        System.out.println();
        HashSet<User> hUsers = new HashSet<>(uList);
        HashSet<User> hOtherUsers = new HashSet<>(uOtherList);
        hUsers.retainAll(hOtherUsers);
        System.out.println("Users together: ");
        for(User u: hUsers){
            System.out.println(u);
        }
    }
}