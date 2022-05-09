package edu.sfsu.cs.datastructures;

import java.util.Objects;

public class User implements Comparable{
    String firstname;
    String lastname;
    String age;
    String email;
    String gender;
    String city;
    String state;

    public User(String firstname, String lastname, String age, String email, String gender, String city, String state) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.age = age;
        this.email = email;
        this.gender = gender;
        this.city = city;
        this.state = state;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    @Override
    public int compareTo(Object o) {
        return (Integer.parseInt(this.getAge()) < Integer.parseInt(((User) o).getAge()) ? 1 : (Integer.parseInt(this.getAge()) == Integer.parseInt(((User) o).getAge()) ? 0 : -1));
    }

    @Override
    public String toString() {
        return "User{" +
                "firstname='" + firstname + '\'' +
                ", lastname='" + lastname + '\'' +
                ", age='" + age + '\'' +
                ", email='" + email + '\'' +
                ", gender='" + gender + '\'' +
                ", city='" + city + '\'' +
                ", state='" + state + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return Objects.equals(firstname, user.firstname) && Objects.equals(lastname, user.lastname) && Objects.equals(age, user.age) && Objects.equals(email, user.email) && Objects.equals(gender, user.gender) && Objects.equals(city, user.city) && Objects.equals(state, user.state);
    }

    @Override
    public int hashCode() {
        return Objects.hash(firstname, lastname, age, email, gender, city, state);
    }
}
