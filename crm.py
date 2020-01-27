def search_records():
    search_records = Tk()
    search_records.title("Search Records")
    search_records.iconbitmap('img/favicon.ico')
    search_records.geometry("450x700")

    def edit_record(record_id, index):
        edit_record = Tk()
        edit_record.title("Edit Record")
        edit_record.iconbitmap('img/favicon.ico')
        edit_record.geometry("320x400")

        sql_edit = "SELECT * FROM customers WHERE user_id = %s"
        name_edit = (record_id, )
        result_edit = my_cursor.execute(sql_edit, name_edit)
        result_edit = my_cursor.fetchall()
        print(result_edit)

        def update_record():
            return

        def delete_record():
            return

        # Create a Label
        title2_label = Label(edit_record, text="Record No. " + record_id, font=("Helvetica", 16))
        title2_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky=W)

        # Create form
        first_name_edit_label = Label(edit_record, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
        global first_name_edit_box
        first_name_edit_box = Entry(edit_record)
        first_name_edit_box.grid(row=1, column=1, pady=2)
        first_name_edit_box.insert(0, result_edit[0][0])

        last_name_edit_label = Label(edit_record, text="Surname").grid(row=2, column=0, sticky=W, padx=10)
        global last_name_edit_box
        last_name_edit_box = Entry(edit_record)
        last_name_edit_box.grid(row=2, column=1, pady=2)
        last_name_edit_box.insert(0, result_edit[0][1])

        address1_edit_label = Label(edit_record, text="Address line 1").grid(row=3, column=0, sticky=W, padx=10)
        global address1_edit_box
        address1_edit_box = Entry(edit_record)
        address1_edit_box.grid(row=3, column=1, pady=2)
        address1_edit_box.insert(0, result_edit[0][6])

        address2_edit_label = Label(edit_record, text="Address line 2").grid(row=4, column=0, sticky=W, padx=10)
        global address2_edit_box
        address2_edit_box = Entry(edit_record)
        address2_edit_box.grid(row=4, column=1, pady=2)
        address2_edit_box.insert(0, result_edit[0][7])

        city_edit_label = Label(edit_record, text="City").grid(row=5, column=0, sticky=W, padx=10)
        global city_edit_box
        city_edit_box = Entry(edit_record)
        city_edit_box.grid(row=5, column=1, pady=2)
        city_edit_box.insert(0, result_edit[0][8])

        county_edit_label = Label(edit_record, text="County").grid(row=6, column=0, sticky=W, padx=10)
        global county_edit_box
        county_edit_box = Entry(edit_record)
        county_edit_box.grid(row=6, column=1, pady=2)
        county_edit_box.insert(0, result_edit[0][9])

        postcode_edit_label = Label(edit_record, text="Postcode").grid(row=7, column=0, sticky=W, padx=10)
        global postcode_edit_box
        postcode_edit_box = Entry(edit_record)
        postcode_edit_box.grid(row=7, column=1, pady=2)
        postcode_edit_box.insert(0, result_edit[0][2])

        country_edit_label = Label(edit_record, text="Country").grid(row=8, column=0, sticky=W, padx=10)
        global country_edit_box
        country_edit_box = Entry(edit_record)
        country_edit_box.grid(row=8, column=1, pady=2)
        country_edit_box.insert(0, result_edit[0][10])

        phone_edit_label = Label(edit_record, text="Phone Number").grid(row=9, column=0, sticky=W, padx=10)
        global phone_edit_box
        phone_edit_box = Entry(edit_record)
        phone_edit_box.grid(row=9, column=1, pady=2)
        phone_edit_box.insert(0, result_edit[0][11])

        email_edit_label = Label(edit_record, text="Email Address").grid(row=10, column=0, sticky=W, padx=10)
        global email_edit_box
        email_edit_box = Entry(edit_record)
        email_edit_box.grid(row=10, column=1, pady=2)
        email_edit_box.insert(0, result_edit[0][5])

        payment_method_edit_label = Label(edit_record, text="Payment Method").grid(row=11, column=0, sticky=W, padx=10)
        global payment_method_edit_box
        payment_method_edit_box = Entry(edit_record)
        payment_method_edit_box.grid(row=11, column=1, pady=2)
        payment_method_edit_box.insert(0, result_edit[0][12])

        discount_code_edit_label = Label(edit_record, text="Discount Code").grid(row=12, column=0, sticky=W, padx=10)
        global discount_code_edit_box
        discount_code_edit_box = Entry(edit_record)
        discount_code_edit_box.grid(row=12, column=1, pady=2)
        discount_code_edit_box.insert(0, result_edit[0][13])


        price_paid_edit_label = Label(edit_record, text="Price Paid").grid(row=13, column=0, sticky=W, padx=10)
        global price_paid_edit_box
        price_paid_edit_box = Entry(edit_record)
        price_paid_edit_box.grid(row=13, column=1, pady=2)
        price_paid_edit_box.insert(0, result_edit[0][3])

        # Buttons

        update_record_btn = Button(edit_record, text="Update Record", command=update_record)
        update_record_btn.config(width=20, height=2)
        update_record_btn.grid(row=14, column=0, pady=5, padx=5)

        delete_record_btn = Button(edit_record, text="Delete Record", command=delete_record)
        delete_record_btn.config(width=20, height=2)
        delete_record_btn.grid(row=14, column=1, pady=5, padx=5)

    def search_init():
        sql = ""
        selected = drop.get()
        if selected == "Search by...":
            test = Label(search_records, text="Choose a parameter from the dropdown list")
            test.grid(row=3, column=0, columnspan=2, sticky=W, padx=5, pady=5)
        elif selected == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name = %s"
        elif selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email = %s"
        elif selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE user_id = %s"
        else:
            test = Label(search_records, text="Invalid Input")
            test.grid(row=3, column=0, columnspan=2, sticky=W, padx=5, pady=5)

        searched = search_box.get()
        name = (searched, )
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result_label = Label(search_records, text="Record Not Found")
            result_label.grid(row=3, column=0, sticky=W)
        else:       
            for index, x in enumerate(result):
                global record_id
                record_id = str(x[4])
                edit_btn = Button(search_records, text="Edit", command=lambda: edit_record(record_id, index))
                edit_btn.config(width=20, height=2)
                edit_btn.grid(row=index+4, column=1, columnspan=2, pady=5, padx=5, sticky=W+N)
                for y in x:
                    result_label = Label(search_records, text="Customer ID:\t" + str(x[4]) + "\nName:\t\t" + x[0] + " " + x[1] + "\nAddress:\t\t" + x[6] + "\n\t\t" + x[7] + "\n\t\t" + x[8] + "\n\t\t" + x[9] + "\n\t\t" + x[10] + "\nPhone No:\t" + x[11] + "\nEmail:\t\t" + x[5] + "\nPayment Type:\t" + x[12] + "\nDiscount Code:\t" + x[13] + "\nAmount Paid:\t" + str(x[3]) + "\n\n", justify=LEFT)
                    result_label.grid(row=index+4, column=0, sticky=W, padx=5)
        
        csv_btn = Button(search_records, text="Export as CSV", command=lambda: selection_as_csv(result))
        csv_btn.config(width=20, height=2)
        csv_btn.grid(row=3, column=0, columnspan=2, pady=5, padx=5, sticky=W)

    search_box = Entry(search_records)
    search_box.grid(row=1, column=0, pady=5, padx=5, sticky=W)

    search_btn = Button(search_records, text="Search", command=search_init)
    search_btn.config(width=20, height=2)
    search_btn.grid(row=2, column=0, columnspan=2, pady=5, padx=5, sticky=W)

    drop = ttk.Combobox(search_records, value=["Search by...", "Last Name", "Email Address", "Customer ID"])
    drop.current(0)
    drop.grid(row=0, column=0, pady=5, padx=5, sticky=W)
