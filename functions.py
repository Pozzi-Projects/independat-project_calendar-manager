
def send_message(calendar_dictionary):
    total_patients = len(calendar_dictionary)
    times = list(calendar_dictionary.keys())
    data = list(calendar_dictionary.values())

    if total_patients == 0:
        print("you have no patients scheduled for tomorrow.")
    else:
        while total_patients > 0:
            total_patients = total_patients - 1

            local_time = times[total_patients]
            local_name = data[total_patients][0]
            local_number = data[total_patients][1]

            # we need to take this message and send it to the phone number
            print(f"{local_number} - message sent to")
            print(f"Hi {local_name}, "
                  f"\nPlease  respond 'Yes' to confirm your appointment for {local_time} tomorrow "
                  f"\nif you need to cancel please respond 'Cancel'. \n")  # We can add the date to this message