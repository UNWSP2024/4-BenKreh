def get_inches():

    months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
    total_inches = 0
    get_years = int(input("Insert how many years you would like to calculate for."))
    for i in range(get_years):

        for x in range(12):
            inches = float(input(f"How many inches of rain in {months[x]}? "))
            total_inches += inches


    print(f"Total rainfall over {get_years} years: {total_inches}")
    print(f"Average rainfall per month: {total_inches / (get_years * 12):.2f} inches")

get_inches()
