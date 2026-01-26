def main():
    months  = {
        "Jan":"January",
        "Feb":"February",
        "Mar":"March",

    }
    print( months)

    #Adding a new item

    months["Apr"] ="April"
    print( months )

    #Updating existing value
    months["Mar"] ="Marche"
    print( months )
    months.update({"Mar":"March"})
    months.update({"May":"May","Jun":"June"})
    print( months)

main()