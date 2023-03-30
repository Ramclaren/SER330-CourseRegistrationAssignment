package com.ser330.courseregistration;

public class Person {

    private String lastName; 
    private String firstName;
    private String school;
    private String dateOfBirth;
    private String userName;
    private String affiliation;
    private String email;

    public Person(String lastName, String firstName, String school, String dateOfBirth, String userName, String affiliation)
    {
        this.lastName = lastName;
        this.firstName = firstName;
        this.school = school;
        this.dateOfBirth = dateOfBirth;
        this.userName = userName;
        this.affiliation = affiliation;
    }
    
    public String getEmail()
    {
        return this.email;
    }

    public void setEmail(String email)
    {
        this.email = email;
    }

}
