import datetime
from geopy.geocoders import Nominatim

contacts={"Raju":9999999999,"Narendra":8888888888,"Gani":7777777777}

while(True):
    print("\nselect an option\n1.Display time\n2.contacts\n3.Add new contact\n4.Health Tracking\n5.Get Geo location \n6.Exit")

    option = int(input("Enter:"))
    if(option==6):
        break
    
    if option == 1:
        now = datetime.datetime.now()
        print ("Current date and time : ")
        print (now.strftime("date:"+"%Y-%m-%d"+"\n"+"Time:"+ "%H:%M:%S"))
        
    elif option == 2:

        print(contacts)
        

    elif option == 3:
        con = {}
        name = input("Name:")
        contact = int(input("Contact No."))
        con[name] = contact
        print("Add successfully...")
        
    elif option == 4:
        print("Heart Rate:",79)
        print("BP:",85)
    elif option==5:
        loc = Nominatim(user_agent="GetLoc")
        getLoc = loc.geocode("Nuzvid Andhra Pradesh")
        print(getLoc.address)
        print("Latitude = ", getLoc.latitude)
        print("Longitude = ", getLoc.longitude)

        
    else:
        
        print("Invalid option")

    print("--------------------------------------------------------");


