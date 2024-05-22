Dojos And Ninjas CRUD Assignment

Learning Objectives:

    - Connect Flask to a database
    - Implement one-to-many relationships in a full-stack Flask
        application.
            - Use SQL joins to query the database for a record,
                including its associated records in a one-to-many
                relationship
            - Build a method that constructs an object representation
                of a record with a one-to-many relationship including
                a list of associated records from the other table.
    - Create one-to-many relationships in the database using
        user input.
            -Pass id data appropriately to and from the client
                in order to create a foreign key relationships
                on creation of a new record with a one-to-many
                relationship.
                
    - Encounter and resolve common Flask development errors using both Flask
        error messages as well as terminal output from the mysqlconnection
        file, utilizing print statements.


Assignment check list:

    - Create a new Flask project
    - Use dojos_and_ninjas_schema created in MySQL course
    - 'Dojo' page to add a new Dojo and display all Dojos
    - The dojo links on the 'Dojo' page should redirect the 'Dojo Show' page
    - 'Ninja' page to add a new Ninja
    - 'Ninja' page should include a drop down menu with all of the dojos in 
        the database
    - Redirect to the 'Dojo Show' page of the dojo selected after creating
        a ninja
    - 'Dojo Show' page should display all the Ninjas who are added to the Dojo
    - All Home links should redirect to 'localhost:5000/dojos'
    - SENSEI BONUS: Update and Delete (optional, but highly encouraged)
        - add update and delete functionality to the Ninjas!