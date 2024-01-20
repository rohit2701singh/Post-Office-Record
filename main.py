from data_file import PostData

API_ENDPOINT = "https://api.sheety.co/xxxxxxxxxxxxxccc91a/postOffice/informations"
AUTH_KEY = "Bearer rxxxxxxxxxxxht"
data = PostData(auth_token=AUTH_KEY, api_endpoint=API_ENDPOINT)

if input("do you want to insert data in sheet? yes/no: ").lower() == "yes":

    data_list = []
    entry_continue = True
    while entry_continue:

        post_name = input("type name of post: ")
        post_from = input("type sender address: ")
        post_to = input("type receiver address: ")
        phone_num = input("type phone number: ")

        if len(post_to) == 0:
            post_to = "unknown"
        if len(phone_num) == 0:
            phone_num = "unknown"

        data_list.append({"name": post_name, "post_from": post_from, "post_to": post_to, "phone_number": phone_num})

        user_choice = input("Do you want to finish? yes/no: ").lower()
        if user_choice == "yes":
            entry_continue = False
    print(data_list)


    def data_insert():
        data.insert_data(data_to_post=data_list)


    user_input = input("Do you want to insert data in google sheet? 'yes/no' ").lower()
    if user_input == "yes":
        data_insert()

    else:
        confirmation = input("you will need to insert data again. Are you sure you don't want to insert data? y/n: ").lower()
        if confirmation != "y":
            print("proceeding to insert data in sheet.")
            data_insert()
else:
    print("rerun the programme if want to insert data.")

entries_in_sheet = data.get_sheet_data()
print(f"here are all the entries in sheet:\n {entries_in_sheet}")
