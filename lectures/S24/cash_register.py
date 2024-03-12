def main():
    log_file = input("Enter filename: ")
    done = False
    while not done:
        sale = input("Enter item name (quit to exit): ")
        if sale == 'quit':
            done = True
        else:
            price = int(input("Enter price of item, in cents: "))
            quantity = int(input("Enter quantity sold: "))
            with open(log_file, 'a') as file_out:
                file_out.write(f"{sale},{price},{quantity}\n")


main()
