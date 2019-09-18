# Encode strings to save UTF8 data as the path of the images

def encode_data(string):
    encoded_string = [n.encode("UTF-8", "ignore") for n in string]
    return(encoded_string)

# decode strings to save
def decode_data(string):
    decoded_string = [n.decode("UTF-8", "ignore") for n in string]
    return(decoded_string)