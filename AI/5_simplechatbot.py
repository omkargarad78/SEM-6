
print("-------------------------------------------------------------")
print("Hello! I'm your advanced real estate chatbot. Let's find your dream property!\n")

    # Asking user about their expectations
location = input("Firstly, where are you looking to buy or rent? ")
budget = float(input("What is your budget for the property? "))
property_type = input("Are you looking for an apartment, house, or commercial property? ")
property_size = input("What size of property are you interested in (small, medium, large)? ")
amenities = input("Any specific amenities you would like (e.g., pool, gym, parking)? ")
neighborhood_characteristics = input("What characteristics do you prefer in a neighborhood (e.g., quiet, lively, family-friendly)? ")
proximity_to_amenities = input("How important is proximity to amenities like schools, hospitals, and supermarkets (high, medium, low)? ")
importance_of_features = input("On a scale of 1 to 10, how important are features like a backyard, balcony, or parking space? ")

#---------------------------------------------------------------------------------------------
print("\nThank you for providing your preferences. Here is a summary of your choices:")

print("\n**Budget:**")
if budget < 50000:
    print("Your budget is relatively low. We can explore affordable options in different areas.")
elif 50000 <= budget <= 150000:
    print(f"Great! With a budget of {budget}, we can find suitable {property_type}s in {location}.")
else:
    print("Your budget is quite high. We can explore premium properties in exclusive locations.")

print("\n**Location and Property Type:**")
if location.lower() == "downtown":
    print("Downtown is a vibrant and central location. We can find properties that match your preferences.")
elif location.lower() == "suburb":
    print("Living in the suburbs offers a quieter lifestyle. We'll look for properties in suburban areas.")
else:
    print("Let's explore properties in different locations based on your preferences.")

print(f"\n**Property Type and Size:**")
if property_type.lower() == "apartment":
    print(f"Apartments are a popular choice. We'll focus on finding a {property_size} apartment with {amenities}.")
elif property_type.lower() == "house":
    print(f"Houses provide more space and privacy. We'll look for a {property_size} house with {amenities}.")
elif property_type.lower() == "commercial property":
    print(f"Commercial properties are unique. We'll explore {property_size} spaces with {amenities}.")
else:
    print("Let's explore various property types to find the perfect match for you.")

print("\n**Neighborhood Preferences:**")
if "quiet" in neighborhood_characteristics.lower():
    print("You prefer a quiet neighborhood. We'll prioritize areas known for their peaceful environment.")
elif "lively" in neighborhood_characteristics.lower():
    print("You enjoy a lively atmosphere. We'll focus on neighborhoods with vibrant activities.")
elif "family-friendly" in neighborhood_characteristics.lower():
    print("Family-friendly neighborhoods are great for a wholesome environment. We'll consider areas suitable for families.")

    # Additional tailored responses based on the new questions
print("\n**Additional Preferences:**")
if proximity_to_amenities.lower() == "high":
    print("Proximity to amenities is important for you. We'll prioritize properties close to schools, hospitals, and supermarkets.")
elif proximity_to_amenities.lower() == "medium":
    print("We'll consider properties with moderate proximity to amenities based on your preferences.")
else:
    print("Proximity to amenities is not a top priority. We can explore a wider range of locations.")

importance_of_features_rating = int(importance_of_features)
if 7 <= importance_of_features_rating <= 10:
    print("Features like a backyard, balcony, or parking space are highly important to you. We'll focus on properties that meet these criteria.")
elif 4 <= importance_of_features_rating <= 6:
    print("We'll consider properties with certain features, but they won't be the primary focus.")
else:
    print("Features like a backyard, balcony, or parking space are less important. We can explore a broader range of options.")

print("\nThank you for providing detailed preferences.")

