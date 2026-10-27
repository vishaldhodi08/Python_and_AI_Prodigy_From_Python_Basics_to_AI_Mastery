def shutdown(answer):
    if answer.lower() == "yes":
        print("Shutting down.")
    elif answer.lower() == "no":
        print("Abort shutdown.")
    else:
        print("Sorry.")

response = input("Do you want to shut down? (yes/no): ")
shutdown(response)