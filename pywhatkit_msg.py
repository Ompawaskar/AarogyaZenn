import pywhatkit

# List of phone numbers
phone_numbers = ["+919321543686", "+918369147159", "+918369097541", "+919175205766"]  # Add more numbers as needed

# Message to send
message = "Hello from AAROGYA ZEN.\nHope you are doing well!"

# Time when the message should be sent (hour and minute)
hour = 22
minute = 26


# Loop through each phone number and send the message at the scheduled time
for number in phone_numbers:
    # Send the messa
    pywhatkit.sendwhatmsg(number, message, hour, minute, 20, True,25)
    # Increment minute for the next message
    minute += 2
