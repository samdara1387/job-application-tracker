import json
from datetime import datetime 
from datetime import date
import time
today= str(date.today())

Rime = datetime.now().strftime("%H:%M") 
try:
    with open("applications.json", "r") as file:
        applications = json.load(file)
except (FileNotFoundError,json.JSONDecodeError):
    applications = []


while True:
    time.sleep(1.5)
    try:
   
     menu=int(input("choose one of the following options:\n1.Add an application\n2.View an application\n3.Quit\n4-search by company name\n5.updating an application’s status\n:"))
    
    except ValueError:
        print("Please enter a number from 1 to 5.")
        continue
    
    
    if menu==1:
        
        company = input("Company name: ").strip()
        while company=="":
             print("company can not be blank")
             company = input("Company name: ").strip()

        role=input("The job title:").strip()
        while role=="":
            print("Role can not be blank")
            role=input("The job title:").strip()
            
                
        statuses = {
        "1": "Applied",
        "2": "Interview",
        "3": "Offer",
        "4": "Rejected"
                        }

        choice = input(
        "Choose a status:\n"
        "1. Applied\n"
        "2. Interview\n"
        "3. Offer\n"
        "4. Rejected\n"
        ": "
            ).strip()

        while choice not in statuses:
            choice = input("Please enter 1, 2, 3, or 4: ").strip()

        status = statuses[choice]
        date =( Rime,today)

        print(date)
      
                
        print("----"*10)
        
        
                
                
                
        application = {
                    "company": company,
                    "role": role,
                    "status": status,
                    "date":date
                }
                
        print("----"*10)
               
                
                
        applications.append(application)
        with open("applications.json", "w") as file:
            json.dump(applications, file, indent=4)
        print("Application added successfully!")
    elif menu == 2:
        print("----"*10)
        if not applications:
            print("No applications added yet.")
        else:
            for application in applications:
                print("Role:", application["role"])
                print("Status:", application["status"])
                print("Company:", application["company"])
                print("Date:", application.get("date", "Not recorded"))
                print("---" * 10)
       
     
    elif menu == 3:
        with open("applications.json", "w") as file:
            json.dump(applications, file, indent=4)

        print("Applications saved. Goodbye!")
        break
    
    elif menu==4:
        print("----"*10)
        search=input("which company are you looking for?    ").strip()
        found=False
        for application in applications:
            if search.lower()==application["company"].lower():
                print("it was found")
               
                print(application)
                found=True
                continue
        if not found:
                print("No matches found.")
        print("---"*10)
    elif menu==5:
        print("----"*10)
        search=input("which company are you looking for?    ")
        for application in applications:
            if search.lower()==application["company"].strip().lower():
                print("it was found")
                print(application) 
                statuses = {
                "1": "Applied",
                "2": "Interview",
                "3": "Offer",
                "4": "Rejected"
                                }

                change = input(
                "Choose a status:\n"
                "1. Applied\n"
                "2. Interview\n"
                "3. Offer\n"
                "4. Rejected\n"
                ": "
                    ).strip()

                while change not in statuses:
                    change = input("Please enter 1, 2, 3, or 4: ").strip()

                application["status"] = statuses[change]
                print("status updated")
                with open("applications.json", "w") as file:
                    json.dump(applications, file, indent=4)
                
                
            else:
                    
                print("no matches found ")
                    
              
    else:
        print("----"*10)
        print("Please choose 1, 2, 3 ,4 or 5.")
        print("----"*10)
    
        
    
    
        
        
      

    
    
