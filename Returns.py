import time
class Returns:

    def __init__(self):
        self.orders = {1: "iPhone 13 64GB", 2: "Nvidia RTX 3080", 3: "Playstation 5"}
        self.facilities = ["Kelowna", "Edmonton", "Toronto"]
        self.shipping = ["Canada Post", "Purolator", "UPS"]


    def Return_Process(self):
        print("Hello!")
        time.sleep(1.2)
        print("Welcome to our automated return service!")
        time.sleep(1.2)
        while True:
            try:
                time.sleep(1.2)
                orderid = int(input("May I please have your order ID?"))
                if 1 <= orderid <= 3:
                    time.sleep(1.2)
                    print("Thank you so much! The order ID you have selected is " + str(orderid))
                    break
                else:
                    time.sleep(1.2)
                    print("Invalid order ID.")
            except ValueError:
                time.sleep(1.2)
                print("Order ID must be an integer.")

        time.sleep(1.2)
        print("The product you wish to return is " + self.orders[orderid])
        time.sleep(1.2)
        reasoning = input("Is there any reason you wish to return " + self.orders[orderid])
        time.sleep(1.2)
        print("I'm sorry to hear that you're unsatisfied with the product.")
        time.sleep(1.2)
        while True:
            time.sleep(1.2)
            facility = str(input("Please choose the facility that is closest to you (" + ", ".join(self.facilities) + "):"))
            if facility.lower() == "kelowna":
                time.sleep(1.2)
                facility = 0
                print("Thank you for choosing the " + self.facilities[facility] + " facility!")
                break
            elif facility.lower() == "edmonton":
                time.sleep(1.2)
                facility = 1
                print("Thank you for choosing the " + self.facilities[facility] + " facility!")
                break
            elif facility.lower() == "toronto":
                time.sleep(1.2)
                facility = 2
                print("Thank you for choosing the " + self.facilities[facility] + " facility!")
                break
            else:
                time.sleep(1.2)
                print("Invalid facility.")

        time.sleep(1.2)
        while True:
            time.sleep(1.2)
            creditOrRefund = str(input("Would you like in-store credit or a refund for your return? (credit/refund)"))
            if creditOrRefund.lower() == "credit":
                time.sleep(1.2)
                email = str(input("May I please have your email?"))
                time.sleep(1.2)
                print("Thank you! The in-store credit will appear in your account shortly.")
                break
            elif creditOrRefund.lower() == "refund":
                time.sleep(1.2)
                email = str(input("May I please have your email?"))
                time.sleep(1.2)
                print("Thank you! A refund will be issued to the default payment method on your account.")
                break
            else:
                time.sleep(1.2)
                print("Invalid response.")

        time.sleep(1.2)
        while True:
            time.sleep(1.2)
            shipform = str(input("We're almost done! Would you like to complete the quick shipping form now or later? (now/later)"))
            if shipform.lower() == "now":
                time.sleep(1.2)
                self.Ship_Progress(facility)
                break
            elif shipform.lower() == "later":
                time.sleep(1.2)
                print("Your return request has been processed!")
                time.sleep(1.2)
                print("An email confirmation along with the shipping form has been emailed to " + email)
                time.sleep(1.2)
                print("Thank you for using our automated return service!")
                break
            else:
                time.sleep(1.2)
                print("Invalid response.")




    def Ship_Progress(self, facility):
        print("in progress")












retbot = Returns()

retbot.Return_Process()